function PerformanceChart({
  history
}) {

  return (
    <div className="chart-container">

      <h2>
        Historial de Scores
      </h2>

      <div className="chart-bars">

        {history.map((item) => (

          <div
            key={item.id}
            className="chart-item"
          >

            <div
              className="chart-bar"
              style={{
                height:
                  `${item.score}%`
              }}
            />

            <span>
              {item.score}%
            </span>

          </div>
        ))}

      </div>

    </div>
  );
}

export default PerformanceChart;