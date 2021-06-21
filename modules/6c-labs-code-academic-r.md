# Labs for the academic research product track in R

![banner](../assets/banner.png)

In this section, we will learn how to write code in R to get historical Twitter data using the academic research product on the Twitter API v2. We will be using the [academicTwitteR](https://cran.r-project.org/web/packages/academictwitteR/index.html) package in R. All the example code used in these labs can be found [here](../labs-code/r/academic-research-product-track).

## Prerequisite

Make sure you have R installed on your machine in order to run these samples. See our [appendix section](./0-appendix.md) for instructions on installing R.

Also, make sure you have your bearer token from an app connected to your academic research project, as shown in [module 4](./4-getting-your-keys-and-token.md)

## Installing the academicTwitteR package

In order to install the academicTwitteR package, in your terminal, run the following:

```bash
install.packages("academicTwitteR")
```

## Importing the academicTwitteR package

In all of the code samples, you will first need to load the academicTwitteR library and set your bearer token in order to connect to the Twitter API v2 programmatically and get the response as shown below:

```R
# This will load the academicTwitteR package
library(academictwitteR)

# Set your own bearer token (replace the XXXXX with your own bearer token)
bearer_token <- "XXXXX"
```

These two lines above will remain the same for all the code examples.

## 1. Searching for Tweets older than the last 7 days as dataframe objects

The get_all_tweets function in academicTwitteR get Tweets from the full archive of public Tweets for the specified query and for the specified time period.

```R
tweets <-
  get_all_tweets("from:twitterdev",
                 "2021-01-01T00:00:00Z",
                 "2021-05-31T00:00:00Z",
                 bearer_token)

View(tweets$text)
```

**Note:**

- You can modify the query here by using the operators available for full-archive search as shown in [module 5](./5-how-to-write-search-queries.md)
- If you do not specify the start_time, the default time period will be 30 days for full-archive search
- academicTwitteR package will get all the Tweets for the specified time period and query by making multiple API requests until it gets all Tweets for the time period your specified.

## 2. Searching for Tweets older than the last 7 days and storing as JSON in a file

If you want to get Tweets from the full-archive, and want to save it for use later, can specify two additional parameters:

- bind_tweets which is set to FALSE
- data_path parameter using which you can specify the directory where you want the JSON data to be written. In the example below, if data folder exists then it will add the files to this existing folder, otherwise the new data folder will be created and files with the Tweet information will be added. **Note:** Tweet information is added to a JSON file that begins with 'data_' and user information is added to a JSON file that begins with 'users_'

```R
tweets <-
  get_all_tweets("from:twitterdev",
                 "2021-01-01T00:00:00Z",
                 "2021-05-31T00:00:00Z",
                 bearer_token,
                 data_path = "data/",
                 bind_tweets = FALSE)
```

## 3. Building the entire conversation thread for a Tweet ID

In the code below, replace the Tweet ID with an ID of your choice to get replies for the Tweet.

```R
tweets <-
  get_all_tweets(
    # Replace with Tweet ID of your choice to get replies
    "conversation_id:1403738886275096605",
    "2021-01-01T00:00:00Z",
    "2021-06-14T00:00:00Z",
    bearer_token
  )

View(tweets$text)
```

**Note:** If you do not specify the start_time, you will only get replies from the last 30 days

## 4. Get geo-tagged Tweets

The `has:geo` operator gives you Tweets that have geo information associated with them.

```R
tweets <-
  get_all_tweets(
    "covid-19 has:geo",
    "2021-01-01T01:00:00Z",
    "2021-01-01T02:00:00Z",
    bearer_token)

View(tweets)
```

**Note:** If you do not specify the start_time, you will only get replies from the last 30 days

## 5. Lookup Users using User IDs

The `get_user_profile` method lets you get the User information using a list of User IDs

```R
# Replace with user IDs of your choice
user_ids <- c("2244994945", "6253282")

users <-
  get_user_profile(
    user_ids,
    bearer_token)

View(users)
```

So this concludes the labs in R for the academic research product track. As the academicTwitteR package supports more endpoints, we will update this guide to demo how to use those endpoints in R.

In the next section, let us take a look at some additional information and best practices around storing Twitter data and how you can keep you dataset in compliance with Twitter's developer policy.

[![Next](../assets/next.png)](../modules/7-storage-and-compliance.md)
