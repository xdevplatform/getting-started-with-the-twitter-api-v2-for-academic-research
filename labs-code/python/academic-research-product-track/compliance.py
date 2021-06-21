from twarc import Twarc2, expansions

# Replace your bearer token below
client = Twarc2(bearer_token="XXXXX")


def main():
    read_path = 'ids.txt'

    all_tweet_ids = []

    compliant_tweet_ids = []

    with open(read_path) as f:
        all_tweet_ids = f.read().splitlines()
    lookup = client.tweet_lookup(tweet_ids=all_tweet_ids)
    for page in lookup:
        result = expansions.flatten(page)
        for tweet in result:
            compliant_tweet_ids.append(tweet['id'])
    non_compliant_tweet_ids = list(set(all_tweet_ids) - set(compliant_tweet_ids))
    print(non_compliant_tweet_ids)


if __name__ == "__main__":
    main()
