# iot_repo

sudo lsof -t -i:8000
sudo kill -9 <PID>

usn: piero
pwd: admin

VOICE to speech technology. 

### WORKER SHELL
celery -A celery_test  worker -l info -B

### BEAT SHELL
celery -A celery_test beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler