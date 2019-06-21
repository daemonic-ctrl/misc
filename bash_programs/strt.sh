#!/bin/bash
ifconfig wlan1 down 1>goodOut 2>badOutput
airmon-ng start wlan0 1>goodOut 2>badOutput
echo -------------Done---------------
