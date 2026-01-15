import requests
from TikSign import Newparams, UserAgentTik, sign
import uuid
import time
from urllib.parse import urlencode
import threading

user = input("[ # ] - Enter Any Username : ")
seen_users = set()
lock = threading.Lock()

def Search(user, cursor="0", search_id=""):
    params = {
        "cursor": cursor,
        "enter_from": "homepage_hot",
        "count": "20",
        "keyword": user,
        "type": "1",
        "query_correct_type": "0",
        "search_source": "switch_tab",
        "search_id": search_id,
        "request_tag_from": "h5",
        "manifest_version_code": "410803",
        "_rticket": str(int(time.time() * 1000)),
        "app_language": "ar",
        "app_type": "normal",
        "iid": None,
        "app_package": "com.zhiliaoapp.musically.go",
        "channel": "googleplay",
        "device_type": "Redmi Note 8 Pro",
        "language": "ar",
        "host_abi": "arm64-v8a",
        "locale": "ar",
        "resolution": "1080*2220",
        "openudid": uuid.uuid4().hex[:16],
        "update_version_code": "410803",
        "ac2": "0",
        "cdid": str(uuid.uuid4()),
        "sys_region": "EG",
        "os_api": "30",
        "timezone_name": "Asia/Aden",
        "dpi": "440",
        "carrier_region": "YE",
        "ac": "mobile",
        "device_id": None,
        "os": "android",
        "os_version": "11",
        "timezone_offset": "10800",
        "version_code": "410803",
        "app_name": "musically_go",
        "ab_version": "41.8.3",
        "version_name": "41.8.3",
        "device_brand": "Redmi",
        "op_region": "YE",
        "ssmix": "a",
        "device_platform": "android",
        "build_number": "41.8.3",
        "region": "EG",
        "aid": "1340",
        "ts": str(int(time.time()))
    }
    params.update(Newparams())

    ua = UserAgentTik(params)
    params["device_type"] = ua["type"]
    params["device_brand"] = ua["brand"]

    signature = sign(params=urlencode(params))

    headers = {
        "User-Agent": ua["User-Agent"],
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "rpc-persist-pyxis-policy-v-tnc": "1",
        "x-ss-dp": "1340",
        "sdk-version": "2",
        "passport-sdk-version": "5050090",
        "x-tt-ultra-lite": "1",
        "x-vc-bdturing-sdk-version": "2.3.15.i18n",
        "x-tt-store-region": "ye",
        "x-tt-store-region-src": "uid",
        "ttzip-tlb": "1",
    }

    response = requests.get(
        "https://search19-normal-alisg.tiktokv.com/aweme/v1/discover/search/",
        headers=headers,
        params=urlencode(params)
    )

    return response.json()

def Ahmed():    
    cursor = "0"
    search_id = ""

    while True:
        try:
            res = Search(user, cursor, search_id)

            rid = res.get("rid", "")
            search_id = rid

            user_list = res.get("user_list", [])
            for user_info in user_list:
                uid = user_info.get("user_info", {}).get("unique_id")
                if uid:
                    with lock:
                        if uid not in seen_users:
                            seen_users.add(uid)
                            print(uid)  
            cursor = str(res.get("cursor", 0))  

        except Exception as e:
            pass


for _ in range(15):
    threading.Thread(target=Ahmed).start()
