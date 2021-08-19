shipwell
========
test for interview - not meant for production. In this demo I'm just using some state data from mapbox, I had intended to use some traffic accident data I got from the city of austin paired with a hex grid but it didn't quite fit into my schedule to finish that but the code still lives in there. Also if you want to run the code, you'll have to get your own mapbox API key.

Here's a screen cast. Click the gif to download a higher quality version. 

.. image:: https://github.com/millerhooks/shipwell/raw/main/docs/screencast.gif
     :target: https://drive.google.com/file/d/1cHjoJV0ZUNQPD0a9yUjbkIvsvprN18Hr/view?usp=sharing

:License: MIT

Quickstart
----------

::

    $ docker-compose -f local.yml up -d
    $ docker-compose -f local.yml run --rm django python manage.py migrate
    [+] Running 1/0
    ⠿ Container postgres  Running                                                                                                                                                                                                                                                                                                                                      0.0s
    PostgreSQL is available
    Operations to perform:
      Apply all migrations: account, admin, auth, authtoken, contenttypes, geo, sessions, sites, socialaccount, users
    Running migrations:
      Applying contenttypes.0001_initial... OK
      Applying contenttypes.0002_remove_content_type_name... OK
      Applying auth.0001_initial... OK
      Applying auth.0002_alter_permission_name_max_length... OK
      Applying auth.0003_alter_user_emai
    
    ......
    
    $ docker-compose -f local.yml run --rm django python manage.py createsuperuser
    $ docker-compose -f local.yml run --rm django python manage.py shell
    Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
    PostgreSQL is available
    Python 3.9.6 (default, Aug 17 2021, 02:38:04) 
    Type 'copyright', 'credits' or 'license' for more information
    IPython 7.26.0 -- An enhanced Interactive Python. Type '?' for help.

    In [1]: from geo.load import load
    
    In [2]: load()
    Saved: 359
    Saved: 358
    Saved: 357
    Saved: 356
    Saved: 355
    
    ......
    
    10682 | COLLISION - SAVED
    10683 | Crash Urgent - SAVED
    10684 | zSTALLED VEHICLE - SAVED
    10685 | COLLISION - SAVED
    10686 | Crash Urgent - SAVED
    10687 | COLLISION WITH INJURY - SAVED
    10688 | COLLISION - SAVED
    10689 | COLLISION - SAVED
    10690 | Crash Service - SAVED
    10691 | COLLISION - SAVED
    10692 | Crash Service - SAVED

    ......
    
    232730 | Traffic Hazard - SAVED
    232731 | COLLISION WITH INJURY - SAVED
    232732 | Traffic Hazard - SAVED

    In [3]: 
    Do you really want to exit ([y]/n)? 


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy shipwell

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html

Deployment
----------

The following details how to deploy this application.

Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html
