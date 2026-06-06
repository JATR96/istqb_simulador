import {
  useEffect,
  useState
} from "react";

import {
  getCertifications
} from "../services/certificationService";

import {
  useCertification
} from "../context/CertificationContext";

function CertificationSelector() {

  const [
    certifications,
    setCertifications
  ] = useState([]);

  const {
    certification,
    setCertification
  } = useCertification();

  useEffect(() => {

    loadCertifications();

  }, []);

  async function loadCertifications() {

    try {

      const data =
        await getCertifications();

      setCertifications(data);

      if (
        data.length > 0 &&
        !certification
      ) {

        setCertification(
          data[0].certification
        );
      }

    } catch (error) {

      console.error(
        "Error loading certifications",
        error
      );
    }
  }

  return (

    <div className="certification-selector">

      <label>
        Certificación {""}
      </label>

      <select

        value={
          certification || ""
        }

        onChange={(event) =>
          setCertification(
            event.target.value
          )
        }
      >

        {certifications.map(
          (item) => (

            <option
              key={
                item.certification
              }

              value={
                item.certification
              }
            >

              {
                item.certification
              }

            </option>
          )
        )}

      </select>

    </div>
  );
}

export default CertificationSelector;