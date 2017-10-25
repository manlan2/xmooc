# xmooc
A Video Study Website with Django.
> tools

* Django
* Virtualenv
* Virtualenvwrapper
* Python2.7
* Xadmin
* PyCharm

> Packages

* Django==1.9.8
* DjangoUeditor==1.8.143
* MySQL-python==1.2.5
* Pillow==4.2.1
* django-crispy-forms==1.6.1
* django-formtools==2.0
* django-pure-pagination==0.3.0
* django-simple-captcha==0.5.5
* future==0.16.0
* gunicorn==19.7.1
* httplib2==0.9.2
* meld3==1.0.2
* olefile==0.44
* setproctitle==1.1.10
* six==1.10.0
* wsgiref==0.1.2

> install 

1. clone project:
```
git clone git@github.com:liuhaitao123/xmooc.git
```
2. modify `settings.py` file:
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
3. install packages:
```
pip install -r requirements.txt
```
4. makemigrations:
```
python manage.py makemigrations
```
5. migrate:
```
python manage.py migrate
```
6. create superuser:
```
python manage.py createsuperuser
```
7. run server:
```
python manage.py runserver
```

