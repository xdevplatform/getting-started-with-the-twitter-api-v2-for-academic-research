from twarc import Twarc2, expansions
from twarc_csv import CSVConverter
import datetime
import json

# Replace your bearer token below
client = Twarc2(bearer_token="XXXXX")


def main():
    start_time = datetime.datetime(2021, 6, 12, 0, 0, 0, 0, datetime.timezone.utc)

    query = "from:Twitterdev -is:retweet"

    search_results = client.search_all(query=query, start_time=start_time, max_results=100)

    for page in search_results:
        result = expansions.flatten(page)
        with open("output.csv", "w") as outfile:
            for tweet in result:
                converter = CSVConverter(json.dumps(tweet), outfile, json_encode_all=False, json_encode_lists=True,
                                     json_encode_text=False, inline_referenced_tweets=True, allow_duplicates=False)
            converter.process


if __name__ == "__main__":
    main()
