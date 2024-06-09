import os

import requests
from langchain_core.tools import tool


@tool
def get_movie_info(movie_title: str) -> dict:
    """
    Retrieves movie information from the TMDB API based on the provided movie title.

    Args:
        movie_title (str): The title of the movie to search for.

    Returns:
        dict: The movie information returned from the TMDB API, or None if an error occurs.
    """
    api = os.getenv("TMDB_API_KEY")
    url = f"https://api.themoviedb.org/3/search/movie?query={movie_title}&include_adult=false&language=en-US&page=1"
    headers = {"accept": "application/json", "Authorization": f"Bearer {api}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        movie_info = response.json()

        return movie_info
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
