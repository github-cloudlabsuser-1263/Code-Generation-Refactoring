// Weather Fetcher in JavaScript (Node.js)
const fetch = require('node-fetch');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

function getWeather(city, apiKey) {
  const url = `https://api.openweathermap.org/data/2.5/weather?q=${encodeURIComponent(city)}&appid=${apiKey}&units=metric`;
  fetch(url)
    .then(res => res.json())
    .then(data => {
      if (data.cod === 200) {
        console.log(`\nWeather in ${city}:`);
        console.log(`Temperature: ${data.main.temp}°C`);
        console.log(`Feels like: ${data.main.feels_like}°C`);
        console.log(`Condition: ${data.weather[0].description}`);
      } else {
        console.log(`\n[Error] ${data.message}`);
      }
      rl.close();
    })
    .catch(err => {
      console.log('\n[Error] Could not fetch weather data.');
      rl.close();
    });
}

console.log('=== Weather Fetcher (OpenWeatherMap) ===');
rl.question('Enter your OpenWeatherMap API key: ', apiKey => {
  rl.question('Enter city name: ', city => {
    getWeather(city, apiKey.trim());
  });
});
