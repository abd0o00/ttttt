import os
import requests
import json
import random
import binascii
import uuid
import time
import urllib.parse

try:
    import SignerPy
except ImportError:
    print("SignerPy not found. Installing...")
    os.system("pip install SignerPy")
    import SignerPy

try:
    from MedoSigner import Argus, Gorgon, Ladon, md5
except ImportError:
    print("MedoSigner not found")
    exit(1)

def sign_medosigner(params, payload: str = None, cookie: str = None, aid: int = 1340, unix: int = None):
    x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload else None
    if not unix:
        unix = int(time.time())
    return Gorgon(params, unix, payload, cookie).get_value() | {
        "x-ladon": Ladon.encrypt(unix, 1611921764, aid),
        "x-argus": Argus.get_sign(params, x_ss_stub, unix, platform=19, aid=aid,
                                  license_id=1611921764, sec_device_id="",
                                  sdk_version="2.3.15.i18n", sdk_version_int=2)
    }

class TikTokProfileManager:
    def __init__(self):
        print("="*60)
        print("TikTok Profile Picture Uploader & Updater")
        print("="*60)
        
        self.session_id = input("Enter TikTok Session ID: ").strip()
        if not self.session_id:
            print("Error: Session ID is required!")
            exit(1)
        
        self.common_cookies = {
            'sessionid': self.session_id,
            'sessionid_ss': self.session_id,
            'sid_tt': self.session_id,
            'store-idc': 'alisg',
            'store-country-code': 'iq',
            'tt-target-idc': 'useast1a',
            'store-country-code-src': 'uid',
            'install_id': str(random.randint(1, 10 ** 19)),
        }
    
    def upload_image(self, image_path):
        print("\n" + "="*60)
        print(f"Uploading image: {os.path.basename(image_path)}")
        print("="*60)
        
        if not os.path.exists(image_path):
            print(f"Error: Image not found: {image_path}")
            return None
        
        try:
            with open(image_path, 'rb') as f:
                image_bytes = f.read()
            
            file_id = str(uuid.uuid4())
            filename = f"{file_id}.jpg"
            
            params = {
                'manifest_version_code': "400603",
                '_rticket': str(int(time.time() * 1000)),
                'app_language': "ar",
                'app_type': "normal",
                'iid': self.common_cookies['install_id'],
                'app_package': "com.zhiliaoapp.musically.go",
                'channel': "googleplay",
                'device_type': "RMX3834",
                'language': "ar",
                'host_abi': "arm64-v8a",
                'locale': "ar",
                'resolution': "720*1454",
                'openudid': binascii.hexlify(os.urandom(8)).decode(),
                'update_version_code': "400603",
                'ac2': "wifi",
                'cdid': str(uuid.uuid4()),
                'sys_region': "EG",
                'os_api': "34",
                'timezone_name': "Asia/Baghdad",
                'dpi': "272",
                'carrier_region': "IQ",
                'ac': "wifi",
                'device_id': str(random.randint(1, 10 ** 19)),
                'os': "android",
                'os_version': "14",
                'timezone_offset': "10800",
                'version_code': "400603",
                'app_name': "musically_go",
                'ab_version': "40.6.3",
                'version_name': "40.6.3",
                'device_brand': "realme",
                'op_region': "IQ",
                'ssmix': "a",
                'device_platform': "android",
                'build_number': "40.6.3",
                'region': "EG",
                'aid': "1340",
                'ts': str(int(time.time())),
            }
            
            print("Generating parameters with SignerPy...")
            try:
                params = SignerPy.get(params=params)
                print("Parameters generated successfully")
            except Exception as e:
                print(f"Error generating parameters: {str(e)}")
                return None
            
            payload = {'source': '0'}
            
            headers = {
                'User-Agent': "com.zhiliaoapp.musically.go/400603 (Linux; U; Android 14; ar; RMX3834; Build/UP1A.231005.007;tt-ok/3.12.13.44.lite-ul)",
             #   'Accept-Encoding': "gzip, ttzip",
                'rpc-persist-pyxis-policy-v-tnc': "1",
                'x-ss-dp': "1340",
                'sdk-version': "2",
                'passport-sdk-version': "5050090",
                'x-tt-ultra-lite': "1",
                'x-vc-bdturing-sdk-version': "2.3.15.i18n",
                'x-tt-store-region': "iq",
                'x-tt-store-region-src': "uid",
                'ttzip-tlb': "1",
            }
            
            cookie_parts = []
            for key, value in self.common_cookies.items():
                cookie_parts.append(f"{key}={value}")
            
            cookie_parts.extend([
                f"msToken={binascii.hexlify(os.urandom(32)).hex()}",
                f"d_ticket={binascii.hexlify(os.urandom(16)).hex()}",
                f"odin_tt={binascii.hexlify(os.urandom(32)).hex()}",
                f"cmpl_token=AgQYAPOn_hfkTl20KNk38TxdPP0bx_P-Gr-HLGCiy48",
                f"sid_guard={self.session_id}%7C{int(time.time())}%7C15551999",
            ])
            
            headers['Cookie'] = '; '.join(cookie_parts)
            
            print("Generating signatures with SignerPy...")
            try:
                signature = SignerPy.sign(params=params, payload=payload)
                
                headers.update({
                    'x-ss-req-ticket': signature.get('x-ss-req-ticket', str(int(time.time() * 1000))),
                    'x-ss-stub': signature.get('x-ss-stub', ''),
                    'x-argus': signature.get("x-argus", ''),
                    'x-gorgon': signature.get("x-gorgon", ''),
                    'x-khronos': signature.get("x-khronos", ''),
                    'x-ladon': signature.get("x-ladon", ''),
                })
                print("Signatures generated successfully")
            except Exception as e:
                print(f"Error generating signatures: {str(e)}")
                return None
            
            files = [('file', (filename, image_bytes, 'image/jpeg'))]
            upload_url = "https://api16-normal-c-alisg.tiktokv.com/aweme/v1/upload/image/"
            
            print("Uploading to TikTok...")
            response = requests.post(upload_url, params=params, data=payload, files=files, headers=headers, timeout=30)
            
            print(f"Upload Response Status: {response.status_code}")
            print(f"Response Text: {response.text[:200]}...")  # طباعة جزء من الرد للتصحيح
            
            if response.status_code == 200:
                try:
                    result = response.json()
                    
                    
                    if 'data' in result and 'uri' in result['data']:
                        avatar_uri = result['data']['uri']
                        print(f"Image uploaded successfully!")
                        print(f"Avatar URI: {avatar_uri}")
                        return avatar_uri
                    else:
                        print(f"URI not found in response. Response structure:")
                        print(json.dumps(result, indent=2))
                except json.JSONDecodeError:
                    print(f"Failed to parse JSON response: {response.text[:200]}")
            else:
                print(f"Upload failed with status code: {response.status_code}")
                print(f"Response: {response.text[:200]}")
            
            return None
            
        except Exception as e:
            print(f"Error during upload: {str(e)}")
            return None
    
    def update_profile_picture(self, avatar_uri):
        print("\n" + "="*60)
        print("Updating Profile Picture")
        print("="*60)
        
        try:
            current_time = int(time.time())
            
            params = {
                'manifest_version_code': "400603",
                '_rticket': str(int(time.time() * 1000)),
                'app_language': "ar",
                'app_type': "normal",
                'iid': self.common_cookies['install_id'],
                'app_package': "com.zhiliaoapp.musically.go",
                'channel': "googleplay",
                'device_type': "RMX3834",
                'language': "ar",
                'host_abi': "arm64-v8a",
                'locale': "ar",
                'resolution': "720*1454",
                'openudid': binascii.hexlify(os.urandom(8)).decode(),
                'update_version_code': "400603",
                'ac2': "wifi",
                'cdid': str(uuid.uuid4()),
                'sys_region': "EG",
                'os_api': "34",
                'timezone_name': "Asia/Baghdad",
                'dpi': "272",
                'carrier_region': "IQ",
                'ac': "wifi",
                'device_id': str(random.randint(1, 10 ** 19)),
                'os': "android",
                'os_version': "14",
                'timezone_offset': "10800",
                'version_code': "400603",
                'app_name': "musically_go",
                'ab_version': "40.6.3",
                'version_name': "40.6.3",
                'device_brand': "realme",
                'op_region': "IQ",
                'ssmix': "a",
                'device_platform': "android",
                'build_number': "40.6.3",
                'region': "EG",
                'aid': "1340",
                'ts': str(current_time),
                'as': "a1340qwert",
                'cp': "cbfghijk1lmn"
            }
            
            payload = {'avatar_uri': avatar_uri}
            payload_str = urllib.parse.urlencode(payload)
            params_str = urllib.parse.urlencode(params)
            
            print("Generating signatures with MedoSigner...")
            signed = sign_medosigner(params=params_str, payload=payload_str, cookie=self.session_id, aid=1340, unix=current_time)
            print("Signatures generated successfully")
            
            headers = {
                'User-Agent': "com.zhiliaoapp.musically.go/400603 (Linux; U; Android 14; ar; RMX3834; Build/UP1A.231005.007;tt-ok/3.12.13.44.lite-ul)",
             #   'Accept-Encoding': "gzip, ttzip",
                'rpc-persist-pyxis-policy-v-tnc': "1",
                'x-ss-dp': "1340",
                'x-ss-stub': md5(payload_str.encode('utf-8')).hexdigest().upper(),
                'sdk-version': "2",
                'passport-sdk-version': "5050090",
                'x-tt-ultra-lite': "1",
                'x-vc-bdturing-sdk-version': "2.3.15.i18n",
                'x-tt-store-region': "iq",
                'x-tt-store-region-src': "uid",
                'ttzip-tlb': "1",
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'x-ladon': signed["x-ladon"],
                'x-khronos': str(signed["x-khronos"]),
                'x-argus': signed["x-argus"],
                'x-gorgon': signed["x-gorgon"],
                'x-ss-req-ticket': str(int(time.time() * 1000)),
            }
            
            cookie_parts = []
            for key, value in self.common_cookies.items():
                cookie_parts.append(f"{key}={value}")
            
            cookie_parts.extend([
                f"msToken={binascii.hexlify(os.urandom(32)).hex()}",
                f"d_ticket={binascii.hexlify(os.urandom(16)).hex()}",
                f"odin_tt={binascii.hexlify(os.urandom(32)).hex()}",
                f"cmpl_token=AgQYAPOn_hfkTl20KNk38TxdPP0bx_P-Gr-HLGCiy48",
                f"sid_guard={self.session_id}%7C{current_time}%7C15551999",
            ])
            
            headers['Cookie'] = '; '.join(cookie_parts)
            headers['x-tt-token'] = f"{self.session_id}--"
            
            update_url = "https://api16-normal-c-alisg.tiktokv.com/aweme/v1/commit/user/"
            
            print("Sending update request...")
            response = requests.post(update_url, params=params, data=payload, headers=headers, timeout=30)
            
       #     print(f"Update Response Status: {response.status_code}")
            
            if response.status_code == 200:
                try:
                    return response.json()
                except:
                    return {"raw_response": response.text, "status_code": response.status_code}
            else:
                print(f"Update failed with status code: {response.status_code}")
                print(f"Response: {response.text[:200]}")
                return {"error": f"HTTP {response.status_code}", "response": response.text[:200]}
                
        except Exception as e:
            print(f"Error during update: {str(e)}")
            return {"error": f"Exception: {str(e)}"}

