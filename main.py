import network
import requests
import utime
import campuswifi
import ure as re
from machine import Pin, SoftSPI,SPI
from ST7735 import TFT

def get_weather_info():
    
    weather_api = "https://api.seniverse.com/v3/weather/daily.json?key=S0KEla3YqL1xzFRwI&location=hefei&language=en&unit=c&start=-1&days=5"
    
    rq = requests.get(weather_api)
    info = rq.content.decode()
    rq.close()
    
    date_pattern = '"date":"(.*?)"'
    text_day_pattern = '"text_day":"(.*?)"'
    code_day_pattern = '"code_day":"(.*?)"'
    text_night_pattern = '"text_night":"(.*?)"'
    code_night_pattern = '"code_night":"(.*?)"'
    high_pattern = '"high":"(.*?)"'
    low_pattern = '"low":"(.*?)"'
    rainfall_pattern = '"rainfall":"(.*?)"'
    precip_pattern = '"precip":"(.*?)"'
    wind_direction_pattern = '"wind_direction":"(.*?)"'
    wind_direction_degree_pattern = '"wind_direction_degree":"(.*?)"'
    wind_speed_pattern = '"wind_speed":"(.*?)"'
    wind_scale_pattern = '"wind_scale":"(.*?)"'
    humidity_pattern = '"humidity":"(.*?)"'
    last_update_pattern = '"last_update":"(.*?)"'

    date = []
    text_day = []
    code_day = []
    text_night = []
    code_night = []
    high = []
    low = []
    rainfall = []
    precip = []
    wind_direction = []
    wind_direction_degree = []
    wind_speed = []
    wind_scale = []
    humidity = []
    last_update = []
    
    date_start = date_pattern.find('(')
    text_day_start = text_day_pattern.find('(')
    code_day_start = code_day_pattern.find('(')
    text_night_start = text_night_pattern.find('(')
    code_night_start = code_night_pattern.find('(')
    high_start = high_pattern.find('(')
    low_start = low_pattern.find('(')
    rainfall_start = rainfall_pattern.find('(')
    precip_start = precip_pattern.find('(')
    wind_direction_start = wind_direction_pattern.find('(')
    wind_direction_degree_start = wind_direction_degree_pattern.find('(')
    wind_speed_start = wind_speed_pattern.find('(')
    wind_scale_start = wind_scale_pattern.find('(')
    humidity_start = humidity_pattern.find('(')
    last_update_start = last_update_pattern.find('(')
    
    whos_turn = 0
    for i in range(0, len(info)):
        info_fromi = info[i:]
        if whos_turn == 0:
            ret = re.match(date_pattern, info_fromi)
            if ret != None:
                date.append(ret.group(0)[date_start : -1])
                i += len(ret.group(0))
                whos_turn += 1
                continue
        elif whos_turn == 1:
            ret = re.match(text_day_pattern, info_fromi)
            if ret != None:
                text_day.append(ret.group(0)[text_day_start : -1])
                i += len(ret.group(0))
                whos_turn += 1
                continue
        elif whos_turn == 2:
            ret = re.match(code_day_pattern, info_fromi)
            if ret != None:
                code_day.append(ret.group(0)[code_day_start : -1])
                i += len(ret.group(0))
                whos_turn += 1
                continue
        elif whos_turn == 3:
            ret = re.match(text_night_pattern, info_fromi)
            if ret != None:
                text_night.append(ret.group(0)[text_night_start : -1])
                i += len(ret.group(0))
                whos_turn += 1
                continue
        elif whos_turn == 4:
            ret = re.match(code_night_pattern, info_fromi)
            if ret != None:
                code_night.append(ret.group(0)[code_night_start : -1])
                i += len(ret.group(0))
                whos_turn += 1
                continue
        elif whos_turn == 5:
            ret = re.match(high_pattern, info_fromi)
            if ret != None:
                high.append(ret.group(0)[high_start : -1])
                i += len(ret.group(0))
                whos_turn += 1
                continue
        elif whos_turn == 6:
            ret = re.match(low_pattern, info_fromi)
            if ret != None:
                low.append(ret.group(0)[low_start : -1])
                i += len(ret.group(0))
                whos_turn += 1
                continue
        elif whos_turn == 7:
            ret = re.match(rainfall_pattern, info_fromi)
            if ret != None:
                rainfall.append(ret.group(0)[rainfall_start : -1])
                i += len(ret.group(0))
                whos_turn += 1
                continue
        elif whos_turn == 8:
            ret = re.match(precip_pattern, info_fromi)
            if ret != None:
                precip.append(ret.group(0)[precip_start : -1])
                i += len(ret.group(0))
                whos_turn += 1
                continue
#         if len(wind_direction) < day_index and day_index < 4:
#             ret = re.match(wind_direction_pattern, info_fromi)
#             if ret != None:
#                 wind_direction.append(ret.group(0)[wind_direction_start : -1])
#                 i += len(ret.group(0))
#                 continue
#         if len(wind_direction_degree) < day_index and day_index < 4:
#             ret = re.match(wind_direction_degree_pattern, info_fromi)
#             if ret != None:
#                 wind_direction_degree.append(ret.group(0)[wind_direction_degree_start : -1])
#                 i += len(ret.group(0))
#                 continue
#         if len(wind_speed) < day_index and day_index < 4:
#             ret = re.match(wind_speed_pattern, info_fromi)
#             if ret != None:
#                 wind_speed.append(ret.group(0)[wind_speed_start : -1])
#                 i += len(ret.group(0))
#                 continue
#         if len(wind_scale) < day_index and day_index < 4:
#             ret = re.match(wind_scale_pattern, info_fromi)
#             if ret != None:
#                 wind_scale.append(ret.group(0)[wind_scale_start : -1])
#                 i += len(ret.group(0))
#                 continue
        elif whos_turn == 9:
            ret = re.match(humidity_pattern, info_fromi)
            if ret != None:
                humidity.append(ret.group(0)[humidity_start : -1])
                i += len(ret.group(0))
                whos_turn = 0
                continue
            
