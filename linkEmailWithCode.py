import os,time,uuid,random,string,secrets,binascii,requests
from urllib.parse import urlencode
from hashlib import md5
from hsopyt import Argus, Ladon, Gorgon, md5
from TikSign import Newparams, UserAgentTik,xor,Argus,Ladon,Gorgon
def sign(params: str, payload: str or None = None, sec_device_id: str = '', cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = 'v05.00.06-ov-android', sdk_version: int = 167775296, platform: int = 0, unix: float = None):
        x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
        if not unix: unix = time.time()

        return Gorgon(params, unix, payload, cookie).get_value() | {
            'content-length' : str(len(payload)),
            'x-ss-stub'      : x_ss_stub.upper(),
            'x-ladon'        : Ladon.encrypt(int(unix), license_id, aid),
            'x-argus'        : Argus.get_sign(params, x_ss_stub, int(unix),
                platform        = platform,
                aid             = aid,
                license_id      = license_id,
                sec_device_id   = sec_device_id,
                sdk_version     = sdk_version_str, 
                sdk_version_int = sdk_version
            )}


params = {
    'channel': "googleplay",
    'aid': "1233",
    'app_name': "musical_ly",
    'version_code': "270702",
    'version_name': "27.7.2",
    'ab_version': "27.7.2",
    'build_number': "27.7.2",
    'app_version': "27.7.2",
    'device_platform': "android",
    'os_version': "15",
    'ac': "wifi",
    'locale': "en",
    'ssmix': "a",
    'device_id':'',
}
params.update(Newparams())
use = UserAgentTik(params)
params["device_type"] = use["type"]
params["device_brand"] = use["brand"]
ema=input("[+]Enter Em : ")
vv = input("sess:")
payload = {
"rules_version": "v2",
"account_sdk_source": "app",
"multi_login": "1",
"type": "3d",
"email": xor(ema),
"mix_mode": "1"}
headers = {
  'User-Agent':use["User-Agent"],
  'Cookie': f"sessionid={vv}"
}
ss=sign(urlencode(params), urlencode(payload), "AadCFwpTyztA5j9L" + ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(9)), None, 1233)
headers.update(ss)
r11 = requests.post("https://api22-normal-c-alisg.tiktokv.com/passport/email/send_code/", params=params, data=payload, headers=headers).text
print(r11)
if "email_ticket" in r11:
 payload= {
   "code": xor(input('[+] Enter Code : ')),
   "email": xor(ema),
   "account_sdk_source": "app",
  "multi_login": '1',
  "email_source": '1',
  "mix_mode": '1'
 }
 ss=sign(urlencode(params), urlencode(payload), "AadCFwpTyztA5j9L" + ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(9)), None, 1233)
 headers.update(ss)
 response = requests.post("https://api22-normal-c-alisg.tiktokv.com/passport/email/bind/", params=params, data=payload, headers=headers)
 
 print(response.text)