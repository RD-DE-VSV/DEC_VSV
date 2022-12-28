import requests
import json

from typing import List, Dict, Any

API_URL = 'https://fake-api-vycpfa6oca-uc.a.run.app/'
ENDPOINT = 'sales'


def get_sales(date: str, auth_token: str) -> List[Dict[str, Any]]:
    """
    Get data from sales API for specified date.

    :param date: data retrieve the data from
    :param auth_token: authorisation token
    :return: list of records
    """

    result = []
    should_fetch_next_page = True
    page = 1

    while should_fetch_next_page:
        response = requests.get(
            url=API_URL+ENDPOINT,
            params={'date': date, 'page': page},
            headers={'Authorization': auth_token},
        )

        if response.status_code == 200:
            result.append(response.json())
            page += 1
        else:
            should_fetch_next_page = False

    return result
