import { useTranslation } from "react-i18next";

import CertificationSelector from "../components/CertificationSelector";

import { useNavigate } from "react-router-dom";

import ExamConfigForm from "../components/ExamConfigForm";

import "../styles/examsPage.css";

function ExamsPage() {

  const { t } = useTranslation();

  const navigate = useNavigate();

  const handleGenerateExam = () => {

  navigate("/exam");

  };

  return (

    <div className="page-container">

      <h2>
        {t("exams.title")}
      </h2>

      <p>
        {t("exams.description")}
      </p>

      <CertificationSelector />

      <ExamConfigForm />

      <div className="generate-exam-container">

        <button
          className="generate-exam-button"
          onClick={handleGenerateExam}
        >
          Generar examen
        </button>

      </div>

    </div>

  );
}

export default ExamsPage;