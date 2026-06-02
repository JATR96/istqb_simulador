import { useEffect, useState } from "react";

import api from "../services/api";

import StatsCard from "../components/StatsCard";

import PerformanceChart from "../components/PerformanceChart";

import "../styles/statistics.css";

function StatisticsPage() {

  const [stats, setStats] =
    useState(null);

  const [loading, setLoading] =
    useState(true);

  /*
  |--------------------------------------------------------------------------
  | LOAD STATS
  |--------------------------------------------------------------------------
  */

  useEffect(() => {

    loadStatistics();

  }, []);

  /*
  |--------------------------------------------------------------------------
  | API
  |--------------------------------------------------------------------------
  */

  const loadStatistics = async () => {

    try {

      const response =
        await api.get(
          "/statistics/global"
        );

      setStats(response.data);

    } catch (error) {

      console.error(error);

    } finally {

      setLoading(false);
    }
  };

  /*
  |--------------------------------------------------------------------------
  | LOADING
  |--------------------------------------------------------------------------
  */

  if (loading) {

    return (
      <div className="statistics-page">
        Cargando estadísticas...
      </div>
    );
  }

  /*
  |--------------------------------------------------------------------------
  | EMPTY
  |--------------------------------------------------------------------------
  */

  if (!stats) {

    return (
      <div className="statistics-page">
        No existen estadísticas
      </div>
    );
  }

  return (
    <div className="statistics-page">

      <h1>
        Dashboard Estadísticas
      </h1>

      {/* ================================== */}
      {/* CARDS */}
      {/* ================================== */}

      <div className="stats-grid">

        <StatsCard
          title="Exámenes"
          value={stats.total_exams}
        />

        <StatsCard
          title="Promedio"
          value={`${stats.average_score}%`}
        />

        <StatsCard
          title="Aprobados"
          value={stats.passed_exams}
        />

        <StatsCard
          title="Pass Rate"
          value={`${stats.pass_rate}%`}
        />

      </div>

      {/* ================================== */}
      {/* CHART */}
      {/* ================================== */}

      <PerformanceChart
        history={
          stats.score_history
        }
      />

      {/* ================================== */}
      {/* INCORRECT QUESTIONS */}
      {/* ================================== */}

      <div className="incorrect-section">

        <h2>
          Preguntas más incorrectas
        </h2>

        {stats.incorrect_questions.map(
          (item) => (

            <div
              key={item.question_id}
              className="incorrect-item"
            >

              Pregunta ID:
              {" "}
              {item.question_id}

              {" "}→{" "}

              {item.incorrect_count}
              {" "}
              errores

            </div>
          )
        )}

      </div>

    </div>
  );
}

export default StatisticsPage;