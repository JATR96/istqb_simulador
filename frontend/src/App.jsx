import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import HomePage from "./pages/HomePage";

import ExamPage from "./pages/ExamPage";

import ResultPage from "./pages/ResultPage";

import StatisticsPage from "./pages/StatisticsPage";

function App() {

  return (
    <BrowserRouter>

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

    </BrowserRouter>
  );
}

export default App;