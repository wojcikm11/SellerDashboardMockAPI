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
    Opinion(id=0, user_id=0, rating=3, description="Produkty wystawione przez sprzedawcę takie sobie, ale za to cena nie jest taka wysoka.", date=datetime(2020, 10, 10, hour=23, minute=54, second=21)),
    Opinion(id=1, user_id=0, rating=4, date=datetime(2021, 5, 12, hour=21, minute=22, second=37)),
    Opinion(id=2, user_id=0, rating=5, description="Cóż napisać ... jestem bardzo zadowolony. Szukałem w sieci różnych rozwiązań i trafiłem przez przypadek na tego sprzedawcę. Po zapoznaniu się z możliwościami sklepu dokonałem zakupu - cena niewielka - w sumie dużo nie ryzykowałem - brak umów więc w razie czego tylko utopione kilka złotych. Jednak się nie zawiodłem. Zarówno możliwości sklepu jak i jego obsługa posprzedaży są na najwyższym poziomie. Właśnie kupuję kolejny towar i jak najbardziej mogę wszystkim polecić. Bardzo dobra cena w stosunku do jakości.", date=datetime(2023, 5, 12, hour=21, minute=22, second=37)),
    Opinion(id=3, user_id=0, rating=1, description="O ile obsługa w sklepie jest ok, o tyle dział rat w arogancki i w ogóle nie wykazujący zainteresowania klientem, obsługa \"z musu\", suma sumarum zrezygnowałem z zakupu produktu, który miałem na oku. A wielka szkoda, bo długo przymierzałem się...", date=datetime(2018, 5, 12, hour=21, minute=22, second=37)),
    Opinion(id=4, user_id=0, rating=3, description="Jest ok", date=datetime(2019, 5, 12, hour=21, minute=22, second=37)),
    Opinion(id=5, user_id=0, rating=2, description="Nie jest ok", date=datetime(2017, 5, 12, hour=21, minute=22, second=37)),
    Opinion(id=6, user_id=0, rating=3, description="Produkty wystawione przez sprzedawcę takie sobie, ale za to cena nie jest taka wysoka.", date=datetime(2020, 10, 10, hour=23, minute=54, second=21)),
    Opinion(id=7, user_id=0, rating=4, date=datetime(2021, 5, 12, hour=21, minute=22, second=37)),
    Opinion(id=8, user_id=0, rating=1, description="Cóż napisać ... jestem bardzo niezadowolony. Szukałem w sieci różnych rozwiązań i trafiłem przez przypadek na tego sprzedawcę. Po zapoznaniu się z możliwościami sklepu dokonałem zakupu - cena niewielka - w sumie dużo nie ryzykowałem - brak umów więc w razie czego tylko utopione kilka złotych. Jednak się nie zawiodłem. Zarówno możliwości sklepu jak i jego obsługa posprzedaży są na najwyższym poziomie. Właśnie kupuję kolejny towar i jak najbardziej mogę wszystkim polecić. Bardzo dobra cena w stosunku do jakości.", date=datetime(2023, 5, 12, hour=21, minute=22, second=37)),
    Opinion(id=9, user_id=0, rating=1, description="O ile obsługa w sklepie jest ok, o tyle dział rat w arogancki i w ogóle nie wykazujący zainteresowania klientem, obsługa \"z musu\", suma sumarum zrezygnowałem z zakupu produktu, który miałem na oku. A wielka szkoda, bo długo przymierzałem się...", date=datetime(2018, 5, 12, hour=21, minute=22, second=37)),
    Opinion(id=10, user_id=0, rating=3, description="Jest ok", date=datetime(2019, 5, 12, hour=21, minute=22, second=37)),
    Opinion(id=11, user_id=0, rating=2, description="Nie jest ok", date=datetime(2017, 5, 12, hour=21, minute=22, second=37))
]
noOpinions: List[Opinion] = []

orders: Orders = Orders(user_id=0, unpaid=1, unsent=2, refunds=3, pending=4)
noOrders: Orders = Orders(user_id=1, unpaid=0, unsent=0, refunds=0, pending=0)
ordersMap = {
    0: orders,
    1: noOrders
}


