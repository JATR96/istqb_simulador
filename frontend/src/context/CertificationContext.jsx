import {
  createContext,
  useContext,
  useState,
  useEffect
} from "react";

const CertificationContext =
  createContext();

export function CertificationProvider({
  children
}) {

  const [
    certification,
    setCertification
  ] = useState(
    localStorage.getItem(
      "selectedCertification"
    ) || null
  );

  useEffect(() => {

    if (certification) {

      localStorage.setItem(
        "selectedCertification",
        certification
      );

    }

  }, [certification]);

  return (

    <CertificationContext.Provider
      value={{
        certification,
        setCertification
      }}
    >

      {children}

    </CertificationContext.Provider>

  );
}

export function useCertification() {

  return useContext(
    CertificationContext
  );
}