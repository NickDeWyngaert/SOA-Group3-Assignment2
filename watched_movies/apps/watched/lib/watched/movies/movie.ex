defmodule Watched.Movies.Movie do
  use Ecto.Schema
  import Ecto.Changeset

  schema "movies" do
    field :about, :string
    field :director, :string
    field :duration, :integer
    field :genre, :string
    field :release, :date
    field :title, :string
  end

  @doc false
  def changeset(movie, attrs) do
    movie
    |> cast(attrs, [:title, :genre, :director, :duration, :release, :about])
    |> validate_required([:title, :genre, :director, :duration, :release, :about])
  end
end
