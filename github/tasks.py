'''
Tasks for celery
'''
from __future__ import absolute_import

from celery import Task
from github.celery import celery
import requests

class DebugTask(Task):#pylint: disable=R0904, W0223
    '''
    Debug tasks
    '''
    abstract = True

    def after_return(self, *args, **kwargs):
        print('Task returned: %r' % (self.request, ))
    
    def on_failure(self, *args, **kwargs):
        print "FAILURE"
        print('Task returned: %r' % (self.request, ))

    def on_retry(self, *args, **kwargs):
        print "RETRY"
        print('Task returned: %r' % (self.request, ))

@celery.task(base=DebugTask)
def get_issues(user, repo, status):
    try:
        url = 'https://api.github.com/repos/{user}/{repo}/issues?state={status}' \
        .format(status=status, user=user, repo=repo)

        request_data = requests.get(url)
        return request_data.json()
    except Exception, exc:
        raise get_issues.retry(exc = exc, countdown=5)