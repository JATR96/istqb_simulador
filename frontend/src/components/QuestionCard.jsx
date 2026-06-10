function QuestionCard({
  question,
  selectedOptions,
  onSelectOption
}) {

  const multipleAnswers =
    question.correct_answers_count > 1;

  return (

    <div className="question-card">

      {/* ================================== */}
      {/* PREGUNTA */}
      {/* ================================== */}

      <h3 className="question-title">
        {question.question}
      </h3>

      {/* ================================== */}
      {/* IMÁGENES */}
      {/* ================================== */}

      {question.images?.length > 0 && (

        <div className="question-images-container">

          {question.images.map(
            (image, index) => (

              <div
                key={index}
                className="question-image-container"
              >

                <img
                  src={image.url}
                  alt={
                    image.description ||
                    `image-${index}`
                  }
                  className="question-image"
                />

                {image.description && (

                  <p className="image-description">
                    {image.description}
                  </p>

                )}

              </div>
            )
          )}

        </div>
      )}

      {/* ================================== */}
      {/* INSTRUCCIÓN */}
      {/* ================================== */}

      <div className="question-instruction">

        {
          question.correct_answers_count === 1

            ? "Seleccione UNA opción"

            : `Seleccione ${question.correct_answers_count} opciones`
        }

      </div>

      {/* ================================== */}
      {/* OPCIONES */}
      {/* ================================== */}

      <div className="options-container">

        {question.options.map((option) => {

          const selected =
            (selectedOptions || []).includes(
              option.id
            );

          return (

            <button
              key={option.id}
              className={
                selected
                  ? "option-button selected"
                  : "option-button"
              }
              onClick={() =>
                onSelectOption(option.id)
              }
            >

              <span className="option-icon">

                {
                  multipleAnswers

                    ? (
                        selected
                          ? "☑"
                          : "☐"
                      )

                    : (
                        selected
                          ? "●"
                          : "○"
                      )
                }

              </span>

              <span className="option-text">
                {option.texto}
              </span>

            </button>

          );

        })}

      </div>

    </div>
  );
}

export default QuestionCard;