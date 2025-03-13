import "./App.css";
import { Routes, Route, BrowserRouter } from "react-router-dom";
import { Main } from "./routes/lazy-routes";
import Navbar from "./ui/navbar";

function App() {
  return (
    <BrowserRouter>
    <Navbar/>
      <Routes >
          <Route path="/" element={<Main/>} />
          <Route path="/main" element={<div>Gestion</div>} />
        </Routes>
    </BrowserRouter>
  );
}

export default App;
