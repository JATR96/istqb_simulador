import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import HomePage from "./pages/HomePage";

import ExamPage from "./pages/ExamPage";

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

      </Routes>

    </BrowserRouter>
  );
}

export default App;