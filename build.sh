#!/bin/sh
set -e

# Specify a folder for targets
if [ ! -d "output" ]; then
	mkdir output
fi

# Build CPC and CPCD
if [ ! -d "cpc-daemon" ]; then
	git clone https://github.com/SiliconLabs/cpc-daemon
fi

cmake -S cpc-daemon -B output
make -C output

# Build CPC-EZSPD
if [ ! -d "silabs-cpc-ezspd" ]; then
	git clone https://github.com/agners/silabs-cpc-ezspd
fi

make -C silabs-cpc-ezspd clean
make -C silabs-cpc-ezspd LDFLAGS="-L$PWD/output" CFLAGS="-I$PWD/cpc-daemon/lib"
cp -fv silabs-cpc-ezspd/ezspd output
