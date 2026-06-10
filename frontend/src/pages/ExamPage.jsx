import { useEffect, useState } from "react";

import { generateExam } from "../services/examService";

import Timer from "../components/Timer";

import ExamHeader from "../components/ExamHeader";

import QuestionCard from "../components/QuestionCard";

import QuestionNavigator from "../components/QuestionNavigator";

import { useNavigate } from "react-router-dom";

import { submitExam } from "../services/examService";

import Loader from "../components/Loader";

import { useCertification } from "../context/CertificationContext";

import { useExamConfig } from "../context/ExamConfigContext";

/*
|--------------------------------------------------------------------------
| styles
|--------------------------------------------------------------------------
*/

import "../styles/exam.css";

/*
|--------------------------------------------------------------------------
| EXAM PAGE
|--------------------------------------------------------------------------
*/

function ExamPage() {

  const [questions, setQuestions] =
    useState([]);

  const [loading, setLoading] =
    useState(true);

  const [currentQuestion, setCurrentQuestion] =
    useState(0);

  const [answers, setAnswers] =
    useState({});

  const [markedQuestions, setMarkedQuestions] =
    useState([]);

  const navigate = useNavigate();

  const {
    certification
  } = useCertification();

  const {
    examConfig
  } = useExamConfig();

  /*
  |--------------------------------------------------------------------------
  | CARGAR EXAMEN
  |--------------------------------------------------------------------------
  */

  useEffect(() => {

    if (certification) {

      loadExam();

    }

  }, [
      certification,
      examConfig.language,
      examConfig.exam_mode,
      examConfig.question_count,
      examConfig.chapters,
      examConfig.learning_objectives
  ]);

  /*
  |--------------------------------------------------------------------------
  | GENERAR EXAMEN
  |--------------------------------------------------------------------------
  */

  const loadExam = async () => {

    setLoading(true);

    try {

      const data =
        await generateExam({

          certification,

          language:
            examConfig.language,

          exam_mode:
            examConfig.exam_mode,

          question_count:
            examConfig.question_count,
          
          chapters:
            examConfig.chapters,

          learning_objectives:
            examConfig.learning_objectives
        });

      setQuestions(data.questions);

      setCurrentQuestion(0);

      setAnswers({});

      setMarkedQuestions([]);

    } catch (error) {

      console.error(error);

    } finally {
      setLoading(false);
    }
  };

  /*
  |--------------------------------------------------------------------------
  | RESPUESTA
  |--------------------------------------------------------------------------
  */

  const handleSelectOption = (
    optionId
  ) => {

    const question =
      questions[currentQuestion];

    const multipleAnswers =
      question.correct_answers_count > 1;

    // ==================================
    // CHECKBOX
    // ==================================

    if (multipleAnswers) {

      const currentSelections =
        answers[currentQuestion] || [];

      const alreadySelected =
        currentSelections.includes(
          optionId
        );

      const updatedSelections =
        alreadySelected

          ? currentSelections.filter(
              (id) => id !== optionId
            )

          : [
              ...currentSelections,
              optionId
            ];

      setAnswers({

        ...answers,

        [currentQuestion]:
          updatedSelections
      });

      return;
    }

    // ==================================
    // RADIO
    // ==================================

    setAnswers({

      ...answers,

      [currentQuestion]:
        [optionId]
    });
  };

  /*
  |--------------------------------------------------------------------------
  | NAVEGACIÓN
  |--------------------------------------------------------------------------
  */

  const goNext = () => {

    if (
      currentQuestion <
      questions.length - 1
    ) {

      setCurrentQuestion(
        currentQuestion + 1
      );
    }
  };

  const goPrevious = () => {

    if (currentQuestion > 0) {

      setCurrentQuestion(
        currentQuestion - 1
      );
    }
  };

  /*
  |--------------------------------------------------------------------------
  | MARCAR PREGUNTA
  |--------------------------------------------------------------------------
  */

  const toggleMarkQuestion = () => {

    const exists =
      markedQuestions.includes(
        currentQuestion
      );

    if (exists) {

      setMarkedQuestions(

        markedQuestions.filter(
          (q) => q !== currentQuestion
        )
      );

    } else {

      setMarkedQuestions([
        ...markedQuestions,
        currentQuestion
      ]);
    }
  };

  /*
  |--------------------------------------------------------------------------
  | TIEMPO FINALIZADO
  |--------------------------------------------------------------------------
  */

  const handleTimeEnd = () => {

    alert(
      "Tiempo finalizado"
    );
  };

  /*
  |--------------------------------------------------------------------------
  | FINALIZAR EXAMEN
  |--------------------------------------------------------------------------
  */

  const finishExam = async () => {

  try {

    const formattedAnswers =
      questions.map((question, index) => ({

        question_id:
          question.id,

        selected_option_ids:
          answers[index] || []
      }));

    const result =
      await submitExam({

        certification,

        language:
          examConfig.language,

        exam_mode:
          examConfig.exam_mode,

        duration_seconds:
          examConfig.duration_seconds,

        answers:
          formattedAnswers
      });

    navigate(
      "/results",
      {
        state: result
      }
    );

    } catch (error) {

      console.error(error);
    }
  };

  /*
  |--------------------------------------------------------------------------
  | LOADING
  |--------------------------------------------------------------------------
  */

  if (loading) {

    return <Loader />;
  }

  /*
  |--------------------------------------------------------------------------
  | SIN PREGUNTAS
  |--------------------------------------------------------------------------
  */

  if (questions.length === 0) {

    return (
      <div className="loading">
        No existen preguntas disponibles
      </div>
    );
  }

  const question =
    questions[currentQuestion];

  return (
    <div className="exam-page">

      {/* ================================== */}
      {/* HEADER */}
      {/* ================================== */}

      <ExamHeader
        currentQuestion={
          currentQuestion
        }
        totalQuestions={
          questions.length
        }
      />

      {/* ================================== */}
      {/* TIMER */}
      {/* ================================== */}

      <Timer
        initialSeconds={examConfig.duration_seconds}
        onTimeEnd={handleTimeEnd}
      />

      {/* ================================== */}
      {/* QUESTION */}
      {/* ================================== */}

      <QuestionCard
        question={question}
        selectedOptions={
          answers[currentQuestion] || []
        }
        onSelectOption={
          handleSelectOption
        }
      />

      {/* ================================== */}
      {/* NAVIGATION */}
      {/* ================================== */}

      <QuestionNavigator
        currentQuestion={
          currentQuestion
        }
        totalQuestions={
          questions.length
        }
        goNext={goNext}
        goPrevious={goPrevious}
        markedQuestions={
          markedQuestions
        }
        toggleMarkQuestion={
          toggleMarkQuestion
        }
      />

      {/* ================================== */}
      {/* FINALIZAR EXAMEN */}
      {/* ================================== */}

      <div className="finish-container">
        <button
          className="finish-button"
          onClick={finishExam}
        >
          Finalizar examen
        </button>
      </div>

    </div>
  );
}

export default ExamPage;