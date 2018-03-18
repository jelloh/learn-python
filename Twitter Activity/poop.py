file = open('cheesecake.txt', 'r', encoding='utf-8')

# The top n users who have tweeted the most related to the search string
# for the entire timeline
relevance_f = open('most_relevant.txt', 'w', encoding='utf-8')
# The top n users who have tweeted the most for every hour
hourly_f = open('most_tweets_per_hour.txt', 'w', encoding='utf-8')
# The top n tweets which have the maximum retweet count
retweets_f = open('most_retweets.txt', 'w', encoding='utf-8')

num = int(input("Enter N: "))

count = 0
for line in file:
    if count > num:
        break

    print(line)

    count = count + 1
