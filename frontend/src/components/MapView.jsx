import React, { useState } from 'react';

function MapView() {
  const [inputData, setInputData] = useState({
    ph: 7.0,
    hardness: 150.0,
    solids: 10000.0,
    chloramines: 5.0,
    sulfate: 300.0,
    conductivity: 400.0,
    organic_carbon: 10.0,
    trihalomethanes: 50.0,
    turbidity: 3.5,
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setInputData({
      ...inputData,
      [name]: parseFloat(value),
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Send data to parent or API
    console.log('Input data:', inputData);
  };

  return (
    <div className="map-view">
      <h2>Water Quality Input</h2>
      <form onSubmit={handleSubmit}>
        {Object.keys(inputData).map((key) => (
          <div key={key} className="form-group">
            <label htmlFor={key}>{key}</label>
            <input
              type="number"
              id={key}
              name={key}
              value={inputData[key]}
              onChange={handleInputChange}
              step="0.01"
            />
          </div>
        ))}
        <button type="submit">Predict</button>
      </form>
    </div>
  );
}

export default MapView;
