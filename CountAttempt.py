#CountVonCount'sSecretSauce

#Program created by Tyler Barron to solve the Riddler Express for September 16th 2016
#Designed to count up in english text to see which has a length of 140 or higher

#Works by looking at each 

import math
import random
#import time

single_list = ["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens_list = ["","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninty"]
big_number_names = ["","thousand","million","billion","trillion","quadrillion","quintillion","sextillion","septillion"]

#takes the last two numbers of a "chunk" (such as the 12 in 712) and turns it into a word
def tens_wordify(input):
    if input == 0:
        return("")
    if input <= 19: #1-19 have unique names
        return(single_list[input])
    else: #otherwise it follows the "tens place name" + "single number name" format
        return(tens_list[math.floor(input/10)-1]+" "+single_list[(input%10)])

#Looks up a number that can only be between zero and ten, inclusively.
def single_wordify(input):
    if input == 0:
        return("")
    if input <= 10:
        return(single_list[input])


#Handles the integer input -- slicing it into 3 number chunks. With these chunks it calls the single_wordify if there is a hundreds place and tens_wordify for the tens
# It then appends a big_number_name to the end, such as million or thousand before proceeding to the next chunk

def word_handler(input):
    word = ""
    for i in range (math.ceil(len(str(input))/3),0,-1): #handles numbers chunk-wise. ceil(len(input)) is the number of chunks
        bite_size_chunk = math.floor(input/1000**(i-1))%1000 #parses large number down to chunk
        if len(str(bite_size_chunk))== 3: #if there is a number in hundreds place
            word = word + " " + single_wordify(math.floor(bite_size_chunk/100)) + " hundred"
        word = word + " " + tens_wordify(bite_size_chunk%100) + " " + big_number_names[i-1]
    word = word.strip()+"!" #removes unnecessary spaces on start and end
    #time.sleep(0.01)
    return word



#Loop until we find something that is 140 characters or larger
tweetable = 1
tweet_number = 1
while tweetable == 1:
    if len(word_handler(tweet_number))>=140:
        tweetable = 0
        print(word_handler(tweet_number))
        print(len(word_handler(tweet_number)))
        print("-- done --")
    else:
        tweet_number = tweet_number + 1
        #print(word_handler(tweet_number))
        #print(len(word_handler(tweet_number)))
