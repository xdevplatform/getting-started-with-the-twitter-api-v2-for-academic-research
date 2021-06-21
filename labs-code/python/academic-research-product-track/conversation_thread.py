from twarc import Twarc2, expansions
import datetime
import json

# Replace your bearer token below
client = Twarc2(bearer_token="XXXXX")


def main():
    start_time = datetime.datetime(2021, 6, 12, 0, 0, 0, 0, datetime.timezone.utc)

    query = "conversation_id:1403738886275096605"

    search_results = client.search_all(query=query, start_time=start_time, max_results=100)

    for page in search_results:
        result = expansions.flatten(page)
        for tweet in result:
            print(tweet)


if __name__ == "__main__":
    main()
