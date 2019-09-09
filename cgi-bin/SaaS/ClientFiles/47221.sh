#! /usr/bin/sh
sudo sshpass -p aryan ssh 192.168.43.47 -p 47221 -o StrictHostKeyChecking=false -X 'dbus-uuidgen > /etc/machine-id; firefox &'