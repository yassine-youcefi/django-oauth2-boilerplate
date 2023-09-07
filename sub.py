import redis
import json
from django.conf import settings

# Initialize a Redis client
# redis_client = redis.StrictRedis(host='192.168.70.98', port=6379, db=0)
redis_client = redis.StrictRedis(host='redis-oauth2', port=6379, db=9)

# Define the channel to subscribe to
channel = 'skyloov_communiverse_mailing'

# Create a pubsub instance and subscribe to the channel
pubsub = redis_client.pubsub()
pubsub.subscribe(channel)


# Listen for messages and print them
for message in pubsub.listen():

    if message['type'] == 'message':
        print('Message : ', message)

        my_dict = json.loads(message['data'])
        print(f"recipient : {my_dict['recipient']}")            
        print(f"message : {my_dict['message']}")    