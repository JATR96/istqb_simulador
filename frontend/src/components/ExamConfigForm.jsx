import {
  useEffect,
  useState
} from "react";

import {
  useExamConfig
} from "../context/ExamConfigContext";

import {
  useCertification
} from "../context/CertificationContext";

import {
  getCertificationMetadata
} from "../services/certificationService";

import ChapterSelector from "./ChapterSelector";

import LearningObjectiveSelector
  from "./LearningObjectiveSelector";

import "../styles/examConfigForm.css";

function ExamConfigForm() {

  const {
    examConfig,
    setExamConfig
  } = useExamConfig();

  const {
    certification
  } = useCertification();

  const [
    chapters,
    setChapters
  ] = useState([]);

  const [
    learningObjectives,
    setLearningObjectives
  ] = useState([]);

  const updateField = (
    field,
    value
  ) => {

    setExamConfig({

      ...examConfig,

      [field]: value
    });
  };

  /*
  |--------------------------------------------------
  | CARGAR METADATA
  |--------------------------------------------------
  */

  useEffect(() => {

    if (!certification) {

      return;
    }

    loadMetadata();

  }, [certification]);

  const loadMetadata =
    async () => {

      try {

        const metadata =
          await getCertificationMetadata(
            certification
          );

        setChapters(
          metadata.chapters || []
        );

        setLearningObjectives(
          metadata.learning_objectives || []
        );

      } catch (error) {

        console.error(error);
      }
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

          <option value="official">
            Real Exam
          </option>

          <option value="chapter">
            Capítulo Específico
          </option>

          <option value="learning_objective">
            Objetivo de Aprendizaje
          </option>

        </select>

      </div>

      {/* Preguntas */}

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

      {/* CHAPTER */}

      {
        examConfig.exam_mode ===
          "chapter" && (

          <ChapterSelector

            chapters={chapters}

            selectedChapters={
              examConfig.chapters
            }

            onChange={(value) =>
              updateField(
                "chapters",
                value
              )
            }
          />
        )
      }

      {/* LEARNING OBJECTIVE */}

      {
        examConfig.exam_mode ===
          "learning_objective" && (

          <LearningObjectiveSelector

            objectives={
              learningObjectives
            }

            selectedObjectives={
              examConfig.learning_objectives
            }

            onChange={(value) =>
              updateField(
                "learning_objectives",
                value
              )
            }
          />
        )
      }

    </div>
  );
}

export default ExamConfigForm;