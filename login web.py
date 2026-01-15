import requests

# @uu_3_u
url = "https://web-sg.tiktok.com/passport/web/user/login/?multi_login=1&did=7587184404951762443&locale=ar&app_language=ar&aid=1459&account_sdk_source=web&sdk_version=2.1.11-tiktokbeta.3&language=ar&verifyFp=verify_mjj5t5qt_M7Aa1423_HpTe_4V8F_9Slx_0SeakwwfWUh6&target_aid=&standalone_aid=&shark_extra=%7B%22aid%22:1459,%22app_name%22:%22Tik_Tok_Login%22,%22channel%22:%22tiktok_web%22,%22device_platform%22:%22web_mobile%22,%22device_id%22:%227587184404951762443%22,%22region%22:%22EG%22,%22priority_region%22:%22%22,%22os%22:%22android%22,%22referer%22:%22https:%2F%2Fwww.google.com%2F%22,%22root_referer%22:%22https:%2F%2Fwww.google.com%2F%22,%22cookie_enabled%22:true,%22screen_width%22:360,%22screen_height%22:800,%22browser_language%22:%22ar-EG%22,%22browser_platform%22:%22Linux+aarch64%22,%22browser_name%22:%22Mozilla%22,%22browser_version%22:%225.0+(Linux%3B+Android+11%3B+RMX3263+Build%2FRP1A.201005.001)+AppleWebKit%2F537.36+(KHTML,+like+Gecko)+Version%2F4.0+Chrome%2F143.0.7499.34+Mobile+Safari%2F537.36%22,%22browser_online%22:true,%22verifyFp%22:%22verify_mjj5t5qt_M7Aa1423_HpTe_4V8F_9Slx_0SeakwwfWUh6%22,%22app_language%22:%22ar%22,%22webcast_language%22:%22ar%22,%22tz_name%22:%22Africa%2FCairo%22,%22is_page_visible%22:true,%22focus_state%22:true,%22is_fullscreen%22:false,%22history_len%22:3,%22user_is_login%22:false,%22data_collection_enabled%22:false%7D&msToken=CnyCxjXkKivW-ER2M5MV4v59iXwPbiW0lH0O1qA9uWOc1z2mtXDwdPv1QmwDkUYD3FvgU6VfaMbcPAz5KKiPe4Fw09g6rKaswkQBHI9Bo--l7vc4idMonY1tuo64QRNiXHfeNL8l-Rw=&X-Bogus=DFSzswVLYreyiSChCFeWMJz3TtcE&X-Gnarly=MFVAz3cKq0iwMS2Zu3CZtwZrcvF/1DHZlgBn8DqP8e9KMFVVwm0mmYnfrJ17r2uBFb4nM9ZDy8t3tVyHg0BQne1i04iH5U36FkKQu/a4kVm0jDPl3bB1Tu-REkQhN0VzZeADnSiDtwAF3v9EtIAyFYBTsTtEqJMDAZiMlKv/D3Ov/EMSQ-t8w8Jgr3YJlO065G2xZ4-jiL9LmNnHi5fkC06h4w4lCGP9S/i6tt17RI3ufmguRr7pYK0ZW8EPtheLw8zLVLGy7/UNsLnHmoA7l2OK5hS3e-sSQUPRY9Tbif4fGMaSSNNafxX3SBQrnJASHDW="

# @uu_3_u
payload = {
    "mix_mode": "1",
    "username": "MARK",
    "password": "MARK",
    "aid": "1459",
    "is_sso": "false",
    "account_sdk_source": "web",
    "region": "EG",
    "language": "ar",
    "locale": "ar",
    "did": "7587184404951762443",
    "fixed_mix_mode": "1"
}

