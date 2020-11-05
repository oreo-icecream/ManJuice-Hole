import tweepy
import wget
import os
import random
import linecache
import requests

auth = tweepy.OAuthHandler("<API Key>", "<API Key Secret>")  # I removed the OAuthHandler thing, because you can tweet stuff using my bot's account using th9s thing
auth.set_access_token("<Token Key>", '<Token Key Secret>') # This too

api = tweepy.API(auth)

cum_text = [
    "https://raw.githubusercontent.com/oreo-icecream/CumTwitterBot/master/101_cum",
    "https://raw.githubusercontent.com/oreo-icecream/CumTwitterBot/testing/original_101_cum.txt",
]  # Downloads a text file (as of dd/mm/yy. It's text FILES)

# Variables and importent stuff ^


def CheckIfWrongOn():  # Function that checks if something is wrong with github/your internet.

    response = requests.get(cum_text[0])
    if response == 200:
        serveron = 1
    elif response != 200:
        serveron = 0
        print("Something is wrong! Response from the server: ")
        print(response)


# Functions ^

try:
    if os.path.exists("original_101_cum.txt") == True:

        if os.path.exists("101_cum.txt") == True:

            random_textfile = random.randint(1, 2) # Randomly selectes a file it will read from
            random_num = random.randint(1, 101)  # Random number generator

            filled_or_other = ["pumped", "filled", "loaded", "crammed", "filled up",]  # Things bot will add in the middle
            random_filled = random.choice(filled_or_other)  # Randomizer

            if random_textfile == 2:

                if (random_filled == filled_or_other[4]):  # If randomizer selected nr 4 aka "filled up" from filled_or_other. This code will run

                    filled_or_other = ["filled me up"]  # A copy from line 19
                    random_filled = random.choice(filled_or_other)  # A copy from line 20

                    my_daddy = ("My daddy " + random_filled + " full of " + linecache.getline("original_101_cum.txt",random_num))

                    #   api.update_status(my_daddy)  # And tweet is published
                    print("Tweet published! (and sent)")
                    print(my_daddy)
                else:

                    my_daddy = ("My daddy " + random_filled + " me full of " + linecache.getline("original_101_cum.txt", random_num))

                    #  api.update_status(my_daddy)
                    print("Tweet published! (and sent)")
                    print(my_daddy)

            if random_textfile == 1:

                if (random_filled == filled_or_other[4]):  # If randomizer selected nr 4 aka "filled up" from filled_or_other. This code will run

                    filled_or_other = ["filled me up"]  # A copy from line 19
                    random_filled = random.choice(filled_or_other)  # A copy from line 20

                    my_daddy = ("My daddy " + random_filled + " full of " + linecache.getline("101_cum.txt", random_num))  # I don't know how to explain this

                    #  api.update_status(my_daddy)  # And tweet is published
                    print("Tweet published! (and sent)")
                    print(my_daddy)
                else:

                    my_daddy = ("My daddy " + random_filled + " me full of " + linecache.getline("101_cum.txt", random_num))

                    # api.update_status(my_daddy)
                    print("Tweet published! (and sent)")
                    print(my_daddy)
        else:
            wget.download(cum_text[0], "101_cum.txt")
    else:
        CheckIfWrongOn()
        if serveron == 1:
            wget.download(cum_text[1], "original_101_cum.txt")
except:
    print("I'm sowwy usew-kun, but something is wwong with the scwipt OwO. Make a issue on my wepo.")