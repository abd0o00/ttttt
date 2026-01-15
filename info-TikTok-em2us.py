
import os, random, binascii, uuid, requests, SignerPy, secrets, re, time, string
from MedoSigner import Argus, Gorgon, Ladon, md5
from typing import Any
def xor(String:str) -> Any: return "".join([hex(ord(c)^5)[2:]for c in String])
g=input('Username or email > ')
url = "https://api32-normal-alisg.tiktokv.com/passport/account_lookup/email/"
params = {"request_tag_from": "h5", "fixed_mix_mode": "1", "mix_mode": "1", "account_param": xor(g), "scene": "1", "device_platform": "android", "os": "android", "ssmix": "a", "_rticket": "1755466425423", "cdid": "cefe6f9c-d9d9-4107-9543-f5226d5b3ccd", "channel": "googleplay", "aid": "1233", "app_name": "musical_ly", "version_code": "370805", "version_name": "37.8.5", "manifest_version_code": "2023708050", "update_version_code": "2023708050", "ab_version": "37.8.5", "resolution": "1600*900", "dpi": "240", "device_type": "SM-S908E", "device_brand": "samsung", "language": "en", "os_api": "28", "os_version": "9", "ac": "wifi", "is_pad": "0", "current_region": "DE", "app_type": "normal", "sys_region": "US", "last_install_time": "1754825061", "mcc_mnc": "26202", "timezone_name": "Asia/Baghdad", "carrier_region_v2": "262", "residence": "DE", "app_language": "en", "carrier_region": "DE", "timezone_offset": "10800", "host_abi": "arm64-v8a", "locale": "en", "content_language": "en,", "ac2": "wifi", "uoo": "1", "op_region": "DE", "build_number": "37.8.5", "region": "US", "ts": "1755466424", "iid": "7536212628504381192", "device_id": "7536211658156213782", "openudid": "4196494d5939fa86", "support_webview": "1", "okhttp_version": "4.2.210.6-tiktok", "use_store_region_cookie": "1", "type":"3736", "app_version":"37.8.5"}
cookies = {"passport_csrf_token": "d52c500f67607c862972a043a4662972", "passport_csrf_token_default": "d52c500f67607c862972a043a4662972", "install_id": "7536212628504381192"}
m=SignerPy.sign(params=params,cookie=cookies)
headers = {'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 9; en; SM-S908E; Build/TP1A.220624.014;tt-ok/3.12.13.16)", 'Accept': "application/json, text/plain, */*", 'Accept-Encoding': "gzip", 'rpc-persist-pyxis-policy-v-tnc': "1", 'x-ss-stub': m['x-ss-stub'], 'x-tt-referer': "https://inapp.tiktokv.com/ucenter_web/account_lookup_tool", 'x-tt-pba-enable': "1", 'x-bd-kmsv': "0", 'x-tt-dm-status': "login=1;ct=1;rt=1", 'x-ss-req-ticket':m['x-ss-req-ticket'], 'x-bd-client-key': "#LFLluN0wIdQaDxIXUUvEDzSMeYqmuwelaqRmzYJxN3Sl5PDfyg0ZQMCLkYm+QRisqBm2hpAXzDekRo0e", 'x-tt-passport-csrf-token': "d52c500f67607c862972a043a4662972", 'sdk-version': "2", 'tt-ticket-guard-iteration-version': "0", 'tt-ticket-guard-version': "3", 'passport-sdk-settings': "x-tt-token", 'passport-sdk-sign': "x-tt-token", 'passport-sdk-version': "6031990", 'oec-vc-sdk-version': "3.0.5.i18n", 'x-vc-bdturing-sdk-version': "2.3.8.i18n", 'x-tt-request-tag': "n=0;nr=011;bg=0", 'x-tt-pba-enable': "1", 'x-ladon':m['x-ladon'], 'x-khronos':m['x-khronos'], 'x-argus': m['x-argus'], 'x-gorgon':m['x-gorgon'], 'content-type': "application/x-www-form-urlencoded"}
response = requests.post(url, headers=headers,params=params,cookies=cookies)
passport_ticket=response.json()["data"]["accounts"][0]["passport_ticket"]
email = requests.post("https://api.internal.temp-mail.io/api/v3/email/new").json()["email"]
params.update({"email":xor(email),"not_login_ticket":passport_ticket}); url = "https://api16-normal-c-alisg.tiktokv.com/passport/email/send_code/"
m=SignerPy.sign(params=params,cookie=cookies)
headers = {'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 9; en; SM-S908E; Build/TP1A.220624.014;tt-ok/3.12.13.16)", 'Accept-Encoding': "gzip", 'x-ss-stub':m['x-ss-stub'], 'x-tt-pba-enable': "1", 'x-tt-multi-sids': "6639559680287080453%3Af67dac7231a906f233a957f8965344ba", 'x-bd-kmsv': "0", 'x-tt-dm-status': "login=1;ct=1;rt=1", 'x-ss-req-ticket': m['x-ss-req-ticket'], 'x-bd-client-key': "#LFLluN0wIdQaDxIXUUvEDzSMeYqmuwelaqRmzYJxN3Sl5PDfyg0ZQMCLkYm+QRisqBm2hpAXzDekRo0e", 'x-tt-passport-csrf-token': "d52c500f67607c862972a043a4662972", 'sdk-version': "2", 'tt-ticket-guard-iteration-version': "0", 'tt-ticket-guard-version': "3", 'passport-sdk-settings': "x-tt-token", 'passport-sdk-sign': "x-tt-token", 'passport-sdk-version': "6031990", 'x-tt-bypass-dp': "1", 'oec-vc-sdk-version': "3.0.5.i18n", 'x-vc-bdturing-sdk-version': "2.3.8.i18n", 'x-tt-request-tag': "n=0;nr=011;bg=0", 'x-tt-pba-enable': "1", 'x-ladon':m['x-ladon'], 'x-khronos':m['x-khronos'], 'x-argus': m['x-argus'], 'x-gorgon':m['x-gorgon']}
response = requests.post(url,params=params, headers=headers,cookies=cookies);time.sleep(4.5)
message = requests.get("https://api.internal.temp-mail.io/api/v3/email/{}/messages".format(email))
username = message.json()[0]["body_text"].split('This email was generated for')[1].split("\n")[0].strip().rstrip(".")
def level(user_id):
    try:
        url = f"https://webcast16-normal-no1a.tiktokv.eu/webcast/user/?request_from=profile_card_v2&request_from_scene=1&target_uid={user_id}&iid={random.randint(1, 10**19)}&device_id={random.randint(1, 10**19)}&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=300102&version_name=30.1.2&device_platform=android&os=android&ab_version=30.1.2&ssmix=a&device_type=RMX3511&device_brand=realme&language=ar&os_api=33&os_version=13&openudid={binascii.hexlify(os.urandom(8)).decode()}&manifest_version_code=2023001020&resolution=1080*2236&dpi=360&update_version_code=2023001020&_rticket={str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + '4632'}&current_region=IQ&app_type=normal&sys_region=IQ&mcc_mnc=41805&timezone_name=Asia%2FBaghdad&carrier_region_v2=418&residence=IQ&app_language=ar&carrier_region=IQ&ac2=wifi&uoo=0&op_region=IQ&timezone_offset=10800&build_number=30.1.2&host_abi=arm64-v8a&locale=ar&region=IQ&content_language=gu%2C&ts={str(round(random.uniform(1.2, 1.6) * 100000000) * -1)}&cdid={uuid.uuid4()}&webcast_sdk_version=2920&webcast_language=ar&webcast_locale=ar_IQ"
        headers = {'User-Agent': "com.zhiliaoapp.musically/2023001020 (Linux; U; Android 13; ar; RMX3511; Build/TP1A.220624.014; Cronet/TTNetVersion:06d6a583 2023-04-17 QuicVersion:d298137e 2023-02-13)"}
        unix = int(time.time())
        x_ss_stub = md5(''.encode('utf-8')).hexdigest()
        sig = Gorgon(url.split('?')[1], unix, '', None).get_value() | {"x-ladon": Ladon.encrypt(unix, 1611921764, 1233), "x-argus": Argus.get_sign(url.split('?')[1], x_ss_stub, unix, platform=19, aid=1233, license_id=1611921764, sec_device_id="AadCFwpTyztA5j9L" + ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(9)), sdk_version="2.3.1.i18n", sdk_version_int=2)}
        headers.update(sig)
        response = requests.get(url, headers=headers, timeout=10)
        level = re.search(r'"default_pattern":"(.*?)"', response.text).group(1)
        return level
    except:
        return "Not Available"
try:
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Android 10; Pixel 3 Build/QKQ1.200308.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6394.70 Mobile Safari/537.36 trill_350402 JsSdk/1.0 NetType/MOBILE Channel/googleplay AppName/trill app_version/35.3.1 ByteLocale/en ByteFullLocale/en Region/IN AppId/1180 Spark/1.5.9.1 AppVersion/35.3.1 BytedanceWebview/d8a21c6"}
    tikinfo = requests.get(f'https://www.tiktok.com/@{username}', headers=headers, timeout=10).text
    if 'webapp.user-detail"' in tikinfo:
        getting = str(tikinfo.split('webapp.user-detail"')[1]).split('"RecommendUserList"')[0]
        id = str(getting.split('id":"')[1]).split('",')[0]
        Name = str(getting.split('nickname":"')[1]).split('",')[0]
        bio = str(getting.split('signature":"')[1]).split('",')[0]
        country = str(getting.split('region":"')[1]).split('",')[0]
        private = str(getting.split('privateAccount":')[1]).split(',"')[0]
        Followers = str(getting.split('followerCount":')[1]).split(',"')[0]
        following = str(getting.split('followingCount":')[1]).split(',"')[0]
        like = str(getting.split('heart":')[1]).split(',"')[0]
        video = str(getting.split('videoCount":')[1]).split(',"')[0]
        UserName = username
        Level = level(id)
        secret = secrets.token_hex(16)
        url = "https://api16-normal-c-alisg.tiktokv.com/passport/find_account/tiktok_username/"
        params = {'request_tag_from': "h5", 'iid': str(random.randint(1, 10**19)), 'device_id': str(random.randint(1, 10**19)), 'ac': "WIFI", 'channel': "googleplay", 'aid': "567753", 'app_name': "tiktok_studio", 'version_code': "370301", 'version_name': "37.3.1", 'device_platform': "android", 'os': "android", 'ab_version': "37.3.1", 'ssmix': "a", 'device_type': "RMX3269", 'device_brand': "realme", 'language': "en", 'os_api': "28", 'os_version': "10", 'openudid': binascii.hexlify(os.urandom(8)).decode(), 'manifest_version_code': "370301", 'resolution': "720*1448", 'dpi': "420", 'update_version_code': "370301", '_rticket': str(round(random.uniform(1.2, 1.6)*100000000)*-1)+"4632", 'is_pad': "0", 'current_region': "en", 'app_type': "normal", 'sys_region': "en", 'last_install_time': "1650243523", 'mcc_mnc': "41840", 'timezone_name': "Asia/Baghdad", 'carrier_region_v2': "418", 'residence': "ُen", 'app_language': "en", 'carrier_region': "IQ", 'ac2': "wifi", 'uoo': "0", 'op_region': "IQ", 'timezone_offset': "10800", 'build_number': "37.3.1", 'host_abi': "arm64-v8a", 'locale': "en", 'region': "IQ", 'ts': str(round(random.uniform(1.2, 1.6)*100000000)*-1), 'cdid': str(uuid.uuid4()), 'support_webview': "1", 'cronet_version': "f6248591_2024-09-11", 'ttnet_version': "4.2.195.9-tiktok", 'use_store_region_cookie': "1", 'app_version': "37.3.1"}
        cookies = {"passport_csrf_token": secret, "passport_csrf_token_default": secret}
        payload = {'mix_mode': "1", 'username': username}        
        for version in [4404, 8404]:
            try:
                m = SignerPy.sign(params=params, cookie=cookies, payload=payload, version=version)
                headers = {'User-Agent': 'com.zhiliaoapp.musically/2023105030 (Linux; U; Android 11; ar; RMX3269; Build/RP1A.201005.001; Cronet/TTNetVersion:2fdb62f9 2023-09-06 QuicVersion:bb24d47c 2023-07-19)', 'x-tt-passport-csrf-token': cookies['passport_csrf_token'], 'x-ss-req-ticket': m['x-ss-req-ticket'], 'x-ss-stub': m['x-ss-stub'], 'x-gorgon': m["x-gorgon"], 'x-khronos': m["x-khronos"], 'content-type': "application/x-www-form-urlencoded"}
                response = requests.post(url, params=params, data=payload, headers=headers, cookies=cookies, timeout=10)
                if response.text.strip() and "token" in response.text:
                    token = response.json()["data"]["token"]
                    params['not_login_ticket'] = token
                    params['_rticket'] = str(round(random.uniform(1.2, 1.6)*100000000)*-1)+"4632"
                    params['ts'] = str(round(random.uniform(1.2, 1.6)*100000000)*-1)
                    m = SignerPy.sign(params=params, cookie=cookies, version=version)
                    headers.update({'x-ss-req-ticket': m['x-ss-req-ticket'], 'x-ss-stub': m['x-ss-stub'], 'x-gorgon': m["x-gorgon"], 'x-khronos': m["x-khronos"]})
                    available_ways = requests.post("https://api16-normal-c-alisg.tiktokv.com/passport/auth/available_ways/", params=params, headers=headers, cookies=cookies, timeout=10)
                    if 'success' in available_ways.text:
                        ways_data = available_ways.json()["data"]
                        passkey = "Yes" if ways_data.get('has_passkey') else "No"
                        out_passkey = "Yes" if ways_data.get('has_oauth') else "No"
                    else:
                        passkey = "No"
                        out_passkey = "No"
                    break
            except:
                continue        
        print(f"Name : {Name}")
        print(f"UserName : {UserName}")
        print(f"Followers : {Followers}")
        print(f"following : {following}")
        print(f"bio : {bio}")
        print(f"country : {country}")
        print(f"private : {private}")
        print(f"like : {like}")
        print(f"video : {video}")
        print(f"passkey : {passkey}")
        print(f"out_passkey : {out_passkey}")
        print(f"Level : {Level}")
    else:
        print("user not found")
except:
    secret = secrets.token_hex(16)
    url = "https://api16-normal-c-alisg.tiktokv.com/passport/find_account/tiktok_username/"
    params = {'request_tag_from': "h5", 'iid': str(random.randint(1, 10**19)), 'device_id': str(random.randint(1, 10**19)), 'ac': "WIFI", 'channel': "googleplay", 'aid': "567753", 'app_name': "tiktok_studio", 'version_code': "370301", 'version_name': "37.3.1", 'device_platform': "android", 'os': "android", 'ab_version': "37.3.1", 'ssmix': "a", 'device_type': "RMX3269", 'device_brand': "realme", 'language': "en", 'os_api': "28", 'os_version': "10", 'openudid': binascii.hexlify(os.urandom(8)).decode(), 'manifest_version_code': "370301", 'resolution': "720*1448", 'dpi': "420", 'update_version_code': "370301", '_rticket': str(round(random.uniform(1.2, 1.6)*100000000)*-1)+"4632", 'is_pad': "0", 'current_region': "en", 'app_type': "normal", 'sys_region': "en", 'last_install_time': "1650243523", 'mcc_mnc': "41840", 'timezone_name': "Asia/Baghdad", 'carrier_region_v2': "418", 'residence': "ُen", 'app_language': "en", 'carrier_region': "IQ", 'ac2': "wifi", 'uoo': "0", 'op_region': "IQ", 'timezone_offset': "10800", 'build_number': "37.3.1", 'host_abi': "arm64-v8a", 'locale': "en", 'region': "IQ", 'ts': str(round(random.uniform(1.2, 1.6)*100000000)*-1), 'cdid': str(uuid.uuid4()), 'support_webview': "1", 'cronet_version': "f6248591_2024-09-11", 'ttnet_version': "4.2.195.9-tiktok", 'use_store_region_cookie': "1", 'app_version': "37.3.1"}
    cookies = {"passport_csrf_token": secret, "passport_csrf_token_default": secret}
    payload = {'mix_mode': "1", 'username': username}    
    for version in [4404, 8404]:
        try:
            m = SignerPy.sign(params=params, cookie=cookies, payload=payload, version=version)
            headers = {'User-Agent': 'com.zhiliaoapp.musically/2023105030 (Linux; U; Android 11; ar; RMX3269; Build/RP1A.201005.001; Cronet/TTNetVersion:2fdb62f9 2023-09-06 QuicVersion:bb24d47c 2023-07-19)', 'x-tt-passport-csrf-token': cookies['passport_csrf_token'], 'x-ss-req-ticket': m['x-ss-req-ticket'], 'x-ss-stub': m['x-ss-stub'], 'x-gorgon': m["x-gorgon"], 'x-khronos': m["x-khronos"], 'content-type': "application/x-www-form-urlencoded"}
            response = requests.post(url, params=params, data=payload, headers=headers, cookies=cookies, timeout=10)
            if response.text.strip() and "token" in response.text:
                token = response.json()["data"]["token"]
                params['not_login_ticket'] = token
                params['_rticket'] = str(round(random.uniform(1.2, 1.6)*100000000)*-1)+"4632"
                params['ts'] = str(round(random.uniform(1.2, 1.6)*100000000)*-1)
                m = SignerPy.sign(params=params, cookie=cookies, version=version)
                headers.update({'x-ss-req-ticket': m['x-ss-req-ticket'], 'x-ss-stub': m['x-ss-stub'], 'x-gorgon': m["x-gorgon"], 'x-khronos': m["x-khronos"]})
                user_detail = requests.post("https://api16-normal-c-alisg.tiktokv.com/passport/user/detail/", params=params, headers=headers, cookies=cookies, timeout=10)
                available_ways = requests.post("https://api16-normal-c-alisg.tiktokv.com/passport/auth/available_ways/", params=params, headers=headers, cookies=cookies, timeout=10)
                if user_detail.text.strip() and 'success' in user_detail.text:
                    user_data = user_detail.json()["data"]["user"]
                    Name = user_data.get("nickname", "")
                    UserName = user_data.get("unique_id", "")
                    Followers = user_data.get("follower_count", 0)
                    following = user_data.get("following_count", 0)
                    bio = user_data.get("signature", "")
                    id = user_data.get("uid", "")
                    country = user_data.get("region", "")
                    private = user_data.get("private_account", "")
                    like = user_data.get("total_favorited", 0)
                    video = user_data.get("aweme_count", 0)                    
                    Level = level(id) if id else "Not Available"                    
                if available_ways.text.strip() and 'success' in available_ways.text:
                    ways_data = available_ways.json()["data"]
                    passkey = "Yes" if ways_data.get('has_passkey') else "No"
                    out_passkey = "Yes" if ways_data.get('has_oauth') else "No"
                else:
                    passkey = "No"
                    out_passkey = "No"                
                print(f"Name : {Name}")
                print(f"UserName : {UserName}")
                print(f"Followers : {Followers}")
                print(f"following : {following}")
                print(f"bio : {bio}")
                print(f"country : {country}")
                print(f"private : {private}")
                print(f"like : {like}")
                print(f"video : {video}")
                print(f"passkey : {passkey}")
                print(f"out_passkey : {out_passkey}")
                print(f"Level : {Level}")
                break
        except:
            continue