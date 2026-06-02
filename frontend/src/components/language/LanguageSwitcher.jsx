import { useTranslation } from "react-i18next";

function LanguageSwitcher() {
  const { i18n, t } = useTranslation();

  /*
  |--------------------------------------------------------------------------
  | CAMBIO DE IDIOMA
  |--------------------------------------------------------------------------
  */

  const changeLanguage = (language) => {
    i18n.changeLanguage(language);

    localStorage.setItem(
      "language",
      language
    );
  };

  return (
    <div className="language-switcher">
      <button
        onClick={() => changeLanguage("es")}
      >
        {t("language.spanish")}
      </button>

      <button
        onClick={() => changeLanguage("en")}
      >
        {t("language.english")}
      </button>
    </div>
  );
}

export default LanguageSwitcher;