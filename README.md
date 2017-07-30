# xmooc
A video study website with Django.
> tools

* Django
* Virtualenv
* Virtualenvwrapper
* Python2.7
* Xadmin
* PyCharm

> Packages

* Django == 1.9.8
* MySQL-python == 1.2.5
* Pillow == 4.1.1
* django-pure-pagination == 0.3.0
* django-simple-captcha == 0.4.6
* future == 0.16.0
* xadmin == 0.6.0 

> install 

1. clone project `git clone git@github.com:liuhaitao123/xmooc.git`
2. modify `settings.py` file :
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database name',
        'USER': 'user',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
3. install packages : `pip install -r requirements.txt`
4. makemigrations: `python manage.py makemigrations`
5. migrate: `python manage.py migrate`
6. create superuser: `python manage.py createsuperuser`
7. run server: `python manage.py runserver`

