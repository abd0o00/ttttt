import requests
#@uu_3_u
url = "https://api16-normal-c-alisg.tiktokv.com/passport/user/login/?passport-sdk-version=6031690&iid=7587190537053046535&device_id=7573709794557871632&ac=WIFI&channel=googleplay&aid=567753&app_name=tiktok_studio&version_code=370301&version_name=37.3.1&device_platform=android&os=android&ab_version=37.3.1&ssmix=a&device_type=RMX3263&device_brand=realme&language=ar&os_api=30&os_version=11&openudid=213cbf93219fac51&manifest_version_code=370301&resolution=720*1504&dpi=320&update_version_code=370301&_rticket=1766558132206&is_pad=0&current_region=EG&app_type=normal&sys_region=EG&last_install_time=1766557878&mcc_mnc=60202&timezone_name=Africa%2FCairo&carrier_region_v2=602&residence=EG&app_language=ar&carrier_region=EG&ac2=wifi&uoo=0&op_region=EG&timezone_offset=7200&build_number=37.3.1&host_abi=arm64-v8a&locale=ar&region=EG&ts=1766558132&cdid=5184e661-a534-419b-9443-7ba9311e0df6&support_webview=1&cronet_version=f6248591_2024-09-11&ttnet_version=4.2.195.9-tiktok&use_store_region_cookie=1"
#@uu_3_u
payload = "password=343736313034373631306e6e3535352626&account_sdk_source=app&multi_login=1&mix_mode=1&username=70766077313d3d333233323c343434343736"
#@uu_3_u
headers = {
    "Host": "api16-normal-c-alisg.tiktokv.com",
    "content-length": "137",
    "cookie": "odin_tt=48dabef48bc77b42f3cbe08d146a6bdecd3089ca01f3623a4be74a17a6b8fb885b114e1d080e0b2e03d989216fb83ff685a69a1e90cd8c890405efdb315eb8e39444d2ed107047a84075302c6a8c81d4",
    "x-tt-pba-enable": "1",
    "tt-ticket-guard-public-key": "BHrliQ/RQBLFzIKWjKiIzxZJ69Fa4xT+VBaAn5g6r3tyNwtBSheqOF+g5PAGNr5ekj6AfkHaqWA0NE/KET0xoRw=",
    "sdk-version": "2",
    "tt-ticket-guard-iteration-version": "0",
    "x-tt-dm-status": "login=0;ct=0;rt=7",
    "x-ss-req-ticket": "1766558132215",
    "tt-ticket-guard-version": "3",
    "passport-sdk-settings": "x-tt-token",
    "passport-sdk-sign": "x-tt-token",
    "passport-sdk-version": "6031690",
    "x-tt-bypass-dp": "1",
    "x-vc-bdturing-sdk-version": "2.3.8.i18n",
    "x-tt-request-tag": "n=0;nr=0;bg=0",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "x-ss-stub": "0F73E10AE19177DAEE5AB0FA89E75684",
    "x-tt-trace-id": "00-4f11ed7810691b38ee5084c610d7ffff-4f11ed7810691b38-01",
    "user-agent": "com.ss.android.tt.creator/370301 (Linux; U; Android 11; ar; RMX3263; Build/RP1A.201005.001; Cronet/TTNetVersion:f6248591 2024-09-11 QuicVersion:182d68c8 2024-05-28)",
    "accept-encoding": "gzip, deflate, br",
    "x-argus": "CsW2RreTTaSFRP2BKRE2tXGx2Tt/l2HQPWjoE7b1icRqdEvMUgc4cXcM93ucwgjA2y6IwfO51jzeaEFm5UxB2Oj1G4klS1jzv2Cs+ZPoOiakiU9hRW46YjMaKSdUfCmx8zHyI29m9I79BtqKUrGndq4xnIpFKKlRpuMlV4d/CAdoV5s3e/FQnbbdNlQawDEN6r9mX9d4HSGHMajDzhtf2IjiQjTXYnPqtnJyIeRCus23J2mFI4rWcLtZjyzJ4VggGzvaTeEZ1obe1imHbKICjyvBtJ/Ua+mOYz4O0Q+M65MEZPdiGu1BYNln7k9ilP9qLqdV+EanEplHb0Vp3Ae7X2ofLBktXhUYx1AFvxLCbdJLDyzfieCKE5l0CD6NRc6CCuzJ0D4BhJnE4GhJT9LHsyoVeFzcv6Qo0FCA/vAR4k17mEvrLs463Xsu7Deq9yfADaS4NBww+iKiis65fXMQRBFNIO+yE55QMNjhoJdPoAy9dfUJ1kJkQWdROH5JzbwaGte0r8nY9T5NM4SsV+cAoa29",
    "x-gorgon": "8404c0070000c5b6d0a7d3b1837c9130ee2cce1008018ebac380",
    "x-khronos": "1766558133",
    "x-ladon": "8jQWJyR7xEUz+9rfqnu7MLwR8XVxUyX1jsb6Fs8NiM0no8el"
}
#@uu_3_u
response = requests.post(url, data=payload, headers=headers)
#@uu_3_u
print(response.text)