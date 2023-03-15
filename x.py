from requests        import Session
from urllib.parse    import quote_plus
from json            import dumps
from random          import choice, randbytes
from os              import system
from time            import sleep
from device_register import device_register
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
    while True:
        try:
            proxy = 'http://{}'.format(choice(proxies)) if proxies else ''
            response = request.post(url, data=data, headers=headers, timeout=5, proxies={'https': proxy})
            if '"status_code":0' in response.text:
                sent += 1
                break
            else:
                continue
        except Exception:
            continue

def stats() -> None:
    global sent
    while True:
        system('title TikTok ViewBot ^| By @auut - Sent: {}'.format(sent))
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
for x in range(5):
    Thread(target=start, args=[item_id]).start()