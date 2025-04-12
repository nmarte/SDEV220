# Walrus operator
# It looks like this
# name := expression

# With our NEW tusk power 
# (aka "assignment expressions") we can combine these into one step

tweet_limit = 280
tweet_string = "Blah" * 50
if diff := tweet_limit - len(tweet_string) >= 0:
    print("A fitting tweet")
else:
    print("Went over by", abs(diff))

