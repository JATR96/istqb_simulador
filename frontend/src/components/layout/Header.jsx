import Navbar from "./Navbar";

function Header() {
  return (
    <header className="header">
      <div className="header-container">
        <h1 className="logo">
          ISTQB Simulator
        </h1>

        <Navbar />
      </div>
    </header>
  );
}

export default Header;