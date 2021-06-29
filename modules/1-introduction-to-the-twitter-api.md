# Module 1: Introduction to Twitter API and examples of research with it

![banner](../assets/banner.png)

Twitter is a platform that is used by people across the world to exchange thoughts, ideas and information with one another, using Tweets. Each Tweet consists of up to 280 characters and may include media such as links, images and videos. In the context of research, Twitter data refers to the public information that is provided via Twitter’s application programming interface (API). The API supports various endpoints such as recent search, filtered steam etc. that let developers and researchers connect to the API and request Twitter data.

*Not sure what an API is and want to learn more? Check out this [appendix](./0-appendix.md) section to learn more.*

**Main Takeaway:** Twitter currently does not provide a website to go and download the data directly, you have to use the API to request this data. The Twitter API is the official source of getting Tweets for research to stay compliant with our developer policy.

## Examples of information (also referred to as data fields) that is available to researchers for a public Tweet include:

- Tweet text
- Tweet ID (that uniquely identifies a Tweet)
- The time at which the Tweet was created
- Public metrics associated with the Tweet such as number of retweets, number of likes etc.
- Public user information such as username, user ID, user bio, profile image url etc.
- Tweet Annotations - some Tweets are annotated based on the topic that they are about and the named entities present in the Tweets. These are new additions in the Twitter API v2.

A complete data dictionary of available fields for a Tweet can be found [here](https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet)

## Examples of information that is not made available as a data field using the Twitter API v2:

- Political affiliation
- Birthdate
- Deleted Tweets

## Examples of research done with Twitter data

Twitter makes global historical and real-time streaming data available through the Twitter API v2, making it an invaluable data source for researchers from various academic disciplines.

- [Using Twitter data to study how people are normalizing climate change](https://developer.twitter.com/en/use-cases/success-stories/uc-davis-max-planck-institute) (UC Davis and Max Planck Institute)
- [Using Twitter data to understand the COVID-19 health crisis and perceptions in local communities](https://developer.twitter.com/en/use-cases/success-stories/penn) (Penn Medicine Center for Digital Health)
- [Understanding toxic conversations and how to combat them with positive interruptions](https://developer.twitter.com/en/use-cases/success-stories/hatelab) (Cardiff University’s Hate Lab)

This is just scratching the surface. Researchers have a pulse on some of the biggest and most important issues of our time. A lot of people share their interest in studying misinformation/disinformation networks, polarized conversations, and responsible and ethical machine learning.

These topics are really interesting to Twitter, too. While we have our own research goals related to some of these topics, we highly encourage more scholarship from the academic community as well. If social media research is a special interest for you, learn more about what teams at Twitter are working on today to see if it might inspire your next research project here: [Twitter Research Areas](https://developer.twitter.com/en/use-cases/do-research/academic-research/research-areas).

In the next module, let us look at how you can apply for a Twitter developer account and select the right product track for your use-case.

[![Next](../assets/next.png)](../modules/2-choosing-the-right-product-track.md)
