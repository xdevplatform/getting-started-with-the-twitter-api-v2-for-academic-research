# Module 6D: Getting Started with Postman

![banner](https://user-images.githubusercontent.com/60015240/191588591-935e18ca-bf11-4cf0-a45a-39facb6b77a6.png)

# What is Postman

> "Postman is an API platform for building and using APIs. Postman simplifies each step of the API lifecycle and streamlines collaboration so you can create better APIs—faster."

Find more information about Postman [here](https://www.postman.com/product/what-is-postman/).

The Twitter API is accessible via Postman, which makes it simpler to get started with testing and exploring the API.

Let us look at setting up Authorization and explore some use cases below, to learn how Postman can be leveraged as a tool to enable use of the Twitter API.

# Setting up
## Fork the Twitter API V2 public collection
The Postman team recommends accessing the Twitter API through Postman's desktop app. In order to follow along, please fork the Twitter API V2 [collection](https://www.postman.com/twitter/workspace/twitter-s-public-workspace/collection/9956214-784efcda-ed4c-4491-a4c0-a26470a67400?action=share&creator=21506762) into your own workspace.

To accomplish a successful fork in Postman, select the horizontal ellipses (or [Meatballs](https://uxplanet.org/choose-correct-menu-icon-for-your-navigation-7ffc22df80ac)) menu on the collection, select **Create a Fork**, and provide details about the destination workspace.

![forkTwitterColl](https://user-images.githubusercontent.com/60015240/187228316-b96f5316-3dad-4b9d-9c34-d219a5959396.gif)

## Create a new Environment to hold keys and secrets
In the workspace where you've added a fork of the Twitter API V2, create a new **Environment** to hold keys and secrets necessary for Authorized use of the Twitter API. The Environment will contain properties that are mentioned within the collection level documentation. Note the addition of Client ID and Client Secret properties. Values must be populated by what's provided to you through the Twitter Developer [Portal](https://developer.twitter.com) when you create a Project and App.

![envSetupDocs](https://user-images.githubusercontent.com/60015240/191588476-8aafa23b-edaf-46cc-a573-dbb208b28408.png)

![addEnv](https://user-images.githubusercontent.com/60015240/187230059-aa08600a-491b-42b3-94d5-3a9c71c97b71.gif)

## Set up Authorization 

You have the option to set up Auth at the **Request** or **Collection** level in Postman, based on your needs.

### Bearer Token

For some Twitter API V2 endpoints, a Bearer Token is all that's needed and will be provided to developers who have set up a project and app in Twitter's [developer portal](developer.twitter.com). In this case, you can set Authorization to Bearer Token and insert the token provided by twitter. 

<img src="https://content.pstmn.io/75b06b8c-0c05-4eb5-97f8-232f135f5508/QXVnLTI2LTIwMjIgMTMtNTQtMTEuZ2lm" alt="">

### OAuth 2.0

Postman has an Auth helper. We can set this up at the Collection level by selecting the **Authorization** tab within our Collection.
- For "type", select **OAuth 2.0**
- For "grant type", select **Authorization Code (with PKCE)**
- For "code challenge method", select **Plain**
 - "Scope" will depend on your use case, but **tweet.read** and **users.read** are examples that can be used.
 - For "state", you can insert **"State"**

![auth-helper](https://user-images.githubusercontent.com/60015240/187233234-1789bc48-a87f-4561-bc19-7a22cc56e285.gif)

Some details you include in the Postman Auth helper must match details in your App settings found in the Twitter Developer Portal. 

For example, see the Callback URL in the app settings found in Twitter:

![callbackURLtwitter](https://user-images.githubusercontent.com/60015240/191588794-92a684dc-0acc-49a2-b77d-2c6adc002c6d.png)

See the Callback URL found in Postman's Auth helper:

![callbackURLpostman](https://user-images.githubusercontent.com/60015240/191588881-e01a46ff-181f-462d-a8ba-1b900f118909.png)

The Auth URL and Access Token URL will come from Twitter's Developer [Docs](https://developer.twitter.com/en/docs/tutorials/postman-getting-started).

![authurl](https://user-images.githubusercontent.com/60015240/191589030-b89739b3-b676-414d-a3a3-fe01fc58b82f.png)


The Client ID and Client Secret in Postman's Auth helper will point to the Environment variables you previously set.

![clientidandsecretvars](https://user-images.githubusercontent.com/60015240/191589223-521efa8b-6acd-4669-8b2d-85d3b2d7993d.png)

# Use Cases
Select the `Run in Postman` button for each of the use cases below to see their documentation within Postman.
>1. "I want to get Tweets about something that happened this past week."

` insert Run in Postman button when workspace is made Public `

>2. "I want to build the entire conversation thread for a Tweet including replies."

` insert Run in Postman button when workspace is made Public `

>3. "I want to get Tweets from a user’s timeline."

` insert Run in Postman button when workspace is made Public `

>4. "I want to write a response from a recent search to a text file."

` insert Run in Postman button when workspace is made Public `

>5. "I want to get a user's tweet timeline."

` insert Run in Postman button when workspace is made Public `

>6. "I want to get a user's mentions."

` insert Run in Postman button when workspace is made Public `

>7. "I want to collect tweets in real time."

` insert Run in Postman button when workspace is made Public `

>8. "I want to collect Tweets in real-time on a breaking event."

` insert Run in Postman button when workspace is made Public `

>9. "I want to get the followers for a user."

` insert Run in Postman button when workspace is made Public `

>10. "I want to get the users that a UserID is following."

` insert Run in Postman button when workspace is made Public `

>11. "I want to lookup users using User IDs."

` insert Run in Postman button when workspace is made Public `

>12. "A fellow researcher shared a set of Tweet IDs and I want build the Twitter dataset for these Tweet IDs."

` insert Run in Postman button when workspace is made Public `

>13. "I want to keep my dataset compliant."

` insert Run in Postman button when workspace is made Public `

# Learn more and get certified through Postman Student Programs

If you're a student or educator learning or teaching APIs, the Postman student program provides training, resources, and opportunities to support and amplify your projects.

Find out more about Postman Student Programs [here](https://www.postman.com/student-program/) and fork our Student Expert training collection [here](https://www.postman.com/postman/workspace/postman-student-program).