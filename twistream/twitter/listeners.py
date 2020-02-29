from tweepy import StreamListener

from twistream.log import log

LOG = log.get_logger()


class HashtagListener(StreamListener):

    def __init__(self, backend, exclude_retweets):
        StreamListener.__init__(self)
        self.backend = backend
        self.exclude_retweets = exclude_retweets

    def on_error(self, status_code):
        if status_code == 401:
            LOG.error('Authorization went wrong...')
            return False

        if status_code == 420:
            # returning False in on_error disconnects the stream
            return False

        # returning non-False reconnects the stream, with backoff.

    def on_status(self, status):
        if self.exclude_retweets and hasattr(status, 'retweeted_status'):
            pass

        else:
            LOG.debug(status.text)
            self.backend.persist_status(status)
