#!/usr/bin/bash

download_cert.py

nginx -g 'daemon off;' 
