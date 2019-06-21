#!/bin/bash
airmon-ng stop wlan1mon
sudo systemctl restart NetworkManager
