# FITMINDER 

## A reminder with scheduling capability controlled with Fitminder Application using Python-Django Web Development.

##### Keywords: Python, Django, Django_Celery_Beat, Redis, RaspberryPi, Automated Schedule, Periodic Tasks, Reminders


## FITMINDER Application Configuration - links to documentation:

#### Python-Django-Celery 

[[1] - developer.mozilla.org ](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment)


[[2] -  virtualenvwrapper ](https://virtualenvwrapper.readthedocs.io/en/latest/)


[[3] - Django Documentation](https://docs.djangoproject.com/en/3.2/)

#### Celery + Redis as broker for AUTOMATED SCHEDULING on Django App - Server

Redis Install guide
https://www.rosehosting.com/blog/how-to-install-configure-and-use-redis-on-ubuntu-16-04/

Django - celery config 
https://medium.com/@yedjoe/celery-4-periodic-task-in-django-9f6b5a8c21c7

#### Geolocation Service from browser
https://docs.djangoproject.com/en/1.11/ref/contrib/gis/geoip/

#### Weather API
https://www.weatherapi.com/docs/

#### Random Joke API - Fortune
https://pypi.org/project/django-fortune/0.1/


# HOW TO PREPARE ENVIRONMENT TO RUN THE FITMINDER APP

=> Install pip3 package manager
``` bash
sudo apt-get install pip
python3 -m pip install --upgrade pip
```

=> Install virtual environment package
``` bash
sudo pip3 install virtualenvwrapper

```
=> Navigate into .bashrc configuration file & adding the code from below

```bash 
nano ~/.bashrc
```
=> Add Python VirtualEnv config like below.

```bash 
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS=' -p /usr/bin/python3 '
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
```

=> Applying changes

```bash 
source ~/.bashrc
```

=> Creating and enabling working virtual envirnment with mkvirtualenv <name_of_Venv>

```bash 
# mkvirtualenv <name_of_environment>
mkvirtualenv fitenv
```

=> Should return: 
``` bash
created virtual environment CPython3.8.5.final.0-64 in 99ms
  creator CPython3Posix(dest=/home/piero/.virtualenvs/fitenv, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/piero/.local/share/virtualenv)
    added seed packages: pip==20.3.3, setuptools==51.3.3, wheel==0.36.2
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator
```


# DEVELOPMENT ENVIRONMENT - RUN APPLICATION GUIDE

### 1. Clone Fitminder (iot_repo) from github to your diskspace
```bash 
git clone https://github.com/PieroH/iot_repo/
```

### 2. Enable virtual environment created above.
```bash 
  workon <name_of_Venv>
```

### 3. Install pip and all required packages with compatible versions from requirements.txt file
```bash 
pip install -r requirements.txt
```

### 4. Run Main Server from Fitminder App at directory based path (with manage.py)
```bash 
  python3 manage.py runserver
```

### 5. Celery Worker Running In Terminal Window
```bash
celery -A fitminder  worker -l info -B
```

### 6. In another, Celery_Beat should scan for periodic tasks saved in the PeriodicTasks.models.

[[6] - Django_Celery_Beat](https://github.com/celery/django-celery-beat)
```bash
celery -A fitminder beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

### 7. Enjoy Fitminder App!


# Troubleshooting techniques for development environment
```bash
# PORT IN USE - kill port
sudo lsof -t -i:8000
sudo kill -9 <PID>
```

### Redis Server CLI Log: 

```bash 
redis-cli
```
### Clean Celery (Purge)

```bash 
celery -A fitminder purge
```




