import urllib.request
import json
import os
from datetime import datetime, timedelta

THEMES = [
    {"grade":"六年级","book":"上册","unit":"Unit 1","name":"The King's New Clothes","words":"magic, clever, foolish, through, laugh, wear, tell, sentence"},
    {"grade":"六年级","book":"上册","unit":"Unit 2","name":"What a Day!","words":"sunny, weather, become, windy, cloudy, sky, bring, rain"},
    {"grade":"六年级","book":"上册","unit":"Unit 3","name":"Holiday Fun","words":"holiday, National Day, Bund, excited, star, ask, bottle, paper"},
    {"grade":"六年级","book":"上册","unit":"Unit 4","name":"Then and Now","words":"ago, use, telephone, mobile phone, newspaper, radio, news, still"},
    {"grade":"六年级","book":"上册","unit":"Unit 5","name":"Signs","words":"sign, mean, careful, restaurant, smoke, floor, litter, Danger"},
    {"grade":"六年级","book":"上册","unit":"Unit 6","name":"Keep Our City Clean","words":"keep, clean, air, dirty, rubbish, messy, plant, throw"},
    {"grade":"六年级","book":"上册","unit":"Unit 7","name":"Protect the Earth","words":"protect, Earth, save, useful, energy, waste, reuse, plastic"},
    {"grade":"六年级","book":"上册","unit":"Unit 8","name":"Chinese New Year","words":"food, plan, light, red packet, lion dance, fireworks, rich, get"},
    {"grade":"六年级","book":"下册","unit":"Unit 1","name":"The Lion and the Mouse","words":"mouse, large, strong, quietly, loudly, net, bite, sharp"},
    {"grade":"六年级","book":"下册","unit":"Unit 2","name":"Good Habits","words":"habit, tidy, fast, never, late, finish, sleepy, slowly"},
    {"grade":"六年级","book":"下册","unit":"Unit 3","name":"A Healthy Diet","words":"healthy, diet, need, cola, a little, a few, at a time"},
    {"grade":"六年级","book":"下册","unit":"Unit 4","name":"Road Safety","words":"road, must, safe, follow, cross, rule, zebra crossing, pavement"},
    {"grade":"六年级","book":"下册","unit":"Unit 5","name":"A Party","words":"begin, end, clown, appear, balloon, Children's Day, put on"},
    {"grade":"六年级","book":"下册","unit":"Unit 6","name":"An Interesting Country","words":"country, learn, welcome, visitor, magazine, kangaroo, koala, exciting"},
    {"grade":"六年级","book":"下册","unit":"Unit 7","name":"Summer Holiday Plans","words":"travel, photo, stay, sound, summer holiday, different, plan, trip"},
    {"grade":"六年级","book":"下册","unit":"Unit 8","name":"Our Dreams","words":"dream, future, scientist, artist, astronaut, dancer, pianist, spaceship"},
    {"grade":"七年级","book":"上册","unit":"Unit 1","name":"This is Me!","words":"greet, introduce, hobby, grade, classmate, friendly, energy, slim"},
    {"grade":"七年级","book":"上册","unit":"Unit 2","name":"Hobbies","words":"jogging, painting, fit, dream, club, join, design, skill"},
    {"grade":"七年级","book":"上册","unit":"Unit 3","name":"Welcome to Our School!","words":"gym, building, modern, bright, spend, chat, borrow, magazine"},
    {"grade":"七年级","book":"上册","unit":"Unit 4","name":"My Day","words":"activity, homework, usually, start, language, practise, trip, seldom"},
    {"grade":"七年级","book":"上册","unit":"Unit 5","name":"A Healthy Lifestyle","words":"lifestyle, health, delicious, diet, important, sugar, enough, meal"},
    {"grade":"七年级","book":"上册","unit":"Unit 6","name":"My Clothes, My Style","words":"style, choose, fashion, comfortable, popular, traditional, silk, material"},
    {"grade":"七年级","book":"上册","unit":"Unit 7","name":"Be Wise with Money","words":"wise, budget, save, expensive, bank, pocket money, lucky, education"},
    {"grade":"七年级","book":"上册","unit":"Unit 8","name":"Let's Celebrate!","words":"celebrate, tradition, symbol, decorate, prepare, midnight, dragon, dumpling"},
    {"grade":"七年级","book":"下册","unit":"Unit 1","name":"Dream Homes","words":"cottage, balcony, bedroom, village, yard, tent, relax, view"},
    {"grade":"七年级","book":"下册","unit":"Unit 2","name":"Neighbours","words":"neighbour, community, volunteer, repair, invite, engineer, fridge, law"},
    {"grade":"七年级","book":"下册","unit":"Unit 3","name":"My Hometown","words":"capital, ancient, treasure, palace, flag, stadium, local, golden"},
    {"grade":"七年级","book":"下册","unit":"Unit 4","name":"Chinese Folk Art","words":"folk, carve, craft, scissors, creative, simple, cultural, quality"},
    {"grade":"七年级","book":"下册","unit":"Unit 5","name":"Amazing Things","words":"butterfly, insect, wing, weight, lonely, touch, goldfish, snake"},
    {"grade":"七年级","book":"下册","unit":"Unit 6","name":"Outdoor Fun","words":"ocean, forest, desert, survive, planet, oxygen, rainbow, waterfall"},
    {"grade":"七年级","book":"下册","unit":"Unit 7","name":"Outdoor Activities","words":"cycle, skate, balance, hike, picnic, medicine, safety, experience"},
    {"grade":"七年级","book":"下册","unit":"Unit 8","name":"Wonderland","words":"adventure, magic, character, imagine, solve, suddenly, decide, goal"},
]

