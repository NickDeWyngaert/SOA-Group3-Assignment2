defmodule Watched.Repo do
  use Ecto.Repo,
    otp_app: :watched,
    adapter: Ecto.Adapters.Postgres
end
