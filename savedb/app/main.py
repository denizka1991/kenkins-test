from google.cloud import pubsub_v1
from pymongo import MongoClient
import base64

import json


def message_from_topic1(request, message):
    project_id = "dynamic-circle-235118"
    subscription_name = "topic1"

    subscriber = pubsub_v1.SubscriberClient()

    subscription_path = subscriber.subscription_path(
        project_id, subscription_name)

    def callback(message):
        print('Received message: {}'.format(message))
        message.ack()

    subscriber.subscribe(subscription_path, callback=callback)

    client = MongoClient('mongodb://main_admin:abc123@35.241.132.65/mysinoptik', 27017)
    db = client.mysinoptik
    collection_weth = db.weather
    if not request:
        return 0
    c = request
    b = base64.b64decode(c['data'])
    d = b.decode('utf-8')
    a = json.loads(d)

    collection_weth.insert_one(a)

    print('Listening messages {0}, {1}'.format(c, type(c)))