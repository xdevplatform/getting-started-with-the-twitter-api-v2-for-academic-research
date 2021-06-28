from twarc import Twarc2
import datetime
import json

# Replace your bearer token below
client = Twarc2(bearer_token="XXXXX")


def main():
    # Specify the start time in UTC for the time period you want Tweets from
    start_time = datetime.datetime(2021, 1, 1, 0, 0, 0, 0, datetime.timezone.utc)

    # Specify the end time in UTC for the time period you want Tweets from
    end_time = datetime.datetime(2021, 5, 30, 0, 0, 0, 0, datetime.timezone.utc)

    # This is where we specify our query as discussed in module 5
    query = "lakers"

    # The counts_all method call the full-archive Tweet counts endpoint to get Tweet volume based on the query, start and end times
    count_results = client.counts_all(query=query, start_time=start_time, end_time=end_time)

    # Twarc returns all Tweet counts for the criteria set above, so we page through the results
    for page in count_results:
        print(json.dumps(page))


if __name__ == "__main__":
    main()
