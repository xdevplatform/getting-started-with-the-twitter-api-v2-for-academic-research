library(academictwitteR)

# Replace with your own bearer token
bearer_token <- "XXXXX"

tweets <-
  get_all_tweets(
    # Replace with Tweet ID of your choice to get replies
    "conversation_id:1403738886275096605",
    "2021-01-01T00:00:00Z",
    "2021-06-14T00:00:00Z",
    bearer_token
  )

View(tweets$text)