today = datetime.utcnow() + timedelta(hours=8)
day_index = (today.timetuple().tm_yday - 1) % len(THEMES)
theme = THEMES[day_index]

title = "📚 今日单词任务"
content = f"""<div style="font-family:sans-serif;padding:16px">
<h2 style="color:#6C5CE7">📚 今日单词任务</h2>
<p style="font-size:14px;color:#666">{today.strftime('%Y年%m月%d日')} 星期{['一','二','三','四','五','六','日'][today.weekday()]}</p>
<div style="background:#f0f2f8;border-radius:12px;padding:16px;margin:12px 0">
<p style="font-size:16px;font-weight:bold">🎯 {theme['grade']}{theme['book']} {theme['unit']}</p>
<p style="font-size:14px;color:#636e72">主题：{theme['name']}</p>
</div>
<div style="background:#f0f2f8;border-radius:12px;padding:16px;margin:12px 0">
<p style="font-size:14px;font-weight:bold">📝 今日8个新词</p>
<p style="font-size:15px;color:#6C5CE7">{theme['words']}</p>
</div>
<div style="background:linear-gradient(135deg,#6C5CE7,#A29BFE);border-radius:12px;padding:16px;margin:12px 0;text-align:center">
<a href="https://cocorefreshing.github.io/vocab-game/" style="color:white;font-size:18px;font-weight:bold;text-decoration:none">⚔️ 点击开始练习 →</a>
</div>
<p style="font-size:12px;color:#aaa;text-align:center">💡 先跟AI老师学一遍，再PK检验成果！</p>
</div>"""

token = os.environ.get('PUSHPLUS_TOKEN', '')
if not token:
    print("未配置PUSHPLUS_TOKEN，跳过推送")
    exit(0)

url = "http://www.pushplus.plus/send"
data = json.dumps({"token": token, "title": title, "content": content, "template": "html"}).encode('utf-8')
req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
try:
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read().decode('utf-8'))
        print(f"推送结果: {result.get('code')} - {result.get('msg')}")
except Exception as e:
    print(f"推送失败: {e}")
