<?php
require 'vendor/autoload.php';

$redis = new Predis\Client();

// Get data from celery worker. If it's empty celery probably is working on something already.
$value = json_decode($redis->get($argv[1]));

//status can be SUCCESS, FAILURE or RETRY
var_dump($value->status);

// So we don't need this anymore let's delete this.
$del = $redis->del($argv[1]);