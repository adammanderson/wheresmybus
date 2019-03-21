const secondsToMinutes = (seconds) => (
  `${Math.floor(seconds % 3600 / 60)}`
)

export default secondsToMinutes
