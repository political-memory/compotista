Deployment
~~~~~~~~~~

Example with domain "lqdn", user "jamespic@gmail.com" and app name "compotista"
from the master branch with redis and cron cartridges::

    rhc app-create \
        python-2.7 \
        "http://cartreflect-claytondev.rhcloud.com/reflect?github=smarterclayton/openshift-redis-cart" \
        cron-1.4 \
        -n lqdn \
        --from-code https://github.com/political-memory/compotista.git \
        -a compotista \
        -e SECRET_KEY=$(openssl rand -base64 32) \
        -e OPENSHIFT_PYTHON_WSGI_APPLICATION=compotista/wsgi.py

Then, either wait for the daily cron to import data, either run it manually::

    rhc ssh -a compotista
    cron/bin/cron_runjobs.sh hourly

Then, to deploy a specific ref - which should be on the repo specified with
``--from-code``::

    rhc app-deploy master -a compotista

The password is encrypted in travis with the ``travis-encrypt`` command.
