from tweepy import StreamListener

from twistream.log import log

LOG = log.get_logger()


class TracksListener(StreamListener):
    def __init__(self, backend, exclude_retweets=True, exclude_quotes=True, extended_text=True):
        StreamListener.__init__(self)
        self.backend = backend
        self.exclude_retweets = exclude_retweets
        self.exclude_quotes = exclude_quotes
        self.extended_text = extended_text

    def on_error(self, status_code):
        """Handles Twitter API error codes

        Check: https://developer.twitter.com/en/docs/basics/response-codes
        """
        # Authorization issues
        if status_code == 401:
            LOG.error("Authorization went wrong...")
            return False

        # Rate limit
        if status_code == 420 or status_code == 429:
            # returning False in on_error disconnects the stream
            return False

        # returning non-False reconnects the stream, with backoff.

    def on_status(self, status):
        """Action when a new tweet arrives"""

        if self.exclude_retweets and hasattr(status, "retweeted_status"):
            LOG.debug(f"Excluding {status.id}. Cause: Retweet")

        elif self.exclude_quotes and hasattr(status, "quoted_status"):
            LOG.debug(f"Excluding {status.id}. Cause: Quote")

        else:
            if self.extended_text and hasattr(status, "extended_tweet"):
                status.text = status.extended_tweet.get("full_text")
            self.backend.persist_status(status)
