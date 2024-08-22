import os
import time
from urllib.request import Request, urlopen

from utils import generate_signature


# This script demonstrates sending a GET request to an API using a signature for
# authentication and retrieving the response.

def send_get_request(partner_id, unix_epoch, signature, api_url):
    """
    Sends a GET request to the specified API URL with custom authentication
    headers.

    :param partner_id: Partner ID used in the request header.
    :param unix_epoch: Current UNIX timestamp.
    :param signature: Signature for authentication.
    :param api_url: URL of the API endpoint.
    :return: JSON response from the API.
    """
    headers = {'X-Fivaldi-Partner': partner_id,
               'X-Fivaldi-Timestamp': unix_epoch,
               'Authorization': f"Fivaldi {signature}"}

    req = Request(api_url, headers=headers, method='GET')
    with urlopen(req) as response:
        print(f"HTTP Status code: {response.status}")
        print(f"HTTP Response body: {response.read().decode()}")


def main():
    """
    Main execution function: retrieves environment variables, generates
    a signature, and sends a GET request to an API endpoint.
    """
    partner_id = os.getenv('PARTNER_ID')
    partner_secret = os.getenv('PARTNER_SECRET')
    unix_epoch = str(int(time.time()))
    api_endpoint = '/customer/api/ping'
    api_url = f"https://api.fivaldi.net{api_endpoint}"

    # Generating signature for the API request
    signature = generate_signature(partner_id, partner_secret, 'GET',
                                   unix_epoch, api_endpoint)
    print(f'Signature: {signature}')

    # Sending GET request and printing the response
    send_get_request(partner_id, unix_epoch, signature, api_url)


if __name__ == '__main__':
    main()
