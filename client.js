const fetch = require("node-fetch");

const getPercentChange = () => {
	fetch('http://127.0.0.1:5000/percent_change/AAPL')
  		.then(response => response.text())
  		.then(data => console.log(data));	
}

getPercentChange();