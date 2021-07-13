import re

# functin to calculate profanity score of input tweet


def profanityScoreOfTweet(tweetContent):
    tweetProfanityScore = 0
    # check the tweet against every defined slur
    for slur in slurs:
        slurTitle = slur[0]
        slurScore = slur[1]
        # the regex pattern can further be optimised using The Levenshtein Distance
        slurPattern = r'' + slurTitle + ''
        # check if the slur was found in the tweet, if yes increment its profanity score as per the score of the slur
        slurFind = re.search(slurPattern, tweetContent, re.IGNORECASE)
        if slurFind:
            tweetProfanityScore += slurScore
    return tweetProfanityScore


# read slurs from the .txt file
slursFile = open('slursFile.txt', 'r')
slurs = []
for slur in slursFile:
    slur = slur.split(',')
    slur[1] = int(slur[1].strip())
    slurs.append(slur)

# read tweets from the .txt file, create a dictionary of tweet excerpts alongside their scores
tweetsFile = open('tweetsFile.txt', 'r')
tweets = {}
for tweet in tweetsFile:
    tweetProfanityScore = profanityScoreOfTweet(tweet)
    tweets[tweet[0:10]] = tweetProfanityScore

# output
print(tweets)
