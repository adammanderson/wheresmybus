import chalk from 'chalk'
import secondsToMinutes from './seconds-to-minutes'
const log = console.log

const formatArrivals = (arrivals) => {
  if (!arrivals.length) {
    return log('No arrivals due')
  }

  const { lineName, stationName, towards } = arrivals[0]
  const arrivalTimes = arrivals.sort((a, b) => (
    a.timeToStation - b.timeToStation
  )).map((prediction) => {
    const minutes = secondsToMinutes(prediction.timeToStation)
    return minutes > 0 ? `${minutes}m` : 'due'
  })
  const formattedArrivalTimes = arrivalTimes.join(' | ')
  const line = chalk.white.bgRed.bold(` ${lineName} `)
  const stopInfo = chalk.dim(`${stationName} towards ${towards}`)

  log(`${line} ${formattedArrivalTimes} ${stopInfo}\n`)
}

export default formatArrivals
