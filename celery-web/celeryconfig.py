from celery.schedules import crontab

broker='pyamqp://guest@localhost//',
backend='rpc://',
include=['tasks']

beat_schedule = {
    'every-5-seconds': {
        'task': 'tasks.call_api_schedule',
        'schedule': crontab('*', '*', '*', '*', '*')
    },
}