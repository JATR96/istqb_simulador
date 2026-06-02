import api from "./api";

/*
|--------------------------------------------------------------------------
| GENERAR EXAMEN
|--------------------------------------------------------------------------
*/

export const generateExam = async (
  payload
) => {

  const response = await api.post(
    "/exams/generate",
    payload
  );

  return response.data;
};

/*
|--------------------------------------------------------------------------
| ENVIAR RESULTADOS
|--------------------------------------------------------------------------
*/

export const submitExam = async (
  payload
) => {

  const response = await api.post(
    "/results/submit",
    payload
  );

  return response.data;
};