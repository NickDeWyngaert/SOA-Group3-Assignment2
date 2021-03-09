defmodule WatchedWeb.Router do
  use WatchedWeb, :router

  pipeline :browser do
    plug :accepts, ["html"]
    plug :fetch_session
    plug :fetch_flash
    plug :protect_from_forgery
    plug :put_secure_browser_headers
  end

  pipeline :api do
    plug :accepts, ["json"]
  end

  # Normal HTML
  scope "/", WatchedWeb do
    pipe_through :browser
    get "/", PageController, :index
  end

  # API
  scope "/api", WatchedWeb do
    pipe_through :api
    resources "/movies", MovieController
  end
  
end
