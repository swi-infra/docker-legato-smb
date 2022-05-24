import os
import logging
import requests


logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


def main():
    """Updates host data on farm api."""
    hostname = os.environ.get("HOSTNAME", None)
    username = os.environ.get("USERNAME", None)
    ip = os.environ.get("IP_ADDR", None)
    farm_api_url = os.environ.get("FARM_API_URL", None)
    if not (hostname and username and ip and farm_api_url):
        logging.error("Missing input:")
        logging.error(f"HOSTNAME: {hostname}")
        logging.error(f"USERNAME: {username}")
        logging.error(f"IP_ADDR: {ip}")
        logging.error(f"FARM_API_URL: {farm_api_url}")
        return False

    headers = {"Content-Type": "application/json; charset=utf-8"}
    host_params = {
        "ip": ip,
        "description": f"Host Owner: {username}",
    }

    url = f"{farm_api_url}/hosts/{hostname}/update"
    logging.info(f"Updating host at: {url}")
    try:
        resp = requests.get(url, headers=headers, params=host_params)
    except requests.exceptions.RequestException as e:
        logging.error(e)
        return False
    if "error" in resp.text:
        logging.error(resp.text)
        return False
    logging.info("Host updated")
    logging.debug(resp.text)
    return True


if __name__ == '__main__':
    exit(0 if main() else 1)
