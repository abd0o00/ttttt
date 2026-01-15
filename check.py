from TikSign import Argus, Gorgon, Ladon, Newparams, UserAgentTik
from hashlib import md5
import requests, os, time
from urllib.parse import urlencode
from solver import send
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxy = None

if os.path.exists("proxt.txt"):
    p = open("proxt.txt").read().strip()
    if p:
        if not p.startswith("http"):
            p = "https://" + p
        proxy = {
            "http": p,
            "https": p
        }
    else:
        proxy = None
else:
    proxy = None
class TikTok:
    def __init__(self, email):
        self.email = email
        self.session = requests.Session()
        if proxy:
            self.session.proxies = {"http": proxy, "https": proxy}

    def xor_email(self):
        return ''.join(f'{ord(c)^5:02x}' for c in self.email)

    def sign(self, params: str, payload: str = None, sec_device_id: str = '',
             cookie: str = None, aid: int = 1233, license_id: int = 1611921764,
             sdk_version_str: str = 'v05.00.06-ov-android', sdk_version: int = 167775296,
             platform: int = 0, unix: float = None):

        if payload:
            x_ss_stub = md5(payload.encode('utf-8')).hexdigest()
        else:
            x_ss_stub = None

        if not unix:
            unix = time.time()

        return Gorgon(aid).Encoder(
            params=params,
            data=payload if payload else "",
            cookies=cookie,
            unix=unix
        ) | {
            'content-length': str(len(payload)) if payload else '0',
            'x-ss-stub': x_ss_stub.upper() if x_ss_stub else None,
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

    def check_email(self):
        p = Newparams()
        ua = UserAgentTik()

        device = [
            p.get("iid", ""),
            p.get("device_id", ""),
            ua.get("type", ""),
            ua.get("brand", ""),
        ]

        try:
            cc = send(device, proxy)
        except:
            cc = ""
        if not cc or "Verification complete" not in cc:
            return "Captcha failed"

        
        params = {
            "passport-sdk-version": "6031490",
            "device_platform": "android",
            "os": "android",
            "ssmix": "a",
            "_rticket": "1766760856464",
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
            "ac": "mobile",
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
            "ac2": "lte",
            "uoo": "0",
            "op_region": "YE",
            "build_number": "37.0.4",
            "region": "EG",
            "ts": "1766760857",
            "iid": "7587357680122824469",
            "device_id": "7578156060823143937",
            "openudid": "2213c11ffdc5fded",
            "support_webview": "1",
            "reg_store_region": "ye",
            "user_selected_region": "0",
            "cronet_version": "f6248591_2024-09-11",
            "ttnet_version": "4.2.195.9-tiktok",
            "use_store_region_cookie": "1"
        }
        params.update(p)

        data = f"account_sdk_source=app&multi_login=1&email={self.xor_email()}&mix_mode=1"
        signature = self.sign(params=urlencode(params), payload=data)
        

        headers = {
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": ua["User-Agent"],
        }
        headers.update(signature)
        
        try:
            res = self.session.post(
            "https://api16-normal-c-alisg.tiktokv.com/passport/user/check_email_registered",
            headers=headers,
            params=params,
            data=data,
            timeout=15,
            verify=False
        )
            if res.json()["data"]["is_registered"] == 1:
                return {"available": True}
            elif res.json()["data"]["is_registered"] == 0:
                return {"available": False}
            else:
                return None
        except Exception as e:
            return e



