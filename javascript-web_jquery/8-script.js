$('document').ready(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    $.each(data.results, function (i, movie) {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
