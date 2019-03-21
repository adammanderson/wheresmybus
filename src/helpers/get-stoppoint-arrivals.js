import fetch from 'node-fetch'
import ora from 'ora'
import { api } from '../../config'
import { apiBase } from '../constants/api'

const getStopPointArrivals = ({ stopPointId }) => (
  new Promise((resolve, reject) => {
    const spinner = ora('Fetching StopPoint Arrivals').start();
    const endpoint = `/StopPoint/${stopPointId}/Arrivals?app_id=${api.appId}&app_key=${api.appKey}`

    fetch(`${apiBase}${endpoint}`)
      .then((response) => {
        spinner.succeed(`Recieved StopPoint Arrival Data`);

        resolve(response.json())
      })
  })
)

export default getStopPointArrivals
