[![Build Status](https://travis-ci.org/political-memory/compotista.svg?branch=travis)](https://travis-ci.org/political-memory/compotista)
[![Documentation Status](https://readthedocs.org/projects/compotista/badge/?version=latest)](http://compotista.readthedocs.org/en/latest/?badge=latest)
[![Requirements Status](https://requires.io/github/political-memory/compotista/requirements.svg?branch=master)](https://requires.io/github/political-memory/compotista/requirements/?branch=master)
```
cd /tmp
virtualenv compotista_example
source compotista_example/bin/activate

git clone https://github.com/political-memory/compotista.git
cd compotista
cp compotista/config.json.sample compotista/config.json
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver
```
