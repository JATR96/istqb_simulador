import api from "./api";

/*
|--------------------------------------------------------------------------
| OBTENER CERTIFICACIONES
|--------------------------------------------------------------------------
*/

export const getCertifications = async () => {

  const response = await api.get(
    "/certifications"
  );

  return response.data;
};