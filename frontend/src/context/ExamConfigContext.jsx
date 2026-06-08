import {
  createContext,
  useContext,
  useState
} from "react";

const ExamConfigContext =
  createContext();

export function ExamConfigProvider({
  children
}) {

  const [
    examConfig,
    setExamConfig
  ] = useState({

    language: "es",

    exam_mode: "quick",

    question_count: 10,

    duration_seconds: 3600
  });

  return (

    <ExamConfigContext.Provider
      value={{
        examConfig,
        setExamConfig
      }}
    >

      {children}

    </ExamConfigContext.Provider>

  );
}

export function useExamConfig() {

  return useContext(
    ExamConfigContext
  );
}