from __future__ import print_function

import json

print('Loading function')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    print("value1 = " + event['key1'] + " from git")
    print("value2 = " + event['key2'] + " waddle doodle")
    print("value3 = " + event['key3'] + " from git")
    return event['key1'] + event['key2']  # Echo back the first key value and second
    #raise Exception('Something went wrong')

