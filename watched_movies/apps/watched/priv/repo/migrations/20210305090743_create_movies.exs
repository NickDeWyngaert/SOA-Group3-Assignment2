defmodule Watched.Repo.Migrations.CreateMovies do
  use Ecto.Migration

  def change do
    create table(:movies) do
      add :title, :string, null: false
      add :genre, :string, null: false
      add :director, :string, null: false
      add :duration, :integer, null: false
      add :release, :date, null: false
      add :about, :text, null: false
    end

  end
end
