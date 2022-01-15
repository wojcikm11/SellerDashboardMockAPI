from datetime import datetime
from math import ceil, floor
from typing import List
from xmlrpc.client import DateTime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Offer, Opinion, Orders, DailyTip,Revenue,Turnover
import base64
from datetime import *
from calendar import monthrange


def convertImgToString(img_path):
    with open(img_path, "rb") as imageFile:
        if (img_path.endswith(".jpg")):
            return 'data:image/jpg;base64,' + str(base64.b64encode(imageFile.read()).decode())
        elif (img_path.endswith(".png")):
            return 'data:image/png;base64,' + str(base64.b64encode(imageFile.read()).decode())

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


opinions: List[Opinion] = [
    Opinion(id=0, rating=3, description="Produkty wystawione przez sprzedawcę takie sobie, ale za to cena nie jest taka wysoka.", date=datetime(2020, 10, 10, hour=23, minute=54, second=21)),
    Opinion(id=1, rating=4, date=datetime(2021, 5, 12, hour=21, minute=22, second=37)),
    Opinion(id=2, rating=5, description="Cóż napisać ... jestem bardzo zadowolony. Szukałem w sieci różnych rozwiązań i trafiłem przez przypadek na tego sprzedawcę. Po zapoznaniu się z możliwościami sklepu dokonałem zakupu - cena niewielka - w sumie dużo nie ryzykowałem - brak umów więc w razie czego tylko utopione kilka złotych. Jednak się nie zawiodłem. Zarówno możliwości sklepu jak i jego obsługa posprzedaży są na najwyższym poziomie. Właśnie kupuję kolejny towar i jak najbardziej mogę wszystkim polecić. Bardzo dobra cena w stosunku do jakości.", date=datetime(2023, 5, 12, hour=21, minute=22, second=37)),
    Opinion(id=3, rating=1, description="O ile obsługa w sklepie jest ok, o tyle dział rat w arogancki i w ogóle nie wykazujący zainteresowania klientem, obsługa \"z musu\", suma sumarum zrezygnowałem z zakupu produktu, który miałem na oku. A wielka szkoda, bo długo przymierzałem się...", date=datetime(2018, 5, 12, hour=21, minute=22, second=37)),
    Opinion(id=4, rating=3, description="Jest ok", date=datetime(2019, 5, 12, hour=21, minute=22, second=37)),
    Opinion(id=5, rating=2, description="Nie jest ok", date=datetime(2017, 5, 12, hour=21, minute=22, second=37)),
    Opinion(id=6, rating=3, description="Produkty wystawione przez sprzedawcę takie sobie, ale za to cena nie jest taka wysoka.", date=datetime(2020, 10, 10, hour=23, minute=54, second=21)),
    Opinion(id=7, rating=4, date=datetime(2021, 5, 12, hour=21, minute=22, second=37)),
    Opinion(id=8, rating=1, description="Cóż napisać ... jestem bardzo niezadowolony. Szukałem w sieci różnych rozwiązań i trafiłem przez przypadek na tego sprzedawcę. Po zapoznaniu się z możliwościami sklepu dokonałem zakupu - cena niewielka - w sumie dużo nie ryzykowałem - brak umów więc w razie czego tylko utopione kilka złotych. Jednak się nie zawiodłem. Zarówno możliwości sklepu jak i jego obsługa posprzedaży są na najwyższym poziomie. Właśnie kupuję kolejny towar i jak najbardziej mogę wszystkim polecić. Bardzo dobra cena w stosunku do jakości.", date=datetime(2023, 5, 12, hour=21, minute=22, second=37)),
    Opinion(id=9, rating=1, description="O ile obsługa w sklepie jest ok, o tyle dział rat w arogancki i w ogóle nie wykazujący zainteresowania klientem, obsługa \"z musu\", suma sumarum zrezygnowałem z zakupu produktu, który miałem na oku. A wielka szkoda, bo długo przymierzałem się...", date=datetime(2018, 5, 12, hour=21, minute=22, second=37)),
    Opinion(id=10, rating=3, description="Jest ok", date=datetime(2019, 5, 12, hour=21, minute=22, second=37)),
    Opinion(id=11, rating=2, description="Nie jest ok", date=datetime(2017, 5, 12, hour=21, minute=22, second=37))
]
noOpinions: List[Opinion] = []

orders: Orders = Orders(unpaid=1, unsent=2, refunds=3, pending=4)
noOrders: Orders = Orders(unpaid=0, unsent=0, refunds=0, pending=0)


