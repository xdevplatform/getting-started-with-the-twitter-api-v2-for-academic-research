from twarc import Twarc2, expansions
import json

# Replace your bearer token below
client = Twarc2(bearer_token="XXXXX")


def main():
    for count, result in enumerate(client.sample()):
        tweet = expansions.flatten(result)
        print(json.dumps(tweet))

        # Replace with the desired number of Tweets
        if count > 100:
            break


if __name__ == "__main__":
    main()
