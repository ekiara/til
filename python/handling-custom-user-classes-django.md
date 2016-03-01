Handlind custom user classes in Django 1.9+
----------------------------------------

>>> from django.contrib.auth import get_user_model

# Create a new users
>>> m = get_user_model()
>>> new_user = m()
>>> new_user.set_password('abcd')
>>> new_user.save()

# Retreive all the users
>>> m = get_user_model()
>>> all_users = m.objects.all()
