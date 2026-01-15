import requests, uuid
from secrets import token_hex
from user_agent import generate_user_agent

mc, ca = None, None

def get_token():
    try:
        headers = {
            'accept': 'text/html',
            'user-agent': generate_user_agent(),
        }

        r = requests.get(
            'https://signup.live.com/signup',
            headers=headers,
            timeout=10
        )

        canary = str.encode(
            r.text.split('"apiCanary":"')[1].split('"')[0]
        ).decode("unicode_escape")

        mc = r.cookies.get('amsc')
        if not mc:
            return None, None

        headers = {
            'accept': 'application/json',
            'canary': canary,
            'content-type': 'application/json',
            'origin': 'https://signup.live.com',
            'referer': 'https://signup.live.com/',
            'user-agent': generate_user_agent(),
        }

        r = requests.post(
            'https://signup.live.com/API/EvaluateExperimentAssignments',
            cookies={'amsc': mc},
            headers=headers,
            json={
                'clientExperiments': [{
                    'parallax': 'enableplaintextforsignupexperiment',
                    'control': 'enableplaintextforsignupexperiment_control',
                    'treatments': [
                        'enableplaintextforsignupexperiment_treatment'
                    ],
                }]
            },
            timeout=10
        ).json()

        ca = r.get('apiCanary')
        if ca:
            return mc, ca

    except:
        pass

    return None, None


def check_live_signup(email):
    global mc, ca

    if not mc or not ca:
        mc, ca = get_token()
        if not mc or not ca:
            return {"status": "token_failed"}

    cookies = {
        'mkt': 'ar-YE',
        'MicrosoftApplicationsTelemetryDeviceId': str(uuid.uuid4()),
        'MUID': token_hex(16),
        'amsc': mc,
    }

    headers = {
        'accept': 'application/json',
        'canary': ca,
        'content-type': 'application/json',
        'origin': 'https://signup.live.com',
        'referer': 'https://signup.live.com/signup',
        'user-agent': generate_user_agent(),
        'x-ms-apiversion': '2',
    }

    params = {
        'mkt': 'AR-AR',
        'lic': '1',
        'uaid': str(uuid.uuid4()),
    }

    data = {
        'signInName': email,
        'includeSuggestions': True,
    }

    try:
        r = requests.post(
            'https://signup.live.com/API/CheckAvailableSigninNames',
            params=params,
            cookies=cookies,
            headers=headers,
            json=data,
            timeout=10
        ).text

        if '"isAvailable":true' in r:
            return {"available": True}

        if '"isAvailable":false' in r:
            return {"available": False}

        mc, ca = get_token()
        return {"status": "unknown"}

    except Exception as e:
        mc, ca = get_token()
        return {"status": "error", "reason": str(e)}

