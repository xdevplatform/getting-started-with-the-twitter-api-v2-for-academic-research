from twarc import Twarc2
import datetime
import json

# Replace your bearer token below
client = Twarc2(bearer_token="XXXXX")


def main():
    # Specify the start time in UTC for the time period you want Tweets from
    start_time = datetime.datetime(2021, 6, 27, 0, 0, 0, 0, datetime.timezone.utc)

    # Specify the end time in UTC for the time period you want Tweets from
    end_time = datetime.datetime(2021, 6, 28, 0, 0, 0, 0, datetime.timezone.utc)

    # This is where we specify our query as discussed in module 5
    query = "lakers"

    # The counts_recent method call the recent Tweet counts endpoint to get Tweets based on the query, start and end times
    count_results = client.counts_recent(query=query, start_time=start_time, end_time=end_time)


    # Recent Tweet counts returns all the Tweet volume for the last 7 days in one page so we break after that
    for page in count_results:
        print(json.dumps(page['data']))
        break

if __name__ == "__main__":
    main()
