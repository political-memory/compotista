# OLD MASTER

This is the master branch as i got it from @psycojoker

For dev:

    git clone git@github.com:Psycojoker/compotista.git
    git clone git@github.com:yohanboniface/django-representatives.git
    git clone git@github.com:Psycojoker/django-parltrack-meps.git
    git clone git@github.com:Psycojoker/django-parltrack-meps-to-representatives.git

    cd compotista
    ln -s ../django-representatives/representatives/ .
    ln -s ../django-parltrack-meps/parltrack_meps/ .
    ln -s ../django-parltrack-meps-to-representatives/parltrack_meps_to_representatives/ .

    python manage.py syncdb
    python manage.py update_meps

To run the conversion:

    python manage.py convert_meps_to_representatives