def main():
    manager = TikTokProfileManager()
    
    while True:
        image_path = input("\nEnter image path (or 'exit' to quit): ").strip()
        
        if image_path.lower() == 'exit':
            print("\nGoodbye!")
            break
        
        if (image_path.startswith('"') and image_path.endswith('"')) or (image_path.startswith("'") and image_path.endswith("'")):
            image_path = image_path[1:-1]
        
        if not os.path.exists(image_path):
     #       print(f"Error: Image not found: {image_path}")
            continue
        
        avatar_uri = manager.upload_image(image_path)
        
        if avatar_uri:
            result = manager.update_profile_picture(avatar_uri)
            
            print("\n" + "="*60)
            print("FINAL RESULT")
            print("="*60)
            print(json.dumps(result, indent=2, ensure_ascii=False))
            
            if isinstance(result, dict):
                if result.get('status_code') == 0:
                    print("\nSUCCESS! Profile picture updated successfully!")
                else:
                    print(f"\nFAILED: {result.get('status_msg', 'Unknown error')}")
        else:
            print("\nFailed to upload image. Profile picture was not updated.")
        
        choice = input("\nDo you want to upload another image? (y/n): ").lower()
        if choice != 'y':
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user")
    except Exception as e:
        print(f"\nCritical error: {str(e)}")