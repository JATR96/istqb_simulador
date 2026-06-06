import { useTranslation } from "react-i18next";

import CertificationSelector
from "../components/CertificationSelector";

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

      <CertificationSelector />

    </div>

  );
}

export default ExamsPage;