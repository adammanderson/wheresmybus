const fetch = require('node-fetch');
const chalk = require('chalk');
const config = require('../config');

console.log(chalk.bold.blue('WHERE\'S MY BUS'))

fetch('https://jsonplaceholder.typicode.com/todos/1')
  .then(response => response.json())
  .then(json => console.log(json))

console.log(config.api.appId)
