import { BrowserRouter, Routes, Route } from "react-router-dom";

import HomePage from "../pages/HomePage";
import ExamsPage from "../pages/ExamsPage";
import ResultPage from "../pages/ResultPage";
import NotFoundPage from "../pages/NotFoundPage";
import StatisticsPage from "../pages/StatisticsPage";
import ExamPage from "../pages/ExamPage";

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
          path="/exam"
          element={<ExamPage />}
        />

        <Route
          path="/results"
          element={<ResultPage />}
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