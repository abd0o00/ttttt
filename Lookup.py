import requests
from TikSign import Argus, Ladon, Gorgon, Newparams, UserAgentTik
import time
from hashlib import md5
from urllib.parse import urlencode
import re
import random

user = input("Enter Username or Email: ")



if "@" in user:
    url = "https://api16-normal-c-alisg.tiktokv.com/passport/account_lookup/email/"
    
else:
    url = "https://" + random.choice(["api16-normal-c-alisg.tiktokv.com", "api16-normal-c-alisg.ttapis.com"]) + f"/passport/account_lookup/username/"
    
    
    
xor = lambda s: ''.join(f'{ord(c)^5:02x}' for c in s)


def sign(
    params: str,
    payload: str or None = None,
    sec_device_id: str = '',
    cookie: str or None = None,
    aid: int = 1233, 
    license_id: int = 1611921764,
    sdk_version_str: str = 'v05.00.06-ov-android',
    sdk_version: int = 167775296,
    platform: int = 0,
    unix: float = None
):
    aid = 1233 
    x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload is not None else None
    if not unix:
        unix = time.time()
    return Gorgon(aid).Encoder(
        params=params,
        data=payload,
        cookies=cookie,
        unix=unix
    ) | {
        'content-length': str(len(payload)),
        'x-ss-stub': x_ss_stub.upper(),
        'x-ladon': Ladon.encrypt(int(unix), license_id, aid),
        'x-argus': Argus.get_sign(
            params,
            x_ss_stub,
            int(unix),
            platform=platform,
            aid=aid,
            license_id=license_id,
            sec_device_id=sec_device_id,
            sdk_version=sdk_version_str,
            sdk_version_int=sdk_version
        )
    }
    
params = {
    "request_tag_from": "h5",
    "fixed_mix_mode": "1",
    "mix_mode": "1",
    "account_param": xor(user),
    "scene": "4",
    "device_platform": "android",
    "os": "android",
    "ssmix": "a",
    "_rticket": "1766574961823",
    "cdid": "48ac5e55-b982-451f-84c4-f4d751339523",
    "channel": "googleplay",
    "aid": "1233",
    "app_name": "musical_ly",
    "version_code": "370004",
    "version_name": "37.0.4",
    "manifest_version_code": "2023700040",
    "update_version_code": "2023700040",
    "ab_version": "37.0.4",
    "resolution": "1080*2220",
    "dpi": "440",
    "device_type": "Redmi Note 8 Pro",
    "device_brand": "Redmi",
    "language": "ar",
    "os_api": "30",
    "os_version": "11",
    "ac": "wifi",
    "is_pad": "0",
    "current_region": "YE",
    "app_type": "normal",
    "sys_region": "EG",
    "last_install_time": "1766569393",
    "mcc_mnc": "42103",
    "timezone_name": "Asia/Aden",
    "residence": "YE",
    "app_language": "ar",
    "carrier_region": "YE",
    "timezone_offset": "10800",
    "host_abi": "arm64-v8a",
    "locale": "ar",
    "ac2": "wifi",
    "uoo": "0",
    "op_region": "YE",
    "build_number": "37.0.4",
    "region": "EG",
    "ts": "1766574961",
    "iid": "7587357680122824469",
    "device_id": "7578156060823143937",
    "openudid": "2213c11ffdc5fded",
    "support_webview": "1",
    "cronet_version": "f6248591_2024-09-11",
    "ttnet_version": "4.2.195.9-tiktok",
    "use_store_region_cookie": "1"
}

params.update(Newparams())
ua = UserAgentTik(params)
params["device_type"] = ua["type"]
params["device_brand"] = ua["brand"]
signature = sign(params=urlencode(params), payload="")
headers = {
  "x-tt-referer": "https://inapp.tiktokv.com/ucenter_web/account_lookup_tool",
  "x-tt-pba-enable": "1",
  "accept": "application/json, text/plain, */*",
  "x-tt-dm-status": "login=0;ct=1;rt=6",
  "content-type": "application/x-www-form-urlencoded",
  "user-agent": ua["User-Agent"],

}
headers.update(signature)
res = requests.post(url, headers=headers, params=params)
if res.json()['message'] == 'success':
    if "username" in res.text:
        user2= (res.json()["data"]["accounts"][0]["username"])
    
    tok = res.json()["data"]["accounts"][0]["passport_ticket"]
    params.update({'passport_ticket': tok})
    signature2 = sign(params=urlencode(params), payload="")
    headers.update(signature2)
    req = requests.post("https://" +random.choice(["api16-normal-c-alisg.tiktokv.com", "api16-normal-c-alisg.ttapis.com"]) +"/passport/user/login_by_passport_ticket/", params=params, headers=headers)
        
    infos = re.search(r'"info":"(.*?)"', str(req.headers)).group(1)
    
    
     
    print("Username : ", user2)
    print("Email : ", infos)
else:
    print(res.text)
    print("Use VPN Or Username Is Not Available")
