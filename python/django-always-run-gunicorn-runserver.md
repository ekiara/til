In development you should always run (at the very minimum):

`gunicorn name_of_my_core_app.wsgi -b 0.0.0.0:1337`

Reason for this is that this:

`python ./manage.py runserver 0.0.0.0:1337`

is prone to weird errors, and unresponsive bugs
