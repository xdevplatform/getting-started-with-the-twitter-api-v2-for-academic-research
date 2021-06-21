from twarc import Twarc2, expansions
import json

# Replace your bearer token below
client = Twarc2(bearer_token="XXXXX")


def main():
    tweet_ids = ['1404192093803741184', '1403738886275096605', '1397216898593525762']
    lookup = client.tweet_lookup(tweet_ids=tweet_ids)
    for page in lookup:
        result = expansions.flatten(page)
        for tweet in result:
            print(json.dumps(tweet))


if __name__ == "__main__":
    main()
