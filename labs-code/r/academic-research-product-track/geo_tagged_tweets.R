library(academictwitteR)

# Replace with your own bearer token
bearer_token <- "XXXXX"

tweets <-
  get_all_tweets(
    "covid-19 has:geo",
    "2021-01-01T01:00:00Z",
    "2021-01-01T02:00:00Z",
    bearer_token)

View(tweets)
