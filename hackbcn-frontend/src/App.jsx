import {  } from 'react'
import './App.css'
import Homepage from './pages/Homepage/Homepage'
import { Route, Routes } from 'react-router-dom'

function App() {

  return (
    <>
      <Routes>
        <Route element={<Homepage/>} path="/"></Route>
      </Routes>
    </>
  )
}

export default App
