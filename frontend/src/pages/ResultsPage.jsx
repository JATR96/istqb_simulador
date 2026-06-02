import { useTranslation } from "react-i18next";

function ResultsPage() {
  const { t } = useTranslation();

  return (
    <div className="page-container">
      <h2>
        {t("results.title")}
      </h2>

      <p>
        {t("results.description")}
      </p>
    </div>
  );
}

export default ResultsPage;