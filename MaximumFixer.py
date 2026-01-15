from TikSign import Argus, Ladon, Gorgon, Newparams, UserAgentTik
import time
from hashlib import md5
from urllib.parse import urlencode
def sign(
    params: str,
    payload: str or None = None,
    sec_device_id: str = '',
    cookie: str or None = None,
    aid: int = 1340, #Replace
    license_id: int = 1611921764,
    sdk_version_str: str = 'v05.00.06-ov-android',
    sdk_version: int = 167775296,
    platform: int = 0,
    unix: float = None
):
    aid = 1340 #Replace
    x_ss_stub = md5(payload.encode('utf-8')).hexdigest() if payload is not None else None
    if not unix:
        unix = time.time()
    return Gorgon(aid).Encoder(
        params=params,
        data=payload,
        cookies=cookie,
        unix=unix
    ) | {
        'content-length': str(len(payload)),
        'x-ss-stub': x_ss_stub.upper(),
        'x-ladon': Ladon.encrypt(int(unix), license_id, aid),
        'x-argus': Argus.get_sign(
            params,
            x_ss_stub,
            int(unix),
            platform=platform,
            aid=aid,
            license_id=license_id,
            sec_device_id=sec_device_id,
            sdk_version=sdk_version_str,
            sdk_version_int=sdk_version
        )
    }
signature = sign(params=urlencode(params), payload=urlencode(payload), cookie=None)