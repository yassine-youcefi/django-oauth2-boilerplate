import json
from django_redis import get_redis_connection

class RedisPublisher:
    def __init__(self):
        # Get a connection to your Redis server
        self.redis_conn = get_redis_connection("default")

    def publish_message(self, channel_name, message):
        # Publish the message to the channel
        self.redis_conn.publish(channel_name, json.dumps(message))

if __name__ == "__main__":
    # Initialize the RedisPublisher with your desired channel name
    publisher = RedisPublisher()

    # Define the message you want to publish
    message = {
        'recipient': ['youcefi@skyloov.com', 'ibrahim.elkhalil@skyloov.com'],
        'message': 'test pub/sub'
    }

    # Publish the message to the Redis channel
    publisher.publish_message('skyloov_communiverse_mailing', message)
