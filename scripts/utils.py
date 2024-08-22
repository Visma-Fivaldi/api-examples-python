import base64
import hashlib
import hmac

# Unix line feed character used for constructing the signing string.
LF = '\n'


def generate_signature(partner_id, partner_secret, http_method, unix_epoch,
                       api_endpoint, content_type=None, body=None):
    """
    Generates an HMAC-SHA256 signature for API request authorization.

    :param partner_id: Partner ID used in the request header.
    :param partner_secret: Secret key for HMAC generation.
    :param http_method: HTTP method ("GET", "POST", etc.).
    :param unix_epoch: Current UNIX epoch time as a string.
    :param api_endpoint: API endpoint URL path.
    :param body: (Optional) Request body for POST requests.
    :param content_type: (Optional) Content-Type of the request body.
    :return: Base64 encoded HMAC-SHA256 signature.
    """
    # MD5 hash the body if present and not a GET request, ensuring body is
    # hashed correctly for signature consistency.
    if body is not None and http_method != "GET":
        body_hash = hashlib.md5(body.encode('utf-8')).hexdigest()
    else:
        body_hash = ''

    # Construct the string to be signed according to the expected format.
    string_to_sign = (f'{http_method}{LF}'
                      f'{body_hash}{LF}'
                      f'{content_type or ""}{LF}'
                      f'x-fivaldi-partner:{partner_id}{LF}'
                      f'x-fivaldi-timestamp:{unix_epoch}{LF}'
                      f'{api_endpoint}')

    # Generate the HMAC-SHA256 signature from the 'string_to_sign'.
    signature = hmac.new(partner_secret.encode('utf-8'),
                         string_to_sign.encode('utf-8'),
                         hashlib.sha256).digest()

    # Return the signature in Base64 encoding.
    return base64.b64encode(signature).decode()
