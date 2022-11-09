# Minimal CPCD and EZSPD demo
This demo downloads and compiles CPCD and the EZSPD ASH wrapper, allowing for simple
testing with existing command line applications that can communicate with existing
TCP socket-based Zigbee coordinators.

## Usage

1. Ensure your development kit is running the stock `zigbee_ncp-ot_rcp-uart` example **with encryption disabled**.
2. Download and build CPCD and EZSPD with `./build.sh`.
3. Edit the correct serial port path into `cpcd.conf`.
4. Launch CPCD: `LD_LIBRARY_PATH=output ./output/cpcd -c cpcd.conf`
5. Launch EZSPD: `LD_LIBRARY_PATH=output ./output/ezspd`
6. Create a Python virtual environment and run the test script:
   ```console
   $ python3 -m venv venv  # may require you to install the `python-venv` package
   $ venv/bin/pip install bellows coloredlogs
   $ venv/bin/python crash.py
   ```
7. Wait for the crash to occur. It can take a few minutes if the network has minimal traffic.
