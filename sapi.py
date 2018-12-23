#!/usr/bin/env python

import requests
import subprocess

# >>> ip = subprocess.check_output(['hostname', '-I'])
# >>> ip
# '10.0.0.232 \n'
# >>> ip.strip()
# '10.0.0.232'
# >>> 

payload = {'accept':'application/json'}
control_url = ""
next_url = ""
prev_url = ""
pause_url = ""

def get_ip():
    ip = subprocess.check_output(['hostname', '-I'])
    return ip.strip()

def setup():
    global control_url, next_url, prev_url, pause_url

    ip = get_ip()

    control_url = "http://" + ip + "/api/v1/assets/control/"
    next_url = control_url + "next"
    prev_url = control_url + "previous"
    pause_url = control_url + "pause"

def action(url):
    if url != "":
        r = requests.get(url, payload)
        print r.json()
        del r
    else:
        print "Call setup() with the ip address of the raspberry pi"

def next():
    action(next_url)

def prev():
    action(prev_url)

def pause():
    action(pause_url)

# Do the setup automatically
setup()
