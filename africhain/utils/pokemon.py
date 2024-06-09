import requests
from langchain_core.tools import tool


@tool
def get_pokemon_info(specie: str) -> dict:
    """
    Retrieves information about a Pokemon species from the PokeAPI.

    Args:
        specie (str): The name or ID of the Pokemon species to retrieve information for.

    Returns:
        dict: A dictionary containing the JSON response from the PokeAPI, or None if an error occurs.
    """
    url = f"https://pokeapi.co/api/v2/pokemon-species/{specie}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
