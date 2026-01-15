import requests, threading, random, time, secrets, os, uuid, telebot, re, json, datetime
from urllib.parse import urlencode
import SignerPy
from concurrent.futures import ThreadPoolExecutor, as_completed
# @ Q_b_h
spam = {}
user_languages = {}  

bot = telebot.TeleBot(input("token:"))
# @ Q_b_h
TEXTS = {
    'ar': {
        'start': """
        - هلا بالغالي في <b>بوت فحص حسابات تيك توك</b>
        اكتب /check + يوزر الحساب عبالك!

        <b>هلا فيك يزم، اكتب /check ويا يوزر الحساب عبالك عشان تفحص الروابط والباسكاي بتاعة تيك توك</b>
        """,
        'processing': "🔄 شغال افحص الحساب...",
        'spam_warning': "لا تكرر الطلب !! 🤬",
        'no_username': "اكتب اليوزر بعد الأمر /check يزم",
        'account_info': "الحساب • @{username}\n\n🔐 {hidden_binding}\n🌐 {external_binding}\n\nالجوال ({phone}) - الإيميل ({email})",
        'hidden_binding_yes': "فيه روابط مخفية بالحساب ⚠️",
        'hidden_binding_no': "ماكو روابط مخفية بالحساب 🟢",
        'external_binding_yes': "فيه روابط برى ({platforms}) 🔴",
        'external_binding_no': "ماكو روابط برى بالحساب 🟢",
        'captcha_error': "خطأ CAPTCHA (شغل VPN او جرب بعد شوي!)",
        'user_not_found': "غلط باليوزر: {username} (ماكو هالك يوزر!)",
        'all_hosts_failed': "خطأ: كل السيرفرات طاحت مع يوزر {username}",
        'unknown_error': "غلط باليوزر: {username} (صار خطأ ماكو داعي!)",
        'lang_changed': "✅ غيرنا اللغة للعراقي",
        'choose_lang': "🌐 اختر لغتك:",
        'current_lang': "اللغة الحالية: عراقي"
    },
    'en': {
        'start': """
        - Welcome to <b>TikTok Account Links Display Bot</b>
        Send /check + username to check!

        <b>Welcome to my bot, send /check followed by your username to check TikTok links and passkey</b>
        """,
        'processing': "🔄 Checking account...",
        'spam_warning': "Don't repeat !! 🤬",
        'no_username': "Please enter username after /check command",
        'account_info': "Account • @{username}\n\n🔐 {hidden_binding}\n🌐 {external_binding}\n\nPhone ({phone}) - Email ({email})",
        'hidden_binding_yes': "Has hidden links in account ⚠️",
        'hidden_binding_no': "No hidden links in account 🟢",
        'external_binding_yes': "Has external links ({platforms}) 🔴",
        'external_binding_no': "No external links in account 🟢",
        'captcha_error': "CAPTCHA error (Please enable VPN or try again later!)",
        'user_not_found': "Username error: {username} (Username doesn't exist!)",
        'all_hosts_failed': "Error: All servers failed for user {username}",
        'unknown_error': "Username error: {username} (Unknown error occurred!)",
        'lang_changed': "✅ Language changed to English",
        'choose_lang': "🌐 Choose your language:",
        'current_lang': "Current language: English"
    }
}

def get_user_language(chat_id):
    return user_languages.get(chat_id, 'ar')

def get_text(chat_id, text_key, **kwargs):
    lang = get_user_language(chat_id)
    text = TEXTS[lang].get(text_key, text_key)
    return text.format(**kwargs) if kwargs else text

