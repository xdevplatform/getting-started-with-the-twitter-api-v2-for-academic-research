from twarc import Twarc2, expansions
import json

# Replace your bearer token below
client = Twarc2(bearer_token="XXXXX")


def main():
    followers = client.followers(user="twitterdev")
    for page in followers:
        result = expansions.flatten(page)
        for user in result:
            print(json.dumps(user))


if __name__ == "__main__":
    main()
