from twarc import Twarc2, expansions
import datetime
import json

# Replace your bearer token below
client = Twarc2(bearer_token="XXXXX")


def main():
    start_time = datetime.datetime(2021, 1, 1, 0, 0, 0, 0, datetime.timezone.utc)

    end_time = datetime.datetime(2021, 5, 30, 0, 0, 0, 0, datetime.timezone.utc)

    query = "from:suhemparack"

    search_results = client.search_all(query=query, start_time=start_time, end_time=end_time, max_results=100)

    for page in search_results:
        result = expansions.flatten(page)
        for tweet in result:
            print(json.dumps(tweet))


if __name__ == "__main__":
    main()
