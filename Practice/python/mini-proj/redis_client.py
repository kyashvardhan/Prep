import redis
from app.config import REDIS_HOST, REDIS_PORT, REDIS_CHANNEL

# Initialize Redis client
r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def publish_message(message: str):
    """
    Publish a message to the configured Redis channel.
    """
    r.publish(REDIS_CHANNEL, message)

def subscribe_to_channel():
    """
    Subscribe to the configured Redis channel and return the pubsub object.
    """
    pubsub = r.pubsub()
    pubsub.subscribe(REDIS_CHANNEL)
    return pubsub
