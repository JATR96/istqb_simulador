import { useTranslation } from "react-i18next";

import Navbar from "./Navbar";

import LanguageSwitcher from "../language/LanguageSwitcher";

function Header() {
  const { t } = useTranslation();

  return (
    <header className="header">
      <div className="header-container">
        <h1 className="logo">
          {t("app.title")}
        </h1>

        <div className="header-right">
          <Navbar />

          <LanguageSwitcher />
        </div>
      </div>
    </header>
  );
}

export default Header;