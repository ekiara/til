Python, string to date

$ python
Python 3.5.0 (default, Dec  3 2015, 12:22:39) 
[GCC 4.8.3 20140911 (Red Hat 4.8.3-7)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import datetime
>>> datetime.datetime.strptime('20151101', '%Y%m%d')
datetime.datetime(2015, 11, 1, 0, 0)
>>> exit()
