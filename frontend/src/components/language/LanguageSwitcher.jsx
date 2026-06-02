import { useTranslation } from "react-i18next";

function LanguageSwitcher() {
  const { i18n, t } = useTranslation();

  /*
  |--------------------------------------------------------------------------
  | CAMBIO DE IDIOMA
  |--------------------------------------------------------------------------
  */

  const changeLanguage = (event) => {

    const language = event.target.value;

    i18n.changeLanguage(language);

    localStorage.setItem(
      "language",
      language
    );
  };

  return (
    <div className="language-switcher">
      <select
        value={i18n.language}
        onChange={changeLanguage}
      >

        <option value="es">
          {t("language.spanish")}
        </option>

        <option value="en">
          {t("language.english")}
        </option>

      </select>
    </div>
  );
}

export default LanguageSwitcher;