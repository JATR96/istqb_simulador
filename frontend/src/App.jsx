import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import HomePage from "./pages/HomePage";

import ExamPage from "./pages/ExamPage";

import ResultPage from "./pages/ResultPage";

import StatisticsPage from "./pages/StatisticsPage";

import ThemeToggle from "./components/ThemeToggle";

import Header from "./components/layout/Header";

function App() {

  return (
    <BrowserRouter>

      <Header />

      <Routes>

        <Route
          path="/"
          element={<HomePage />}
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

      </Routes>

      <ThemeToggle />

    </BrowserRouter>
  );
}

export default App;