import fetch from 'node-fetch'
import chalk from 'chalk'
import ora from 'ora'
import log from  './log'
import { api } from '../../config'
import { apiBase } from '../constants/api'

const getStopPointArrivals = ({ stopPointId }) => (
  new Promise((resolve, reject) => {
    const spinner = ora(log('Fetching StopPoint Arrivals', 'info')).start();
    const endpoint = `/StopPoint/${stopPointId}/Arrivals?app_id=${api.appId}&app_key=${api.appKey}`

    fetch(`${apiBase}${endpoint}`)
      .then(response => response.json())
      .then((arrivals) => {
          spinner.succeed(log('Recieved response', 'success'))
          if (!arrivals.length) {
            spinner.fail(log(arrivals.message, 'error'))
            return reject()
          }
          return resolve(arrivals)
      })
      .catch((err) => {
          spinner.fail(log('Data Error', 'error'))
          reject(err)
      })
  })
)

export default getStopPointArrivals
