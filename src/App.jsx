import { Route, Routes } from 'react-router-dom'
import './App.css'
import Navbar from './component/Navbar'
import ImageSlider from './component/ImageSlider'
import About from './pages/About.jsx'
import Contact from './pages/Contact.jsx'
import Services from './pages/Services.jsx'
import Practice from './pages/Practice.jsx'


function App() {
  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<ImageSlider />} />
        <Route path="/aboutus" element={<About />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/services" element={<Services />} />
        <Route path="/practice" element={<Practice />} />
        <Route path="*" element={<main className="container py-5"><h1>Page not found</h1></main>} />
      </Routes>
    </>
  )
}

export default App
