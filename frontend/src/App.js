import React, { useState, useRef } from "react";

function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);
  const [suggests, setSuggests] = useState([]);
  const [openSuggest, setOpenSuggest] = useState(false);
  const [detail, setDetail] = useState(null);
  const [showDetail, setShowDetail] = useState(false);
  const debounceRef = useRef(null);

  const API_BASE = "http://localhost:8000";

  const handleSearch = async (q = query) => {
    if (!q.trim()) return;
    const response = await fetch(`${API_BASE}/foods/search?query=${encodeURIComponent(q)}`);
    const data = await response.json();
    setResults(Array.isArray(data) ? data : []);
  };

  const handleChange = (e) => {
    const v = e.target.value;
    setQuery(v);

    if (debounceRef.current) clearTimeout(debounceRef.current);

    if (!v.trim()) {
      setSuggests([]);
      setOpenSuggest(false);
      return;
    }

    setOpenSuggest(true);

    debounceRef.current = setTimeout(async () => {
      try {
        const res = await fetch(`${API_BASE}/foods/autocomplete?query=${encodeURIComponent(v)}&limit=10`);
        const data = await res.json();
        setSuggests(Array.isArray(data) ? data : []);
      } catch {
        setSuggests([]);
      }
    }, 250);
  };

  const handleSelect = (item) => {
    setQuery(item.name);
    setOpenSuggest(false);
    handleSearch(item.name);
  };

  const fetchDetail = async (name) => {
    const res = await fetch(`${API_BASE}/foods/detail?name=${encodeURIComponent(name)}`);
    const data = await res.json();
    setDetail(data);
    setShowDetail(true);
  };

  return (
    <div style={{ padding: "20px", maxWidth: "700px", margin: "0 auto" }}>
      <h1>식품 검색</h1>

      <div style={{ position: "relative" }}>
        <input
          type="text"
          value={query}
          onChange={handleChange}
          placeholder="검색어 입력"
          style={{ width: "100%", padding: "10px", fontSize: "16px" }}
          onFocus={() => setOpenSuggest(Boolean(query.trim()))}
          onKeyDown={(e) => {
            if (e.key === "Enter") handleSearch();
            if (e.key === "Escape") setOpenSuggest(false);
          }}
        />

        {/* 자동완성 */}
        {openSuggest && suggests.length > 0 && (
          <div
            style={{
              position: "absolute",
              top: 42,
              left: 0,
              right: 0,
              border: "1px solid #ddd",
              background: "#fff",
              borderRadius: "6px",
              boxShadow: "0 4px 12px rgba(0,0,0,0.1)",
              zIndex: 10,
            }}
          >
            {suggests.map((s) => (
              <div
                key={s.id}
                onMouseDown={(e) => e.preventDefault()}
                onClick={() => handleSelect(s)}
                style={{
                  padding: "8px 12px",
                  cursor: "pointer",
                  borderBottom: "1px solid #f5f5f5",
                }}
              >
                {s.name}
              </div>
            ))}
          </div>
        )}
      </div>

      <button onClick={() => handleSearch()} style={{ marginTop: "10px" }}>
        검색
      </button>

      {/* 검색 결과 리스트 */}
      <ul style={{ marginTop: "20px" }}>
        {results.map((item) => (
          <li
            key={item.name}
            onClick={() => fetchDetail(item.name)}
            style={{ cursor: "pointer", padding: "6px 0" }}
          >
            <b>{item.name}</b> - {item.calories} kcal
            {" | "} 단백질: {item.protein} g
            {" | "} 탄수화물: {item.carbs} g
            {" | "} 지방: {item.fat} g
            {" | "} 변형: {item.variants} 종
          </li>
        ))}
      </ul>

      {/* 상세 정보 모달 */}
      {showDetail && detail && (
        <div
          style={{
            position: "fixed",
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            background: "rgba(0,0,0,0.5)",
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            zIndex: 1000,
          }}
          onClick={() => setShowDetail(false)}
        >
          <div
            style={{
              background: "#fff",
              padding: "20px",
              borderRadius: "10px",
              width: "600px",
              maxHeight: "80vh",
              overflowY: "auto",
            }}
            onClick={(e) => e.stopPropagation()}
          >
            <h2>{detail.name}</h2>
            <p>검색된 데이터 수(평균값): {detail.variants} 종</p>
            <table style={{ width: "100%", borderCollapse: "collapse" }}>
              <thead>
                <tr>
                  <th>칼로리</th>
                  <th>탄수화물</th>
                  <th>단백질</th>
                  <th>지방</th>
                  <th>당류</th>
                  <th>식이섬유</th>
                  <th>나트륨</th>
                  <th>콜레스테롤</th>
                  <th>포화지방</th>
                  <th>트랜스지방</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td>{detail.calories}</td>
                  <td>{detail.carbs}</td>
                  <td>{detail.protein}</td>
                  <td>{detail.fat}</td>
                  <td>{detail.sugars}</td>
                  <td>{detail.fiber}</td>
                  <td>{detail.sodium}</td>
                  <td>{detail.cholesterol}</td>
                  <td>{detail.saturated_fat}</td>
                  <td>{detail.trans_fat}</td>
                </tr>
              </tbody>
            </table>
            <button onClick={() => setShowDetail(false)} style={{ marginTop: "10px" }}>
              닫기
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;
