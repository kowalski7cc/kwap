#!/usr/bin/env python3

from dataclasses import dataclass
from urllib.parse import urljoin

import requests

@dataclass
class Kwap(object):

    base_url: str
    username: str
    password: str

    def fetch_bundle_list(self):
        return fetch_bundle_list(self.base_url, self.username, self.password)

    def upload_bundle(self, file_path):
        return upload_bundle(self.base_url, self.username, self.password, file_path)


def fetch_bundle_list(base_url, username, password, verify: bool = True):
    url = urljoin(base_url, "/system/console/bundles/.json")
    response = requests.get(url, auth=(username, password), verify=verify)
    if response.status_code != 200:
        print("Fetch failed: {} {}", response.status_code, response.text)
        raise IOError("Fetch failed: {response.status_code} {response.text}")
    return response.json()


def upload_bundle(
    base_url,
    username,
    password,
    file_path,
    verify: bool = True,
    start_level: int = 80,
    start: bool = False,
    refresh: bool = False,
):
    with open(file_path, "rb") as f:
        files = [("bundlefile", ("bundle.jar", f, "application/java-archive"))]
        url = urljoin(base_url, "/system/console/bundles")
        response = requests.post(
            url,
            auth=(username, password),
            files=files,
            data={
                "action": "install",
                "bundlestartlevel": "{start_level}",
                **({"refreshPackages": "refresh"} if refresh else {}),
                **({"bundlestart": "start"} if start else {}),
            },
            verify=verify,
        )
        if response.status_code != 200:
            raise IOError(
                f"Upload failed: {response.status_code} {response.text}")
