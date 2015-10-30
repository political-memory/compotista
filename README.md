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
