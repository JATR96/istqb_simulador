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

  /*
  |--------------------------------------------------------------------------
  | OPTION LETTER
  |--------------------------------------------------------------------------
  */

  const getOptionLetter = (optionId) => {

    const letters = {
      1: "A",
      2: "B",
      3: "C",
      4: "D",
      5: "E",
      6: "F"
    };

    return letters[optionId] || "";
  };

  /*
  |--------------------------------------------------------------------------
  | OPTION LETTERS
  |--------------------------------------------------------------------------
  */

  const getOptionLetters = (
    optionIds
  ) => {

    if (
      !optionIds ||
      optionIds.length === 0
    ) {

      return "Sin responder";
    }

    return optionIds
      .map(
        (id) =>
          getOptionLetter(id)
      )
      .join(", ");
  };

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

          {
            result.passed
              ? "APROBADO"
              : "REPROBADO"
          }

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

            <h3 className="question">
              {item.question}
            </h3>

            <p>

              Tu respuesta:

              {" "}

              {
                getOptionLetters(
                  item.selected_option_ids
                )
              }

            </p>

            <p>

              Correcta:

              {" "}

              {
                getOptionLetters(
                  item.correct_option_ids
                )
              }

            </p>

            <p
              className={
                item.is_correct
                  ? "correct"
                  : "incorrect"
              }
            >

              {
                item.is_correct
                  ? "Correcta"
                  : "Incorrecta"
              }

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