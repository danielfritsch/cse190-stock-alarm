const fetch = require("node-fetch");

const getPercentChange = () => {
	fetch('http://127.0.0.1:5000/percent_change/AAPL')
  		.then(response => response.text())
  		.then(data => console.log(data));	
}

getPercentChange();

const getRange = () => {
	fetch('http://127.0.0.1:5000/get_sensitivity_range/AAPL/HIGH')
  		.then(response => response.text())
  		.then(data => console.log(data));	
}

getRange();