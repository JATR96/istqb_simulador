import { Link } from "react-router-dom";

import { useTranslation } from "react-i18next";

function Navbar() {
  const { t } = useTranslation();

  return (
    <nav className="navbar">
      <Link to="/">
        {t("navbar.home")}
      </Link>

      <Link to="/exams">
        {t("navbar.exams")}
      </Link>

      <Link to="/results">
        {t("navbar.results")}
      </Link>
    </nav>
  );
}

export default Navbar;