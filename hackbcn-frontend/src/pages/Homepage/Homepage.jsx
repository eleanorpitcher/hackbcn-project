import React from 'react'
import './Homepage.scss'
import SearchBar from '../../components/SearchBar'

function Homepage() {
  return (
    <div>
      <h1 className='homepage-header'>Accessibility in Barcelona</h1>
      <SearchBar></SearchBar>
    </div>
  )
}

export default Homepage