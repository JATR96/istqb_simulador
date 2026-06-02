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
      >
        ← Anterior
      </button>

      <button
        className={
          isMarked
            ? "mark-button active"
            : "mark-button"
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
      >
        Siguiente →
      </button>

    </div>
  );
}

export default QuestionNavigator;