class TikTokAPI:
    HOSTS = [
        "api16-normal-c-alisg.tiktokv.com",
        "api.tiktokv.com",
        "api-h2.tiktokv.com",
        "api-va.tiktokv.com",
        "api16.tiktokv.com",
        "api16-va.tiktokv.com",
        "api19.tiktokv.com",
        "api19-va.tiktokv.com",
        "api21.tiktokv.com",
        "api15-h2.tiktokv.com",
        "api21-h2.tiktokv.com",
        "api21-va.tiktokv.com",
        "api22.tiktokv.com",
        "api22-va.tiktokv.com",
        "api-t.tiktok.com",
        "api16-normal-baseline.tiktokv.com",
        "api23-normal-zr.tiktokv.com",
        "api21-normal.tiktokv.com",
        "api22-normal-zr.tiktokv.com",
        "api33-normal.tiktokv.com",
        "api22-normal.tiktokv.com",
        "api31-normal.tiktokv.com",
        "api15-normal.tiktokv.com",
        "api31-normal-cost-sg.tiktokv.com",
        "api3-normal.tiktokv.com",
        "api31-normal-zr.tiktokv.com",
        "api9-normal.tiktokv.com",
        "api16-normal.tiktokv.com",
        "api16-normal.ttapis.com",
        "api19-normal-zr.tiktokv.com",
        "api16-normal-zr.tiktokv.com",
        "api16-normal-apix.tiktokv.com",
        "api74-normal.tiktokv.com",
        "api32-normal-zr.tiktokv.com",
        "api23-normal.tiktokv.com",
        "api32-normal.tiktokv.com",
        "api16-normal-quic.tiktokv.com",
        "api-normal.tiktokv.com",
        "api16-normal-apix-quic.tiktokv.com",
        "api19-normal.tiktokv.com",
        "api31-normal-cost-mys.tiktokv.com",
        "im-va.tiktokv.com",
        "imapi-16.tiktokv.com",
        "imapi-16.musical.ly",
        "imapi-mu.isnssdk.com",
        "api.tiktok.com",
        "api.ttapis.com",
        "api.tiktokv.us",
        "api.tiktokv.eu",
        "api.tiktokw.us",
        "api.tiktokw.eu"
    ]

    @staticmethod
    def send_single_request(host, username, attempt_num):
        try:
            secret = secrets.token_hex(16)
            cookies = {
                "passport_csrf_token": secret,
                "passport_csrf_token_default": secret
            }

            params_step1 = {
                'request_tag_from': "h5",
                'manifest_version_code': "410203",
                '_rticket': str(int(time.time() * 1000)),
                'app_language': "ar",
                'app_type': "normal",
                'iid': str(random.randint(1, 10**19)),
                'app_package': "com.zhiliaoapp.musically.go",
                'channel': "googleplay",
                'device_type': "RMX3834",
                'language': "ar",
                'host_abi': "arm64-v8a",
                'locale': "ar",
                'resolution': "720*1454",
                'openudid': "b57299cf6a5bb211",
                'update_version_code': "410203",
                'ac2': "lte",
                'cdid': str(uuid.uuid4()),
                'sys_region': "EG",
                'os_api': "34",
                'timezone_name': "Asia/Baghdad",
                'dpi': "272",
                'carrier_region': "IQ",
                'ac': "4g",
                'device_id': str(random.randint(1, 10**19)),
                'os': "android",
                'os_version': "14",
                'timezone_offset': "10800",
                'version_code': "410203",
                'app_name': "musically_go",
                'ab_version': "41.2.3",
                'version_name': "41.2.3",
                'device_brand': "realme",
                'op_region': "IQ",
                'ssmix': "a",
                'device_platform': "android",
                'build_number': "41.2.3",
                'region': "EG",
                'aid': "1340",
                'ts': str(int(time.time())),
                'okhttp_version': "4.1.103.107-ul",
                'use_store_region_cookie': "1"
            }
            
            url_step1 = f"https://{host}/passport/find_account/tiktok_username/?" + urlencode(params_step1)
            
            payload_step1 = {
                'mix_mode': "1",
                'username': username,
            }

            signature = SignerPy.sign(params=url_step1, payload=payload_step1, version=4404)
            
            headers_step1 = {
                'User-Agent': "com.zhiliaoapp.musically.go/410203 (Linux; U; Android 14; ar; RMX3834; Build/UP1A.231005.007;tt-ok/3.12.13.44.lite-ul)",
                'x-ss-req-ticket': signature['x-ss-req-ticket'],
                'x-ss-stub': signature['x-ss-stub'],
                'x-gorgon': signature["x-gorgon"],
                'x-khronos': signature["x-khronos"],
                'x-tt-passport-csrf-token': cookies['passport_csrf_token'],
                'passport_csrf_token': cookies['passport_csrf_token'],
                'content-type': "application/x-www-form-urlencoded",
                'x-ss-dp': "1340",
                'sdk-version': "2",
                'x-tt-ultra-lite': "1",
                'x-vc-bdturing-sdk-version': "2.3.15.i18n",
                'ttzip-tlb': "1",
            }

            response_step1 = requests.post(
                url_step1,
                data=payload_step1,
                headers=headers_step1,
                cookies=cookies,
                timeout=15
            )
            
            response_json_step1 = response_step1.json()
            print(f"🔧 المحاولة {attempt_num} - السيرفر {host}: {response_step1.status_code}")

            if "token" in response_json_step1.get("data", {}):
                token = response_json_step1["data"]["token"]
                
                params_step2 = params_step1.copy()
                params_step2['not_login_ticket'] = token
                params_step2['ts'] = str(int(time.time()))
                params_step2['_rticket'] = str(int(time.time() * 1000))

                url_step2 = f"https://{host}/passport/auth/available_ways/?" + urlencode(params_step2)

                signature_step2 = SignerPy.sign(params=url_step2, payload=None, version=4404)
                
                headers_step2 = {
                    'User-Agent': "com.zhiliaoapp.musically.go/410203 (Linux; U; Android 14; ar; RMX3834; Build/UP1A.231005.007;tt-ok/3.12.13.44.lite-ul)",
                    'x-ss-req-ticket': signature_step2['x-ss-req-ticket'],
                    'x-ss-stub': signature_step2['x-ss-stub'],
                    'x-gorgon': signature_step2["x-gorgon"],
                    'x-khronos': signature_step2["x-khronos"],
                    'x-tt-passport-csrf-token': cookies['passport_csrf_token'],
                    'passport_csrf_token': cookies['passport_csrf_token'],
                    'content-type': "application/x-www-form-urlencoded",
                    'x-ss-dp': "1340",
                    'sdk-version': "2",
                    'x-tt-ultra-lite': "1",
                }

                res_step2 = requests.post(
                    url_step2,
                    headers=headers_step2,
                    cookies=cookies,
                    timeout=15
                )
                
                response_json_step2 = res_step2.json()
                print(f"✅ نجح مع السيرفر: {host}")

                if 'success' in response_json_step2.get("message", ""):
                    data = response_json_step2.get('data', {})
                    
                    has_email = data.get('has_email', False)
                    has_mobile = data.get('has_mobile', False)
                    has_oauth = data.get('has_oauth', False)
                    has_passkey = data.get('has_passkey', False)
                    oauth_platforms = data.get('oauth_platforms', [])

                    return {
                        'data': {
                            'has_email': has_email,
                            'has_mobile': has_mobile,
                            'has_oauth': has_oauth,
                            'has_passkey': has_passkey,
                            'oauth_platforms': oauth_platforms
                        },
                        'message': 'success',
                        'host': host
                    }

            elif "verify_center_decision_conf" in response_step1.text:
                print(f"❌ CAPTCHA مع السيرفر: {host}")
                return {"message": "error", "status": "captcha", "host": host}
            else:
                print(f"❌ ماكو هالك يوزر مع السيرفر: {host}")
                return {"message": "error", "status": "user not found", "host": host}

        except Exception as e:
            print(f"❌ خطأ بالطلب مع السيرفر {host}: {str(e)}")
            return {"message": "error", "status": "request_failed", "host": host, "error": str(e)}
        
        return {"message": "error", "status": "unknown", "host": host}

    @staticmethod
    def send_with_threading(username, max_workers=10):
        print(f"🚀 بادري فحص {max_workers} ثريد لـ {len(TikTokAPI.HOSTS)} سيرفر")
        
        successful_responses = []
        failed_hosts = []
        
        def worker(host):
            result = TikTokAPI.send_single_request(host, username, 1)
            if result.get('message') == 'success':
                successful_responses.append(result)
            else:
                failed_hosts.append({'host': host, 'status': result.get('status', 'unknown')})
            return result

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(worker, host): host for host in TikTokAPI.HOSTS}
            
            for future in as_completed(futures):
                host = futures[future]
                try:
                    future.result()
                except Exception as e:
                    print(f"❌ خطأ بالثريد للسيرفر {host}: {e}")
                    failed_hosts.append({'host': host, 'status': 'thread_error'})

        if successful_responses:
            print(f"✅ نجح مع {len(successful_responses)} سيرفر من {len(TikTokAPI.HOSTS)}")
            return successful_responses[0]
        else:
            print(f"❌ طاحت كل السيرفرات ({len(failed_hosts)} فشل)")
            return {"message": "error", "status": "all hosts failed", "failed_count": len(failed_hosts)}

