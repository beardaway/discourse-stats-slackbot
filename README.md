# Discourse Stats Slackbot

![](/Assets/DiscourseStatsSlackbot.png)

<a href="https://www.discourse.org/"><img src="https://img.shields.io/badge/Discourse-Community-blueviolet" alt=""/></a>     <a href="https://www.discourse.org/plugins/data-explorer.html"><img src="https://img.shields.io/badge/Data-Explorer-blueviolet" alt=""/></a>   <a href="https://api.slack.com/bot-users"><img src="https://img.shields.io/badge/Slack-Bot-blueviolet" alt=""/></a>

You want to analyze your Discourse Developer Community Forum activity? Using Data Explorer plugin, utilising SQL powers to get that data? Always going to Data Explorer UI, meandering between all those queries that you created to find the one that you're looking for? Executing it and then copy pasting data to Slack to get your team aware of the numbers?

**Avoid that exhausting procedure by executing one command in your team's Slack channel!**

### Core Concept

The main concept standing behind the idea of having such tool was to save time by executing one command instead of following the path described in the intro of this repo. One command, making proper request, parsing the response and then presenting the results, that's it. The only thing you need to prepare is to have a query of your choice that will be fetching the data you need. **Saving time one query at a time!**

### The Webtask Way

This version was developed using Python. The code for the script can be found [here](https://github.com/beardaway/discourse-stats-slackbot/blob/master/Scripts/python_webhook_version.py). This method requires you to run it manually from your local computer, from terminal. **If you filled in the script with your developer keys it should not be shared with others as the keys are not kept secret**. Here are the steps to make the method work:

* Create your Slack Workspace by going to https://slack.com/get-started#/create
* Create a channel that you would like to send your stats to
* Go to https://yourWorkspaceName.slack.com/apps/manage
* In the search bar type in: Incoming WebHooks and click: Add Configuration
* Follow the instructions and copy the Webhook URL given at the end
* Download the [Python Script](https://github.com/beardaway/discourse-stats-slackbot/blob/master/Scripts/python_webhook_version.py)
* Install Python on your computer
* Follow the instructions described in script's comments
* Go to your terminal and navigate to the folder where you have the script
* Type in your terminal: ```python nameOfYourScriptFile.py ```

**Now you should have your stats in the channel!**

### The Webhook Way


### Supporting documentation

If you want to find out more about the stack used in those tools or even build your own tools, make sure to visit following links and get inspired:

* [Developing Slackbots](https://api.slack.com/bot-users) <br>
* [Slack API](https://api.slack.com/) <br>
* [Webtask]((https://webtask.io/docs/101)) <br>
* [Data Explorer Plugin](https://meta.discourse.org/t/data-explorer-plugin/32566) <br>
* [What cool Data Explorer queries have you come up with?](https://meta.discourse.org/t/what-cool-data-explorer-queries-have-you-come-up-with/43516) <br>
