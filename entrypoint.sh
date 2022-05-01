#!/usr/bin/bash

python3 download_cert.py

nginx -g 'daemon off;' 
