import chalk from 'chalk'
import { stopPointId, refresh } from '../config'
import getStopPointArrivals from './helpers/get-stoppoint-arrivals'
import formatArrivals from './helpers/format-arrivals'
import scrollController from 'scroll-controller'

const log = console.log
log(chalk.bold.blue('WHERE\'S MY BUS'))

setInterval(() => {
  getStopPointArrivals({ stopPointId })
    .then((arrivals) => {
      formatArrivals(arrivals)
      let arr = []
      for(var i = 0; i < 119; i++){
          arr[i] = i%2 == 0 ? 255 : 0
      }
      setTimeout(()=>{
          scrollController.display(arr)
      },100)
    })
    .catch(() => {})
}, 2000)
