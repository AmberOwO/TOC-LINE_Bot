import os

from flask import Flask, request, abort
import requests
import json

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_image_url(reply_token, img_url):
    line_bot_api = LineBotApi(channel_access_token)
    message = ImageSendMessage( original_content_url=img_url, preview_image_url=img_url )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

"""
def send_button_message(id, text, buttons):
    pass
"""

def GetWeather(station):
    end_point = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization=rdec-key-123-45678-011121314"

    data = requests.get(end_point).json()
    data = data["records"]["location"]

    target_station = "not found"
    for item in data:
        if item["locationName"] == str(station):
            target_station = item
    return target_station


def MakeWeather(station):
    WeatherData = GetWeather(station)
    if WeatherData == "not found":
        return False

    WeatherData = WeatherData["weatherElement"]
    msg = "桐人天氣報報 - " + station
    msg += "\n\n氣溫 = " + WeatherData[3]["elementValue"] + "℃\n"
    msg += "濕度 = " + \
        str(float(WeatherData[4]["elementValue"]) * 100) + "% RH\n"

    return msg

def handle_message(reply_token, cmd):
    #cmd = text.message.text.split(" ")

    if cmd[0] == "天氣":
        station = cmd[1]
        WeatherMsg = MakeWeather(station)

        if not WeatherMsg:
            WeatherMsg = "沒這個氣象站啦"

        #line_bot_api.reply_message( event.reply_token, TextSendMessage(text=WeatherMsg))
        
        line_bot_api = LineBotApi(channel_access_token)
        line_bot_api.reply_message(reply_token, TextSendMessage(text=WeatherMsg))
