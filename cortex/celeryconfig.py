from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'every-5-seconds': {
        'task': 'tasks.call_api_schedule',
        'schedule': timedelta(seconds=5),
    },
}