import React, { useState } from "react";

function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    const response = await fetch(`http://localhost:8000/search?query=${query}`);
    const data = await response.json();
    setResults(data);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>식품 검색</h1>
      <input
        type="text"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        placeholder="검색어 입력"
      />
      <button onClick={handleSearch}>검색</button>

      <ul>
        {results.map((item) => (
          <li key={item.id}>
            <b>{item.name}</b> - {item.calories} kcal
            {" | "} 단백질: {item.protein} g
            {" | "} 탄수화물: {item.carbs} g
            {" | "} 지방: {item.fat} g
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;