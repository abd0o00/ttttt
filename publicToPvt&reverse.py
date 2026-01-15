import re
import json
import requests
import time
import random
import base64
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlencode
import SignerPy
import sys
import os


class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'

def print_color(text, color):
    print(f"{color}{text}{Colors.END}")

class TikTokVideoManager:
    def __init__(self, sessionid):
        self.sessionid = sessionid
        self.request_count = 0
        self.all_aweme_ids = set()
        self.user_agent = "com.zhiliaoapp.musically.go/410203 (Linux; U; Android 14; ar_EG; RMX3834; Build/UP1A.231005.007;tt-ok/3.12.13.44.lite-ul)"
        
    def get_headers(self, extra_headers=None):
     
        headers = {
            'User-Agent': self.user_agent,
            'rpc-persist-pyxis-policy-v-tnc': "1",
            'x-ss-dp': "1340",
            'sdk-version': "2",
            'passport-sdk-version': "5050090",
            'x-tt-ultra-lite': "1",
            'x-vc-bdturing-sdk-version': "2.3.15.i18n",
            'x-tt-store-region': "iq",
            'x-tt-store-region-src': "uid",
            'ttzip-tlb': "1",
            'Cookie': f"sessionid={self.sessionid}; sessionid_ss={self.sessionid};"
        }
        
        if extra_headers:
            headers.update(extra_headers)
        
        return headers
    
    def get_user_info(self, username):
      
        try:
            url = f"https://www.tiktok.com/@{username}"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36",
                "Accept-Language": "en-US,en;q=0.9",
            }

            response = requests.get(url, headers=headers, timeout=10)
            m = re.search(r'({"__DEFAULT_SCOPE__":.*})</script>', response.text)
            if not m:
                return None, None
            
            data = json.loads(m.group(1))
            user_info = data["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]["user"]
            secUid = user_info.get("secUid", "")
            user_id = user_info.get("id", "")
            
            return secUid, user_id
            
        except Exception as e:
            print_color(f"❌ خطأ في الحصول على معلومات المستخدم: {str(e)}", Colors.RED)
            return None, None
    
    def get_private_videos_list(self, max_cursor=0):
    
        url = f"https://api16-normal-c-alisg.tiktokv.com/lite/v2/private/item/list/?max_cursor={max_cursor}&count=100000&manifest_version_code=410203&_rticket={int(time.time()*1000)}&app_language=ar&app_type=normal&iid=7570139761176839937&app_package=com.zhiliaoapp.musically.go&channel=googleplay&device_type=RMX3834&language=ar&host_abi=arm64-v8a&locale=ar&resolution=720*1454&openudid=b57299cf6a5bb211&update_version_code=410203&ac2=wifi&cdid=566bdea1-9b82-4846-af74-29d2e1b9a1a9&sys_region=EG&os_api=34&timezone_name=Asia%2FBaghdad&dpi=272&carrier_region=IQ&ac=wifi&device_id=7456376313159714309&os=android&os_version=14&timezone_offset=10800&version_code=410203&app_name=musically_go&ab_version=41.2.3&version_name=41.2.3&device_brand=realme&op_region=IQ&ssmix=a&device_platform=android&build_number=41.2.3&region=EG&aid=1340&ts={int(time.time())}"

        headers = self.get_headers()
        
        try:
            signature = SignerPy.sign(params=url, version=8404)
            
            headers.update({
                'x-ss-stub': signature['x-ss-stub'],
                'x-gorgon': signature["x-gorgon"],
                'x-khronos': signature["x-khronos"],
                'x-ladon': signature["x-ladon"],
                'x-argus': signature['x-argus'],
            })

            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code != 200:
                print_color(f"❌ خطأ في الاستجابة: {response.status_code}", Colors.RED)
                return {'aweme_ids': [], 'has_more': False, 'next_cursor': 0}
            
            return self.parse_response(response.json())
            
        except Exception as e:
            print_color(f"❌ خطأ في الطلب: {str(e)}", Colors.RED)
            return {'aweme_ids': [], 'has_more': False, 'next_cursor': 0}
    
    def get_public_videos_list(self, username, max_cursor=0):
     
        try:
            secUid, user_id = self.get_user_info(username)
            if not secUid or not user_id:
                return {'aweme_ids': [], 'has_more': False, 'next_cursor': 0}

            _url = "https://api16-normal-c-alisg.tiktokv.com/lite/v2/public/item/list/"
            params = {
                "source": "0",
                "max_cursor": str(max_cursor),
                "cursor": "0",
                "sec_user_id": secUid,
                "user_id": str(user_id),
                "count": "100",
                "filter_private": "1",
                "lite_flow_schedule": "new",
                "cdn_cache_is_login": "1",
                "cdn_cache_strategy": "v0",
                "data_saver_type": "1",
                "data_saver_work": "false",
                "page_type": "1",
                "manifest_version_code": "400451",
                "_rticket": str(int(time.time() * 1000)),
                "app_language": "en",
                "app_type": "normal",
                "iid": "7549676125857842951",
                "app_package": "com.tiktok.lite.gp",
                "channel": "googleplay",
                "device_type": "SO-51A",
                "language": "en",
                "host_abi": "arm64-v8a",
                "locale": "en",
                "resolution": "1096*2434",
                "openudid": "78c721f9cc941eba",
                "update_version_code": "400451",
                "ac2": "wifi",
                "cdid": "856f0b03-c02f-456a-b37a-e8a5508cac06",
                "sys_region": "IQ",
                "os_api": "31",
                "timezone_name": "Asia/Baghdad",
                "dpi": "420",
                "carrier_region": "IQ",
                "ac": "wifi",
                "device_id": "7356755889536468481",
                "os": "android",
                "os_version": "12",
                "timezone_offset": "10800",
                "version_code": "400451",
                "app_name": "musically_go",
                "ab_version": "40.4.51",
                "version_name": "40.4.51",
                "device_brand": "docomo",
                "op_region": "IQ",
                "ssmix": "a",
                "device_platform": "android",
                "build_number": "40.4.51",
                "region": "IQ",
                "aid": "1340",
                "ts": str(int(time.time()))
            }

            headers = self.get_headers()
            headers.update(SignerPy.sign(params=params, aid=1340))
            al = urlencode(params)
            url = f"{_url}?{al}"
            
            response = requests.get(url, headers=headers, timeout=10)
            
            if response.status_code != 200:
                print_color(f"❌ خطأ في الاستجابة: {response.status_code}", Colors.RED)
                return {'aweme_ids': [], 'has_more': False, 'next_cursor': 0}
            
            return self.parse_response(response.json())
            
        except Exception as e:
            print_color(f"❌ خطأ في الطلب: {str(e)}", Colors.RED)
            return {'aweme_ids': [], 'has_more': False, 'next_cursor': 0}
    
    def parse_response(self, data):
  
        aweme_ids = []
        
        try:
            if "aweme_list" in data and data["aweme_list"]:
                for aweme in data["aweme_list"]:
                    aweme_id = aweme.get("aweme_id")
                    if aweme_id and aweme_id not in self.all_aweme_ids:
                        aweme_ids.append(aweme_id)
                        self.all_aweme_ids.add(aweme_id)
                
                has_more = data.get("has_more", False)
                next_cursor = data.get("max_cursor", 0)
                
                return {
                    'aweme_ids': aweme_ids,
                    'has_more': has_more,
                    'next_cursor': next_cursor
                }
            else:
                return {'aweme_ids': [], 'has_more': False, 'next_cursor': 0}
                
        except Exception as e:
            print_color(f"❌ خطأ في تحليل البيانات: {str(e)}", Colors.RED)
            return {'aweme_ids': [], 'has_more': False, 'next_cursor': 0}
    
    def harvest_private_videos(self, total_requests=100):
     
        print_color(f"🚀 بدء استخراج الفيديوهات الخاصة - الهدف: {total_requests} طلب", Colors.CYAN)
        
        cursor = 0
        requests_made = 0
        all_video_ids = []
        
        while requests_made < total_requests:
            print_color(f"\n📡 جارٍ تحميل الدُفعة {requests_made + 1}", Colors.BLUE)
            
            result = self.get_private_videos_list(cursor)
            
            if result['aweme_ids']:
                for video_id in result['aweme_ids']:
                    print(f"{Colors.GREEN}{video_id}{Colors.END}")
                    all_video_ids.append(video_id)
                print_color(f"🎯 تم استخراج {len(result['aweme_ids'])} فيديو جديد", Colors.GREEN)
            
            if result['has_more']:
                cursor = result['next_cursor']
            else:
                print_color("🔚 لا توجد فيديوهات أخرى", Colors.YELLOW)
                break
            
            requests_made += 1
            
            delay = random.uniform(1, 2)
            print_color(f"⏳ جارٍ الانتظار {delay:.1f} ثانية...", Colors.YELLOW)
            time.sleep(delay)
        
        print_color(f"\n🎉 اكتمل الاستخراج!", Colors.GREEN)
        print_color(f"📊 إجمالي الفيديوهات المجمعة: {len(all_video_ids)}", Colors.CYAN)
        print_color(f"🔢 عدد الطلبات المكتملة: {requests_made}", Colors.CYAN)
        
      
        if all_video_ids:
            self.save_to_file(all_video_ids, "private_videos.txt")
        
        return all_video_ids
    
    def harvest_public_videos(self, username, total_requests=100):
      
        print_color(f"🚀 بدء استخراج الفيديوهات العامة لـ @{username} - الهدف: {total_requests} طلب", Colors.CYAN)
        
        cursor = 0
        requests_made = 0
        all_video_ids = []
        
        while requests_made < total_requests:
            print_color(f"\n📡 جارٍ تحميل الدُفعة {requests_made + 1}", Colors.BLUE)
            
            result = self.get_public_videos_list(username, cursor)
            
            if result['aweme_ids']:
                for video_id in result['aweme_ids']:
                    print(f"{Colors.GREEN}{video_id}{Colors.END}")
                    all_video_ids.append(video_id)
                print_color(f"🎯 تم استخراج {len(result['aweme_ids'])} فيديو جديد", Colors.GREEN)
            
            if result['has_more']:
                cursor = result['next_cursor']
            else:
                print_color("🔚 لا توجد فيديوهات أخرى", Colors.YELLOW)
                break
            
            requests_made += 1
            
            delay = random.uniform(1, 2)
            print_color(f"⏳ جارٍ الانتظار {delay:.1f} ثانية...", Colors.YELLOW)
            time.sleep(delay)
        
        print_color(f"\n🎉 اكتمل الاستخراج!", Colors.GREEN)
        print_color(f"📊 إجمالي الفيديوهات المجمعة: {len(all_video_ids)}", Colors.CYAN)
        print_color(f"🔢 عدد الطلبات المكتملة: {requests_made}", Colors.CYAN)
        
     
        if all_video_ids:
            self.save_to_file(all_video_ids, f"public_videos_{username}.txt")
        
        return all_video_ids
    
    def modify_video_privacy(self, video_id, privacy_type):
   
        try:
            modify_url = f"https://api16-normal-c-alisg.tiktokv.com/aweme/v1/aweme/modify/visibility/?aweme_id={video_id}&type={privacy_type}&request_tag_from=h5&manifest_version_code=410203&_rticket=1762590577695&app_language=ar&app_type=normal&iid=7570139761176839937&app_package=com.zhiliaoapp.musically.go&channel=googleplay&device_type=RMX3834&language=ar&host_abi=arm64-v8a&locale=ar&resolution=720*1454&openudid=b57299cf6a5bb211&update_version_code=410203&ac2=wifi&cdid=566bdea1-9b82-4846-af74-29d2e1b9a1a9&sys_region=EG&os_api=34&timezone_name=Asia%2FBaghdad&dpi=272&carrier_region=IQ&ac=wifi&device_id=7456376313159714309&os=android&os_version=14&timezone_offset=10800&version_code=410203&app_name=musically_go&ab_version=41.2.3&version_name=41.2.3&device_brand=realme&op_region=IQ&ssmix=a&device_platform=android&build_number=41.2.3&region=EG&aid=1340&ts=1762590563"

            headers = self.get_headers()
            
            signature = SignerPy.sign(params=modify_url, version=8404)
            headers.update({
                'x-ss-stub': signature['x-ss-stub'],
                'x-gorgon': signature["x-gorgon"],
                'x-khronos': signature["x-khronos"],
                'x-ladon': signature["x-ladon"],
                'x-argus': signature['x-argus'],
            })
            
            response = requests.post(modify_url, headers=headers, timeout=10)
            if response.status_code == 200:
                response_data = response.json()
                if response_data.get('status_code') == 0:
                    return True
                else:
                    print_color(f"❌ خطأ في تغيير الخصوصية للفيديو {video_id}: {response_data.get('message', 'خطأ غير معروف')}", Colors.RED)
                    return False
            else:
                print_color(f"❌ خطأ HTTP {response.status_code} للفيديو {video_id}", Colors.RED)
                return False
                
        except Exception as e:
            print_color(f"❌ استثناء أثناء تغيير الخصوصية للفيديو {video_id}: {str(e)}", Colors.RED)
            return False
    
    def change_videos_privacy(self, video_ids, target_privacy, max_workers=10):
  
        print_color(f"🚀 بدء تغيير خصوصية {len(video_ids)} فيديو...", Colors.CYAN)
        
        success_count = 0
        failed_videos = []
        
        def process_single_video(video_id):
            nonlocal success_count
            try:
                if self.modify_video_privacy(video_id, target_privacy):
                    success_count += 1
                    print_color(f"✅ تم تغيير الفيديو {video_id} ({success_count}/{len(video_ids)})", Colors.GREEN)
                    return True
                else:
                    failed_videos.append(video_id)
                    return False
            except Exception as e:
                failed_videos.append(video_id)
                return False
        
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(process_single_video, vid): vid for vid in video_ids}
            
            for future in as_completed(futures):
                future.result()
        
        print_color(f"\n🎉 اكتملت العملية!", Colors.GREEN)
        print_color(f"📊 النتائج:", Colors.CYAN)
        print_color(f"   • النجاح: {success_count}", Colors.GREEN)
        print_color(f"   • الفشل: {len(failed_videos)}", Colors.RED if failed_videos else Colors.GREEN)
        
        if failed_videos:
            print_color(f"\n📋 قائمة الفيديوهات الفاشلة ({len(failed_videos)}):", Colors.YELLOW)
            for vid in failed_videos[:10]:  
                print_color(f"   - {vid}", Colors.YELLOW)
            if len(failed_videos) > 10:
                print_color(f"   ... و {len(failed_videos) - 10} فيديو آخر", Colors.YELLOW)
            
            self.save_to_file(failed_videos, "failed_videos.txt")
        
        return success_count, failed_videos
    
    def save_to_file(self, video_ids, filename):
     
        try:
            with open(filename, "w", encoding="utf-8") as f:
                for vid in video_ids:
                    f.write(f"{vid}\n")
            print_color(f"💾 تم حفظ {len(video_ids)} معرف فيديو في {filename}", Colors.GREEN)
        except Exception as e:
            print_color(f"❌ خطأ في حفظ الملف: {str(e)}", Colors.RED)
    
    def private_to_public(self, total_requests=130):
     
        print_color("🔄 بدء تحويل الفيديوهات الخاصة إلى عامة...", Colors.CYAN)
        
       
        video_ids = self.harvest_private_videos(total_requests)
        
        if not video_ids:
            print_color("❌ لم يتم العثور على فيديوهات خاصة", Colors.RED)
            return
        
        print_color(f"\n🚀 بدء تحويل {len(video_ids)} فيديو إلى عام...", Colors.CYAN)
        
     
        success_count, failed_videos = self.change_videos_privacy(video_ids, 1)
        
        print_color(f"\n✅ اكتمل تحويل الفيديوهات الخاصة إلى عامة!", Colors.GREEN)
        print_color(f"📊 الإجمالي: {len(video_ids)} فيديو", Colors.CYAN)
        print_color(f"✅ الناجحة: {success_count}", Colors.GREEN)
        print_color(f"❌ الفاشلة: {len(failed_videos)}", Colors.RED if failed_videos else Colors.GREEN)
    
    def public_to_private(self, username, total_requests=130):
    
        print_color(f"🔄 بدء تحويل فيديوهات @{username} العامة إلى خاصة...", Colors.CYAN)
        
     
        video_ids = self.harvest_public_videos(username, total_requests)
        
        if not video_ids:
            print_color("❌ لم يتم العثور على فيديوهات عامة", Colors.RED)
            return
        
        print_color(f"\n🚀 بدء تحويل {len(video_ids)} فيديو إلى خاص...", Colors.CYAN)
        
    
        success_count, failed_videos = self.change_videos_privacy(video_ids, 2)
        
        print_color(f"\n✅ اكتمل تحويل فيديوهات @{username} العامة إلى خاصة!", Colors.GREEN)
        print_color(f"📊 الإجمالي: {len(video_ids)} فيديو", Colors.CYAN)
        print_color(f"✅ الناجحة: {success_count}", Colors.GREEN)
        print_color(f"❌ الفاشلة: {len(failed_videos)}", Colors.RED if failed_videos else Colors.GREEN)

