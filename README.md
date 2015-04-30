For dev:
    mkdir compotista
    cd compotista
    git clone git@git.laquadrature.net:memopol/compotista.git
    cp compotista/install.sh .
    ./install.sh

Run (in compotista dir with the right virtualenv)
    python manage.py syncdb
    python manage.py import_parltrack_representatives

