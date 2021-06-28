from twarc import Twarc2, expansions
import json

# Replace your bearer token below
client = Twarc2(bearer_token="XXXXX")


def main():
    # This timeline functions gets the Tweet timeline for a specified user
    user_timeline = client.timeline(user="twitterdev")

    # Twarc returns all Tweets for the criteria set above, so we page through the results
    for page in user_timeline:
        # The Twitter API v2 returns the Tweet information and the user, media etc.  separately
        # so we use expansions.flatten to get all the information in a single JSON
        result = expansions.flatten(page)
        for tweet in result:
            # Here we are printing the full Tweet object JSON to the console
            print(json.dumps(tweet))


if __name__ == "__main__":
    main()
