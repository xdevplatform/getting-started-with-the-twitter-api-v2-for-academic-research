from twarc import Twarc2, expansions
import json

# Replace your bearer token below
client = Twarc2(bearer_token="XXXXX")


def main():
    user_mentions = client.mentions(user="twitterdev")
    for page in user_mentions:
        result = expansions.flatten(page)
        for tweet in result:
            print(json.dumps(tweet))


if __name__ == "__main__":
    main()
