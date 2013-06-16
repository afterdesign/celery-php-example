<?php

require 'vendor/autoload.php';

$redis = new Predis\Client();

$task = array(
    'task' => 'github.tasks.get_issues',
    'kwargs' => array(
        'repo' => 'MacTerminal',
        'status' => 'open',
        'user' => 'afterdesign'
    ),
    'retries' => 0,
    'expires' => null
);

$task['id'] = sha1(json_encode($task['kwargs']).time());

$bodyTask = array(
    'body' => base64_encode(json_encode($task)),
    'headers' => new stdClass,
    'content-type' => 'application/json',
    'properties' => array(
        'body_encoding' => 'base64',
        'delivery_info' => array(
            'priority' => 0,
            'routing_key' => 'github',
            'exchange' => 'github'
        ),
        'delivery_tag' => sha1(base64_encode(json_encode($task)).time()),
        'delivery_mode' => 2
    ),
    'content-encoding' => 'utf-8'
);

echo "celery-task-meta-".$task['id']."\n";
$redis->lPush('github', json_encode($bodyTask));