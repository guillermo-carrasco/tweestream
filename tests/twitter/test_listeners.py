from unittest.mock import patch

from twistream.twitter.listeners import TwistreamListener


@patch("twistream.backends.sqlite.SqliteStorageBackend", autospec=True)
def test_twistream_listener_filters_replies(mocked_backend, reply_status):

    listener = TwistreamListener(mocked_backend)

    listener.on_status(reply_status)
    listener.backend.persist_status.assert_called_with(reply_status)
    listener.backend.reset_mock()

    listener.exclude_replies = True
    listener.on_status(reply_status)
    listener.backend.persist_status.assert_not_called()


@patch("twistream.backends.sqlite.SqliteStorageBackend", autospec=True)
def test_twistream_listener_filters_quotes(mocked_backend, quoted_status):

    listener = TwistreamListener(mocked_backend)

    listener.on_status(quoted_status)
    listener.backend.persist_status.assert_called_with(quoted_status)
    listener.backend.reset_mock()

    listener.exclude_quotes = True
    listener.on_status(quoted_status)
    listener.backend.persist_status.assert_not_called()


@patch("twistream.backends.sqlite.SqliteStorageBackend", autospec=True)
def test_twistream_listener_filters_retweets(mocked_backend, retweeted_status):

    listener = TwistreamListener(mocked_backend)

    listener.on_status(retweeted_status)
    listener.backend.persist_status.assert_called_with(retweeted_status)
    listener.backend.reset_mock()

    listener.exclude_retweets = True
    listener.on_status(retweeted_status)
    listener.backend.persist_status.assert_not_called()
