import { useTranslation } from "react-i18next";

function ExamsPage() {
  const { t } = useTranslation();

  return (
    <div className="page-container">
      <h2>
        {t("exams.title")}
      </h2>

      <p>
        {t("exams.description")}
      </p>
    </div>
  );
}

export default ExamsPage;