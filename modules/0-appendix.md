# Appendix

![banner](../assets/banner.png)

## What is an application programming interface (API)?

### A real-world example

A common example used to explain APIs is that of going to a restaurant. Let’s say you want to go to a restaurant to eat some BBQ chicken pizza. When you arrive at the restaurant, you do not simply walk into their kitchen and start making the pizza yourself. In most cases, you don’t even get access to the kitchen or the chef. Instead, you speak with a server. The server presents a menu to you and you select what you’d like to order from the menu. You are only able to order what is available on the menu. Once you are ready, you place the order with the server. The server then goes back into the kitchen and gives your order details to the chef who then cooks it for you. When your order is ready, the server brings it to your table from the kitchen. Once you have the food at your table, you are now able to enjoy it. This same analogy applies to an API.
Companies store data in a database and people outside do not have access to these databases directly (the kitchen in this example). If they want the data, they have to interface with the API (the server in this example) and specify the data they need along with the appropriate authentication. Then, it is up to the API to get the data from the databases (the kitchen in this example) and present it to the user in an easy to understand manner.

So in a way, APIs provide a programmatic way (using some code) to exchange data between applications and services. The most common type of APIs are what are called ‘REST APIs’. Learn more about REST API’s [here](https://blog.postman.com/rest-api-definition/).

In the context of the Twitter API, when you want to request Tweets from Twitter, you need to make an API call, with appropriate authentication mechanism and specify the Tweets you want. The API will then take care of getting the data from Twitter for you and present it to you in the JSON format.

## Installing Python

Check out [this tutorial](https://realpython.com/installing-python/) that explains how to install Python on your computer

## Introductory course for Python

Here is a [list of beginners guides](https://wiki.python.org/moin/BeginnersGuide/Programmers) for Python

## Installing R and introductory course on R

Check out [this guide](https://rstudio-education.github.io/hopr/starting.html) that explains how to install R and Rstudio on your computer and provides an introduction to getting started in R

## Endpoint

You will come across the word ‘endpoint’. This basically refers to a path or a ‘method’ within the Twitter API to get Twitter data. So for example, the Twitter API v2 consists of various endpoints such as recent search, full-archive search, filtered stream, Tweet lookup etc. and each of these provide a different functionality with respect to getting Twitter data.

## Parameters

When using an endpoint, you can specify details such as the maximum number of Tweets you want returned, using parameters. These are usually a key-value pair.

## Hydration

This term refers to using a Tweet ID or a set of Tweet IDs to obtain the information about Tweets such as the Tweet text, the time that the Tweet was created at, the author of the Tweet etc. Thus, when someone gives you a list of Tweet IDs and asks you to hydrate it, they want you to use any existing library or code to call the Twitter API with those Tweet IDs and obtain the corresponding Tweet information.

## Tweet payload

The response obtained from the Twitter API is in the JSON format. This response, when it contains information about a Tweet is referred to as the ‘Tweet payload’. See example of what a JSON looks like below.

## JSON

JavaScript Object Notation (JSON) is a lightweight data-interchange format. Whenever you use the Twitter API, the response that you get back is in the JSON format. An example of a JSON object is:

 ```json
 {
   "name":"TwitterDev",
   "handle":"@TwitterDev"
}
```

## CSV

Comma-separated values (CSV) is a text file format where values are separated by a comma and is supported by many applications.

## Rate limit

Every day many thousands of developers make requests to the Twitter developer platform. To help manage the sheer volume of these requests, limits are placed on the number of requests that can be made. These limits help us provide the reliable and scalable API that our developer community relies on. Learn more about rate limits [here](https://developer.twitter.com/en/docs/rate-limits).

## Search query

In order to get data from the Twitter API using search endpoints (recent search and full-archive search), you have to specify the kind of data you are looking for. In order to describe this data, you need to write a search query that consists of operators (described below)

## Rules

In order to get data from the filtered-stream endpoint, you have to specify the kind of data that you are looking for. Similar to a search query, you can describe this data by adding rules to the filtered stream endpoint. The Twitter API v2 lets you add up to 25 rules, each of length 512 characters for the recent search endpoint and 1000 rules, each of 1024 characters for the full-archive search endpoint.

## Operators

Operators let you specify the data that you want in your search queries and rules. Examples of operators include is:retweet, has:media etc.

## Tweet ID

A [Tweet ID](https://developer.twitter.com/en/docs/twitter-ids) uniquely identifies a Tweet. For example, the Tweet ID for this Tweet: <https://twitter.com/suhemparack/status/1397926405132849155> is 1397926405132849155. In Twitter API v2, it is represented as a string value.

## Conversation thread

Conversation thread refers to the full conversation from a Tweet including all the replies to it. In order to get the full conversation thread, developers use the [conversation_id operator](https://developer.twitter.com/en/docs/twitter-api/conversation-id) in their search queries.

## Project

[Projects](https://developer.twitter.com/en/docs/projects/overview) allow you to organize your work based on how you intend to use the Twitter API, so you can effectively manage your access to the API and monitor your usage.

## Apps

[Apps](https://developer.twitter.com/en/docs/apps/overview) are placeholders for your keys and [tokens](https://developer.twitter.com/en/docs/authentication/oauth-2-0/bearer-tokens), that you need in order to connect to the Twitter API

## Tweet cap

Tweet cap refers to the total number of Tweets that you can get back from the Twitter API v2 per month. Learn more about Tweet caps [here](https://developer.twitter.com/en/docs/projects/overview).

## Standard product track

The standard product refers to the default product offering and access level available to all developers with an approved developer account. Learn more about product tracks [here](https://developer.twitter.com/en/products/twitter-api/early-access/guide#na_2).

## Academic Research product track

The academic research product track refers to the product offering and access level that is available only to qualified academics and includes a higher level of access compared to the standard product track, tailored specifically for academic researchers. Learn more about product tracks [here](https://developer.twitter.com/en/products/twitter-api/early-access/guide#na_2).

## Tweet annotations

Tweet annotations provide contextual information about a team and provide named entity recognition in Tweets. Learn more about annotations [here](https://developer.twitter.com/en/docs/twitter-api/annotations).

## Real-time Twitter data

Real-time Twitter data refers to data from endpoints such as sampled stream endpoint, filtered stream endpoint etc. that provide Tweets in real-time as they are happening on Twitter.

## Historical Twitter data

Historical data refers to the Tweets from the past and are obtained from endpoints such as recent search and full-archive search.

## Follower graph

The follower graph refers to the network and relationship of users on Twitter

## Text mining

It refers to the the process of deriving analytics and insights from Text

## Named entity-recognition

Named-entity recognition is a sub-task of information extraction that seeks to locate and classify named entities mentioned in unstructured text into predefined categories such as person names, organizations, locations, medical codes, time expressions, quantities, monetary values, percentages, etc. [Source: Wikipedia]

## Topic modelling

Topic modeling is a type of statistical modeling for discovering the abstract “topics” that occur in a collection of documents [Source: Wikipedia]

## Libraries /Packages

Libraries and packages contain code that make it easy for you to do a task, by abstracting complex code and often provide you easy functions to complete a task. In the context of the Twitter API, libraries and packages for the Twitter API abstract away the concepts of making an HTTP request etc. and provide you with simple functions that you can use in your code to get the data you need from Twitter without worrying about the technical implementation details.
