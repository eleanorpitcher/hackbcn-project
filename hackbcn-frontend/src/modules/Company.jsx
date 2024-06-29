import React from 'react'
import './Company.scss'
import GoogleDummyImage from '../assets/dummy-google-image.png'

function Company() {
  return (
    <div className='container'>
        <div className='left_container'>
            <h1>Dummy Company Name</h1>
            <h2>Address Field</h2>
            <h2>Accessibility probability score</h2>
        </div>
        <div className='right_container'>
            <div className='image_container'>
                <img className='image' src={GoogleDummyImage} alt="" />
            </div>
        </div>
    </div>

  )
}

export default Company