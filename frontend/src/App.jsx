import React, { useState } from "react";
import MapView from "./components/MapView";
import "./index.css";

function App() {
  const [predictions, setPredictions] = useState([]);

  const handlePrediction = async (data) => {
    try {
      console.log("Sending data to backend:", data);
      const response = await fetch("http://localhost:8000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      });
      const result = await response.json();
      console.log("Prediction result:", result);
      setPredictions([...predictions, result]);
    } catch (error) {
      console.error("Error:", error);
    }
  };

  return (
    <div className="app">
      <header>
        <h1>Water Potability Predictor</h1>
      </header>
      <main>
        {/* Pass handlePrediction as the onPredict prop */}
        <MapView onPredict={handlePrediction} />

        <div className="predictions">
          <h2>Predictions</h2>
          {predictions.map((pred, idx) => (
            <div key={idx} className="prediction-card">
              <p>Potability: {pred.potability === 1 ? "Potable" : "Not Potable"}</p>
              <p>Confidence: {(pred.confidence * 100).toFixed(2)}%</p>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
}

export default App;