offers: List[Offer] = [
    Offer(id=0, photoBytes=convertImgToString("chiken.png"), name="Kurczak w sosie własnym", sold=24, turnover=59, views=103),
    Offer(id=1, photoBytes=convertImgToString("chiken.png"), name="Pizza 4 sery - tylko u nas PROMOCJA", sold=32, turnover=21, views=224),
    Offer(id=2, photoBytes=convertImgToString("phone.jpg"), name="Spaghetti prosto z Włoch", sold=100, turnover=2, views=42),
    Offer(id=3, photoBytes=convertImgToString("kaczka.jpg"), name="Sushi z tego dobrego miejsca gdzie są zniżki", sold=101, turnover=103, views=13),
    Offer(id=4, photoBytes=convertImgToString("kaczka.jpg"), name="Chińczyk", sold=6, turnover=12, views=399)
]

noOffers: List[Offer] = []

tipsEng : List[DailyTip] =[
    DailyTip(id=0,tip="Avoid selling low quality items."),
    DailyTip(id=1,tip="Send orders on time. Buyers will surely appreciate your dedication and discipline."),
    DailyTip(id=2,tip="Offer a Fair Return Policy. Buyers  look for sellers who offer a return policy as this builds trust.")

]

tipsPl : List[DailyTip] =[
    DailyTip(id=0,tip="Unikaj sprzedaży produktów o niskiej jakości."),
    DailyTip(id=1,tip="Wysyłaj zamówienia na czas. Kupujący z pewnością docenią Twoje zaangażowanie i dyscyplinę."),
    DailyTip(id=2,tip="Zaoferuj uczciwą politykę zwrotów. Kupujący szukają sprzedawców, którzy oferują zwroty, ponieważ buduje to zaufanie miedzy stronami.")

]

revenue : List[Revenue]=[
    Revenue(id=0,user_id=0,date=datetime(2022, 1, 17,0,0),n=10000000),
    Revenue(id=0,user_id=0,date=datetime(2021, 2, 1,0,0),n=5555),
    Revenue(id=0,user_id=0,date=datetime(2021, 3, 1,0,0),n=4392),
    Revenue(id=0,user_id=0,date=datetime(2021, 4, 1,0,0),n=7431),
    Revenue(id=0,user_id=0,date=datetime(2021, 5, 1,0,0),n=6666),
    Revenue(id=0,user_id=0,date=datetime(2021, 6, 1,0,0),n=4500),
    Revenue(id=0,user_id=0,date=datetime(2021, 7, 1,0,0),n=12453),
    Revenue(id=0,user_id=0,date=datetime(2021, 8, 12,0,0),n=500),
    Revenue(id=0,user_id=0,date=datetime(2021, 8, 1,0,0),n=3000),
    Revenue(id=0,user_id=0,date=datetime(2021, 9, 1,0,0),n=1245),
    Revenue(id=0,user_id=0,date=datetime(2021, 10, 1,0,0),n=8500),
    Revenue(id=0,user_id=0,date=datetime(2021, 11, 1,0,0),n=5000),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 1,0,0),n=12453),
    Revenue(id=0,user_id=0,date=datetime(2022, 12, 1,0,0),n=147),
    Revenue(id=0,user_id=0,date=datetime(2022, 1, 1,0,0),n=147),
    Revenue(id=0,user_id=0,date=datetime(2022, 1, 2,0,0),n=234),
    Revenue(id=0,user_id=0,date=datetime(2022, 1, 3,0,0),n=578),
    Revenue(id=0,user_id=0,date=datetime(2022, 1, 4,0,0),n=90.56),
    Revenue(id=0,user_id=0,date=datetime(2022, 1, 4,0,0),n=1000000),
    Revenue(id=0,user_id=0,date=datetime(2022, 1, 5,0,0),n=123),
    Revenue(id=0,user_id=0,date=datetime(2022, 1, 6,0,17),n=367),
    Revenue(id=0,user_id=0,date=datetime(2022, 1, 7,23,4),n=286),
    Revenue(id=0,user_id=0,date=datetime(2022, 1, 7,0,17),n=286),
    Revenue(id=0,user_id=1,date=datetime(2022, 1, 7,0,17),n=286)
]

