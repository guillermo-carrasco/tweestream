import tweepy

from twistream.log import log

LOG = log.get_logger()


class HashtagListener(tweepy.StreamListener):

    def on_error(self, status_code):
        if status_code == 401:
            LOG.error('Authorization went wrong...')
            return False

        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False

        # returning non-False reconnects the stream, with backoff.

    def on_status(self, status):
        print(status.text)
