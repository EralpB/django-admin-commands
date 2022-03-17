=====================
Django Admin Commands
=====================

A super simple library to allow admins to run Django management commands at panel. This saves admins from the hassle of ssh'ing into the servers, also gives more auditability since all the runtimes, commands, and outputs will be captured in the admin panel.

To understand the design decisions you can read the following blog posts where I justify the need for these cases.

https://eralpbayraktar.com/blog/django/2022/


Getting It
==========
::

    $ pip install django-admin-commands


Usage
=====

Add admincommands to your INSTALLED_APPS in settings.py.

Run ./manage.py migrate to have the CommandRunInstance created in your database.

(Optional) Allow granular access who can run/delete/view command run instances using Django's permissions system.

