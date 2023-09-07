from django_redis import get_redis_connection

class RedisSubscriber:
    def __init__(self):
        # Get a connection to your Redis server
        self.redis_conn = get_redis_connection("default")

    def listen(self, channel_name):
        # Subscribe to the channel and listen for messages
        pubsub = self.redis_conn.pubsub()
        pubsub.subscribe(channel_name)
        
        for message in pubsub.listen():
            if message['type'] == 'message':
                print('Message : ', message)
               

if __name__ == "__main__":
    # Initialize the RedisSubscriber with your desired channel name
    subscriber = RedisSubscriber()

    # Start listening for messages
    subscriber.listen("skyloov_communiverse_mailing")
