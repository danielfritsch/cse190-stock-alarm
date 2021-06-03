import logo from './logo.svg';
import './App.css';

const fetch = require("node-fetch");

function App() {
  var ticker;
  var sens;
  var range;

  function handleClick(tick) {
    ticker = tick;
    alert("You selected ticker: " + ticker);
  }

  function handleSens(sen) {
    sens = sen;
    alert("You selected sensitivity level: " + sens);
  }

  async function getCurrentPercentChange(ticker) {
    const response = await fetch('http://127.0.0.1:5000/percent_change/' + ticker, {
      method: 'get',
      mode: 'cors',
    });

    return response;
  }

  async function getRange(tic, sen) {
    const response = await fetch('http://127.0.0.1:5000/get_sensitivity_range/' + tic + '/' + sen, {
      method: 'get',
      mode: 'cors'
    });

    return response;
  }

  async function handleDone() {
    alert("Thank you! Another alert will display when selected ticker has moved beyond your selected sensitivity level");
    const range_response = await getRange(ticker, sens);
    let range = await range_response.json();
    range = range['range'];
    console.log("This is the range the stock is expected to move in-between at a " + sens + " sensitivity level: " + range);

    let percent_change = 0;
    while (true) {
      // NOTE: uncomment the next three lines to simulate a stock's movement
      // percent_change = percent_change + 0.25;
      // sleep(3000);
      // console.log("CURRENT PERCENT CHANGE: " + percent_change);

      // NOTE: comment out the next four lines to simulate a stock's movement above
      const percent_response = await getCurrentPercentChange(ticker);
      percent_change = await percent_response.json();
      percent_change = percent_change['percent_change']
      console.log(percent_change)

      if (percent_change <= range[0]) break;
      else if (percent_change >= range[1]) break;
    }
    alert(ticker + "'s activity has moved outside of your selected sensitivity level: " + sens);
  }

  function sleep(milliseconds) {
    const date = Date.now();
    let currentDate = null;
    do {
      currentDate = Date.now();
    } while (currentDate - date < milliseconds);
  }

  /**
   * 
   */
  return (
    <div className="App" style={{ backgroundColor: '#d7f8ff', height: 1000 }}>
      <br/>
      <div style={styles.centerDiv}>
        <h1 style={{ height: 10 }}>Stock Sensitivity Alarm Clock</h1>
      </div>

      <br />
      <br/>
      <br/>
      <br/>

      <div style={styles.centerDiv}>
        <label>Select Tickers &nbsp;</label>
        <button className='tck_button' id='AAPL' style={{ width: 130 }} onClick={() => handleClick("AAPL")}>
          AAPL
					</button>
        <button className='tck_button' id='TSLA' style={{ width: 130 }} onClick={() => handleClick("TSLA")}>
          TSLA
					</button>
        <button className='tck_button' id='SQ' style={{ width: 130 }} onClick={() => handleClick("SQ")}>
          SQ
					</button>
        <button className='tck_button' id='AMZN' style={{ width: 130 }} onClick={() => handleClick("AMZN")}>
          AMZN
					</button>
        <button className='tck_button' id='MSFT' style={{ width: 130 }} onClick={() => handleClick("MSFT")}>
          MSFT
					</button>
        <button className='tck_button' id='BABA' style={{ width: 130 }} onClick={() => handleClick("BABA")}>
          BABA
					</button>
        <button className='tck_button' id='FB' style={{ width: 130 }} onClick={() => handleClick("FB")}>
          FB
					</button>
        <button className='tck_button' id='PANW' style={{ width: 130 }} onClick={() => handleClick("PANW")}>
          PANW
					</button>
        <button className='tck_button' id='NFLX' style={{ width: 130 }} onClick={() => handleClick("NFLX")}>
          NFLX
					</button>
        <button className='tck_button' id='NVDA' style={{ width: 130 }} onClick={() => handleClick("NVDA")}>
          NVDA
					</button>
      </div>

      <br />
      <br/>

      <div style={styles.centerDiv}>
        <label>Select Sensitivity &nbsp;</label>
        <button className='sen_button' id='LOW' style={{ width: 130 }} onClick={() => handleSens("LOW")}>
          LOW
					</button>
        <button className='sen_button' id='MEDIUM' style={{ width: 130 }} onClick={() => handleSens("MEDIUM")}>
          MEDIUM
					</button>
        <button className='sen_button' id='HIGH' style={{ width: 130 }} onClick={() => handleSens("HIGH")}>
          HIGH
          </button>
      </div>

      <br />

      <br/>
      <br/>
      <br/>
      <div style={styles.centerDiv}>
        <button className='DONE' style={styles.allButton} onClick={() => handleDone()}>
          DONE
          </button>
      </div>
    </div>
  );
}

const styles = {
  centerDiv: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    height: 20
  },
  allButton: {
    height: 40,
    width: 500
  }
};

export default App;
