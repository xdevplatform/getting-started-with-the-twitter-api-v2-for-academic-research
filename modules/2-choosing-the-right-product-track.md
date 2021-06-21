# Module 2: Applying for a Twitter developer account and choosing the right product track

![banner](../assets/banner.png)

In order to get access to Twitter data, you need to first [apply for a Twitter developer account](https://developer.twitter.com/en/apply-for-access). Once your developer application has been approved, you get access to the standard product track (by default). However, if you are an academic researcher and meet certain requirements (mentioned below), you can [apply to the academic research product track](https://developer.twitter.com/en/portal/petition/academic/is-it-right-for-you) which will give you elevated access to the Twitter API v2 including access to historical public Tweets for free.

## Standard product track

This product track is intended to serve our broadest range of developers and is available for free.

It is ideal for undergraduate or high school students who want to use Twitter data for a class project or to use Twitter data for assignments on text mining, entity extraction, topic modelling, etc. As part of this product track you can:

- Search for Tweets from the last 7 days by specifying queries using supported operators (more on building queries in later sections)
- Stream Tweets in real-time as they are happening by specifying rules to filter for Tweets that you are interested in.
- Get Tweets from a user’s timeline (up to 3200 most recent Tweets)
- Build the full Tweet objects from a Tweet ID, or a set of Tweet IDs
- Look up follower relationships

These are just some examples of what you can get from the standard product track, relevant to academics. For a complete list of available endpoints, check out the [Twitter API documentation](https://developer.twitter.com/en/docs/twitter-api).

Currently, you can get upto 500,000 Tweets per month using the standard product track and this limit does not apply to the sampled stream endpoint, which gives a 1% sample of public Tweets in real-time

## Academic Research product track

This product track includes elevated features and functionality tailored for  academics with more advanced professional research needs. This grants a higher level of access to data for free, but as a result, the application process is more involved (more on that, below).

This track includes:

- Ability to get historical Tweets from the entire archive of public conversation on Twitter, dating back to 2006 (using the full-archive search endpoint)
- Higher monthly Tweet volume cap of 10 million Tweets per month
- More advanced filter options to return relevant data, including a longer query length, support for more concurrent rules (for filtered stream endpoint), and additional operators that are only supported in this product track (more on this later)

Today, the Academic Research product track is reserved for those conducting professional academic research who have a specific research purpose with Twitter data. In order to get access to the academic research product track, these are the requirements:

- You are a graduate student, doctoral candidate, post-doc, faculty, or research-focused employee at an academic institution or university.
- You have a clearly defined research objective, and you have specific plans for how you intend to use, analyze, and share Twitter data from your research.
- You will use this product track for non-commercial purposes.

Once you apply for access, your application is manually reviewed by Twitter. If additional information is required, the team will reach out to you asking for more information. Once you have been approved, you will be able to see your academic project in the [Twitter developer portal dashboard](https://developer.twitter.com/en/portal/dashboard).

Before we get to exploring and using the developer portal, in the next module, let us learn how to decide what endpoints you need, in order to get the data you need for your research project.

[![Next](../assets/next.png)](../modules/3-deciding-which-endpoints-to-use.md)
