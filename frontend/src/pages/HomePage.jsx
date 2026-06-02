import { useTranslation } from "react-i18next";

function HomePage() {
  const { t } = useTranslation();

  return (
    <div className="page-container">
      <h2>
        {t("home.title")}
      </h2>

      <p>
        {t("home.description")}
      </p>
    </div>
  );
}

export default HomePage;