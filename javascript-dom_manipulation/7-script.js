fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    const movieList = document.getElementById('list_movies');

    data.results.forEach(movie => {
      const listItem = document.createElement('li');
      listItem.textContent = movie.title;
      movieList.appendChild(listItem);
    });
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });