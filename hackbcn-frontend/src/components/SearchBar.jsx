import React, { useState } from 'react'

function SearchBar() {
    const [query, setQuery] = useState('')

    return (
        <div>
            <form action="">
            <input
            type="text"
            value={query}
            // onChange={handleInputChange}
            placeholder="Search..."
            />
            <button type='submit'>Search</button>
            </form>
        </div>
    )
}

export default SearchBar