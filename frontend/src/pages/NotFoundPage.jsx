import {
  Link
} from "react-router-dom";

function NotFoundPage() {

  return (
    <div
      style={{
        padding: "60px",
        textAlign: "center"
      }}
    >

      <h1>
        404
      </h1>

      <h2>
        Página no encontrada
      </h2>

      <Link to="/">
        Volver al inicio
      </Link>

    </div>
  );
}

export default NotFoundPage;