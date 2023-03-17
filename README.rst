========
 THHome
========

THHome is still under development.


Local development
-----------------

To setup a local development version run::

    $ python -m venv .virtualenv
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


Credits
-------

The used template is `Creative
<http://startbootstrap.com/template-overviews/creative/>`_. The code of
this template was released under the `Apache 2.0
<https://github.com/IronSummitMedia/startbootstrap-creative/blob/gh-pages/LICENSE>`_
license by `Start Bootstrap <http://startbootstrap.com/>`_, Iron Summit
Media Strategies, LLC.
