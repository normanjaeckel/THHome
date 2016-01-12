========
 THHome
========

THHome is still under development.


Local development
-----------------

To setup a local development version run::

    $ virtualenv .virtualenv --python=python3
    $ source .virtualenv/bin/activate
    $ pip install -U pip
    $ pip install --requirement requirements.txt
    $ python manage.py migrate
    $ python manage.py createsuperuser
    $ sed -i 's/DEBUG = False/DEBUG = True/' THHome_deployment/settings.py
    $ python manage.py runserver

To check coding styles run::

    $ pip install flake8 isort
    $ flake8 --exclude="THHome/migrations/" manage.py THHome
    $ isort --multi_line 3 --check-only --skip THHome/migrations --recursive manage.py THHome


Template
--------

`Start Bootstrap - Creative
<http://startbootstrap.com/template-overviews/creative/>`_, Copyright
2013-2015 Iron Summit Media Strategies, LLC. Code released under the
`Apache 2.0
<https://github.com/IronSummitMedia/startbootstrap-creative/blob/gh-pages/LIC
ENSE>`_ license.
