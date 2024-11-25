# OmniParser: Screen Parsing tool for Pure Vision Based GUI Agent

<p align="center">
  <img src="imgs/logo.png" alt="Logo">
</p>

[![arXiv](https://img.shields.io/badge/Paper-green)](https://arxiv.org/abs/2408.00203)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

📢 [[Project Page](https://microsoft.github.io/OmniParser/)] [[Blog Post](https://www.microsoft.com/en-us/research/articles/omniparser-for-pure-vision-based-gui-agent/)] [[Models](https://huggingface.co/microsoft/OmniParser)] [[Huggingface demo](https://huggingface.co/spaces/microsoft/OmniParser)]

**OmniParser** is a comprehensive method for parsing user interface screenshots into structured and easy-to-understand elements, which significantly enhances the ability of GPT-4V to generate actions that can be accurately grounded in the corresponding regions of the interface. 

## News
- [2024/10] OmniParser is the #1 trending model on huggingface model hub (starting 10/29/2024). 
- [2024/10] Feel free to checkout our demo on [huggingface space](https://huggingface.co/spaces/microsoft/OmniParser)! (stay tuned for OmniParser + Claude Computer Use)
- [2024/10] Both Interactive Region Detection Model and Icon functional description model are released! [Hugginface models](https://huggingface.co/microsoft/OmniParser)
- [2024/09] OmniParser achieves the best performance on [Windows Agent Arena](https://microsoft.github.io/WindowsAgentArena/)! 

## Install 
Install environment for droplet with Ubuntu:
```bash
sudo apt update
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh
bash miniconda.sh
sudo apt-get install -y mesa-utils

/root/miniconda3/bin/conda init
source ~/.bashrc

conda create -n "omni" python==3.12
conda activate omni
```

Git clone the repo:
```bash
git clone https://github.com/sayuj01/OmniParser_microsoft.git
cd OmniParser_microsoft
```

Then just run the sh file
 
```bash
chmod +x master.sh
bash master.sh
```

## Examples:
We put together a few simple examples in the demo.ipynb. 

##Flash API
```
cd api
pip -r requirements.txt
python app.py
```

##Gunicorn for concurrent requests
```
gunicorn app:app --workers=4 --threads=1 --bind 0.0.0.0:8000
```

## Gradio Demo
To run gradio demo, simply run:
```python
python gradio_demo.py
```

## Model Weights License
For the model checkpoints on huggingface model hub, please note that icon_detect model is under AGPL license since it is a license inherited from the original yolo model. And icon_caption_blip2 & icon_caption_florence is under MIT license. Please refer to the LICENSE file in the folder of each model: https://huggingface.co/microsoft/OmniParser.

## 📚 Citation
Our technical report can be found [here](https://arxiv.org/abs/2408.00203).
If you find our work useful, please consider citing our work:
```
@misc{lu2024omniparserpurevisionbased,
      title={OmniParser for Pure Vision Based GUI Agent}, 
      author={Yadong Lu and Jianwei Yang and Yelong Shen and Ahmed Awadallah},
      year={2024},
      eprint={2408.00203},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2408.00203}, 
}
```
