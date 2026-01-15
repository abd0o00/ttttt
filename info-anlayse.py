import requests
import json
import re
import datetime
from user_agent import generate_user_agent as gen
from SignerPy import sign, get
import pycountry
import telebot
from telebot.types import InputMediaPhoto
import logging
import html

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

bot = telebot.TeleBot(input(" التوكن: "))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = """
السلام! 👋

انا بوت تيك توك. ابعثلي يوزر تيك توك (مع @ او بدونه) وابعتلك كل المعلومات عنه.

📝 **كيف تستهدم:**
ابعث يوزر تيك توك زي:
- `username`
- `@username`

مثال: `bmw` او `@bmw`

ابعتلك:
• المعلومات الأساسية
• الإحصائيات
• نسبة التفاعل
• وأكثر!
    """
    bot.reply_to(message, welcome_text)

@bot.message_handler(func=lambda message: True)
def handle_username(telegram_message):
    username = telegram_message.text.strip().lstrip('@')
    
    if not username:
        bot.reply_to(telegram_message, "لازم تبعث يوزر تيك توك!")
        return
    
    wait_msg = bot.reply_to(telegram_message, f"🔄 جاري تجميع المعلومات ل @{username}...")
    
    url = f"https://www.tiktok.com/@{username}"
    headers = {'User-Agent': gen()}
    
    response = requests.get(url, headers=headers)
    match = re.search(r'({"__DEFAULT_SCOPE__":.*})</script>', response.text)
    
    if not match:
        bot.edit_message_text(chat_id=telegram_message.chat.id, message_id=wait_msg.message_id, text="❌ غلط: ما حصلت اشي على اليوزر")
        return
    
    data = json.loads(match.group(1))
    user_data = data["__DEFAULT_SCOPE__"]["webapp.user-detail"]["userInfo"]
    user = user_data["user"]
    stats = user_data["stats"]
    stats_v2 = user_data.get("statsV2", {})
    
    user_id = user.get('id', '')
    name = user.get('nickname', '')
    unique_id = user.get('uniqueId', '')
    bio = user.get('signature', '')
    country = user.get('region', '')
    verified = user.get('verified', False)
    private = user.get('privateAccount', False)
    secid = user.get('secUid', '')
    create_time = user.get('createTime', '')
    
    followers = stats_v2.get('followerCount', stats.get('followerCount', ''))
    following = stats_v2.get('followingCount', stats.get('followingCount', ''))
    likes = stats_v2.get('heartCount', stats.get('heartCount', ''))
    videos = stats_v2.get('videoCount', stats.get('videoCount', ''))
    digg_count = stats_v2.get('diggCount', stats.get('diggCount', ''))
    friend_count = stats_v2.get('friendCount', stats.get('friendCount', ''))
    
    avatar_larger = user.get('avatarLarger', '')
    
    bio_link = user.get('bioLink', {})
    bio_link_url = bio_link.get('link', '') if bio_link else ''
    
    commerce_user = user.get('commerceUserInfo', {}).get('commerceUser', False)
    is_organization = user.get('isOrganization', 0)
    language = user.get('language', '')
    
    comment_setting = user.get('commentSetting', 0)
    duet_setting = user.get('duetSetting', 0)
    stitch_setting = user.get('stitchSetting', 0)
    download_setting = user.get('downloadSetting', 0)
    
    if bio:
        bio = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', str(bio))
        bio = re.sub(r'\s+', ' ', bio)
        bio = bio.strip()
        if len(bio) > 500:
            bio = bio[:497] + "..."
    
    country_name = ""
    country_flag = ""
    if country:
        try:
            country_data = pycountry.countries.get(alpha_2=country)
            if country_data:
                country_name = getattr(country_data, 'name', '')
                country_flag = getattr(country_data, 'flag', '')
        except:
            pass
    
    created_date = ""
    if create_time:
        try:
            created_date = datetime.datetime.fromtimestamp(create_time).strftime("%Y-%m-%d %H:%M:%S")
        except:
            created_date = ""
    
    
    def clean_text(text):
        if not text:
            return ""
     
     
        cleaned = re.sub(r'[\x00-\x1f\x7f-\x9f]', '', str(text))
        cleaned = re.sub(r'\s+', ' ', cleaned)
        cleaned = cleaned.strip()
        
 
        escape_chars = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
        
        for char in escape_chars:
            cleaned = cleaned.replace(char, '\\' + char)
        
        return cleaned
    

    cleaned_name = clean_text(name)
    
    web_info = {
        "user_id": user_id,
        "name": cleaned_name,
        "username": unique_id,
        "bio": bio,
        "country": country,
        "country_name": country_name,
        "country_flag": country_flag,
        "verified": verified,
        "private": private,
        "commerce_user": commerce_user,
        "is_organization": is_organization,
        "language": language,
        "followers": followers,
        "following": following,
        "likes": likes,
        "videos": videos,
        "digg_count": digg_count,
        "friend_count": friend_count,
        "secid": secid,
        "created_date": created_date,
        "avatar_larger": avatar_larger,
        "bio_link": bio_link_url,
        "comment_setting": comment_setting,
        "duet_setting": duet_setting,
        "stitch_setting": stitch_setting,
        "download_setting": download_setting
    }
    
    url = "https://webcast22-normal-c-alisg.tiktokv.com/webcast/user/"
    
    headers = {
        "Host": "webcast22-normal-c-alisg.tiktokv.com",
        "cookie": "store-idc=alisg; passport_csrf_token=20e9da8b0e16abaa45d4ce2ad75a1325; passport_csrf_token_default=20e9da8b0e16abaa45d4ce2ad75a1325; d_ticket=913261767c3f16148c133796e661c1d83cf5d; multi_sids=7464926696447099909%3A686e699e8bbbc4e9f5e08d31c038c8e4; odin_tt=e2d5cd703c2e155d572ad323d28759943540088ddc6806aa9a9b48895713be4b585e78bf3eb17d28fd84247c4198ab58fab17488026468d3dde38335f4ab928ad1b9bd82a2fb5ff55da00e3368b4d215; cmpl_token=AgQQAPMsF-RPsLemUeAYPZ08_KeO5HxUv5IsYN75Vg; sid_guard=686e699e8bbbc4e9f5e08d31c038c8e4%7C1751310846%7C15552000%7CSat%2C+27-Dec-2025+19%3A14%3A06+GMT; uid_tt=683a0288ad058879bbc16d3b696fa815e1d72c050bdb2d14b824141806068417; uid_tt_ss=683a0288ad058879bbc16d3b696fa815e1d72c050bdb2d14b824141806068417; sid_tt=686e699e8bbbc4e9f5e08d31c038c8e4; sessionid=686e699e8bbbc4e9f5e08d31c038c8e4; sessionid_ss=686e699e8bbbc4e9f5e08d31c038c8e4; store-country-code=eg; store-country-code-src=uid; tt-target-idc=alisg; ttwid=1%7Cmdx9QyT3L35S3CFNpZ_6a1mG2Q3hbfWvwQh6gY5hjhw%7C1751310949%7C253ef523ddc8960c5f52b286d8ce0afc2623ec081a777dac3ba5606ecdc1bd40; store-country-sign=MEIEDPH3p6xlgJXYVovxBgQgMf22gnCf0op7iOSSy6oKKB7paF60OVLAsxbGkh6BUGAEEF0aMxzItZZ03IrkjedsuYY; msToken=Srtgt7p6ncYXI8gph0ecExfl9DpgLtzOynFNZjVGLkKUjqV0J1JI8aBoE8ERmO5f43HQhtJxcU2FeJweSbFIlIOADOHP_z75VvNeA2hp5LN1JZsKgj-wymAdEVJt",
        "x-tt-pba-enable": "1",
        "x-bd-kmsv": "0",
        "x-tt-dm-status": "login=1;ct=1;rt=1",
        "live-trace-tag": "profileDialog_batchRequest",
        "sdk-version": "2",
        "x-tt-token": "034865285659c6477b777dec3ab5cd0aa70363599c1acde0cd4e911a51fed831bdb2ec80a9a379e8e66493471e519ccf05287299287a55f0599a72988865752a3668a1a459177026096896cf8d50b6e8b5f4cec607bdcdee5a5ce407e70ce91d52933--0a4e0a20da4087f3b0e52a48822384ac63e937da36e5b0ca771f669a719cf633d66f8aed12206a38feb1f115b80781d5cead8068600b779eb2bba6c09d8ae1e6a7bc44b46b931801220674696b746f6b-3.0.0",
        "passport-sdk-version": "6031490",
        "x-vc-bdturing-sdk-version": "2.3.8.i18n",
        "x-tt-request-tag": "n=0;nr=011;bg=0",
        "x-tt-store-region": "eg",
        "x-tt-store-region-src": "uid",
        "rpc-persist-pyxis-policy-v-tnc": "1",
        "x-ss-dp": "1233",
        "x-tt-trace-id": "00-c24dca7d1066c617d7d3cb86105004d1-c24dca7d1066c617-01",
        "user-agent": "com.zhiliaoapp.musically/2023700010 (Linux; U; Android 11; vi; SM-A105F; Build/RP1A.200720.012; Cronet/TTNetVersion:f6248591 2024-09-11 QuicVersion:182d68c8 2024-05-28)",
        "accept-encoding": "gzip, deflate, br",
        "x-tt-dataflow-id": "671088640"
    }
    
    params = {
        "user_role": '{"7464926696447099909":1,"7486259459669820432":1}',
        "request_from": "profile_card_v2",
        "sec_anchor_id": "MS4wLjABAAAAiwBH59yM2i_loS11vwxZsudy4Bsv5L_EYIkYDmxgf-lv3oZL4YhQCF5oHQReiuUV",
        "request_from_scene": "1",
        "need_preload_room": "false",
        "target_uid": user_id,
        "anchor_id": "246047577136308224",
        "packed_level": "2",
        "need_block_status": "true",
        "current_room_id": "7521794357553400594",
        "device_platform": "android",
        "os": "android",
        "ssmix": "a",
        "_rticket": "1751311566864",
        "cdid": "808876f8-7328-4885-857d-8f15dd427861",
        "channel": "googleplay",
        "aid": "1233",
        "app_name": "musical_ly",
        "version_code": "370001",
        "version_name": "37.0.1",
        "manifest_version_code": "2023700010",
        "update_version_code": "2023700010",
        "ab_version": "37.0.1",
        "resolution": "720*1382",
        "dpi": "280",
        "device_type": "SM-A105F",
        "device_brand": "samsung",
        "language": "vi",
        "os_api": "30",
        "os_version": "11",
        "ac": "wifi",
        "is_pad": "0",
        "current_region": "VN",
        "app_type": "normal",
        "sys_region": "VN",
        "last_install_time": "1751308971",
        "timezone_name": "Asia/Baghdad",
        "residence": "VN",
        "app_language": "vi",
        "timezone_offset": "10800",
        "host_abi": "armeabi-v7a",
        "locale": "vi",
        "content_language": "vi,",
        "ac2": "wifi",
        "uoo": "1",
        "op_region": "VN",
        "build_number": "37.0.1",
        "region": "VN",
        "ts": "1751311566",
        "iid": "7521814657976928001",
        "device_id": "7405632852996097552",
        "openudid": "c79c40b21606bf59",
        "webcast_sdk_version": "3610",
        "webcast_language": "vi",
        "webcast_locale": "vi_VN",
        "es_version": "3",
        "effect_sdk_version": "17.6.0",
        "current_network_quality_info": '{"tcp_rtt":16,"quic_rtt":16,"http_rtt":584,"downstream_throughput_kbps":1400,"quic_send_loss_rate":-1,"quic_receive_loss_rate":-1,"net_effective_connection_type":3,"video_download_speed":1341}'
    }
    
    unsigned_params = get(params=params)
    
    cookies = {}
    for item in headers["cookie"].split(';'):
        if item.strip():
            try:
                key, value = item.strip().split('=', 1)
                cookies[key.strip()] = value.strip()
            except ValueError:
                cookies[item.strip()] = ''
    
    signature = sign(params=unsigned_params, cookie=cookies)
    
    headers.update({
        'x-ss-req-ticket': signature['x-ss-req-ticket'],
        'x-ss-stub': signature['x-ss-stub'],
        'x-argus': signature["x-argus"],
        'x-gorgon': signature["x-gorgon"],
        'x-khronos': signature["x-khronos"],
        'x-ladon': signature["x-ladon"],
    })
    
    headers["accept-encoding"] = "identity"
    response = requests.get(url, headers=headers, params=unsigned_params)
    
    try:
        data = response.json()
        if data.get('status_code') != 0:
            level = ""
        else:
            if 'data' in data and 'badge_list' in data['data']:
                badge_list = data['data']['badge_list']
                for badge in badge_list:
                    combine = badge.get('combine', {})
                    if combine and 'text' in combine:
                        text = combine.get('text', {})
                        if 'default_pattern' in text:
                            level = text['default_pattern']
                        else:
                            level = ""
                    else:
                        level = ""
            else:
                level = ""
    except json.JSONDecodeError:
        level = ""
    
    url = "https://influencers.club/wp-json/tools/v1/proxy/analyzer/"
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Mobile Safari/537.36",
        'Content-Type': "application/json",
        'sec-ch-ua-platform': "\"Android\"",
        'sec-ch-ua': "\"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"138\", \"Google Chrome\";v=\"138\"",
        'sec-ch-ua-mobile': "?1",
        'origin': "https://d2dve41rwvcssr.cloudfront.net",
        'sec-fetch-site': "cross-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://d2dve41rwvcssr.cloudfront.net/",
        'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
        'priority': "u=1, i"
    }
    
    payload = {"platform": "tiktok", "filter_key": "user", "filter_value": username}
    
    try:
        response = requests.post(url, data=json.dumps(payload), headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        tiktok_data = data.get("tiktok", {})
        
        analytics_data = {
            "avg_likes": tiktok_data.get("avg_likes"),
            "engagement_rate": tiktok_data.get("engagement_rate"),
            "avg_views": tiktok_data.get("avg_views"),
            "avg_comments": tiktok_data.get("avg_comments"),
            "median_engagement_percent": tiktok_data.get("median_engagement_percent"),
            "min_engagement_percent": tiktok_data.get("min_engagement_percent"),
            "max_engagement_percent": tiktok_data.get("max_engagement_percent"),
            "tiktok_hashtags": tiktok_data.get("tiktok_hashtags", []),
            "follower_range": tiktok_data.get("follower_range", []),
            "total_likes": tiktok_data.get("total_likes"),
            "number_of_posts": tiktok_data.get("number_of_posts"),
            "posts_per_month": tiktok_data.get("posts_per_month"),
            "creator_growth": tiktok_data.get("creator_growth"),
            "follower_growth_90_days": tiktok_data.get("follower_growth_90_days"),
            "tagged": tiktok_data.get("tagged", []),
            "brands": tiktok_data.get("brands", [])
        }
    except:
        analytics_data = {}
    

    def format_number(num):
        if not num:
            return ""
        try:
            if isinstance(num, str):
                
                
                num = str(num).replace(',', '')
                num = float(num) if '.' in num else int(num)
            
            formatted = ""
            if num >= 1000000000:
                formatted = f"{num/1000000000:.1f}B"
            elif num >= 1000000:
                formatted = f"{num/1000000:.1f}M"
            elif num >= 1000:
                formatted = f"{num/1000:.1f}K"
            else:
                formatted = str(num)
            
        
            return clean_text(formatted)
        except:
            return clean_text(str(num))
    

    def get_settings_description(setting_value):
        settings_map = {0: "الكل", 1: "الاصدقاء", 2: "ماكو"}
        description = settings_map.get(setting_value, "مو معروف")
        return clean_text(description)
    

    info_text = "🔍 *معلومات حساب تيك توك*\n\n"
    info_text += f"👤 *اليوزر:* @{clean_text(username)}\n"
    info_text += f"📛 *الاسم:* {clean_text(web_info.get('name', ''))}\n"
    
    if web_info.get('bio'):
        info_text += f"📝 *البايو:* {clean_text(web_info.get('bio', ''))}\n"
    
    if web_info.get('bio_link'):
        info_text += f"🔗 *الرابط:* {clean_text(web_info.get('bio_link', ''))}\n"
    
    info_text += "\n📊 *الإحصائيات:*\n"
    info_text += f"👥 *المتابعين:* {format_number(web_info.get('followers', ''))}\n"
    info_text += f"🔄 *يتبع:* {format_number(web_info.get('following', ''))}\n"
    info_text += f"❤️ *مجموع لايكات:* {format_number(web_info.get('likes', ''))}\n"
    info_text += f"🎬 *عدد الفيديوات:* {format_number(web_info.get('videos', ''))}\n"
    
    if web_info.get('digg_count'):
        info_text += f"👍 *الفيديوات المعجبة:* {format_number(web_info.get('digg_count', ''))}\n"
    
    if web_info.get('friend_count'):
        info_text += f"🤝 *عدد الأصدقاء:* {format_number(web_info.get('friend_count', ''))}\n"
    
    info_text += "\n🔐 *معلومات الحساب:*\n"
    info_text += f"✅ *مؤكد:* {'اي' if web_info.get('verified') else 'لا'}\n"
    info_text += f"🔒 *الحالة:* {'خاص' if web_info.get('private') else 'عام'}\n"
    info_text += f"💼 *نوع الحساب:* {'تجاري' if web_info.get('commerce_user') else 'شخصي'}\n"
    info_text += f"🏢 *منظمة:* {'اي' if web_info.get('is_organization') == 1 else 'لا'}\n"
    
    if web_info.get('country_name'):
        info_text += f"🌍 *البلد:* {clean_text(web_info.get('country_name', ''))} {web_info.get('country_flag', '')}\n"
    
    if web_info.get('language'):
        info_text += f"🗣️ *اللغة:* {clean_text(web_info.get('language', ''))}\n"
    
    if web_info.get('created_date'):
        info_text += f"📅 *تاريخ التسجيل:* {clean_text(web_info.get('created_date', ''))}\n"
    
    if level:
        info_text += f"⭐ *مستوى الحساب:* {clean_text(level)}\n"
    
    info_text += "\n⚙️ *الإعدادات:*\n"
    info_text += f"💬 *التعليقات:* {get_settings_description(web_info.get('comment_setting', 0))}\n"
    info_text += f"🎭 *دويت:* {get_settings_description(web_info.get('duet_setting', 0))}\n"
    info_text += f"✂️ *ستيتش:* {get_settings_description(web_info.get('stitch_setting', 0))}\n"
    info_text += f"📥 *التنزيل:* {get_settings_description(web_info.get('download_setting', 0))}\n"
    
    if analytics_data:
        info_text += "\n📈 *تحليل:*\n"
        
        if analytics_data.get('avg_likes'):
            info_text += f"📊 *متوسط الإعجابات:* {format_number(analytics_data.get('avg_likes', ''))}\n"
        
        if analytics_data.get('engagement_rate'):
            engagement_rate = analytics_data.get('engagement_rate', 0)
            engagement_str = f"{engagement_rate:.2f}"
            info_text += f"📈 *نسبة التفاعل:* {clean_text(engagement_str)}%\n"
        
        if analytics_data.get('avg_views'):
            info_text += f"👀 *متوسط المشاهدات:* {format_number(analytics_data.get('avg_views', ''))}\n"
        
        if analytics_data.get('avg_comments'):
            info_text += f"💬 *متوسط التعليقات:* {format_number(analytics_data.get('avg_comments', ''))}\n"
        
        if analytics_data.get('median_engagement_percent'):
            median_engagement = analytics_data.get('median_engagement_percent', 0)
            median_str = f"{median_engagement:.2f}"
            info_text += f"📋 *متوسط التفاعل:* {clean_text(median_str)}%\n"
        
        hashtags = analytics_data.get('tiktok_hashtags', [])
        if hashtags:
            hashtag_list = []
            for h in hashtags[:3]:
                for key, value in h.items():
                    hashtag_list.append(f"#{clean_text(key)}")
            if hashtag_list:
                info_text += f"🏷️ *الهاشتاقات:* {', '.join(hashtag_list)}\n"
    
    info_text += "\n🔧 *معلومات تقنية:*\n"
    info_text += f"🆔 *آيدي اليوزر:* {clean_text(web_info.get('user_id', ''))}\n"
    info_text += f"🔐 *SecUID:* {clean_text(web_info.get('secid', ''))}\n"
    
    info_message = info_text
    
  
    max_length = 4000
    if len(info_message) <= max_length:
        message_parts = [info_message]
    else:
        message_parts = []
        remaining_message = info_message
        while remaining_message:
            if len(remaining_message) <= max_length:
                message_parts.append(remaining_message)
                break
            
            split_index = remaining_message.rfind('\n', 0, max_length)
            if split_index == -1:
                split_index = max_length
            
            message_parts.append(remaining_message[:split_index])
            remaining_message = remaining_message[split_index:].lstrip()
    
    avatar_url = web_info.get('avatar_larger', '')
    
    try:
        if avatar_url and avatar_url.startswith('http'):
            bot.send_photo(
                chat_id=telegram_message.chat.id, 
                photo=avatar_url, 
                caption=message_parts[0], 
                parse_mode="Markdown", 
                reply_to_message_id=telegram_message.message_id
            )
            
            for part in message_parts[1:]:
                bot.send_message(
                    chat_id=telegram_message.chat.id, 
                    text=part, 
                    parse_mode="Markdown"
                )
            
            bot.delete_message(
                chat_id=telegram_message.chat.id, 
                message_id=wait_msg.message_id
            )
        else:
            for i, part in enumerate(message_parts):
                if i == 0:
                    bot.edit_message_text(
                        chat_id=telegram_message.chat.id, 
                        message_id=wait_msg.message_id, 
                        text=part, 
                        parse_mode="Markdown"
                    )
                else:
                    bot.send_message(
                        chat_id=telegram_message.chat.id, 
                        text=part, 
                        parse_mode="Markdown"
                    )
    except Exception as e:
     
        try:
    
            html_text = info_text.replace('*', '')
            html_text = html_text.replace('✅', '✅')
            html_text = html_text.replace('❌', '❌')
            
            if avatar_url and avatar_url.startswith('http'):
                bot.send_photo(
                    chat_id=telegram_message.chat.id,
                    photo=avatar_url,
                    caption=html_text[:1024],
                    parse_mode="HTML",
                    reply_to_message_id=telegram_message.message_id
                )
            else:
                bot.edit_message_text(
                    chat_id=telegram_message.chat.id,
                    message_id=wait_msg.message_id,
                    text=html_text[:4000],
                    parse_mode="HTML"
                )
        except:
           
            try:
                bot.edit_message_text(
                    chat_id=telegram_message.chat.id,
                    message_id=wait_msg.message_id,
                    text=f"✅ تم تجميع المعلومات لـ @{username}\n\n👤 الاسم: {name}\n👥 المتابعين: {followers}\n🎬 الفيديوات: {videos}"
                )
            except:
                pass

print("🤖 بوت تيك توك داير...")
try:
    bot.infinity_polling()
except Exception as e:
    print(f"غلط بوت: {e}")
    import time
    time.sleep(5)
    print("باشر البوت...")