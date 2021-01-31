## Explanation Video Uploaded ! 
https://youtu.be/zfkovG9ez3U
## ABOUT
This is a contribution for the official [Proxy-Anchor Loss](https://github.com/tjddus9597/Proxy-Anchor-CVPR2020) implementation.
## Contribution
This repositury provide the code to support training of Proxy-Anchor Loss on [Caltech-256 Dataset](http://www.vision.caltech.edu/Image_Datasets/Caltech256/).
## Steps
1. Clone the official repository from [here](https://github.com/tjddus9597/Proxy-Anchor-CVPR2020)
1. Replace code/train.py with train.py from this repositry
1. Copy __init__.py and caltech256 to code/dataset
1. Downalod Caltech-256 dataset from [here](http://www.vision.caltech.edu/Image_Datasets/Caltech256/).
1. Extract and copy the dataset folder to /data directory.
## Training Command
```python
train.py  --gpu-id 0 
          --loss Proxy_Anchor \
          --model bn_inception \
          --embedding-size 512 \
          --batch-size 180 \
          --lr 1e-3 \
          --dataset caltech256 \
          --warm 1 \
          --bn-freeze 1 \
          --lr-decay-step 1 \
          --alpha 16 \
          --epochs 5 \
          --workers 24 \
          --mrg 0.1
```
## Good Luck 
<p align="center">
  <img src="https://github.com/moured/Metric-Learning-Proxy-Anchor-Loss/blob/main/caltech256.png?raw=true" /> 
</p>
