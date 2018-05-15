import os

import yaml

from twistream.log import log

LOG = log.get_logger()

CONFIG_DIR = os.path.join(os.environ['HOME'], '.twistream')
CONFIG_FILE = os.path.join(os.environ['HOME'], '.twistream', 'twistream.yml')

def check_config():
    """ Check that configuration directory exists and creates it otherwise
    """
    if not os.path.exists(CONFIG_DIR):
        os.mkdir(CONFIG_DIR)

def get_log_file():
    """ Returns path to the log file
    """
    check_config()
    return os.path.join(CONFIG_DIR, 'twistream.log')


def get_config(subsection=None):
    """ Return configuration object

    Params:
        subsection - str: Return a subsection of the configuration
    Returns:
        configuration - dict: The configuration object
    """
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = yaml.load(f)
    except FileNotFoundError:
        LOG.warn('Configuration file not found, not using configuration')

    return config.get(subsection, {}) if subsection else config
