// apiService.js

const API_BASE_URL =  //backendURL

export const fetchData = () => {
  const url = // Replace with endpoint

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
