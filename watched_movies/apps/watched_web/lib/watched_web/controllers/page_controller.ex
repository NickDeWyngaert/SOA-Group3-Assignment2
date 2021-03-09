defmodule WatchedWeb.PageController do
  use WatchedWeb, :controller

  alias Watched.Movies

  def index(conn, _params) do
    movies = Movies.list_movies()
    render(conn, "index.html", movies: movies)
  end
end
