from twarc import Twarc2, expansions
import json

# Replace your bearer token below
client = Twarc2(bearer_token="XXXXX")


def main():
    users = ['2244994945', '783214', '6253282']
    lookup = client.user_lookup(users=users)
    for page in lookup:
        result = expansions.flatten(page)
        for user in result:
            print(json.dumps(user))


if __name__ == "__main__":
    main()
