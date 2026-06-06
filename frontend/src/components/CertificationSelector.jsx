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

import "../styles/certificationSelector.css";

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

      <h3>
        Seleccione una certificación
      </h3>

      <div className="certification-grid">

        {certifications.map(
          (item) => (

            <div

              key={
                item.certification
              }

              className={`certification-card ${
                certification ===
                item.certification
                  ? "selected"
                  : ""
              }`}

              onClick={() =>
                setCertification(
                  item.certification
                )
              }
            >

              <h4>
                {
                  item.certification
                }
              </h4>

              {
                item.version && (
                  <p>
                    {item.version}
                  </p>
                )
              }

              {
                item.total_questions && (
                  <p>
                    {
                      item.total_questions
                    } preguntas
                  </p>
                )
              }

            </div>
          )
        )}

      </div>

    </div>
  );
}

export default CertificationSelector;