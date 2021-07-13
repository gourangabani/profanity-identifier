
# Profanity Score Calculator for Tweets

A simple implementation to identify racial slurs in tweets, and rate them based on the intensity of the abuse.

## Usage

The module depends on two external .txt files for input, both of which should be in the same working directory. 

### slursFile.txt

This file would contain a list of all the slurs that need to be identified, alongside a relative score of the intensity of their abuse as compared against other slurs, both separated by a comma and each pair on a new line, as exemplified below:

```
diff,1
natives,9
```

### tweetsFile.txt

This file would store a list of all the tweets that need to be analysed, each on a new line, as demonstrated below:

```
Your not much diff from natives when it comes to drinking ... Except your clean
Dad cuts up Water Melon for my lunch, looks at me and says ‘Here’s your nigger food’.” #Hahaha #LoveYou
This group of chinks on the bus f***ing wreak I’m gagging and covering my face in my shirt
I think I hate cardio as much as I hate paki’s
Man these pakis need to leave the gym it’s starting to smell like stale Burger King in here
Drunk natives brushing his pony tail on me #help #gross
When my friends make me sit next to the nigger in the theater ... #thanksbitches
```

### profanityIdentifier.py

The main script should be run in a Python 3 environment, with the above requisite files in the same presnt and populated with relevant data in the same directory.

After changing the working directory, the following command should be executed in a terminal window:

```console
python profanityIdentifier.py
```

## Assumptions & Data

The above tweets were sourced from [https://firstmonday.org/article/view/5450/4207](https://firstmonday.org/article/view/5450/4207) after a random search on commonly used racial slurs on Twitter. The list of specific racial slurs have randomly been selected from the tweets.

## Disclaimer

Any profane language used in the above example(s) is solely for the purpose of demonstration, and not intended for any person or entity in general, or particular.

## Improvements

As per the above example, this module wasn't able to identify slurs that were slightly misspelled, or had a few letters replaced with aesterisks. A solution for this could be the incorporation of The Levenshtein Distance; by identifying slight misspells (intentional or random), the capability of identifying slurs would increase substantially.