def process_account_data(response_data, username, chat_id):
    try:
        data = response_data.get('data', {})
        
        has_email = data.get('has_email', False)
        has_mobile = data.get('has_mobile', False)
        has_passkey = data.get('has_passkey', False)
        oauth_platforms = data.get('oauth_platforms', [])
        
        if not isinstance(oauth_platforms, list):
            oauth_platforms = []
        
        hidden_binding = get_text(chat_id, 'hidden_binding_yes') if has_passkey else get_text(chat_id, 'hidden_binding_no')
        
        if oauth_platforms:
            platforms_text = ', '.join([str(p) for p in oauth_platforms])
            external_binding = get_text(chat_id, 'external_binding_yes', platforms=platforms_text)
        else:
            external_binding = get_text(chat_id, 'external_binding_no')
        
        phone_status = "✔️" if has_mobile else "❌"
        email_status = "✔️" if has_email else "❌"
        
        message_text = get_text(chat_id, 'account_info', 
                              username=username,
                              hidden_binding=hidden_binding,
                              external_binding=external_binding,
                              phone=phone_status, 
                              email=email_status)
        
        if response_data.get('host'):
            message_text += " good"
        
        return message_text
        
    except Exception as e:
        error_message = f"Account • @{username}\n\nغلط بمعالجة البيانات: {str(e)}"
        return error_message

