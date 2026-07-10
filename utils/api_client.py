"""import requests
class APIS:

    def __init__(self):
        self.base_url = "https://fakerestapi.azurewebsites.net/api/v1"
        self.headers = {
            "Accept": "text/plain; v=1.0",
            "Content-Type": "application/json; v=1.0"
        }

    def get(self, endpoint):
        url = self.base_url + endpoint
        return requests.get(url, headers=self.headers)

    def post(self, endpoint, payload):
        url = self.base_url + endpoint
        return requests.post(url, headers=self.headers, json=payload)

    def put(self, endpoint, payload):
        url = self.base_url + endpoint
        return requests.put(url, headers=self.headers, json=payload)

    def delete(self, endpoint):
        url = self.base_url + endpoint
        return requests.delete(url, headers=self.headers)
"""
import requests
import time

from utils.logger import logger


class APIS:

    def __init__(self):
        self.base_url = "https://fakerestapi.azurewebsites.net/api/v1"

        self.headers = {
            "Accept": "text/plain; v=1.0",
            "Content-Type": "application/json; v=1.0"
        }


    def get(self, endpoint):

        url = self.base_url + endpoint

        logger.info("========== GET REQUEST ==========")
        logger.info(f"URL : {url}")
        logger.info(f"Headers : {self.headers}")

        start_time = time.time()

        response = requests.get(
            url,
            headers=self.headers
        )

        end_time = time.time()

        logger.info(f"Status Code : {response.status_code}")
        logger.info(f"Response Time : {end_time-start_time:.2f} seconds")
        logger.info(f"Response Body : {response.text}")

        return response



    def post(self, endpoint, payload):

        url = self.base_url + endpoint

        logger.info("========== POST REQUEST ==========")
        logger.info(f"URL : {url}")
        logger.info(f"Headers : {self.headers}")
        logger.info(f"Request Body : {payload}")

        start_time = time.time()

        response = requests.post(
            url,
            headers=self.headers,
            json=payload
        )

        end_time = time.time()

        logger.info(f"Status Code : {response.status_code}")
        logger.info(f"Response Time : {end_time-start_time:.2f} seconds")
        logger.info(f"Response Body : {response.text}")

        return response



    def put(self, endpoint, payload):

        url = self.base_url + endpoint

        logger.info("========== PUT REQUEST ==========")
        logger.info(f"URL : {url}")
        logger.info(f"Headers : {self.headers}")
        logger.info(f"Request Body : {payload}")

        start_time = time.time()

        response = requests.put(
            url,
            headers=self.headers,
            json=payload
        )

        end_time = time.time()

        logger.info(f"Status Code : {response.status_code}")
        logger.info(f"Response Time : {end_time-start_time:.2f} seconds")
        logger.info(f"Response Body : {response.text}")

        return response



    def delete(self, endpoint):

        url = self.base_url + endpoint

        logger.info("========== DELETE REQUEST ==========")
        logger.info(f"URL : {url}")
        logger.info(f"Headers : {self.headers}")

        start_time = time.time()

        response = requests.delete(
            url,
            headers=self.headers
        )

        end_time = time.time()

        logger.info(f"Status Code : {response.status_code}")
        logger.info(f"Response Time : {end_time-start_time:.2f} seconds")

        return response