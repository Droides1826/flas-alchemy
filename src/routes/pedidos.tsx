import { useState,useEffect } from "react"
import { Pedidos } from "../types/pedidos"


export default function Pedidos () {
    const [data,setData] = useState<Pedidos>()

    useEffect(() => {
        fetch("http://127.0.0.1:5000/pedidos").then((reponse) => reponse.json()).then((pedidos) => setData(pedidos))
    })

    return(
        <div>
            {data?.data.map((item) => (
                <div>
                    <li>{item.fecha}</li>
                </div>
            ) )}
        </div>
    )
}