@bot.message_handler(commands=["start"])
def start(message):
    from telebot.types import InlineKeyboardMarkup as mk
    from telebot.types import InlineKeyboardButton as bt
    
    chat_id = message.chat.id
    
    ew = bt("القناة", url="https://t.me/q_b_h")
    lang_btn = bt("🌐 اللغة", callback_data="change_lang")
    
    n = mk(row_width=2)
    n.add(ew, lang_btn)
    
    bot.send_message(
        chat_id,
        text=get_text(chat_id, 'start'),
        parse_mode="HTML",
        reply_markup=n
    )

@bot.message_handler(commands=["check"])
def check(message):
    T = time.time()
    chat_id = message.chat.id
    
    if chat_id in spam:
        sp, sm = spam[chat_id]
        if T - sp <= 1:  
            if sm >= 1:
                bot.reply_to(message, get_text(chat_id, 'spam_warning'))
                return
            spam[chat_id] = (T, sm + 1)
        else:
            spam[chat_id] = (T, 1)
    else:
        spam[chat_id] = (T, 1)
    
    m = message.text.split(maxsplit=1)
    if len(m) > 1:
        username = m[1].lstrip('@')
        try:
            processing_msg = bot.reply_to(message, get_text(chat_id, 'processing'))
            
            response_data = TikTokAPI.send_with_threading(username, max_workers=15)

            if response_data and response_data.get('message') == 'success':
                message_text = process_account_data(response_data, username, chat_id)
                
                bot.delete_message(chat_id, processing_msg.message_id)
                bot.reply_to(message, message_text)
            else:
                bot.delete_message(chat_id, processing_msg.message_id)
                
                status = response_data.get('status', 'unknown')
                if status == "captcha":
                    bot.reply_to(message, get_text(chat_id, 'captcha_error'))
                elif status == "user not found":
                    bot.reply_to(message, get_text(chat_id, 'user_not_found', username=username))
                elif status == "all hosts failed":
                    bot.reply_to(message, get_text(chat_id, 'all_hosts_failed', username=username))
                else:
                    bot.reply_to(message, get_text(chat_id, 'unknown_error', username=username))
        except Exception as e:
            try:
                if 'processing_msg' in locals():
                    bot.delete_message(chat_id, processing_msg.message_id)
            except:
                pass
            bot.reply_to(message, f"غلط باليوزر! {str(e)}")
    else:
        bot.reply_to(message, get_text(chat_id, 'no_username'))

