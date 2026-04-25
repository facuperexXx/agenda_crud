import { useState, useEffect } from 'react'
import './App.css'

function Home() {
  const [texto, setMensaje] = useState("OK")

  useEffect(() => {

    fetch('http://localhost:5000').then(respuesta => {return respuesta.text();

    }).then(texto => {setMensaje(texto)})

  }, []);

  return(
    <div>
      <h3>Respuesta API</h3>
      <p>{texto}</p>
    </div>
  )
}

export default Home
