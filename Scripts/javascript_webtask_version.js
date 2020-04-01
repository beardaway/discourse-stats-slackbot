module.exports = (ctx, cb) => {

// TODO: Click on the key button in the upper left corner and add http and json NPM modules

const http = require('https');
const json = require('json');

// TODO: Click on the key button once again and then go to Secrets and add two secrets:
// api_key: you can generate that by going to Discourse Admin API section
// api_username: type in system if you created API Key for All Users otherwise type in your Discourse username

// TODO: Fill in the options constant hostname and path fields

const options = {
  hostname: '<YOUR_COMMUNITY_FORUM_MAIN_PAGE_URL',
  path: '/admin/plugins/explorer/queries/<YOUR_Query_ID>/run',
  method: 'POST',
  headers: {
    accept: 'application/json',
    'Content-Type': 'multipart/form-data',
    'Api-Key': ctx.secrets.api_key,
    'Api-Username': ctx.secrets.api_username
  }
};

const req = http.request(options, (res) => {
  console.log(`statusCode: ${res.statusCode}`);

  res.on('data', (d) => {
    process.stdout.write(d);

    // Processed API request response - now it's parsed into a dictionary

    const parsed_response = JSON.parse(d);

    // Sample Request Output
    // {"success":true,"errors":[],"duration":73.2,"result_count":1,"params":{},"columns":["newusers","activeusers","newtopics","replies","emp_replies"],"default_limit":1000,"relations":{},"colrender":{},"rows":[[577,492,520,1876,1071]]}

    // Scenario Description
    // In this scenario the response includes columns array which stores names of the columns (new_users, active_users, etc.)
    // Each column has one row (one value) that is the numeric value we want to present in Slack

    const new_users = parsed_response.rows[0][0];
    const active_users = parsed_response.rows[0][1];
    const new_topics = parsed_response.rows[0][2];
    const employees_replies = parsed_response.rows[0][3];
    const users_replies = parsed_response.rows[0][4];

    cb(null, { text: ('Community Forum - Last Month Stats 👨‍💻 \nNew Users: ' + (new_users) + '\nActive Users: ' + (active_users) + '\nNew Topics: ' + (new_topics) + '\nEmployees Replies: ' + (employees_replies) + '\nExternal Users Replies: ' + (users_replies)),
             response_type: 'in_channel'});
  });

    // Output Form
    // Community Forum - Last Month Stats 👨‍💻
    // New Users: 425
    // Active Users: 389
    // New Topics: 427
    // Employees Replies: 737
    // External Users Replies: 610
});

req.on('error', (error) => {
  console.error(error);
});

req.end();
}
