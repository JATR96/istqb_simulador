import React from "react";

import ReactDOM from "react-dom/client";

import AppRouter from "./router/AppRouter";

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

      <AppRouter />

    </ThemeProvider>

  </React.StrictMode>
);