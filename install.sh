#!/bin/bash

# Copy this install script in a «compotista_project» directory
branch=dev
git_compotista=git@git.laquadrature.net:memopol/compotista.git
git_django_representatives=git@git.laquadrature.net:memopol/compotista_django-representatives.git
git_import_parltrack=git@git.laquadrature.net:memopol/compotista_import_parltrack.git

virtualenv --python=python2.7 ve

git clone $git_compotista compotista
git clone $git_django_representatives django-representatives
git clone $git_import_parltrack compotista-import_parltrack

cd compotista

git checkout $branch

cd ..
source ve/bin/activate

pip install -r compotista/requirements.txt

# python compotista/manage.py syncdb
