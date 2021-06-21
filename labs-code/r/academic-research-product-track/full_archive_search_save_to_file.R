library(academictwitteR)

# Replace with your own bearer token
bearer_token <- "XXXXX"

tweets <-
  get_all_tweets("from:twitterdev",
                 "2021-01-01T00:00:00Z",
                 "2021-05-31T00:00:00Z",
                 bearer_token,
                 data_path = "data/",
                 bind_tweets = FALSE)
