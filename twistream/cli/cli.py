import click
import os

from dateutil.parser import parse

from twistream.log import logging

LOG = logging.get_logger()


def validate_date(ctx, args, date):
    try:
        return parse(date)
    except ValueError:
        raise click.BadParameter('Dates should be in format YY-MM-DDTHH:MM:SS')


@click.group(invoke_without_command=True)
@click.option('--log-level', type=click.Choice(['INFO', 'DEBUG', 'ERROR']),
              default='INFO')
@click.option('--hashtags', type=click.STRING,
              help='Comma separated list of hashtags to follow (exclude #)')
@click.pass_context
def main(ctx, log_level, hashtags):
    LOG.setLevel(log_level)
    ctx.obj = {
        'log_level': log_level,
        'hashtags':hashtags
    }
    hashtags = [h for h in hashtags.split(',')] if hashtags is not None else []
    LOG.debug(f"Using hashtags: {', '.join(hashtags)}")


@main.command(help='Schedule when to read from Twitter Stream API')
@click.argument('from-date', callback=validate_date,)
@click.argument('to-date', callback=validate_date)
@click.pass_context
def schedule(ctx, from_date, to_date):
    print(ctx.obj)
