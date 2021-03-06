=================
django-newsletter
=================

.. image:: https://secure.travis-ci.org/dokterbob/django-newsletter.png
    :target: http://travis-ci.org/dokterbob/django-newsletter

Newsletter application for the Django web framework.
----------------------------------------------------

What is it?
===========
Django app for managing multiple mass-mailing lists with both plaintext as
well as HTML templates with rich text widget integration, images and a
smart queueing system all right from the admin interface.

Status
======
We are currently using this package in several large to medium scale production environments, but it
should be considered a permanent work in progress.

Translations
============
Most of the strings have been translated to Dutch and a German translation should be available soon. Feel free to contribute any translations through `Transifex <http://www.transifex.net/projects/p/django-newsletter/>`_.

Requirements
============
Please refer to `requirements.txt <http://github.com/dokterbob/django-newsletter/blob/master/requirements.txt>`_ for an updated list of required packes.

Installation
============
#)  Get it from the Cheese Shop::

	pip install django-newsletter

    **Or** get the latest & greatest from Github and link it to your
    application tree::

	pip install -e git://github.com/dokterbob/django-newsletter.git#egg=django-newsletter

    (In either case it is recommended that you use
    `VirtualEnv <http://pypi.python.org/pypi/virtualenv>`_ in order to
    keep your Python environment somewhat clean.)

#)  Add newsletter and to ``INSTALLED_APPS`` in settings.py and make sure that
    your favourite rich text widget and django-extensions are there as well::

	INSTALLED_APPS = (
	    ...
	    'imperavi',
	    'django_extensions',
	    ...
	    'newsletter',
	    ...
	)

#)  Set the path to your preferred rich text widget (optional). If not set,
    django-newsletter will fall back to Django's default TextField widget::

	# Using django-imperavi
	NEWSLETTER_RICHTEXT_WIDGET = "imperavi.widget.ImperaviWidget"

        # Using django-tinymce
	NEWSLETTER_RICHTEXT_WIDGET = "tinymce.widgets.TinyMCE"

#)  Import subscription, unsubscription and archive URL's somewhere in your
    `urls.py`::

	urlpatterns = patterns('',
	    ...
	    (r'^newsletter/', include('newsletter.urls')),
	    ...
	)

#)  Enable Django's `staticfiles <http://docs.djangoproject.com/en/dev/howto/static-files/>`_
    app so the admin icons, CSS and JavaScript will be available where
    we expect it.

#)  Create required data structure and load default template fixture::

	./manage.py syncdb
	./manage.py loaddata default_templates

#)  Change the default contact email listed in
    ``templates/newsletter/subscription_subscribe.html`` and
    ``templates/newsletter/subscription_update.html``.

#)  Run the tests to see if it all works::

	./manage.py test

    If this fails, please contact me!
    If it doesn't: that's a good sign, chap. You'll probably have yourself a
    working configuration!

#)  Add jobs for sending out mail queues to `crontab <http://linuxmanpages.com/man5/crontab.5.php>`_::

	@hourly /path/to/my/project/manage.py runjobs hourly
	@daily /path/to/my/project/manage.py runjobs daily
	@weekly /path/to/my/project/manage.py runjobs weekly
	@monthly /path/to/my/project/manage.py runjobs monthly


Usage
=====
#) Start the development server: ``./manage.py runserver``
#) Navigate to ``/admin/`` and: behold!
#) Put a submission in the queue.
#) Submit your message with ``./manage.py runjob submit``
#) For a proper understanding, please take a look at the `model graph <https://github.com/dokterbob/django-newsletter/raw/master/graph_models.png>`_.

.. image:: https://github.com/dokterbob/django-newsletter/raw/master/graph_models.png

Unit tests
==========
Fairly extensive tests are available for internal frameworks, web
(un)subscription and mail sending. Sending a newsletter to large groups of recipients 
(+10k) has been confirmed to work in multiple production environments.
Please to note that the unittests (or actually, Django) currently
requires a `404.html` in your `templates` directory in order to be able to
test 404 responses.

License
=======
This application is released
under the GNU Affero General Public License version 3.
