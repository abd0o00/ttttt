import requests
import json
url = "https://tnc-boot.tiktokv.com/get_domains/v5/"
params = {
    "version_code": "2023504040",
    "user_id": "0",
    "aid": "1233",
    "ac": "mobile",
    "device_type": "Redmi Note 8 Pro",
    "app_name": "musical_ly",
    "channel": "googleplay",
    "os_version": "11",
    "device_platform": "android",
    "update_version_code": "2023504040",
    "os_api": "30",
    "device_brand": "Redmi",
    "version_name": "35.4.4",
    "manifest_version_code": "2023504040",
    "abi": "arm64-v8a",
    "region": "ye",
    "sys_region": "eg",
    "carrier_region": "ye",
    "cronet_version": "f58efab5_2024-06-13",
    "ttnet_version": "4.2.137.79-tiktok",
    "use_store_region_cookie": "1",
    "tnc_src": "4",
    "delay": "0"
}

headers = {
  'User-Agent': "com.zhiliaoapp.musically/2023504040 (Linux; U; Android 11; ar_EG; Redmi Note 8 Pro; Build/RP1A.200720.011; Cronet/TTNetVersion:f58efab5 2024-06-13 QuicVersion:5d23606e 2024-05-23)",
  'Local-Etag': "0",
  'passport-sdk-version': "6010290",
  'sdk-version': "2",
  
  'Cookie': "store-country-code=ye; store-country-code-src=local"
}

response = requests.get(url, headers=headers, params=params)

print(json.dumps(response.json(), indent=2, ensure_ascii=False))