function QuestionCard({
  question,
  selectedOptions,
  onSelectOption
}) {

  return (
    <div className="question-card">

      {/* ================================== */}
      {/* PREGUNTA */}
      {/* ================================== */}

      <h3 className="question-title">
        {question.question}
      </h3>

      {/* ================================== */}
      {/* IMAGEN */}
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
      {/* OPCIONES */}
      {/* ================================== */}

      <div className="options-container">

        {question.options.map((option) => (

          <button
            key={option.id}

            className={
              (selectedOptions || []).includes(
                option.id
              )
                ? "option-button selected"
                : "option-button"
            }

            onClick={() =>
              onSelectOption(option.id)
            }
          >

            {option.texto}

          </button>
        ))}

      </div>

    </div>
  );
}

export default QuestionCard;