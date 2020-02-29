import os

import yaml
from click.testing import CliRunner

from twistream.cli import cli


def test_twistream_no_args():
    """No params should trigger the help command"""

    runner = CliRunner()
    result = runner.invoke(cli.twistream)
    assert result.exit_code == 0
    assert 'Usage: ' in result.output


def test_twistream_help():
    """--help should show usage"""

    runner = CliRunner()
    result = runner.invoke(cli.twistream, ['--help'])
    assert result.exit_code == 0
    assert 'Usage: twistream' in result.output


def test_twistream_init():
    """Test configuration file initialization"""

    # Emulate user input for the init command
    input_cli = [
        'consumer_key',
        'consumer_secret',
        'access_token',
        'access_token_secret',
        'sqlite',
        'test.db',
        'test.yaml',
    ]

    runner = CliRunner()
    result = runner.invoke(cli.twistream, ['init'], input='\n'.join(input_cli))
    assert result.exit_code == 0

    # Check that a configuration file has been created
    with open('test.yaml', 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    # Check all the sections have been created
    assert [s in config.keys() for s in ['twitter', 'backend', 'backend_params']], \
        'Sections in the configuration file are not correct'

    # Check that the contents of the sections correspond to the user input
    assert config.get('twitter').get('consumer_key') == 'consumer_key'
    assert config.get('twitter').get('consumer_secret') == 'consumer_secret'
    assert config.get('twitter').get('access_token') == 'access_token'
    assert config.get('twitter').get('access_token_secret') == 'access_token_secret'

    assert config.get('backend') == 'sqlite'
    assert config.get('backend_params').get('db_path') == 'test.db'

    os.remove('test.yaml')


def test_twistream_collect_no_params():
    """Collect without params should trigger usage"""

    runner = CliRunner()
    result = runner.invoke(cli.twistream, ['collect'])
    assert result.exit_code == 2  # calling with no arguments does not return "correct"
    assert 'Usage: twistream collect' in result.output


def test_twistream_collect_no_tracks():
    """--track option is required"""

    runner = CliRunner()
    result = runner.invoke(cli.twistream, ['collect', 'test.yaml'])
    assert result.exit_code == 2  # calling with no arguments does not return "correct"
    assert 'Missing option "--tracks"' in result.output
