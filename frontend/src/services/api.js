import axios from "axios";

/*
|--------------------------------------------------------------------------
| CONFIGURACIÓN GLOBAL AXIOS
|--------------------------------------------------------------------------
|
| Centralizamos aquí toda la comunicación
| con FastAPI.
|
| Esto facilita:
| - mantenimiento
| - escalabilidad
| - cambio futuro de URL
|
*/

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

export default api;