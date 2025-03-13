import "./App.css";
import { Routes, Route, BrowserRouter } from "react-router-dom";
import { Main } from "./routes/lazy-routes";
import Navbar from "./ui/navbar";
import Pedidos from "./routes/pedidos";
import Categorias from "./routes/categorias";
import Historial from "./routes/historial";

function App() {
  return (
    <BrowserRouter>
    <Navbar/>
      <Routes >
          <Route path="/" element={<Main/>} />
          <Route path="/categorias" element={<Categorias/>} />
          <Route path="historial" element={<Historial/>}/>
          <Route path="/pedidos" element={<Pedidos/>} />
        </Routes>
    </BrowserRouter>
  );
}

export default App;
