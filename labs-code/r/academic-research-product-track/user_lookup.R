library(academictwitteR)

# Replace with your own bearer token
bearer_token <- "XXXXX"

# Replace with user IDs of your choice
user_ids <- c("2244994945", "6253282")

users <-
  get_user_profile(
    user_ids,
    bearer_token)

View(users)
