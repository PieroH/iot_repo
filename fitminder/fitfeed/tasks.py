from __future__ import absolute_import, unicode_literals
from celery import group, shared_task

import time


@shared_task()
def task_sum(a, b):
	time.sleep(10)
	return a + b

