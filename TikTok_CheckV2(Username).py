from TikSign import sign, Newparams,UserAgentTik, host
import secrets
import requests
import random

proxy = None #Add Your Custom Proxy

user = input("[ # ] - Enter Any TikTok Username : ")

secret = secrets.token_hex(16)

cookies ={
  "passport_csrf_token": secret,
  "passport_csrf_token_default": secret
}
params = {
  'request_tag_from': "h5",
  'iid': "7372616297484125984",
  'device_id': "7372613015445308933",
  'ac': "MOBILE_4G",
  'channel': "googleplay",
  'aid': "1233",
  'app_name': "musical_ly",
  'version_code': "310503",
  'version_name': "31.5.3",
  'device_platform': "android",
  'os': "android",
  'ab_version': "31.5.3",
  'ssmix': "a",
  'device_type': "ART-L29N",
  'device_brand': "HUAWEI",
  'language': "en",
  'os_api': "29",
  'os_version': "10",
  'openudid': "47b07f1a42f3d962",
  'manifest_version_code': "2023105030",
  'resolution': "720*1491",
  'dpi': "320",
  'update_version_code': "2023105030",
  '_rticket': "1723030891856",
  'is_pad': "0",
  'current_region': "YE",
  'app_type': "normal",
  'sys_region': "YE",
  'mcc_mnc': "42102",
  'timezone_name': "Asia/Aden",
  'carrier_region_v2': "421",
  'residence': "YE",
  'app_language': "en",
  'carrier_region': "YE",
  'ac2': "lte",
  'uoo': "1",
  'op_region': "YE",
  'timezone_offset': "10800",
  'build_number': "31.5.3",
  'host_abi': "arm64-v8a",
  'locale': "en",
  'content_language': "en,",
  'ts': "1723030896",
  'cdid': "e8461423-0663-4a6a-88d6-61c364ffad9a",
  'support_webview': "1",
  'cronet_version': "2fdb62f9_2023-09-06",
  'ttnet_version': "4.2.152.11-tiktok",
  'use_store_region_cookie': "1"
}
params.update(Newparams())

ua = UserAgentTik(params)
params.update({'device_type': ua["type"]})
params.update({'device_brand': ua["brand"]})

payload = f"mix_mode=1&username={user}"
signature = sign(params=params,payload=payload,cookie=cookies, version="8404")

headers = {
  'User-Agent': ua["User-Agent"],
  'Content-Type': "application/x-www-form-urlencoded",
    'Accept': "application/json, text/plain, */*",
  'x-tt-passport-csrf-token': secret,
 }
headers.update(signature)

res = requests.post("https://api16-normal-c-alisg.tiktokv.com/passport/find_account/tiktok_username/", params=params, data=payload, headers=headers, cookies=cookies, proxies=proxy)
if res.json()["message"] == "success":
    print(f"[ # ] - Username Found In TikTok (Not Available) : {user}")
elif res.json()["data"]["description"] == "Couldn't find a TikTok account associated with this username":
    print(f"[ # ] - Username Not Found In TikTok (Available) : {user}")
else:
    print(f"Try Another Host : {host()}")