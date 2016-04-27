 DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Make sure you do `pip install psycopg2`
         'NAME':'database_name',
         'USER': 'database_user',  # Database user name might be `postgres`
         'PASSWORD': 'database_password_123',
         'HOST': '192.168.1.2',  # Database host IP Address
         'PORT': '5432',  # Database host TCP Port
     },
}
