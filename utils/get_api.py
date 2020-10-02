"""
Simple method to quickly get an API object, already authenticated, to work with interactively. It expects a config.yaml
file in the same directory where it is ran. This yaml file should contain twitter application credentials in the same
format expected by twistream. In fact, you can very well use the same configuration file.
"""
import yaml

from tweepy import API
from twistream.twitter import client


def get_api() -> API:
    with open("config.yaml", "r") as f:
        config = yaml.load(f, Loader=yaml.FlowMappingEndToken)

    return client.get_api(
        config.get("twitter").get("consumer_key"),
        config.get("twitter").get("consumer_secret"),
        config.get("twitter").get("access_token"),
        config.get("twitter").get("access_token_secret"),
    )
