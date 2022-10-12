# Simple Form WEB
## Requirements

* Python 3.6
* Virtualenv
* Flask 1.0.2 


## Install
```bash
git clone https://github.com/Enconix/webformtest.git

cd webformtest

python3 -m venv env

source env/bin/activate

pip install -r requirements.txt

```
## Running the server 
### For linux 
```bash
export FLASK_APP=app.py 

```
### For Windows
```bash
set FLASK_APP=app.py

```
### Run locally on your computer
```bash

flask run

```
### Run locally on your network
```bash

flask run --host=your_computer_ip

```
