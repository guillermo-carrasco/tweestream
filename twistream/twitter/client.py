import tweepy

from twistream.config import config
from twistream.log import log

LOG = log.get_logger()


def _authorize():
    """ Authorization with Twitter API
    """
    auth_params = config.get_config(subsection='twitter')
    auth = tweepy.OAuthHandler(auth_params.get('consumer_key'),
                               auth_params.get('consumer_secret'))
    auth.set_access_token(auth_params.get('access_token'),
                          auth_params.get('access_token_secret'))

    return auth


def get_api():
    auth = _authorize()
    return tweepy.API(auth)
