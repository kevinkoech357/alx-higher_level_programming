#!/usr/bin/node

const request = require('request');

// Check if the API URL is provided as an argument
if (process.argv.length !== 3) {
  process.exit(1); // Exit with an error code
}

const apiUrl = process.argv[2];

// Make a GET request to the specified API URL
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
  } else if (response.statusCode !== 200) {
    console.error(`Failed to retrieve task information. Status Code: ${response.statusCode}`);
  } else {
    try {
      const tasks = JSON.parse(body);

      // Create an object to store the number of completed tasks by user ID
      const completedTasksByUser = {};

      // Iterate through the tasks and count completed tasks for each user
      for (const task of tasks) {
        if (task.completed) {
          if (completedTasksByUser[task.userId]) {
            completedTasksByUser[task.userId]++;
          } else {
            completedTasksByUser[task.userId] = 1;
          }
        }
      }

      console.log(completedTasksByUser);
    } catch (parseError) {
      console.error('Error occurred while parsing the response:');
      console.error(parseError);
    }
  }
});
