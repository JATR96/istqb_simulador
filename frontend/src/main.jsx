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

import {
  ToastProvider
} from "./context/ToastContext";

ReactDOM.createRoot(
  document.getElementById("root")
).render(

  <React.StrictMode>

    <ThemeProvider>

      <ToastProvider>

        <AppRouter />

      </ToastProvider>

    </ThemeProvider>

  </React.StrictMode>
);