def get_session_from_user():
    
    print_color("\n" + "="*50, Colors.CYAN)
    print_color("🎯 TikTok Video Privacy Manager", Colors.GREEN)
    print_color("="*50, Colors.CYAN)
    
    print_color("\n🔑 أدخل sessionid الخاص بـ TikTok:", Colors.YELLOW)
    print_color("(يمكنك الحصول عليه من cookies المتصفح)", Colors.BLUE)
    
    sessionid = input("sessionid: ").strip()
    
    if len(sessionid) < 10:
        print_color("❌ sessionid غير صالح!", Colors.RED)
        return None
    
    return sessionid

def show_menu():
  
    print_color("\n" + "="*50, Colors.CYAN)
    print_color("📋 القائمة الرئيسية", Colors.GREEN)
    print_color("="*50, Colors.CYAN)
    
    print_color("\n1. 📤 تحويل الفيديوهات الخاصة إلى عامة", Colors.BLUE)
    print_color("2. 📥 تحويل الفيديوهات العامة إلى خاصة", Colors.BLUE)
    #print_color("3. 🔍 استخراج الفيديوهات الخاصة فقط", Colors.BLUE)
#    print_color("4. 🔍 استخراج الفيديوهات العامة فقط", Colors.BLUE)
#    print_color("5. 🚪 الخروج", Colors.RED)
#    
    choice = input("\n🔢 اختر رقم الخيار: ").strip()
    return choice

