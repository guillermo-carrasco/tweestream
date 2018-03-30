# Twistream: Twitter Stream API data collection

Twistream helps you automatically collect and store data from Twitter Stream API.

## Installation

From source:

    git clone https://github.com/guillermo-carrasco/twistream.git
    cd twistream
    pip install .

From PyPi:

    pip install twistream

### Setting up

You need your twitter credentials in order to be able to use Twitter API. For that,
create an application [here](https://apps.twitter.com). Once created, create a configuration
file and add the credentials there:

```
~> cat ~/.twistream/twistream.yml      

twitter:                  
  consumer_key: your_consumer_key                   
  consumer_secret: your_consumer_secret             
  access_token_key: your_access_token_key             
  access_token_secret: your_access_token_secret       

logging:                  
  log_level: INFO         

persist:                  
  engine: sqlite
```

## Usage
