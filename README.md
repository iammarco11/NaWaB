# NaWaB bot
![Status](https://img.shields.io/badge/Status-Under_Development-Red.svg) 

## What is it?
This bot is a content curator for the topics related to the networks. Made with python and twitter API, it is the best solution to be updated in the latest technologies, developements and discussion of networks on twitter.

## Features of NaWaB bot
* Scrapes all the tweets related to networks and retweets. The retweeted public tweets will have at least one among the listed hashtags in the `protobuf_list.txt`.
* When running the script, it logs errors, results and the id of the retweeted tweets into different files.
* The `blacklist.txt` contains the blacklisted accounts username, whose tweets would be ignored by the bot.
* The `banwords.txt` contains the banned words which again would be ignored by the bot.
* The `whitelist.txt` contains the whitelisted acccounts usernames, whose tweets would be tweeted

## Getting Started
* Clone the repository
```
$ git clone https://github.com/Aniketh01/NaWaB.git
```
* Create a virtual environment to install the necessary python packages for this script. For this:

``` 
$ virtualenv -p /usr/bin/python3 <virtualenv name> 
```

* Activate the virtualenv

```
$ source <virtualenv name>/bin/activate
```

* Install all the required packages 
```
$ pip install -r requirements.txt
```

* Run the script
```
$ python3 nawab_bot.py
```

## Developers 
1. [Aniketh Girish](https://github.com/Aniketh01/)
2. [Ananthanandanan](https://github.com/ananthanandanan)
3. [Akshay Praveen Nair](https://github.com/iammarco11/)

## Want to contribute?
Take a look at the issues listed [here](https://github.com/Aniketh01/NaWaB/issues)