def main():
 # @Q_b_h tele
    sessionid = get_session_from_user()
    if not sessionid:
        return
    
    
    manager = TikTokVideoManager(sessionid)
    
    while True:
        choice = show_menu()
        
        if choice == "1":
         
            try:
                total_requests = int(input("🎯 أدخل عدد الطلبات (افتراضي 130): ").strip() or "130")
                manager.private_to_public(total_requests)
            except ValueError:
                print_color("❌ الرقم غير صالح!", Colors.RED)
        
        elif choice == "2":
 
            username = input("👤 أدخل اسم المستخدم (بدون @): ").strip()
            if username:
                try:
                    total_requests = int(input("🎯 أدخل عدد الطلبات (افتراضي 130): ").strip() or "130")
                    manager.public_to_private(username, total_requests)
                except ValueError:
                    print_color("❌ الرقم غير صالح!", Colors.RED)
            else:
                print_color("❌ اسم المستخدم غير صالح!", Colors.RED)
        
        elif choice == "3":
          
            try:
                total_requests = int(input("🎯 أدخل عدد الطلبات (افتراضي 100): ").strip() or "100")
                manager.harvest_private_videos(total_requests)
            except ValueError:
                print_color("❌ الرقم غير صالح!", Colors.RED)
        
        elif choice == "4":
          
            username = input("👤 أدخل اسم المستخدم (بدون @): ").strip()
            if username:
                try:
                    total_requests = int(input("🎯 أدخل عدد الطلبات (افتراضي 100): ").strip() or "100")
                    manager.harvest_public_videos(username, total_requests)
                except ValueError:
                    print_color("❌ الرقم غير صالح!", Colors.RED)
            else:
                print_color("❌ اسم المستخدم غير صالح!", Colors.RED)
        
        elif choice == "5":
        
            print_color("👋 مع السلامة!", Colors.GREEN)
            break
        
        else:
            print_color("❌ خيار غير صالح!", Colors.RED)
        
     
        cont = input("\n🔁 هل تريد تنفيذ عملية أخرى؟ (y/n): ").strip().lower()
        if cont != 'y':
            print_color("👋 مع السلامة!", Colors.GREEN)
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_color("\n\n⏹️ تم إيقاف البرنامج من قبل المستخدم", Colors.YELLOW)
    except Exception as e:
        print_color(f"\n❌ خطأ غير متوقع: {str(e)}", Colors.RED)