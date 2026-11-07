# Whs laptops
This git repo is for a [website](https://laptops.409060.xyz).

# Purpose
Whs laptops is for giving laptops to students who don't have a laptop, or have a damaged, old, or borrowed laptop.

# Setup
Quick setup (debian apt)
```
sudo apt install python3 python-is-python3 python3-bottle
git clone https://github.com/martycat111/whs-laptops
cd whs-laptops
python main.py
```
or use pip...
```
sudo apt install python3 python3-pip python-is-python3
git clone https://github.com/martycat111/whs-laptops
cd whs-laptops
sudo pip install bottle --no-preserve-root
python main.py 
```
Basically, install python, and bottle.
Then clone this repo, cd in and run the main.py

# Technical
This is written in python, using the bottle library for website writing.
The rest is pure Html, Css, and a little Javascript.
