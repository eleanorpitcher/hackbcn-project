
const API_BASE_URL = "http://127.0.0.1:5000" //backendURL

export const fetchPlace = (placeId) => {
    const url = `https://example.com/api/places/${placeId}`; 

    return fetch(url)
        .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
        })
        .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        throw error;
        });
};