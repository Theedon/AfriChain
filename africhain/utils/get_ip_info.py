import os
from datetime import datetime

import requests
from langchain_core.tools import tool


@tool
def get_ip_info(ip_address: str) -> dict:
    """
    Retrieves IP address information from the ipapi.co service.

    Args:
        ip_address (str): The IP address to look up.

    Returns:
        dict: A dictionary containing the IP address information, or None if an error occurred.
    """
    url = f"https://ipapi.co/{ip_address}/json/"
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        return data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
