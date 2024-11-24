#!/bin/bash

# Install the required Python dependencies
pip install -r requirements.txt

# Make the weights_download.sh script executable
chmod +x weights_download.sh

# Run the weights_download.sh script
bash weights_download.sh
