import click
import os

from twistream.log import logging

LOG = logging.get_logger()


@click.command()
@click.option('--log-level',
              type=click.Choice(['INFO', 'DEBUG', 'ERROR']),
              default='INFO')
@click.option('--hashtags',
              type=click.STRING,
              help='Comma separated list of hashtags to follow (exclude #)')
def main(log_level, hashtags):
    LOG.setLevel(log_level)
    hashtags = [h for h in hashtags.split(',')] if hashtags is not None else []
    LOG.debug(f"Using hashtags: {', '.join(hashtags)}")
