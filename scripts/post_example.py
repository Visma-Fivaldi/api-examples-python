import json
import os
import time
from urllib.request import Request, urlopen

from utils import generate_signature


# This script demonstrates sending a POST request to an API with a JSON body
# and a signature for authentication.

def send_post_request(partner_id, unix_epoch, signature, api_url, content_type,
                      body):
    """
    Sends a POST request to the specified API URL with custom authentication
    headers and a JSON body.

    :param partner_id: Partner ID used in the request header.
    :param unix_epoch: Current UNIX timestamp.
    :param signature: Signature for authentication.
    :param api_url: URL of the API endpoint.
    :param content_type: MIME type of the request body.
    :param body: JSON string to be sent as the request body.
    :return: JSON response from the API.
    """
    headers = {'Content-Type': content_type, 'X-Fivaldi-Partner': partner_id,
               'X-Fivaldi-Timestamp': unix_epoch,
               'Authorization': f"Fivaldi {signature}"}

    req = Request(api_url, data=body.encode(), headers=headers, method='POST')
    with urlopen(req) as response:
        print(f"HTTP Status code: {response.status}")
        print(f"HTTP Response body: {response.read().decode()}")


def main():
    """
    Main execution function: reads environment variables, reads and prepares
    the request body, generates a signature, and sends a POST request to an
    API endpoint.
    """
    partner_id = os.getenv('PARTNER_ID')
    partner_secret = os.getenv('PARTNER_SECRET')
    unix_epoch = str(int(time.time()))
    cuid = "1234"  # Provide a cuid which the partner id has permissions for
    api_endpoint = f"/customer/api/companies/{cuid}/customers/createCustomer"
    api_url = f"https://api.fivaldi.net{api_endpoint}"
    content_type = 'application/json'

    # Reading and preparing JSON body from a file
    with open('body.json', 'r', encoding='utf8') as file:
        body = json.dumps(json.load(file))

    # Generating the signature for the POST request
    signature = generate_signature(partner_id, partner_secret, 'POST',
                                   unix_epoch, api_endpoint, content_type,
                                   body)
    print(f'Signature: {signature}')

    # Sending the POST request and printing the API response
    send_post_request(partner_id, unix_epoch, signature, api_url, content_type,
                      body)


if __name__ == '__main__':
    main()
