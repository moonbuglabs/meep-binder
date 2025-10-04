#!/bin/bash
pip install -r requirements.txt
apt update
apt install -y libopenmpi-dev openmpi-bin h5utils
