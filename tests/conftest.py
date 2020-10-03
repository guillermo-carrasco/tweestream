import json
from pathlib import Path

import pytest
from tweepy import Status


def load_tweet(tweet_path: Path) -> Status:
    with open(tweet_path, "r") as f:
        tweet_json = json.load(f)

    return Status.parse(None, tweet_json)


@pytest.fixture(scope="module")
def original_status():
    """Returns an original tweet (no retweeted, no quoted, not a reply, etc.)"""
    return load_tweet(Path("tests/data/tweet_original.json"))


@pytest.fixture(scope="module")
def original_status_truncated():
    """Returns a tweet which content has been truncated"""
    return load_tweet(Path("tests/data/tweet_original_truncated.json"))


@pytest.fixture(scope="module")
def quoted_status():
    """Returns a quoted tweet"""
    return load_tweet(Path("tests/data/tweet_quoted.json"))


@pytest.fixture(scope="module")
def retweeted_status():
    """Returns a tweet that is a retweet"""
    return load_tweet(Path("tests/data/tweet_retweeted.json"))


@pytest.fixture(scope="module")
def reply_status():
    """Returns a tweet that is a reply to another tweet"""
    return load_tweet(Path("tests/data/tweet_is_reply.json"))
