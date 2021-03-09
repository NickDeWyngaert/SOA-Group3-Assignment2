defmodule Watched.MoviesTest do
  use Watched.DataCase

  alias Watched.Movies

  describe "movies" do
    alias Watched.Movies.Movie

    @valid_attrs %{about: "some about", director: "some director", duration: 42, genre: "some genre", release: ~D[2010-04-17], title: "some title"}
    @update_attrs %{about: "some updated about", director: "some updated director", duration: 43, genre: "some updated genre", release: ~D[2011-05-18], title: "some updated title"}
    @invalid_attrs %{about: nil, director: nil, duration: nil, genre: nil, release: nil, title: nil}

    def movie_fixture(attrs \\ %{}) do
      {:ok, movie} =
        attrs
        |> Enum.into(@valid_attrs)
        |> Movies.create_movie()

      movie
    end

    test "list_movies/0 returns all movies" do
      movie = movie_fixture()
      assert Movies.list_movies() == [movie]
    end

    test "get_movie!/1 returns the movie with given id" do
      movie = movie_fixture()
      assert Movies.get_movie!(movie.id) == movie
    end

    test "create_movie/1 with valid data creates a movie" do
      assert {:ok, %Movie{} = movie} = Movies.create_movie(@valid_attrs)
      assert movie.about == "some about"
      assert movie.director == "some director"
      assert movie.duration == 42
      assert movie.genre == "some genre"
      assert movie.release == ~D[2010-04-17]
      assert movie.title == "some title"
    end

    test "create_movie/1 with invalid data returns error changeset" do
      assert {:error, %Ecto.Changeset{}} = Movies.create_movie(@invalid_attrs)
    end

    test "update_movie/2 with valid data updates the movie" do
      movie = movie_fixture()
      assert {:ok, %Movie{} = movie} = Movies.update_movie(movie, @update_attrs)
      assert movie.about == "some updated about"
      assert movie.director == "some updated director"
      assert movie.duration == 43
      assert movie.genre == "some updated genre"
      assert movie.release == ~D[2011-05-18]
      assert movie.title == "some updated title"
    end

    test "update_movie/2 with invalid data returns error changeset" do
      movie = movie_fixture()
      assert {:error, %Ecto.Changeset{}} = Movies.update_movie(movie, @invalid_attrs)
      assert movie == Movies.get_movie!(movie.id)
    end

    test "delete_movie/1 deletes the movie" do
      movie = movie_fixture()
      assert {:ok, %Movie{}} = Movies.delete_movie(movie)
      assert_raise Ecto.NoResultsError, fn -> Movies.get_movie!(movie.id) end
    end

    test "change_movie/1 returns a movie changeset" do
      movie = movie_fixture()
      assert %Ecto.Changeset{} = Movies.change_movie(movie)
    end
  end
end
