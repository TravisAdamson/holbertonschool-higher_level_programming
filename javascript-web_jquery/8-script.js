$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (dataRes) {
  $('UL#list_movies').append(dataRes.results.map(movie => `<li>${movie.title}</li>`));
});
