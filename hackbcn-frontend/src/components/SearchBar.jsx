import { useState } from 'react'

function SearchBar() {
    const [query] = useState('')

    return (
        <div style={{display:'flex', flexDirection:'row', width:'70%'}}>
            <form action="">
            <input
            type="text"
            value={query}
            // onChange={handleInputChange}
            placeholder="Search..."
            style={{borderRadius: '10px', height: '40px'}}
            />
            <button type='submit' style={{borderRadius:'30px', height: '30px', justifyContent:'center', alignItems:'center'}}>Search</button>
            </form>
        </div>
    )
}

export default SearchBar