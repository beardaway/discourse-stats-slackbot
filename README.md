# Discourse Stats Slack

![](/Assets/DiscourseStatsSlackbot.png)

<a href="https://www.discourse.org/"><img src="https://img.shields.io/badge/Discourse-Community-blueviolet" alt=""/></a>     <a href="https://www.discourse.org/plugins/data-explorer.html"><img src="https://img.shields.io/badge/Data-Explorer-blueviolet" alt=""/></a>   <a href="https://api.slack.com/bot-users"><img src="https://img.shields.io/badge/Slack-Bot-blueviolet" alt=""/></a>

You want to analyze your Discourse Developer Community Forum activity? Using Data Explorer plugin, utilising SQL powers to get that data? Always going to Data Explorer UI, meandering between all those queries that you created to find the one that you're looking for? Executing it and then copy pasting data to Slack to get your team aware of the numbers?

**Avoid that exhausting procedure by executing one command in your team's Slack channel!**

### Core Concept

The main concept standing behind the idea of having such tool was to save time by executing one command instead of following the path described in the intro of this repo. One command, making proper request, parsing the response and then presenting the results, that's it. The only thing you need to prepare is to have a query of your choice that will be fetching the data you need. Sample queries can be found in the [SQLQueries Folder](https://github.com/konradsopala/discourse-stats-slack/tree/master/SQLQueries). For even more queries visit [Discourse SQL Wizard](https://github.com/konradsopala/discourse-sql-wizard).

**Saving time one query at a time!**

### The Webtask Way

This version was developed using JavaScript and Node.js. Full script code can be found [here](https://github.com/beardaway/discourse-stats-slackbot/blob/master/Scripts/javascript_webtask_version.js). Simplified script code is shown below:

```
module.exports = (ctx, cb) => {

const http = require('https');
const json = require('json');

const options = {
  hostname: 'community.yourCompanyName.com',
  path: '/admin/plugins/explorer/queries/yourQueryID/run',
  method: 'POST',
  headers: {
    accept: 'application/json',
    'Content-Type': 'multipart/form-data',
    'Api-Key': api_key,
    'Api-Username': api_username
  }
};

const req = http.request(options, (res) => {
  console.log(`statusCode: ${res.statusCode}`);

  res.on('data', (d) => {
    process.stdout.write(d);
    const parsed_response = JSON.parse(d);
    const stats = parsed_response.stats[0]

    cb(null, { text: ('Stats: ' + (stats)),
             response_type: 'in_channel'});
  });
});

req.on('error', (error) => {
  console.error(error);
});

req.end();
}
```

This method is run from Slack channel once you execute your webtask by typing in ```/wt yourWebtaskName```. Can be run by anyone that you will give access to unlike the webhook version that can be run only by those having developer keys. Here are the steps to make the method work:

* Create your Slack Workspace by going to https://slack.com/get-started#/create
* Go to https://yourWorkspaceName.slack.com/apps/manage
* In the search bar type in: Slash Webtask and click: Add Configuration
* Follow the instructions described there
* Download the [JavaScript Code](https://github.com/beardaway/discourse-stats-slackbot/blob/master/Scripts/javascript_webtask_version.js)
* Setup yourself an account on https://webtask.io/
* In Slack type in ```wt make nameOfYourWebtask```
* Go to Webtask Editor and edit the webtask you just created using the code you downloaded
* Save the webtask once you finish editing it by clicking on the floppy icon
* Type ```/wt nameOfYourWebtask``` into your Slack channel

![](/Assets/WebtaskResultScreenshot.png)

**Now you should have your stats in the channel!**

### The Webhook Way

This version was developed using Python. Full script code can be found [here](https://github.com/beardaway/discourse-stats-slackbot/blob/master/Scripts/python_webhook_version.py). Simplified script code is shown below:

```
import requests
import json

def send_request(endpoint):

    headers = {'Content-Type': 'multipart/form-data', 'Api-Key': API_KEY, 'Api-Username': API_USERNAME}
    request = requests.post(url = endpoint, headers = headers)

    response = json.loads(request.text)
    stats_to_post = response["number"]
    post_text = "Stats: {}".format(stats_to_post)

    return response_text

def post_to_slack(processed_response):

    slack_message = {'text': processed_response}
    requests.post(WEBHOOK_URL, json.dumps(slack_message))

processed_response = send_request(endpoint)
post_to_slack(processed_response)
```

This method runs the Python script automatically provided that you scheduled that with cron (described below). Here are the steps to make the method work, assuming you have Python installed on your computer:

* Create your Slack Workspace by going to https://slack.com/get-started#/create
* Create a channel that you would like to send your stats to
* Go to https://yourWorkspaceName.slack.com/apps/manage
* In the search bar type in: Incoming WebHooks and click: Add Configuration
* Follow the instructions and copy the Webhook URL given at the end
* Download the [Python Script](https://github.com/beardaway/discourse-stats-slackbot/blob/master/Scripts/python_webhook_version.py)
* Follow the instructions described in script's comments

To make it execute itself on the first day of each month at 12:00 automatically, go through following steps:

* Open terminal (Mac / Linux)
* Type in ```crontab -e```
* Press ```i``` to enable insert mode in Vim
* Copy and paste this snippet adjusting the path for where you downloaded your script:

```
0 12 1 * * cd <insert_script_folder_location_path> && python python_webhook_version.py

```
* Press esc and type ```:wq```

If you want to schedule the execution of the script at different time, follow this cron scheduling mechanism:
```
# ┌───────────── minute (0 - 59)
# │ ┌───────────── hour (0 - 23)
# │ │ ┌───────────── day of month (1 - 31)
# │ │ │ ┌───────────── month (1 - 12)
# │ │ │ │ ┌───────────── day of week (0 - 6) (Sunday to Saturday;
# │ │ │ │ │                                       7 is also Sunday on some systems)
# │ │ │ │ │
# │ │ │ │ │
# * * * * *  command_to_execute
```

![](/Assets/WebhookResultScreenshoot.png)

**Now you should have your stats in the channel every month automatically!**

### Supporting documentation

If you want to find out more about the stack used in those tools or even build your own tools, make sure to visit following links and get inspired:

* [Cron](https://en.wikipedia.org/wiki/Cron) <br>
* [Developing Slackbots](https://api.slack.com/bot-users) <br>
* [Slack API](https://api.slack.com/) <br>
* [Webtask](https://webtask.io/docs/101) <br>
* [Data Explorer Plugin](https://meta.discourse.org/t/data-explorer-plugin/32566) <br>
* [What cool Data Explorer queries have you come up with?](https://meta.discourse.org/t/what-cool-data-explorer-queries-have-you-come-up-with/43516) <br>
