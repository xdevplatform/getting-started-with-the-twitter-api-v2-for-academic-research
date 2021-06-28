from twarc import Twarc2, expansions
import json

# Replace your bearer token below
client = Twarc2(bearer_token="XXXXX")


def main():
    # The sample method gives a 1% random sample of all Tweets
    for count, result in enumerate(client.sample()):
        # The Twitter API v2 returns the Tweet information and the user, media etc.  separately
        # so we use expansions.flatten to get all the information in a single JSON
        tweet = expansions.flatten(result)
        # Here we are printing the full Tweet object JSON to the console
        print(json.dumps(tweet))

        # Replace with the desired number of Tweets, otherwise it will stop after 100 Tweets
        if count > 100:
            break


if __name__ == "__main__":
    main()
