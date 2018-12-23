#!/bin/bash

# Copy unit file to systemd dir
# NOTE: if the service's ExecStart line tries to dump output to a local 
#       log file the output actually gets written to /var/log/daemon.log
sudo cp -p buttons.service /lib/systemd/system/

sudo systemctl daemon-reload 
sudo systemctl enable buttons.service

