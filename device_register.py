import subprocess, requests, time, os





from os        import system
from ttencrypt import ttencrypt
from json      import dumps
from time      import time
from random    import randbytes, choice
from uuid      import uuid4
from requests  import post
from time import sleep
devices = 0
class Colors:
    purple = "\033[38;2;255;0;255m"
    reset  = "\033[38;2;255;255;255m"
    green  = "\033[1;92m"
    blue   = "\033[38;2;0;0;255m"
    red    = "\033[1;91m"


system("")
system("title TikTok ViewBot")


system('')

def tt_encrypt(data: dict) -> bytes:
    return bytes.fromhex(ttencrypt().encrypt(dumps(data)))

def device_register(proxies: dict) -> dict:
    global devices
    start = time()

    device = {
        'openudid'   : randbytes(8).hex(),
        'cdid'       : str(uuid4()),
        'google_aid' : str(uuid4()),
        'clientudid' : str(uuid4()),
        'req_id'     : str(uuid4()),
    }

    while True:
        try:
            proxy = 'http://{}'.format(choice(proxies)) if proxies else ''

            url = 'https://log-va.tiktokv.com/service/2/device_register/'
    
            params = {
                'ac': 'wifi',
                'channel': 'googleplay',
                'aid': '1340',
                'app_name': 'musically_go',
                'version_code': '270903',
                'version_name': '27.9.3',
                'device_platform': 'android',
                'ab_version': '27.9.3',
                'ssmix': 'a',
                'device_type': 'SM-N975F',
                'device_brand': 'samsung',
                'language': 'en',
                'os_api': '25',
                'os_version': '7.1.2',
                'openudid': device['openudid'],
                'manifest_version_code': '270903',
                'resolution': '1080*1920',
                'dpi': '360',
                'update_version_code': '270903',
                '_rticket': [
                    '1672774844814',
                    '1672774844856'
                ],
                'app_type': 'normal',
                'sys_region': 'US',
                'timezone_name': 'America/Chicago',
                'ts': '1672774843',
                'timezone_offset': '-21600',
                'build_number': '27.9.3',
                'app_language': 'en',
                'carrier_region': 'DE',
                'region': 'US',
                'locale': 'en',
                'op_region': 'DE',
                'ac2': 'wifi',
                'cdid': device['cdid'],
                'tt_data': 'a',
                'okhttp_version': '4.1.103.1-ul',
                'use_store_region_cookie': '1'
            }
            
            data = {
                'magic_tag': 'ss_app_log',
                'header': {
                    'display_name': 'TikTok Lite',
                    'update_version_code': 270903,
                    'manifest_version_code': 270903,
                    'app_version_minor': '',
                    'aid': 1340,
                    'channel': 'googleplay',
                    'package': 'com.zhiliaoapp.musically.go',
                    'app_version': '27.9.3',
                    'version_code': 270903,
                    'sdk_version': '2.12.1.global-rc.20',
                    'sdk_target_version': 29,
                    'git_hash': 'ce36e02b',
                    'os': 'Android',
                    'os_version': '7.1.2',
                    'os_api': 25,
                    'device_model': 'SM-N975F',
                    'device_brand': 'samsung',
                    'device_manufacturer': 'samsung',
                    'cpu_abi': 'arm64-v8a',
                    'release_build': '3b7924e_20221223',
                    'density_dpi': 360,
                    'display_density': 'mdpi',
                    'resolution': '1920x1080',
                    'language': 'en',
                    'timezone': -6,
                    'access': 'wifi',
                    'not_request_sender': 0,
                    'carrier': 'O2',
                    'mcc_mnc': '26203',
                    'rom': 'rel.se.infra.20200819.140601',
                    'rom_version': 'samsung-user 7.1.2 20171130.276299 release-keys',
                    'cdid': device['cdid'],
                    'sig_hash': 'aea615ab910015038f73c47e45d21466',
                    'gaid_limited': 0,
                    'google_aid': device['google_aid'],
                    'openudid': device['openudid'],
                    'clientudid': device['clientudid'],
                    'region': 'US',
                    'tz_name': 'America/Chicago',
                    'tz_offset': -21600,
                    'sim_region': 'de',
                    'req_id': device['req_id'],
                    'apk_first_install_time': 1672774833463,
                    'is_system_app': 0,
                    'sdk_flavor': 'global'
                },
                '_gen_time': 1672774844813
            }
            
            headers = {
                'accept-encoding'           : 'gzip',
                'connection'                : 'Keep-Alive',
                'content-type'              : 'application/octet-stream;tt-data=a',
                'host'                      : 'log-va.tiktokv.com',
                'passport-sdk-version'      : '30790',
                'sdk-version'               : '2',
                'user-agent'                : 'com.zhiliaoapp.musically.go/270903 (Linux; U; Android 7.1.2; en_US; SM-N975F; Build/N2G48H;tt-ok/3.12.13.2-rc.5)',
                'x-tt-ultra-lite'           : '1',
                'x-vc-bdturing-sdk-version' : '2.2.1.i18n'
            }
            
            response = post(url, params=params, data=tt_encrypt(data), headers=headers, proxies={'https': proxy}, timeout=3).json()
    
            if response['install_id'] == 0 or response['device_id'] == 0:
                continue
            devices += 1
            
            return {
                'install_id' : response['install_id'],
                'device_id'  : response['device_id']
            }
        except Exception:
            continue