turnover : List[Turnover]=[
    Turnover(id=0,user_id=0,date=datetime(2022, 1, 17,0,0),n=10000000),
    Turnover(id=0,user_id=0,date=datetime(2021, 2, 1,0,0),n=5555),
    Turnover(id=0,user_id=0,date=datetime(2021, 3, 1,0,0),n=4392),
    Turnover(id=0,user_id=0,date=datetime(2021, 4, 1,0,0),n=7431),
    Turnover(id=0,user_id=0,date=datetime(2021, 5, 1,0,0),n=6666),
    Turnover(id=0,user_id=0,date=datetime(2021, 6, 1,0,0),n=4500),
    Turnover(id=0,user_id=0,date=datetime(2021, 7, 1,0,0),n=12453),
    Turnover(id=0,user_id=0,date=datetime(2021, 8, 12,0,0),n=500),
    Turnover(id=0,user_id=0,date=datetime(2021, 8, 1,0,0),n=3000),
    Turnover(id=0,user_id=0,date=datetime(2021, 9, 1,0,0),n=1245),
    Turnover(id=0,user_id=0,date=datetime(2021, 10, 1,0,0),n=8500),
    Turnover(id=0,user_id=0,date=datetime(2021, 11, 1,0,0),n=5000),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 1,0,0),n=12453),
    Turnover(id=0,user_id=0,date=datetime(2022, 1, 1,0,0),n=147),
    Turnover(id=0,user_id=0,date=datetime(2022, 1, 2,0,0),n=234),
    Turnover(id=0,user_id=0,date=datetime(2022, 1, 3,0,0),n=578),
    Turnover(id=0,user_id=0,date=datetime(2022, 1, 4,0,0),n=90),
    Turnover(id=0,user_id=0,date=datetime(2022, 1, 4,0,0),n=1000000),
    Turnover(id=0,user_id=0,date=datetime(2022, 1, 5,0,0),n=123),
    Turnover(id=0,user_id=0,date=datetime(2022, 1, 6,0,0),n=367),
    Turnover(id=0,user_id=0,date=datetime(2022, 1, 7,0,0),n=286),
    Turnover(id=0,user_id=1,date=datetime(2022, 1, 7,0,0),n=286)
]


@app.get("/chart/revenue/{id}")
def root(id :int):
    a = list()
    for i in revenue:
        if i.user_id == id:
            a.append(i)
    return a

@app.get("/tips/eng")
def root():
    return tipsEng

@app.get("/tips/pl")
async def root():
    return tipsPl


def getRevenueById(id :int) -> list[Revenue]:
    a = list()
    for i in revenue:
        if i.user_id == id:
            a.append(i)
    return a


def getChartDataCurrentDay(l : List, today :DateTime) -> List:
    h =  [0 for i in range(ceil((today-datetime(today.year,today.month,today.day,0,0,0)).seconds/3600))]
    for i in l :
        if (i.date.year==today.year) & (i.date.month==today.month) & (i.date.day==today.day) :
            h[floor(i.date.hour)] +=i.n
    return h

def getChartDataCurrentYear(l : List, today :DateTime):
    months =  [0 for i in range(today.month)]
    first_day = datetime(today.year,1,1)
    for i in l:
        if (i.date>=first_day) & (i.date<=today):
            months[i.date.month-1] += i.n

    return months

def getChartDataCurrentWeek(l : List, today :DateTime) -> List:
    monday = today - timedelta(days = today.weekday())
    if (today-monday).days == 0:
         days =  [0 for i in range(1)]
    else:
         days =  [0 for i in range((today-monday).days+1)]
    print(len(days))
    for i in l:
        if (i.date >= monday) & (i.date <=today):
            print(i.date.weekday())
            days[i.date.weekday()] += i.n
    return days



def getRevenueById(id :int):
    a = list()
    for i in revenue:
        if i.user_id == id:
            a.append(i)
    return a


@app.get("/chart/revenue/year/")
def root(id :int, date :datetime):
    revenue = getRevenueById(id)
    revenue = getChartDataCurrentYear(revenue,date)
    return revenue

@app.get("/chart/turnover/year/")
def root(id :int, date :datetime):
    revenue = getRevenueById(id)
    revenue = getChartDataCurrentYear(turnover,date)
    return revenue

@app.get("/chart/revenue/week/")
def root(id :int, date :datetime):
    turnover = getRevenueById(id)
    turnover = getChartDataCurrentWeek(revenue,date)
    return turnover

@app.get("/chart/turnover/week/")
def root(id :int, date :datetime):
    turnover = getRevenueById(id)
    turnover = getChartDataCurrentWeek(turnover,date)
    return turnover


@app.get("/chart/revenue/day/")
def root(id :int, date :datetime):
    revenue = getRevenueById(id)
    revenue = getChartDataCurrentDay(revenue,date)
    return revenue

@app.get("/chart/turnover/day/")
def root(id :int, date :datetime):
    turnover = getRevenueById(id)
    turnover = getChartDataCurrentDay(turnover,date)
    return turnover

@app.get("/chart/revenue/{id}")
def root(id :int):
    a = list()
    for i in revenue:
        if i.user_id == id:
            a.append(i)
    return a

@app.get("/tips/eng")
def root():
    return tipsEng

@app.get("/tips/pl")
async def root():
    return tipsPl

@app.get("/opinions")
async def root():
    return opinions

@app.get("/no_opinions")
async def root():
    return noOpinions
    
@app.get("/orders")
async def root():
    return orders
    
@app.get("/no_orders")
async def root():
    return noOrders

@app.get("/offers")
async def root():
    return offers

@app.get("/no_offers")
async def root():
    return noOffers