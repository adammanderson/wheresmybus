import chalk from 'chalk'

const LOG_LEVELS = {
  ERROR: 'error',
  WARNING: 'warning',
  INFO: 'info',
  SUCCESS: 'success',
}

const log = (message, type) => {
  let colorMessage
  switch (type) {
    case LOG_LEVELS.ERROR:
      colorMessage = chalk.red(`[${LOG_LEVELS.ERROR}] ${message}`)
      break
    case LOG_LEVELS.WARNING:
      colorMessage = chalk.orange(`[${LOG_LEVELS.WARNING}] ${message}`)
      break
    case LOG_LEVELS.INFO:
      colorMessage = chalk.blue(`[${LOG_LEVELS.INFO}] ${message}`)
      break
    case LOG_LEVELS.SUCCESS:
      colorMessage = chalk.green(`[${LOG_LEVELS.SUCCESS}] ${message}`)
      break
    default:
      colorMessage = message
  }
  return colorMessage
}

export default log
