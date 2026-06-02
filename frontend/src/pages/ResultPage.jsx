import { useLocation } from "react-router-dom";

import "../styles/result.css";

function ResultPage() {

  const location = useLocation();

  const result = location.state;

  if (!result) {

    return (
      <div className="result-page">
        No existen resultados
      </div>
    );
  }

  return (
    <div className="result-page">

      {/* ================================== */}
      {/* SCORE */}
      {/* ================================== */}

      <div className="result-summary">

        <h1>
          Resultado Final
        </h1>

        <h2>
          {result.score}%
        </h2>

        <div
          className={
            result.passed
              ? "passed"
              : "failed"
          }
        >

          {result.passed
            ? "APROBADO"
            : "REPROBADO"}

        </div>

        <p>
          Correctas:
          {" "}
          {result.correct_answers}
        </p>

        <p>
          Incorrectas:
          {" "}
          {result.incorrect_answers}
        </p>

      </div>

      {/* ================================== */}
      {/* REVIEW */}
      {/* ================================== */}

      <div className="review-container">

        {result.review.map((item) => (

          <div
            key={item.question_id}
            className="review-card"
          >

            <h3>
              {item.question}
            </h3>

            <p>
              Tu respuesta:
              {" "}
              {item.selected_option_id}
            </p>

            <p>
              Correcta:
              {" "}
              {item.correct_option_id}
            </p>

            <p
              className={
                item.is_correct
                  ? "correct"
                  : "incorrect"
              }
            >

              {item.is_correct
                ? "Correcta"
                : "Incorrecta"}

            </p>

            <div className="explanation">

              {item.explanation}

            </div>

          </div>
        ))}

      </div>

    </div>
  );
}

export default ResultPage;