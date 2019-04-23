from google.cloud import pubsub_v1
import json
import requests

def get_data_from_api(request):
    project_id = "dynamic-circle-235118"
    topic_name1 = "topic1"

    publisher = pubsub_v1.PublisherClient()

    topic_path1 = publisher.topic_path(project_id, topic_name1)


    list_of_city = [703447, 698740, 702550, 706483, 709930, 707471, 710719, 689558, 703845, 690548]
    apikey = '688bc3704f60250be00b93ccbdbf7c9b'

    for i in list_of_city:
        r = requests.get('http://api.openweathermap.org/data/2.5/weather?id={0}&APPID={1}'.format(i, apikey))
        data = json.loads(r.content)
        data_topic1 = json.dumps(data).encode('utf-8')
        future1 = publisher.publish(topic_path1, data=data_topic1)

        print(future1.result(), data_topic1)

    return 1