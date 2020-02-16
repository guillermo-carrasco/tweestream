import click

from twistream.log import log
from twistream.twitter import twitter

LOG = log.get_logger()


@click.group(invoke_without_command=True)
@click.option('--log-level', type=click.Choice(['INFO', 'DEBUG', 'ERROR']),
              default='INFO')
@click.option('--hashtags', type=click.STRING,
              help='Comma separated list of hashtags to follow (exclude #)')
@click.pass_context
def main(ctx, log_level, hashtags):
    log.set_level(log_level)
    ctx.obj = {
        'log_level': log_level,
        'hashtags':hashtags
    }
    hashtags = [h for h in hashtags.split(',')] if hashtags is not None else []
    LOG.debug(f"Listening for tweets with hashtags: {', '.join(hashtags)}")

    # Initialize stream listener ans start listening
    twitter.listen_hashtags(hashtags)
