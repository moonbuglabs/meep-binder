#!/bin/bash
pip install -q condacolab
python -c "import condacolab; condacolab.install()"
source /usr/local/etc/profile.d/conda.sh
conda config --set always_yes true
conda config --set changeps1 false
conda config --add channels conda-forge
conda config --set channel_priority strict
conda env create -f environment.yml -y
conda activate pmp
conda run -n pmp python -m ipykernel install --user --name pmp --display-name "PyMeep (MPI)"
