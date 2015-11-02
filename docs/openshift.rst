Deployment
~~~~~~~~~~

Example with domain "lqdn", user "jamespic@gmail.com" and app name "compo" from
the master branch with redis and cron cartridges::

    rhc app-create \
        python-2.7 \
        "http://cartreflect-claytondev.rhcloud.com/reflect?github=smarterclayton/openshift-redis-cart" \
        cron-1.4 \
        -n lqdn \
        --from-code https://github.com/political-memory/compotista.git \
        -a compo \
        -e SECRET_KEY=$(openssl rand -base64 32) \
        -e OPENSHIFT_PYTHON_WSGI_APPLICATION=compotista/wsgi.py

.. danger:: Do not call your openshift app "compotista", or deployment will
            fail with ``We were unable to clone your application's git repo -
            The directory you are cloning into already exists.``

Then, either wait for the daily cron to import data, either run it manually::

    # Feel free to look around, use the find command and all to explore the
    # container, there are logs for everything.
    rhc ssh -a compo

    # Let's run this command in a tmux session in case our ssh connection goes
    # down
    TERM=xterm tmux

    # Force execution of the daily cron.
    cron/bin/cron_runjobs.sh daily

Then, to deploy a specific ref - which should be on the repo specified with
``--from-code``::

    rhc app-deploy master -a compo

The password is encrypted in travis with the ``travis-encrypt`` command. It was
setup with the ``travis setup openshift``.
