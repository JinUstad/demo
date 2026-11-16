import { NavLink } from 'react-router-dom'

function Navbar() {
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <div className="container">
                <NavLink className="navbar-brand" to="/">Demo Practice </NavLink>
                <button
                    className="navbar-toggler"
                    type="button"
                    data-bs-toggle="collapse"
                    data-bs-target="#mainNavbar"
                    aria-controls="mainNavbar"
                    aria-expanded="false"
                    aria-label="Toggle navigation"
                >
                    <span className="navbar-toggler-icon" />
                </button>
                <div className="collapse navbar-collapse" id="mainNavbar">
                    <ul className="navbar-nav ms-auto">
                        <li className="nav-item">
                            <NavLink className={({ isActive }) => `nav-link${isActive ? ' active' : ''}`} to="/" end>
                                Home
                            </NavLink>
                        </li>
                        <li className="nav-item">
                            <NavLink className={({ isActive }) => `nav-link${isActive ? ' active' : ''}`} to="/aboutus">
                                About
                            </NavLink>
                        </li>
                        <li className="nav-item">
                            <NavLink className={({ isActive }) => `nav-link${isActive ? ' active' : ''}`} to="/services">
                                Services
                            </NavLink>
                        </li>
                        <li className="nav-item">
                            <NavLink className={({ isActive }) => `nav-link${isActive ? ' active' : ''}`} to="/contact">
                                Contact Us
                            </NavLink>
                        </li>
                        <li className="nav-item">
                            <NavLink className={({ isActive }) => `nav-link${isActive ? ' active' : ''}`} to="/practice">
                                Practice
                            </NavLink>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    )
}
export default Navbar
