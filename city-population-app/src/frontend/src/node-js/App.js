import React, { useState } from "react";

function App() {
  const [health, setHealth] = useState("");
  const [upsertResponse, setUpsertResponse] = useState("");
  const [queryResponse, setQueryResponse] = useState("");

  const checkHealth = async () => {
    try {
      const response = await fetch("http://localhost:8000/health");
      const text = await response.text();
      setHealth(text);
    } catch (error) {
      setHealth("Error: " + error.message);
    }
  };

  const upsertCity = async () => {
    try {
      // Example data (adjust as needed)
      const city = "New York";
      const population = 8500000;
      const response = await fetch("http://localhost:8000/upsert", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ city, population }),
      });
      const result = await response.json();
      setUpsertResponse(JSON.stringify(result));
    } catch (error) {
      setUpsertResponse("Error: " + error.message);
    }
  };

  const queryCity = async () => {
    try {
      // Example city name
      const city = "New York";
      const response = await fetch(`http://localhost:8000/query?city=${city}`);
      const result = await response.json();
      setQueryResponse(JSON.stringify(result));
    } catch (error) {
      setQueryResponse("Error: " + error.message);
    }
  };

  return (
    <div style={{ padding: "1rem", fontFamily: "Arial" }}>
      <h1>City Population API Explorer</h1>
      <div style={{ marginBottom: "1rem" }}>
        <button onClick={checkHealth}>Check Health</button>
        <div>
          <strong>Health Response:</strong> {health}
        </div>
      </div>
      <div style={{ marginBottom: "1rem" }}>
        <button onClick={upsertCity}>Upsert City</button>
        <div>
          <strong>Upsert Response:</strong> {upsertResponse}
        </div>
      </div>
      <div style={{ marginBottom: "1rem" }}>
        <button onClick={queryCity}>Query City</button>
        <div>
          <strong>Query Response:</strong> {queryResponse}
        </div>
      </div>
    </div>
  );
}

export default App;
