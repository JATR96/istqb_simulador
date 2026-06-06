import { BrowserRouter, Routes, Route } from "react-router-dom";

import HomePage from "../pages/HomePage";
import ExamsPage from "../pages/ExamsPage";
import ResultsPage from "../pages/ResultPage";
import NotFoundPage from "../pages/NotFoundPage";
import StatisticsPage from "../pages/StatisticsPage";

import ThemeToggle from "../components/ThemeToggle";
import Header from "../components/layout/Header";

function AppRouter() {
  return (
    <BrowserRouter>
      <Header />

      <Routes>
        <Route
          path="/"
          element={<HomePage />}
        />

        <Route
          path="/exams"
          element={<ExamsPage />}
        />

        <Route
          path="/results"
          element={<ResultsPage />}
        />

        <Route
          path="/statistics"
          element={<StatisticsPage />}
        />

        <Route
          path="/error"
          element={<NotFoundPage />}
        />
      </Routes>

      <ThemeToggle />

    </BrowserRouter>
  );
}

export default AppRouter;