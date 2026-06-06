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

import {
  CertificationProvider
} from "./context/CertificationContext";

ReactDOM.createRoot(
  document.getElementById("root")
).render(

  <React.StrictMode>

    <ThemeProvider>

      <ToastProvider>

        <CertificationProvider>

          <AppRouter />

        </CertificationProvider>

      </ToastProvider>

    </ThemeProvider>

  </React.StrictMode>
);