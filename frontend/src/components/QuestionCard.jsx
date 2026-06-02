function QuestionCard({
  question,
  selectedOption,
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

      {question.image_url && (

        <div className="question-image-container">

          <img
            src={question.image_url}
            alt={
              question.image_description
            }
            className="question-image"
          />

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
              selectedOption === option.id
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