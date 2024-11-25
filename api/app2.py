


@app.route('/process', methods=['POST'])
def process_request():
    try:
        # Generate a unique filename for each request
        unique_filename = f"../imgs/saved_image_{uuid.uuid4().hex}.png"
        
        # Parse the input data
        image_data = request.json.get('image_input')
        box_threshold = float(request.json.get('box_threshold', 0.05))
        iou_threshold = float(request.json.get('iou_threshold', 0.1))
        use_paddleocr = bool(request.json.get('use_paddleocr', True))
        imgsz = int(request.json.get('imgsz', 640))
        
        # Decode the image and save it
        image = Image.open(io.BytesIO(base64.b64decode(image_data)))
        image.save(unique_filename)

        # Calculate overlay ratio for bounding boxes
        box_overlay_ratio = image.size[0] / 3200
        draw_bbox_config = {
            'text_scale': 0.8 * box_overlay_ratio,
            'text_thickness': max(int(2 * box_overlay_ratio), 1),
            'text_padding': max(int(3 * box_overlay_ratio), 1),
            'thickness': max(int(3 * box_overlay_ratio), 1),
        }

        # Perform OCR and YOLO model processing
        ocr_bbox_rslt, is_goal_filtered = check_ocr_box(
            unique_filename,
            display_img=False,
            output_bb_format='xyxy',
            goal_filtering=None,
            easyocr_args={'paragraph': False, 'text_threshold': 0.9},
            use_paddleocr=use_paddleocr
        )
        text, ocr_bbox = ocr_bbox_rslt

        dino_labeled_img, label_coordinates, parsed_content_list = get_som_labeled_img(
            unique_filename,
            yolo_model,
            BOX_TRESHOLD=box_threshold,
            output_coord_in_ratio=True,
            ocr_bbox=ocr_bbox,
            draw_bbox_config=draw_bbox_config,
            caption_model_processor=caption_model_processor,
            ocr_text=text,
            iou_threshold=iou_threshold,
            imgsz=imgsz
        )

        # Convert processed image to base64
        processed_image = Image.open(io.BytesIO(base64.b64decode(dino_labeled_img)))
        buffer = io.BytesIO()
        processed_image.save(buffer, format="PNG")
        processed_image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')

        # Combine text and coordinates into a single JSON structure
        text_with_coordinates = []
        for box_id, coordinates in label_coordinates.items():
            full_text = parsed_content_list[int(box_id)]  # Full text like "Text Box ID 2: Tech Deployment Track"
            # Extract ID type, ID, and Description
            id_type_match = full_text.split("ID")[0].strip()  # "Text Box"
            id_value = int(full_text.split("ID")[1].split(":")[0].strip())  # Extract ID number, e.g., "2"
            description = full_text.split(":")[1].strip()  # Extract description, e.g., "Tech Deployment Track"

            text_with_coordinates.append({
                "ID type": id_type_match,
                "ID": id_value,
                "Description": description,
                "Coordinates": coordinates
            })

        # Prepare the response
        response = {
            "image_output_component": processed_image_base64,
            "text_with_coordinates": text_with_coordinates
        }

        # Clean up temporary file
        os.remove(unique_filename)

        return jsonify(response)

    except Exception as e:
        logging.error("An error occurred: %s", e)
        logging.error(traceback.format_exc())
        return jsonify({'error': str(e)}), 500
