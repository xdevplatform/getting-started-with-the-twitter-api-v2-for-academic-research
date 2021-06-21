from twarc import Twarc2, expansions
import json

# Replace your bearer token below
client = Twarc2(bearer_token="XXXXX")


def main():

    query = "conversation_id:1403738886275096605"

    search_results = client.search_recent(query=query, max_results=100)

    for page in search_results:
        result = expansions.flatten(page)
        for tweet in result:
            print(json.dumps(tweet))


if __name__ == "__main__":
    main()
