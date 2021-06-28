from twarc import Twarc2, expansions
import datetime
import json

# Replace your bearer token below
client = Twarc2(bearer_token="XXXXX")


def main():
    # Specify the start time in UTC for the time period you want replies from
    start_time = datetime.datetime(2021, 6, 12, 0, 0, 0, 0, datetime.timezone.utc)

    # Specify the Tweet ID for which you want the conversation thread
    query = "conversation_id:1403738886275096605"

    # The search_all method call the full-archive search endpoint to get the Tweets (replies) for the conversation
    search_results = client.search_all(query=query, start_time=start_time, max_results=100)

    # Twarc returns all Tweets for the criteria set above, so we page through the results
    for page in search_results:
        # The Twitter API v2 returns the Tweet information and the user, media etc.  separately
        # so we use expansions.flatten to get all the information in a single JSON
        result = expansions.flatten(page)
        for tweet in result:
            # Here we are printing the full Tweet object JSON to the console
            print(json.dumps(tweet))


if __name__ == "__main__":
    main()
