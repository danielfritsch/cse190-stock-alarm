import logo from './logo.svg';
import './App.css';

function App() {
  var tickers = [];

  function handleClick(tick) {
    tickers.push(tick);

    for (var i = 0; i < tickers.length; i += 1) console.log(tickers[i]);
  }

  return (
    <div className="App" style={{ backgroundColor: '#d7f8ff', height: 1000 }}>
      <div style={styles.centerDiv}>
        <h1 style={{ height: 10 }}>Stock Sensitivity Alarm Clock</h1>
      </div>

      <br />

      <div style={styles.centerDiv}>
        <label>Select Tickers &nbsp;</label>
        <button class='tck_button' id='AAPL' style={{ width: 130 }} onClick={() => handleClick("AAPL")}>
          AAPL
					</button>
        <button class='tck_button' id='TSLA' style={{ width: 130 }} onClick={() => handleClick("TSLA")}>
          TSLA
					</button>
        <button class='tck_button' id='SQ' style={{ width: 130 }} onClick={() => handleClick("SQ")}>
          SQ
					</button>
        <button class='tck_button' id='AMZN' style={{ width: 130 }} onClick={() => handleClick("AMZN")}>
          AMZN
					</button>
        <button class='tck_button' id='MSFT' style={{ width: 130 }} onClick={() => handleClick("MSFT")}>
          MSFT
					</button>
        <button class='tck_button' id='BABA' style={{ width: 130 }} onClick={() => handleClick("BABA")}>
          BABA
					</button>
        <button class='tck_button' id='FB' style={{ width: 130 }} onClick={() => handleClick("FB")}>
          FB
					</button>
        <button class='tck_button' id='AMD' style={{ width: 130 }} onClick={() => handleClick("AMD")}>
          AMD
					</button>
        <button class='tck_button' id='NFLX' style={{ width: 130 }} onClick={() => handleClick("NFLX")}>
          NFLX
					</button>
        <button class='tck_button' id='NVDA' style={{ width: 130 }} onClick={() => handleClick("NVDA")}>
          NVDA
					</button>
      </div>

      <br />

      <div style={styles.centerDiv}>
        <label>Select Sensitivity &nbsp;</label>
        <button class='sen_button' id='AAPL' style={{ width: 130 }} onClick={() => handleClick("LOW")}>
          LOW
					</button>
        <button class='sen_button' id='TSLA' style={{ width: 130 }} onClick={() => handleClick("MEDIUM")}>
          MEDIUM
					</button>
        <button class='sen_button' id='SQ' style={{ width: 130 }} onClick={() => handleClick("HIGH")}>
          HIGH
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
