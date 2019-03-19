import requests
import re
import json
from httplib2 import Http


def url_response_check():
    message = ""
    patterns = ['https://(.*)radar(.*)gif', 'https://(.*)eqa2(.*)gif']
    response = ['radar', 'earthquake']

    API_URL = "http://img.n-kishou.co.jp/an/data/bosai_alert_pro.html?pa=nkishou&device_os=5.1&app_version=1.17&service_type=sbps&boap=1&code=27100_23&eqacode=all&eqasnd=3&wake=3233353637380203040506070810121314151617181920212223242526&kckd=10&kamn=2&torn=1&kr1=1&dosya=1&fx=10"

    r = requests.get(API_URL)
    for index in range(len(patterns)):
        if not re.search(patterns[index], r.content.decode("utf8", "ignore")):
            print(patterns[index] + " is missing")
            message += response[index] + " is missing\n\r"

    # print(message)
    return message


def send_result(message):
    # message = "日課チェックのテストメッセージです"
    url = "https://chat.googleapis.com/v1/spaces/AAAA_GetkgM/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=tknSQaVR6eVER-1fAeU5YHmFMW3BmPBAxeWOaSHYfLo%3D"
    to_hangout(message=message, webhook=url)


def to_hangout(message, webhook):
    url = webhook
    method = "POST"
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}
    http_obj = Http()
    response = http_obj.request(
        uri=url,
        method=method,
        headers=message_headers,
        body=json.dumps({'text': message}),
    )
    print(response)


def lambda_handler():
    message = url_response_check()

    if len(message) > 0:
        print(message)
        return False


if __name__ == '__main__':
    lambda_handler()
