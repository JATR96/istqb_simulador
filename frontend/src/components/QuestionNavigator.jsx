function QuestionNavigator({
  currentQuestion,
  totalQuestions,
  goNext,
  goPrevious,
  markedQuestions,
  toggleMarkQuestion
}) {

  const isMarked =
    markedQuestions.includes(
      currentQuestion
    );

  return (
    <div className="question-navigation">

      <button
        onClick={goPrevious}
        disabled={currentQuestion === 0}
        className="button-navigation-question"
      >
        ← Anterior
      </button>

      <button
        className={
          isMarked
            ? "mark-button active"
            : "mark-button button-navigation-question"
        }
        onClick={toggleMarkQuestion}
      >
        🚩 Revisar
      </button>

      <button
        onClick={goNext}
        disabled={
          currentQuestion ===
          totalQuestions - 1
        }
        className="button-navigation-question"
      >
        Siguiente →
      </button>

    </div>
  );
}

export default QuestionNavigator;