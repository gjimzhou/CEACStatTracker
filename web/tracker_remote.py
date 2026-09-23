import os
import requests

URL = os.environ.get("CEAC_REMOTE_URL", "")


def _remote_url():
    if not URL:
        raise RuntimeError("CEAC_REMOTE_URL is not configured")
    return URL

def query_ceac_state_safe(loc, case_no, pp_no="", surname=""):
    req = requests.post(_remote_url(), json=[[loc, case_no, pp_no, surname]], timeout=100)
    ret = req.json()
    return ret[case_no]


def query_ceac_state_remote(req_data):
    req = requests.post(URL, json=req_data, timeout=180)
    ret = req.json()
    return ret


if __name__ == "__main__":
    print(query_ceac_state_safe("BEJ","AA00A38G49"))