import {  } from 'react'
import './App.css'
import Homepage from './modules/Homepage'
import Company from './modules/Company'
import Navbar from './components/Navbar'
import Place from './modules/Place'
import { Route, Routes} from 'react-router-dom'

function App() {

  return (
    <>
    <Navbar></Navbar>
      <Routes>
        <Route element={<Homepage/>} path="/"></Route>
        <Route element={<Company/>} path="/dummy-company"></Route>
        <Route element={<Place/>} path="/places/:id"></Route>

      </Routes>
    </>
  )
}

export default App