from requests        import Session
from urllib.parse    import quote_plus
from json            import dumps
from random          import choice, randbytes
from os              import system
from time            import sleep
from hashlib         import md5
from threading       import Thread

request = Session()
sent    = 0
failed    = 0
views = 0

def sign(params: str, headers: dict) -> dict:
    while True:
        try:
            return request.post(
                url     = 'https://www.tikwm.com/api/service/sign', 
                data    = 'params={}&headers={}'.format(quote_plus(params), quote_plus(dumps(headers))),
                headers = {'content-type' : 'application/x-www-form-urlencoded'}
            ).json()['data']
        except Exception:
            continue

def play_delta(url: str, data: str, headers: dict) -> None:
    global proxies
    global sent
    global failed
    while True:
        try:
            proxy = 'http://{}'.format(choice(proxies)) if proxies else ''
            response = request.post(url, data=data, headers=headers, timeout=5, proxies={'https': proxy})
            if '"status_code":0' in response.text:
                sent += 1
                break
            else:
                failed += 1
                continue
        except Exception:
            failed += 1
            continue


def vps() -> None:
  global views
  global sent
  while True:
    before = sent
    sleep(1)
    after = sent
    views = (after - before)



def stats() -> None:
  global sent
  global devices
  global failed
  global views
  while True:
    system("cls")
    print(f"{Colors.reset} Sent: {Colors.green}{sent} {Colors.reset}|{Colors.reset} Failed: {Colors.red}{failed} {Colors.reset}|{Colors.reset} Devices: {Colors.purple}{devices} {Colors.reset}|{Colors.reset} Views/s: {Colors.blue}{views}")
    sleep(1)

def start(item_id: str):
    global proxies
    while True:
        try:
            device = device_register(proxies)

            sessionid = randbytes(16).hex()
        
            url = 'https://api22-core-c-useast1a.tiktokv.com/aweme/v1/aweme/stats/?os_api=25&device_type=SM-N975F&ssmix=a&manifest_version_code=270903&dpi=360&region=US&carrier_region=DE&app_name=musically_go&version_name=27.9.3&timezone_offset=-21600&ts=1672774843&ab_version=27.9.3&ac2=wifi&ac=wifi&app_type=normal&channel=googleplay&update_version_code=270903&_rticket=1672774848175&device_platform=android&iid={}&build_number=27.9.3&locale=en&op_region=DE&version_code=270903&device_id={}&sys_region=US&app_language=en&resolution=1080*1920&device_brand=samsung&language=en&os_version=7.1.2&aid=1340'.format(device['install_id'], device['device_id'])
            
            data = 'item_id={}&play_delta=1'.format(item_id)
            
            headers = {
                'accept-encoding'           : 'gzip',
                'connection'                : 'Keep-Alive',
                'content-type'              : 'application/x-www-form-urlencoded; charset=UTF-8',
                'cookie'                    : 'store-idc=maliva; store-country-code=de; store-country-code-src=did; install_id={}; ttreq=1${}; sessionid={}'.format(device['install_id'], randbytes(20).hex(), sessionid),
                'host'                      : 'api22-core-c-useast1a.tiktokv.com',
                'passport-sdk-version'      : '30790',
                'sdk-version'               : '2',
                'user-agent'                : 'com.zhiliaoapp.musically.go/270903 (Linux; U; Android 7.1.2; en_US; SM-N975F; Build/N2G48H;tt-ok/3.12.13.2-rc.5)',
                'x-ss-stub'                 : md5(data.encode()).hexdigest().upper(),
                'x-tt-store-region'         : 'de',
                'x-tt-store-region-src'     : 'did',
                'x-tt-token'                : '03{}0386c93842b46edff14c9b15b77224174f128cb008e3d6d8c127855b829100038e503b50a424e3fbfb1582faf0fb6f98753bc7b7f853b712dcdf271df4ff5c97268f4c8a334573e3f5eb9a3abd32ed3d67c-CkBmODRkOWQxOTRkYzE0NWRlYzIxM2U1NmUyNTEzYzdhZGZkOWJkNDAxOGQwNmMzZGQ2NDEyMTQ0ODQ1ZDNiMWQ2-2.0.0'.format(sessionid),
                'x-tt-ultra-lite'           : '1',
                'x-vc-bdturing-sdk-version' : '2.2.1.i18n'
            }
            
            headers.update(sign(url.split('?')[1], headers))
            
            for x in range(500):
                Thread(target=play_delta, args=[url, data, headers]).start()
        except Exception:
            continue

proxies = open('proxies.txt', 'r').read().splitlines()
item_id = input('[?] Video Link >>> ').split('/')[5].split('?')[0]
system('cls')
Thread(target=stats).start()
Thread(target=vps).start()
for x in range(5):
    Thread(target=start, args=[item_id]).start()