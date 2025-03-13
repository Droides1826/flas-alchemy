import "./App.css";
import { Routes, Route, BrowserRouter } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <Routes>
          <Route path="/" element={<div>Hello world</div>} />
          <Route path="/main" element={<div>Gestion</div>} />
        </Routes>
    </BrowserRouter>
  );
}

export default App;
