import { useEffect, useState } from "react";

import {
  generateExam
} from "../services/examService";

import Timer from "../components/Timer";

import ExamHeader from "../components/ExamHeader";

import QuestionCard from "../components/QuestionCard";

import QuestionNavigator from "../components/QuestionNavigator";

import "../styles/exam.css";

import { useNavigate } from "react-router-dom";

import { submitExam } from "../services/examService";

import Loader from "../components/Loader";

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

  /*
  |--------------------------------------------------------------------------
  | CARGAR EXAMEN
  |--------------------------------------------------------------------------
  */

  useEffect(() => {

    loadExam();

  }, []);

  /*
  |--------------------------------------------------------------------------
  | GENERAR EXAMEN
  |--------------------------------------------------------------------------
  */

  const loadExam = async () => {

    try {

      const data =
        await generateExam({

          certification:
            "Foundation",

          language: "es",

          exam_mode: "quick",

          question_count: 10
        });

      setQuestions(data.questions);

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

    setAnswers({

      ...answers,

      [currentQuestion]:
        optionId
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

        question_id: question.id,

        selected_option_id:
          answers[index] || -1
      }));

    const result =
      await submitExam({

        certification:
          "Foundation",

        language: "es",

        exam_mode: "quick",

        duration_seconds: 3600,

        answers: formattedAnswers
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
        initialSeconds={3600}
        onTimeEnd={handleTimeEnd}
      />

      {/* ================================== */}
      {/* QUESTION */}
      {/* ================================== */}

      <QuestionCard
        question={question}
        selectedOption={
          answers[currentQuestion]
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

      <button
        className="finish-button"
        onClick={finishExam}
      >
        Finalizar examen
      </button>

    </div>
  );
}

export default ExamPage;