#@uu_3_u
headers = {
    "Host": "web-sg.tiktok.com",
    "content-length": "218",
    "sec-ch-ua-platform": "Android",
    "sec-ch-ua": '"Android WebView";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    "x-tt-passport-ttwid-ticket": "ATaspln9S4wSv3Xq2noh2wiQ4q74_-MLTFVmKX_fdlv4zY20RVoy3kJa32Z-b9KwDQ==",
    "sec-ch-ua-mobile": "?1",
    "x-tt-passport-csrf-token": "094581bd4544af40cea0f4f6eed9fbe9",
    "tt-ticket-guard-web-version": "1",
    "tt-ticket-guard-version": "2",
    "user-agent": "Mozilla/5.0 (Linux; Android 11; RMX3263 Build/RP1A.201005.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/143.0.7499.34 Mobile Safari/537.36",
    "accept": "application/json, text/javascript",
    "tt-ticket-guard-public-key": "BJ6SMDi5jp5XWv6C4JEgdSCdo/O4Zejv5tP0XUM2yfI9XRG23PpuuH2XC8q3wU8xJalgQULEE/ZZ7UxET1+jbR8=",
    "content-type": "application/x-www-form-urlencoded",
    "tt-ticket-guard-iteration-version": "0",
    "x-mssdk-info": "KZDHxelEk3TeI59BP53b5aaZw2se7Zoa.57EdNLWvUq3DmVLwDfjI9FsoZwxOLgjjAfFMYu7ja0sPS5IBXxrTUxADtF2I7Grzqua9eDLWHUxANu6mzXZgYPewTzThl485AngdLBq.hzt86TUQe39lIzZi2Hai-x3MhvQY5rmGdzjKASNG27lcahwPavwbD0ldVOTsdx3j4xVTilKRLL-UG.edYKArDpdAACGreOTYgU7KLA3LC.xTdvmTLbw2FL1IR.pMKipy5H21AfIlGuG9I7qM7jA9oHT2NPi2GDgvbKre7fIbrbAJMgr6gxNSMmy8pxCrQSjQcwa9eDr0xbzikY4oV9FHAUnxVOp4nj-Jkjic281fyCMzMATU-IzkN5C4oT-byoHgWLQU2p2juXzJDY2EjJUPanKzS0oaf25XrYLgFbBEE-g6EluSwurLkcHjd5yILsGdiEtB29-jhLCkTYTvbhUn5QNVsESkfFUzQAuR4rMafaJqk32ObHNRS2WbCZsAzuY1IB9UEvYyaPIHbqjAL5XEY7bQGZxdyznBerIjkcX..HvGqVlGB4DS-TTLaujczsyqsD3p-Z.9Ds7B8eE0-oWgn6KJ9m8LrTNwecNn3qAuNttJ3E4s2CdWEYe1xdcWzLbpvqKGwzHOZoAdu1EY43SpssSMGiQap4Y08hEppgUvBLJVrc0Dz1BgWtNpHlrA82vo6xHpEay8gZoiZru79IP0M0jgt8LB3zswdZr9-YSz4l51qWHyMKkWX368MFzV2GCtsXg1LcYJYEtpii1X6r.FwPTC3z2tViMOs3OCl0xCrkl6DzTng52Gk6KYkaiOWSkDGEzk0Dskp0aSjZFAJaIbvXIzFB.1fZz-VV.EvTam9msthWHGP.cFWNUBJwQstxowk8g.4D6mFE5zgVd0S5lRZP-LEtByvX619CQPcMp.tQecK1NYcdgWmcu58rf5-FV1ENr5.mFFTGrU8NjFAETqo958tI5M-OKjnubQXNnv2Z3xmO8pcvI7ue0UlDR4DLJnXMq7VgB3cspX-P0-lNW13PnKsIeMuNj9aGbgyhbOLuXg-m3k9VxK6Ys7BszijnwACvOCAJMZKw84bDUjI5NvK2W9-N6UCYp1BjirtKlW6BtgbxXgqCGQoLp3gg0KMtizJKJsmc31cOAOpSzdPpuaWRoILDgj4JptuaQBVHdW65kOXhM8QxXu3RyFoxgSzm8hCyvWh2eMnWVe.lnFb1byWSMc4ddB.fAsig1.USslOwHXePru7YieM80kPegsYzCR7pTHnVyuIkX8rUIazqtpEhYwbLu5sLLP-75iW2z7vbveH.8OznmWgaJqyA8yIbfad.pOjI.CwcQ4ysybnamUhIGPx-hDeE-gEUP5YnOMyKUhkFFZKSm9eVqqKvi2yCyEEfTCO84ZIxY6OoLYAzSQWMxAevHyrb-Xwa5ievpqTRem36jGrl.jbfL6DeQmMnqcrOwDmga8eqhOlxDtUATWL7-Sjf4WoCqg79fdfKZdYQDtCJMebEiuncoNdsoOAPSAvlqB4pZcwGdpyw8LCaDadcWFIHsAyllSNJc3vuiSDV9XM2WNlC71Vc4qALXBELwbcvplkqPz2L5pVGVzdbheKARDuL34.UcBeBbtxN0NsHf14PNdlFPjnU7sgWCdfCIBGwtBFBdFhy0PosR7ZvQi.pyGcsQ1b04ehw3BP.nu9yZxySqTFEuTAK5zAS2U0vdZoHm0t5gidTDtzNYrV.GD12U6VcSzXamw81C8Qe4t-Via0dD-uM5BynW-1g0Lq.sRf26g79XHYHMUxtpfA9fxdKTwMXZfQYZRXvVQA2.c1GaCfjOgephPQ-DNOk.9Fxfqv-egNHRzHb-fdcujDgxhGYaJS6z12sygyKQoe6q86IcAN2sgJqvAKLvSc6npQtZcVzoKDiOjxqPVPeo1vholiN0HtMrsbcS-yPz0bAjlg3nSix.neUZOizSXY5yonjV8fbSEw0BL1LaY7hc6N3S.rrmCiLbUtrkjB-SkQYDesqrbLTIOCylchoaAM8v6CsNgteIWx5ugxDo.H9GzHPa6n-M.KJm3DWSeD0EvKBwqrw7wM8FbuGRUL.MgUu71gJ-8kNW4RUXSZRvbJwfZbO.NT2kl6KoLUXq.IW904viVAolR-6id0P.2NhHNXbXfSjpH93O7FAC7cfp8C02G2oykMXeB.l1V9FxuVMIPiC6-YBFvI8U3YmKKBddqdoHdAFc7T2V6BOTzecUDm6dU06k-51pUge9R-e8tuNYVN2SFcabIgAkcSc6ZaV5stxP9fflImy6lxqtGFiH0MyTlyaSkPP6K9wKAMEykFGT-RheX7wi53VKBCZiZ6sdZbiDBhNNYdGMCNx.XuWNMJ4YDPmpLnsD3uNcszTO8YKdJykB01Iyk3qtSvs-Amtnx3w2cCl.ntIszU4SjE0Rv1Zn0sVqA9pJF1VV6ebIU3UY9rpR.UK0Fl6fGTC4nQr2v7nI",
    "origin": "https://www.tiktok.com",
    "x-requested-with": "pure.lite.browser",
    "sec-fetch-site": "same-site",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://www.tiktok.com/",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7",
    "cookie": "tt_csrf_token=tlPhOxln-GdxXznkOOM69wLc7ortay8MQMWQ; ttwid=1%7CqlNXDSKE-LqUL_ezGAw5QqWNhETBhiTFD97SgeOXTJM%7C1766529084%7Cc43bd0d8a31ea0191fb97eacb57626acffc31fa981ee0336afa8156cf27d3668; passport-sotl-auth-token-nonce_QoTgASLs8CMUwAgCZm81hEwHXG686Q3u8t7o6pbtFm0=QoTgASLs8CMUwAgCZm81hEwHXG686Q3u8t7o6pbtFm0; passport_csrf_token=094581bd4544af40cea0f4f6eed9fbe9; passport_csrf_token_default=094581bd4544af40cea0f4f6eed9fbe9; s_v_web_id=verify_mjj5t5qt_M7Aa1423_HpTe_4V8F_9Slx_0SeakwwfWUh6; msToken=CnyCxjXkKivW-ER2M5MV4v59iXwPbiW0lH0O1qA9uWOc1z2mtXDwdPv1QmwDkUYD3FvgU6VfaMbcPAz5KKiPe4Fw09g6rKaswkQBHI9Bo--l7vc4idMonY1tuo64QRNiXHfeNL8l-Rw="
}

# @uu_3_u
session = requests.Session()
response = session.post(url, data=payload, headers=headers)

# @uu_3_u
print(response.status_code)
print(response.json())