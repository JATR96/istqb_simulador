import {
  useExamConfig
} from "../context/ExamConfigContext";

import "../styles/examConfigForm.css";

function ExamConfigForm() {

  const {
    examConfig,
    setExamConfig
  } = useExamConfig();

  const updateField = (
    field,
    value
  ) => {

    setExamConfig({

      ...examConfig,

      [field]: value
    });
  };

  return (

    <div className="exam-config-form">

      <h3>
        Configuración del examen
      </h3>

      {/* Idioma */}

      <div className="config-group">

        <label>
          Idioma
        </label>

        <select
          value={examConfig.language}
          onChange={(event) =>
            updateField(
              "language",
              event.target.value
            )
          }
        >

          <option value="es">
            Español
          </option>

          <option value="en">
            Inglés
          </option>

        </select>

      </div>

      {/* Modo */}

      <div className="config-group">

        <label>
          Modo
        </label>

        <select
          value={examConfig.exam_mode}
          onChange={(event) =>
            updateField(
              "exam_mode",
              event.target.value
            )
          }
        >

          <option value="quick">
            Quick
          </option>

          <option value="real">
            Real Exam
          </option>

          <option value="study">
            Study
          </option>

        </select>

      </div>

      {/* Cantidad */}

      <div className="config-group">

        <label>
          Preguntas
        </label>

        <input
          type="number"
          min="1"
          max="200"
          value={
            examConfig.question_count
          }
          onChange={(event) =>
            updateField(
              "question_count",
              Number(
                event.target.value
              ) || 0
            )
          }
        />
      </div>

      {/* Tiempo */}

      <div className="config-group">

        <label>
          Tiempo (minutos)
        </label>

        <input
          type="number"
          min="1"
          value={
            examConfig.duration_seconds / 60
          }
          onChange={(event) =>
            updateField(
              "duration_seconds",
              (Number(
                event.target.value
              ) || 0) * 60
            )
          }
        />
      </div>

    </div>
  );
}

export default ExamConfigForm;