import React from "react";

import ReactDOM from "react-dom/client";

import App from "./App";

/*
|--------------------------------------------------------------------------
| i18next
|--------------------------------------------------------------------------
*/

import "./i18n";

/*
|--------------------------------------------------------------------------
| ESTILOS
|--------------------------------------------------------------------------
*/

import "./styles/global.css";

import "./styles/responsive.css";

import {
  ThemeProvider
} from "./context/ThemeContext";

ReactDOM.createRoot(
  document.getElementById("root")
).render(

  <React.StrictMode>

    <ThemeProvider>

      <App />

    </ThemeProvider>

  </React.StrictMode>
);