import os

CONFIG_DIR = os.path.join(os.environ['HOME'], '.twistream')

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
