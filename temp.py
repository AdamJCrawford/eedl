import requests
import os

latest = requests.get("https://pypi.org/pypi/eedl/json").json()["info"]["version"]
import eedl

version_number = eedl.__version__
setupcfg_version = os.environ.get("GREP_RESULT")
assert version_number == setupcfg_version and version_number > latest
