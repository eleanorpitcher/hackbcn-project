import {  } from 'react'
import './App.css'
import Homepage from './modules/Homepage'
import Company from './modules/Company'
import Navbar from './components/Navbar'
import { Route, Routes } from 'react-router-dom'

function App() {

  return (
    <>
    <Navbar></Navbar>
      <Routes>
        <Route element={<Homepage/>} path="/"></Route>
        <Route element={<Company/>} path="/dummy-company"></Route>
      </Routes>
    </>
  )
}

export default App
