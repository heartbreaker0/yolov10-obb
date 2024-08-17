#!/bin/bash
apt install libgl1-mesa-glx
conda install -c pytorch -c nvidia -c conda-forge pytorch torchvision pytorch-cuda=12.1 ultralytics