offers: List[Offer] = [
    Offer(id=0, user_id=0, photoBytes=convertImgToString("chiken.png"), name="Kurczak w sosie własnym", sold=24, turnover=59, views=103),
    Offer(id=1, user_id=0, photoBytes=convertImgToString("chiken.png"), name="Pizza 4 sery - tylko u nas PROMOCJA", sold=32, turnover=21, views=224),
    Offer(id=2, user_id=0, photoBytes=convertImgToString("phone.jpg"), name="Spaghetti prosto z Włoch", sold=100, turnover=2, views=42),
    Offer(id=3, user_id=0, photoBytes=convertImgToString("kaczka.jpg"), name="Sushi z tego dobrego miejsca gdzie są zniżki", sold=101, turnover=103, views=13),
    Offer(id=4, user_id=0, photoBytes=convertImgToString("kaczka.jpg"), name="Chińczyk", sold=6, turnover=12, views=399),
    Offer(id=5, user_id=0, photoBytes=convertImgToString("kaczka.jpg"), name="LOLOLOLO", sold=2, turnover=6, views=100)
]

noOffers: List[Offer] = []

tipsEng : List[DailyTip] =[
    DailyTip(id=0, user_id=0, tip="Avoid selling low quality items."),
    DailyTip(id=1, user_id=0, tip="Send orders on time. Buyers will surely appreciate your dedication and discipline."),
    DailyTip(id=2, user_id=0, tip="Offer a Fair Return Policy. Buyers  look for sellers who offer a return policy as this builds trust.")

]

tipsPl : List[DailyTip] =[
    DailyTip(id=0, user_id=0, tip="Unikaj sprzedaży produktów o niskiej jakości."),
    DailyTip(id=1, user_id=0, tip="Wysyłaj zamówienia na czas. Kupujący z pewnością docenią Twoje zaangażowanie i dyscyplinę."),
    DailyTip(id=2, user_id=0, tip="Zaoferuj uczciwą politykę zwrotów. Kupujący szukają sprzedawców, którzy oferują zwroty, ponieważ buduje to zaufanie miedzy stronami.")

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
    h =  [0 for i in range(24)]
    for i in l :
        if (i.date.year==today.year) & (i.date.month==today.month) & (i.date.day==today.day) :
            h[floor(i.date.hour)] +=i.n
        hours = {i : h[i] for i in range(24)}
    return h

def getChartDataCurrentYear(l : List, today :DateTime):
    months =  [0 for i in range(12)]
    first_day = datetime(today.year,1,1)
    for i in l:
        if (i.date>=first_day) & (i.date<=today):
            months[i.date.month-1] += i.n
    m = {i+1 : months[i] for i in range(12)}
    return m

def getChartDataCurrentWeek(l : List, today :DateTime) -> List:
    monday = today - timedelta(days = today.weekday())
    days =  [0 for i in range(7)]
    for i in l:
        if (i.date >= monday) & (i.date <=today):
            days[i.date.weekday()] += i.n
    d = {i+1 : days[i] for i in range(7)}
    return d



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

@app.get("/tips/eng/{id}")
def root(id: int):
    tipsEngFiltered = list()
    for i in tipsEng:
        if i.user_id == id:
            tipsEngFiltered.append(i)
    return tipsEngFiltered

@app.get("/tips/pl/{id}")
async def root(id: int):
    tipsPlFiltered = list()
    for i in tipsPl:
        if i.user_id == id:
            tipsPlFiltered.append(i)
    return tipsPlFiltered


@app.get("/opinions/{id}")
async def root(id: int):
    opinionsFiltered = list()
    for i in opinions:
        if i.user_id == id:
            opinionsFiltered.append(i)
    return opinionsFiltered

@app.get("/no_opinions/{id}")
async def root(id: int):
    no_opinionsFiltered = list()
    for i in noOpinions:
        if i.user_id == id:
            no_opinionsFiltered.append(i)
    return no_opinionsFiltered
    
@app.get("/orders/{id}")
async def root(id: int):
    return ordersMap[id]
    
@app.get("/no_orders/{id}")
async def root(id: int):
    return ordersMap[id]

@app.get("/offers/{id}")
async def root(id: int):
    offers_filtered = list()
    for i in offers:
        if i.user_id == id:
            offers_filtered.append(i)
    return offers_filtered

@app.get("/no_offers/{id}")
async def root(id: int):
    no_offers_filtered = list()
    for i in noOffers:
        if i.user_id == id:
            no_offers_filtered.append(i)
    return no_offers_filtered