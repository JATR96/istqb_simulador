import i18n from "i18next";

import { initReactI18next } from "react-i18next";

import translationES from "../locales/es/translation.json";
import translationEN from "../locales/en/translation.json";

/*
|--------------------------------------------------------------------------
| RECURSOS DE IDIOMA
|--------------------------------------------------------------------------
*/

const resources = {
  es: {
    translation: translationES,
  },

  en: {
    translation: translationEN,
  },
};

/*
|--------------------------------------------------------------------------
| IDIOMA GUARDADO
|--------------------------------------------------------------------------
*/

const savedLanguage =
  localStorage.getItem("language") || "es";

/*
|--------------------------------------------------------------------------
| CONFIGURACIÓN i18next
|--------------------------------------------------------------------------
*/

i18n.use(initReactI18next).init({
  resources,

  lng: savedLanguage,

  fallbackLng: "es",

  interpolation: {
    escapeValue: false,
  },
});

export default i18n;