@bot.message_handler(commands=["lang"])
def change_language(message):
    chat_id = message.chat.id
    from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
    
    keyboard = InlineKeyboardMarkup(row_width=2)
    
    languages = [
        ('🇸🇦 عراقي', 'ar'),
        ('🇺🇸 English', 'en')
    ]
    
    buttons = []
    for lang_name, lang_code in languages:
        buttons.append(InlineKeyboardButton(lang_name, callback_data=f"setlang_{lang_code}"))
    
    for i in range(0, len(buttons), 2):
        if i + 1 < len(buttons):
            keyboard.add(buttons[i], buttons[i + 1])
        else:
            keyboard.add(buttons[i])
    
    bot.send_message(chat_id, get_text(chat_id, 'choose_lang'), reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def handle_callbacks(call):
    chat_id = call.message.chat.id
    message_id = call.message.message_id
    
    if call.data == "change_lang":
        from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
        
        keyboard = InlineKeyboardMarkup(row_width=2)
        languages = [
            ('🇸🇦 عراقي', 'ar'),
            ('🇺🇸 English', 'en')
        ]
        
        buttons = []
        for lang_name, lang_code in languages:
            buttons.append(InlineKeyboardButton(lang_name, callback_data=f"setlang_{lang_code}"))
        
        for i in range(0, len(buttons), 2):
            if i + 1 < len(buttons):
                keyboard.add(buttons[i], buttons[i + 1])
            else:
                keyboard.add(buttons[i])
        
        try:
            bot.edit_message_text(
                get_text(chat_id, 'choose_lang'),
                chat_id,
                message_id,
                reply_markup=keyboard
            )
        except Exception as e:
            print(f"غلط بتعديل الرسالة: {e}")
            bot.send_message(chat_id, get_text(chat_id, 'choose_lang'), reply_markup=keyboard)
    
    elif call.data.startswith("setlang_"):
        lang_code = call.data.split("_")[1]
        user_languages[chat_id] = lang_code
        
        try:
            bot.edit_message_text(
                get_text(chat_id, 'lang_changed'),
                chat_id,
                message_id
            )
        except:
            pass
        
        bot.answer_callback_query(call.id, get_text(chat_id, 'lang_changed'))
        
        bot.send_message(chat_id, get_text(chat_id, 'lang_changed'))

def test_internet_connection(max_attempts=3):
    for attempt in range(max_attempts):
        try:
            print(f"🔍 جاري فحص اتصال الإنترنت {attempt + 1}/{max_attempts}")
            
            response = requests.get('http://httpbin.org/ip', timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                print(f"✅ الاتصال شغال - IP: {data.get('origin', 'ماكو')}")
                return True
            else:
                print(f"❌ استجابة مو زينة: {response.status_code}")
                
        except Exception as e:
            print(f"❌ خطأ باتصال الإنترنت بالمحاولة {attempt + 1}: {type(e).__name__}")
        
        if attempt < max_attempts - 1:
            time.sleep(2)
    
    print("❌ طاحت كل محاولات فحص الإنترنت")
    return False

def start_bot():
    print("🚀 بادري البوت...")
    print(f"📡 عدد السيرفرات المتاحة: {len(TikTokAPI.HOSTS)}")
    while True:
        try:
            bot.infinity_polling(none_stop=True, timeout=60)
        except Exception as e:
            print(f"❌ خطأ بالبوت: {e}")
            print("🔄 جاري إعادة المحاولة بعد 10 ثواني...")
            time.sleep(10)

if __name__ == "__main__":
    print("🔍 جاري فحص اتصال الإنترنت...")
    
    internet_works = test_internet_connection()
    
    if not internet_works:
        print("⚠️ تحذير: الإنترنت مو شغال، لكن راح اكمل...")
    
    start_bot()