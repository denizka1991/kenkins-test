from google.cloud import pubsub_v1
import base64
import json
import redis


def message_from_topic2(request, message):
    project_id = "dynamic-circle-235118"
    subscription_name = "topic1"

    subscriber = pubsub_v1.SubscriberClient()
    r = redis.StrictRedis(host='35.187.98.192', port=6379, db=0)

    subscription_path = subscriber.subscription_path(
        project_id, subscription_name)

    def callback(message):
        print('Received message: {}'.format(message))
        message.ack()

    subscriber.subscribe(subscription_path, callback=callback)

    if not request:
        return 0
    c = request
    b = base64.b64decode(c['data'])
    d = b.decode('utf-8')
    a = json.loads(d)
    city = a['id']
    r.set(city, b)

    print('Listening messages {0}, {1}'.format(a, type(a)))