## Why ?
I'm going to write a post/tip on coderwall about this so I need some code to show how this is working.

## What you need to run this:
1. celery ```pip install celery-with-redis```
2. requests ```pip install requests```
3. predis ```composer install```
4. redis

## How to run this ?
1. run celery: ```celery worker --app=github```
2. add task from php ```php php/celery-put.php```
3. copy task id and do ```php php/celery-get.php $ID```
