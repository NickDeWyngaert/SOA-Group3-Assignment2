defmodule WatchedWeb.MovieView do
  use WatchedWeb, :view
  alias WatchedWeb.MovieView

  def render("all_movies.json", %{movies: movies}) do
    %{data: render_many(movies, MovieView, "plain_movie.json")}
  end

  def render("show.json", %{movie: movie}) do
    %{data: render_one(movie, MovieView, "extended_movie.json")}
  end

  def render("plain_movie.json", %{movie: movie}) do
    %{id: movie.id,
      title: movie.title}
  end

  def render("extended_movie.json", %{movie: movie}) do
    %{title: movie.title,
      genre: movie.genre,
      director: movie.director,
      duration: movie.duration,
      release: movie.release,
      about: movie.about}
  end
end