#         if whos_turn == 0:
#             ret = re.match(last_update_pattern, info_fromi)
#             if ret != None:
#                 last_update.append(ret.group(0)[last_update_start : -1])
#                 i += len(ret.group(0))
#                 break
            
    return {\
        "date": date, \
        "text_day": text_day, \
        "code_day": code_day, \
        "text_night": text_night, \
        "code_night": code_night, \
        "high": high, \
        "low": low, \
        "rainfall": rainfall, \
        "precip": precip, \
        "wind_direction": wind_direction, \
        "wind_direction_degree": wind_direction_degree, \
        "wind_speed": wind_speed, \
        "wind_scale": wind_scale, \
        "humidity": humidity, \
        "last_update": last_update\
    }

def getcurrenttime():
    time_api = "http://quan.suning.com/getSysTime.do"
    
    rq = requests.get(time_api)
    info = rq.content.decode()
    rq.close()
    
    systime_pattern = '"sysTime2":"(.*?)"'
    systime = ''
    systime_start = systime_pattern.find('(')
    for i in range(0, len(info)):
        info_fromi = info[i:]
        ret = re.match(systime_pattern, info_fromi)
        if ret != None:
            systime = ret.group(0)[systime_start : -1]
            break
    return systime

tft = None

def init():
    ssid = "ustcnet"
    password =  ""
    user_name = "bonjour866"
    user_password = "Nea@313818"

    campuswifi.connect(ssid, password, user_name, user_password)
    
    spi = SoftSPI(baudrate=800000, polarity=1, phase=0, sck=Pin(2), mosi=Pin(3), miso=Pin(10))
    global tft
    tft = TFT(spi,6,10,7) #DC, Reset, CS
    tft.initr()
    tft.rgb(True)
    tft.rotation(1)
    tft.fill(tft.BLACK)
    

if __name__ == "__main__":
    init()
    
    while True:
        tft.fill(tft.BLACK)
        weather_info = get_weather_info()
        systime = getcurrenttime()
        
        xpos = 70
        ypos = 0
        tft.showbmp((xpos, ypos), "weathericon/{}.bmp".format(weather_info["code_day"][0]))
        xpos += 40 + 5
        tft.showbmp((115, 0), "weathericon/{}.bmp".format(weather_info["code_night"][0]))
        
        normal_fontsize = (1.8, 2)
        small_fontsize = (1, 1)
        tiny_fontsize = (0.9, 0.9)
        
        xpos = 70
        ypos += 40 + 5
        temp_str = "{th}".format(th = weather_info["high"][0])
        tft.textout((xpos, ypos), temp_str, tft.WHITE, aSize = normal_fontsize)
        xpos += 2 * 6 * normal_fontsize[0] + 7
        tft.char((xpos, ypos), '/', tft.WHITE, aSize = (1, 2))
        xpos += 6 + 7
        temp_str = "{tl}".format(tl = weather_info["low"][0])
        tft.textout((xpos, ypos), temp_str, tft.WHITE, aSize = normal_fontsize)
        xpos += 2 * 6 * normal_fontsize[0] + 5
        tft.char((xpos, ypos), "degreec-first-half", tft.WHITE, aSize = (1.8, 2))
        xpos += 1 * 6 * normal_fontsize[0]
        tft.char((xpos, ypos), "degreec-second-half", tft.WHITE, aSize = (1.8, 2))
        
        xpos = 0
        ypos = 0
        temp_str = weather_info["date"][0]
        tft.textout((xpos, ypos), temp_str[-5:], tft.WHITE, aSize = normal_fontsize)
        
        xpos = 0
        ypos += 8 * normal_fontsize[1] + 5
        temp_str = weather_info["rainfall"][0]
        tft.textout((xpos, ypos), temp_str, tft.BLUE, aSize = normal_fontsize)
        xpos += 6 * normal_fontsize[0] * len(temp_str) + 2
        ypos += 8 * normal_fontsize[1] - 8 * small_fontsize[1]
        tft.textout((xpos, ypos), "mm", tft.BLUE, aSize = small_fontsize)
        ypos -= 8 * normal_fontsize[1] - 8 * small_fontsize[1]
        
        xpos = 0
        ypos = 45
        temp_str = weather_info["precip"][0]
        tft.textout((xpos, ypos), temp_str, tft.CYAN, aSize = normal_fontsize)
        xpos += 6 * normal_fontsize[0] * len(temp_str) + 2
        ypos += 8 * normal_fontsize[1] - 8 * small_fontsize[1]
        tft.textout((xpos, ypos), "%", tft.CYAN, aSize = small_fontsize)
        ypos -= 8 * normal_fontsize[1] - 8 * small_fontsize[1]
        
        xpos = 0
        ypos += 8 * normal_fontsize[1] + 6
        temp_str = "Updated: {}".format(systime)
        tft.textout((xpos, ypos), temp_str, tft.GRAY, aSize = tiny_fontsize)
        
        utime.sleep(60 * 60)
    
    