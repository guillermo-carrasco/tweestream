import click
import tweepy

from twistream.log import log
from twistream.twitter import client, listeners
from twistream.backends.sqlite import SqliteStorageBackend

LOG = log.get_logger()

BACKENDS = {
    'sqlite': SqliteStorageBackend
}


@click.group(invoke_without_command=True)
@click.option('--log-level', type=click.Choice(['INFO', 'DEBUG', 'ERROR']),
              default='INFO')
@click.option('--hashtags', type=click.STRING,
              help='Comma separated list of hashtags to follow (exclude #)')
@click.option('--storage-backend', type=click.Choice(['sqlite']), default='sqlite',
              help='Storage backend')
def main(log_level, hashtags, storage_backend):
    log.set_level(log_level)

    hashtags = [h for h in hashtags.split(',')] if hashtags is not None else []

    LOG.info(f"Listening for tweets with hashtags: {', '.join(hashtags)}")
    LOG.info(f'Using {storage_backend} backend')

    # Initialize stream listener and start listening
    # TODO: Connection parameters should be read from somewhere else
    storage_backend = BACKENDS[storage_backend]('sqlite:////tmp/twistream.db')
    listener = listeners.HashtagListener(storage_backend)
    auth = client.get_api().auth
    stream = tweepy.Stream(auth=auth, listener=listener)
    stream.filter(track=hashtags)
