import api from "./api";

/*
|--------------------------------------------------------------------------
| OBTENER CERTIFICACIONES
|--------------------------------------------------------------------------
*/

export const getCertifications = async (
  payload
) => {

  const response = await api.get(
    "/certifications",
    payload
  );

  return response.data;
};