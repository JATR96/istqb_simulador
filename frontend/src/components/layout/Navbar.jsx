import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav className="navbar">
      <Link to="/">Inicio</Link>

      <Link to="/exams">
        Exámenes
      </Link>

      <Link to="/results">
        Resultados
      </Link>
    </nav>
  );
}

export default Navbar;