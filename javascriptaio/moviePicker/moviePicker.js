const chooseMovie = (choices) => {
  return choices[Math.floor(Math.random() * choices.length)];
};

const displayMovieChoice = () => {
  const movieChoice = chooseMovie(movies);
  document.getElementById("movie-choice").innerHTML = movieChoice.title;
};
