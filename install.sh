#!/bin/bash

# Copy this install script in a «compotista_project» directory

python=/usr/bin/python2.7
git_compotista=git@git.laquadrature.net:luxcem/compotista.git
git_django_representatives=git@git.laquadrature.net:luxcem/memopol_django-representatives.git
git_django_parltrack_meps=git@git.laquadrature.net:luxcem/compotista_django-parltrack-meps.git
git_django_parltrack_meps_to_representatives=git@git.laquadrature.net:luxcem/compotista_django-parltrack-meps-to-representatives.git

virtualenv -p $python ve

git clone $git_compotista compotista
git clone $git_django_representatives django-representatives
git clone $git_django_parltrack_meps django-parltrack_meps
git clone $git_django_parltrack_meps_to_representatives django-parltrack_meps_to_representatives

cd compotista

ln -s ../django-representatives/representatives/ .
ln -s ../django-parltrack_meps/parltrack_meps/ .
ln -s ../django-parltrack_meps_to_representatives/parltrack_meps_to_representatives/ .

cd ..
source ve/bin/activate

pip install -r compotista/requirements.txt
pip install -r django-parltrack_meps/requirements.txt

# python compotista/manage.py syncdb
