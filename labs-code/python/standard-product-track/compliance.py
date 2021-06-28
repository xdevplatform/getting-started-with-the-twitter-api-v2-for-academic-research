from twarc import Twarc2, expansions

# Replace your bearer token below
client = Twarc2(bearer_token="XXXXX")


def main():
    # Path and name of file that contains the Tweet IDs, one Tweet ID per line
    read_path = 'ids.txt'

    compliant_tweet_ids = []

    with open(read_path) as f:
        all_tweet_ids = f.read().splitlines()
    # The tweet_lookup function will look up Tweets with the specified ids
    lookup = client.tweet_lookup(tweet_ids=all_tweet_ids)
    for page in lookup:
        result = expansions.flatten(page)
        for tweet in result:
            compliant_tweet_ids.append(tweet['id'])
    # Here we get a difference betweetn the original
    non_compliant_tweet_ids = list(set(all_tweet_ids) - set(compliant_tweet_ids))
    # Here we are printing the list of Tweet IDs that are not compliant in your dataset
    print(non_compliant_tweet_ids)


if __name__ == "__main__":
    main()
