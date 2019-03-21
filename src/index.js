import chalk from 'chalk'
import { stopPointId, refresh } from '../config'
import getStopPointArrivals from './helpers/get-stoppoint-arrivals'
import formatArrivals from './helpers/format-arrivals'

const log = console.log
log(chalk.bold.blue('WHERE\'S MY BUS'))

setInterval(() => {
  getStopPointArrivals({ stopPointId })
    .then((arrivals) => {
      formatArrivals(arrivals)
    })
}, refresh)
