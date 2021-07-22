# FITMINDER 

## A reminder with scheduling capability controlled with Fitminder Application using Python-Django Web Development.

### Keywords: Python, Django, Django_Celery_Beat, Redis, RaspberryPi, Automated Schedule, Periodic Tasks, Reminders


#### Trouble shooting techniques for development
```bash
# PORT IN USE
sudo lsof -t -i:8000
sudo kill -9 <PID>
```





## DEV - RUN APP requirements
#### 1. Run Main Server from Fitminder App at directory based path (with manage.py)
```bash 
  python3 manage.py runserver
```
#### 2. Celery Worker Running In Terminal Window
```bash
celery -A celery_test  worker -l info -B
```

#### 3. In another, Celery_Beat should scan for periodic tasks saved in the PeriodicTasks.models.

[[6] - Django_Celery_Beat](https://github.com/celery/django-celery-beat)
```bash
celery -A celery_test beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```




```bash 
```
## FITMINDER Application Configuration

#### Python-Django-Celery 

[[1] - developer.mozilla.org ](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment)


[[2] -  virtualenvwrapper ](https://virtualenvwrapper.readthedocs.io/en/latest/)


[[3] - Django Documentation](https://docs.djangoproject.com/en/3.2/)




=> Installing virtual environment package
``` bash
sudo pip3 install virtualenvwrapper

```
=> Navigating into .bashrc configuration file & adding the code from below

```bash 
nano ~/.bashrc
```
=> Adding Python VirtualEnv config.

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
=> Install pip and all required packages with compatible versions from requirements.txt file

```bash 
# Get pip
sudo apt-get install pip

# upgrade
python3 -m pip install --upgrade pip

# Install all packages from Requirements.txt
pip install -r requirements.txt
```

##### CRON 

##### Celery + Redis as broker for AUTOMATED SCHEDULING on Django App - Server

Redis Install guide
https://www.rosehosting.com/blog/how-to-install-configure-and-use-redis-on-ubuntu-16-04/

Django - celery config 
https://medium.com/@yedjoe/celery-4-periodic-task-in-django-9f6b5a8c21c7


## Celery Worker Running In Terminal Window


```bash
$ celery -A celery_test  worker -l info -B


[2021-07-10 20:41:51,725: INFO/MainProcess] Task scheduler.views.task1[b68765ec-a04f-476b-97c6-6cab2a83c383] received
[2021-07-10 20:41:51,727: WARNING/ForkPoolWorker-2] ---- ITS WORKING!!! ----
[2021-07-10 20:41:51,728: WARNING/ForkPoolWorker-2]  
[2021-07-10 20:41:51,728: WARNING/ForkPoolWorker-2] Created Message!
[2021-07-10 20:41:51,728: WARNING/ForkPoolWorker-2] 

```

### In another, Celery_Beat should scan for periodic tasks saved in the PeriodicTasks.models.

[[6] - Django_Celery_Beat](https://github.com/celery/django-celery-beat)
```bash

$ celery -A celery_test beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler

[2021-07-11 13:10:00,317: INFO/MainProcess] Scheduler: Sending due task RPI TASK (scheduler.views.task1)

```
### Redis Server CLI Log: 


```bash 
redis-cli
```

### Clean Celery (Purge)

```bash 
celery -A celery_test purge
```

## RPI

python manage.py runserver 0.0.0.0:8080



### Geolocation Service from browser
https://docs.djangoproject.com/en/1.11/ref/contrib/gis/geoip/


### Weather API
https://www.weatherapi.com/docs/