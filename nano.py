from TikSign import Argus, Ladon, Gorgon, Newparams, UserAgentTik, trace_id
import time
import random
import secrets
import requests
from hashlib import md5
from urllib.parse import urlencode
host_list = [
    'api16-normal-apix-quic.tiktokv.com', 'api16-normal-apix.tiktokv.com',
    'api16-normal-baseline.tiktokv.com', 'api16-normal-c-alisg.tiktokv.com',
    'api16-normal-c-useast1a.tiktokv.com', 'api16-normal-c-useast1a.musical.ly',
    'api16-normal-no1a.tiktokv.eu', 'api16-normal-quic.tiktokv.com',
    'api16-normal-useast5.tiktokv.us', 'api16-normal-useast5.us.tiktokv.com',
    'api16-normal-zr.tiktokv.com', 'api16-normal.tiktokv.com',
    'api16-normal.ttapis.com', 'api19-normal-c-alisg.tiktokv.com',
    'api19-normal-c-useast1a.musical.ly', 'api19-normal-c-useast1a.tiktokv.com',
    'api19-normal-useast5.us.tiktokv.com', 'api19-normal-zr.tiktokv.com',
    'api19-normal.tiktokv.com', 'api2-19-h2.musical.ly', 'api2.musical.ly',
    'api21-h2.tiktokv.com', 'api21-normal.tiktokv.com',
    'api22-normal-c-alisg.tiktokv.com', 'api22-normal-c-useast1a.tiktokv.com',
    'api22-normal-zr.tiktokv.com', 'api22-normal.tiktokv.com',
    'api23-normal.tiktokv.com', 'api23-normal-zr.tiktokv.com',
    'api3-normal.tiktokv.com', 'api31-normal-alisg.tiktokv.com',
    'api31-normal.tiktokv.com', 'api31-normal-useast2a.tiktokv.com',
    'api31-normal-zr.tiktokv.com', 'api32-normal-alisg.tiktokv.com',
    'api32-normal.tiktokv.com', 'api32-normal-zr.tiktokv.com',
    'api74-normal.tiktokv.com', 'api9-normal.tiktokv.com'
]

host = random.choice(host_list)


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


url = f'https://{host}/passport/email/bind_without_verify/'


params = {
    'passport-sdk-version': '19',
    'iid': '7372841843832473349',
    'device_id': '7194351170030650885',
    'ac': 'WIFI',
    'channel': 'googleplay',
    'aid': '1233',
    'app_name': 'musical_ly',
    'version_code': '310503',
    'version_name': '31.5.3',
    'device_platform': 'android',
    'os': 'android',
    'ab_version': '31.5.3',
    'ssmix': 'a',
    'device_type': 'Infinix+X6816',
    'device_brand': 'Infinix',
    'language': 'ar',
    'os_api': '30',
    'os_version': '11',
    'openudid': '3293d1a6e9361cb7',
    'manifest_version_code': '2023105030',
    'resolution': '720*1568',
    'dpi': '303',
    'update_version_code': '2023105030',
    '_rticket': '1722418820230',
    'is_pad': '0',
    'current_region': 'IQ',
    'app_type': 'normal',
    'sys_region': 'IQ',
    'mcc_mnc': '41805',
    'timezone_name': 'Asia/Baghdad',
    'carrier_region_v2': '418',
    'residence': 'IQ',
    'app_language': 'ar',
    'carrier_region': 'IQ',
    'ac2': 'wifi5g',
    'uoo': '0',
    'op_region': 'IQ',
    'timezone_offset': '10800',
    'build_number': '31.5.3',
    'host_abi': 'arm64-v8a',
    'locale': 'ar',
    'region': 'IQ',
    'content_language': 'ar,',
    'ts': '1722418819',
    'cdid': '556d8162-2721-4760-a509-a92b3cf27738',
    'support_webview': '1',
    'cronet_version': '2fdb62f9_2023-09-06',
    'ttnet_version': '4.2.152.11-tiktok',
    'use_store_region_cookie': '1',
    'app_version': '31.5.3'
}


params.update(Newparams())


ua = UserAgentTik(params)
params.update({
    'device_type': ua["type"],
    'device_brand': ua["brand"]
})


payload = {
    'account_sdk_source': 'app',
    'multi_login': '1',
    'email_source': '9',
    'email': 'xzhlrce@hi2.in',
    'mix_mode': '1'
}


signature = sign(
    params=urlencode(params),
    payload=urlencode(payload),
    cookie=None
)


passport_csrf_token = secrets.token_hex(16)
trace = trace_id()

try:
 
    sessions_response = requests.get("https://raw.githubusercontent.com/elia23py/-_py/refs/heads/main/Seasons")
    sessions_text = sessions_response.text.replace('"', '')
    
   
    sessions = [session.strip() for session in sessions_text.split(',') if session.strip()]
    
    if not sessions:
        raise ValueError("No valid sessions found in the response")
    
    selected_session = random.choice(sessions)
    print(f"Selected session: {selected_session}")
    
except Exception as e:
    print(f"Error fetching sessions: {e}")
   
    selected_session = "73d108ee305e5c4e2abb81354ee69eef"
    print(f"Using default session: {selected_session}")

# رؤوس الطلب
headers = {
    'User-Agent': ua["User-Agent"],
    'x-tt-passport-csrf-token': passport_csrf_token,
    'sdk-version': '2',
    'multi_login': '1',
    'passport-sdk-version': '19',
    'x-bd-kmsv': '0',
    'x-vc-bdturing-sdk-version': '2.2.1.i18n',
    'x-tt-dm-status': 'login=1;ct=1;rt=1',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'x-tt-store-region': 'iq',
    'x-tt-store-region-src': 'uid',
    'x-tt-store-region-uid': 'iq',
    'x-tt-store-region-did': 'iq',
    'x-ss-dp': '1233',
    'x-tt-trace-id': trace,
    'Cookie': f'sessionid={selected_session}'
}


headers.update(signature)


#print("\nHeaders being sent:")
for key, value in headers.items():
    if key.lower() == 'cookie':
        print(f"{key}: sessionid=***")
    else:
        print(f"{key}: {value}")


try:
    res = requests.post(url, params=params, data=payload, headers=headers, timeout=30)
    print(f"\nResponse Status Code: {res.status_code}")
    print(f"Response Text: {res.text}")
    
except requests.exceptions.RequestException as e:
    print(f"\nRequest failed: {e}")