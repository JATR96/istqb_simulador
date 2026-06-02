function StatsCard({
  title,
  value
}) {

  return (
    <div className="stats-card">

      <h3>
        {title}
      </h3>

      <div className="stats-value">

        {value}

      </div>

    </div>
  );
}

export default StatsCard;