#!/usr/bin/node
const thisRequest = require('request');
thisRequest(process.argv[2], function (error, response, body) {
  if (!error) {
    const tasks = JSON.parse(body);
    const compTasks = {};
    tasks.forEach((task) => {
      if (task.completed && compTasks[task.userId] === undefined) {
        compTasks[task.userId] = 1;
      } else if (task.completed) {
        compTasks[task.userId] += 1;
      }
    });
    console.log(compTasks);
  }
});
