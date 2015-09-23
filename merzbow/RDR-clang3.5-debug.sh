#!/bin/bash

source /Users/roberto/.bashrc
export PATH=/opt/intel/composer_xe_2015.0.077/bin/intel64:/opt/intel/composer_xe_2015.0.077/mpirt/bin/intel64:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/opt/intel/composer_xe_2015.0.077/debugger/gdb/intel64/bin

PCMSolver_TMPDIR=/Users/roberto/Scratch/RDR-clang3.5-debug
mkdir -p $PCMSolver_TMPDIR
export PCMSolver_TMPDIR
export NPROCS=`sysctl -n hw.ncpu`
export CTEST_MAKE_NUM_PROCS=$NPROCS

TMP_DIR=/Users/roberto/Scratch/tmprunpcmsolver/RDR-clang3.5-debug
mkdir -p $TMP_DIR

git clone -b Rob-API git@gitlab.com:PCMSolver/pcmsolver.git $TMP_DIR

cd $TMP_DIR

python setup.py --fc=gfortran --cc=clang --cxx=clang++ --type=debug --python=/usr/local/bin/python --cmake-options='-DBUILDNAME=RDR-MacOS-10.10-clang3.5-debug -DSITE=merzbow' 

cd $TMP_DIR/build

ctest -D Nightly -j$NPROCS

cd
rm -rf $PCMSolver_TMPDIR $TMP_DIR

exit 0
