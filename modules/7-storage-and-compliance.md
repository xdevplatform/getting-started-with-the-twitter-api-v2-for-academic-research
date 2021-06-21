# Module 7: Storage and Compliance

![banner](../assets/banner.png)

Now that you know how to get the Twitter data you need, what do you do with it all? Before you can start your analysis, you will need to determine whether and where you want to store your data. You will also need to make sure that you have a process in place to keep your data in compliance - that is, you have a way to honor Tweet deletions or other events in your dataset.

## Methods for storing Twitter data

When you use the Twitter API, the response is in JSON format. You may want to save this data first, and read it later for your analysis. To save this data, you can write each JSON object to a newline in a file (in your code) and then once the file has a desired number of Tweets (per file), you can save that file to the desired destination. Some libraries also allow you to convert this JSON data to CSV (to be saved as csv files). The labs in module 6 above include some examples of writing Tweets to a file.

## Some additional examples of how researchers store this data include:

### Storing the data to a relational database

In some cases, you may want to store your Tweets to a relational database, with each row containing the Tweet ID (primary key) along with the additional fields such as Tweet text, created_at etc.

### Storing the data to object store

A common way that researchers store Tweets is by writing those to a file, then compressing those files and saving those in an object store such as Amazon Web Services (AWS) S3, Azure Blob storage etc. Then, when you want to read this data for analysis, you can get it from these object stores to your local machine. Additionally, some of these cloud services provide tools in the cloud for analysis that connect to the object store directly. An example of this is Amazon Athena, that lets you run SQL queries for data in Amazon S3.

### Storing the data to a NoSQL database

You can also store your data in a NoSQL document database such as Amazon DynamoDB, MongoDB etc.

## Advanced tutorials and tools for storage

If you wish to store your data in the cloud such as AWS, check out this [guide on introduction to Twitter data processing and storage on AWS](https://dev.to/twitterdev/introduction-to-twitter-data-processing-and-storage-on-aws-1og).

If you want to process data from the filtered stream endpoint and store the Tweets into hourly compressed files, check out [this tool](https://github.com/igorbrigadir/covid19-twitter-stream-tool). Although this tool is shown for the covid-19 stream endpoint (which was a limited availability streaming endpoint in the past), it can be adapted to get data from the filtered stream endpoint and then the data can be saved in compressed files, hourly.

## Content compliance

When you are using the Twitter API, you should ensure that you are complying with the [Twitter developer policy](https://developer.twitter.com/en/developer-terms/policy). If you store Twitter data offline, you must keep it up to date with the current state of that content on Twitter. Specifically, you must delete or modify any content in your dataset if it is deleted or modified on Twitter.

One way academics can do this is by periodically calling the [Tweet lookup endpoint](https://developer.twitter.com/en/docs/twitter-api/tweets/lookup/introduction), with a list of Tweet IDs (upto 100 per request) from their datasets. If a Tweet has been deleted or was posted from a now- suspended or private account, the API response will indicate that and you should delete that Tweet (JSON) from your dataset. An example of this is shown in the labs in module 6 above.

## Sharing Tweet IDs for peer-review

Academic researchers are permitted to distribute an unlimited number of Tweet IDs and/or User IDs if they are doing so for the purposes of non-commercial research and to validate or replicate previous academic studies. **You should not share the entire Tweet text directly**. Instead, you can build a list of Tweet IDs and share those. The researchers who you share this set of Tweet IDs with, can then use the Twitter API to hydrate and get the full Tweet objects from the Tweet IDs.

When sharing these Tweet IDs, it is a good practice to document the search queries or rules that you used to obtain this data, along with the time period and the endpoints used. This will allow those that use this dataset to understand the assumptions behind the collection process and they can then add any additional keywords and conditions that would meet their research objectives to supplement your dataset.

In the next section, let us look at some final thoughts and resources to help you when using the Twitter API v2 for academic research.

[![Next](../assets/next.png)](../modules/8-wrap-up-and-resources.md)
