#! /bin/bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
python3 -m venv venv

activate () {
    . venv/bin/activate 
}

activate
pip3 install -r requirements.txt
python3 create.py 
python3 app.py