import { useTranslation } from "react-i18next";

function NotFoundPage() {
  const { t } = useTranslation();

  return (
    <div className="page-container">
      <h2>404</h2>

      <p>
        {t("notFound.title")}
      </p>
    </div>
  );
}

export default NotFoundPage;