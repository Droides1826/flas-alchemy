import { useEffect, useState } from "react";
import { Response } from "../types/response";

export default function Categorias() {
  const [data, setData] = useState<Response>();

  useEffect(() => {
    fetch("http://127.0.0.1:5000/categorias")
      .then((response) => response.json())
      .then((data) => setData(data));
  }, []);

  if (data) {
    return (
      <>
        <div className="flex gap-2 flex-col">
          {data.data.map((item) => (
            <div className="flex flex-row rounded-md p-3 border border-zinc-200 justify-between">
              <div>
                <p className="font-semibold text-xl">{item.nombre}</p>
                <p>{item.descripcion}</p>
              </div>
              <div></div>
              <div className="flex flex-row gap-2">
                <div>
                  <button className="btn btn-neutral">Eliminar</button>
                </div>
                <div>
                  <button className="btn btn-primary">Actualizar</button>
                </div>
              </div>
            </div>
          ))}
        </div>
      </>
    );
  }
}
