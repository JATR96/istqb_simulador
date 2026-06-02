function ExamHeader({
  currentQuestion,
  totalQuestions
}) {

  const progress =
    ((currentQuestion + 1) /
      totalQuestions) * 100;

  return (
    <div className="exam-header">

      <h2>
        Simulador ISTQB
      </h2>

      <div className="progress-info">

        Pregunta {currentQuestion + 1}{" "}
        de {totalQuestions}

      </div>

      <div className="progress-bar">

        <div
          className="progress-fill"
          style={{
            width: `${progress}%`
          }}
        />

      </div>

    </div>
  );
}

export default ExamHeader;