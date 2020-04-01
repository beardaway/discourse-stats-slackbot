# Imports

import requests
import json

# TODO: Fill in the values
# WEBHOOK_URL - Webhhok URL for the Slack channel that you would like to post to
# ENDPOINT - URL of the endpoint that you're hitting executing your Data Explorer query
# API_KEY - Key that you can generate in API section in your Discourse Dashboard
# API_USERNAME - # Put system if yoy created the API Key for all users otherwise put in your Discourse username

WEBHOOK_URL = '<YOUR_WEBHOOK_URL>'
ENDPOINT = 'https://linkToYourCommunity/admin/plugins/explorer/queries/<YOUR_QUERY_ID/run'
API_KEY = '<YOUR_API_KEY'
API_USERNAME = '<USERNAME>'

# Core Functions

def send_request(endpoint):

    # There is no error handling here in terms of request. If the API changes anytime in the future, adjust the code based on request status code

    headers = {'Content-Type': 'multipart/form-data', 'Api-Key': API_KEY, 'Api-Username': API_USERNAME}
    request = requests.post(url = endpoint, headers = headers)
    print("Request Status Code: {}".format(request.status_code))

    # Unprocessed API request response

    response = json.loads(request.text)

    # Processed API request response - now it's parsed into a dictionary
    # TODO: Based on your query you will need to adjust the syntax below to access the dictionary element of your choice
    
    # Sample Request Output
    # {"success":true,"errors":[],"duration":73.2,"result_count":1,"params":{},"columns":["newusers","activeusers","newtopics","replies","emp_replies"],"default_limit":1000,"relations":{},"colrender":{},"rows":[[577,492,520,1876,1071]]}

    response_rows = response["rows"]

    # Scenario Description
    # In this scenario the response includes columns array which stores names of the columns (new_users, active_users, etc.)
    # Each column has one row (one value) that is the numeric value we want to present in Slack

    new_users = response_rows[0][0]
    active_users = response_rows[0][1]
    new_topics = response_rows[0][2]
    employees_replies = response_rows[0][3]
    external_users_replies = response_rows[0][4]

    response_text = "Community Forum - Last Month Stats 👨‍💻\nNew Users: {}\nActive Users: {}\nNew Topics: {}\nEmployees Replies: {}\nExternal Users Replies: {}".format(new_users, active_users, new_topics, employees_replies, external_users_replies)

    # Output Form
    # Community Forum - Last Month Stats 👨‍💻
    # New Users: 425
    # Active Users: 389
    # New Topics: 427
    # Employees Replies: 737
    # External Users Replies: 610

    return response_text

def post_to_slack(processed_response):

    slack_message = {'text': processed_response}
    requests.post(WEBHOOK_URL, json.dumps(slack_message))

processed_response = send_request(ENDPOINT)
post_to_slack(processed_response)
