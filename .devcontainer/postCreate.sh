#!/bin/bash

curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
pip install --upgrade pip
pip3 install --user -r requirements.txt