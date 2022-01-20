from datetime import datetime
from math import ceil, floor
from typing import List
from xmlrpc.client import DateTime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Offer, Opinion, Orders, DailyTip,Revenue,Turnover, User
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
    Opinion(id=11, user_id=0, rating=2, description="Nie jest ok", date=datetime(2017, 5, 12, hour=21, minute=22, second=37)),

    Opinion(id=12, user_id=1, rating=3, date=datetime(2020, 6, 4, hour=12, minute=8, second=34), description='ok'),
    Opinion(id=13, user_id=1, rating=3, date=datetime(2020, 6, 4, hour=12, minute=8, second=34), description='ok'),
    Opinion(id=14, user_id=1, rating=3, date=datetime(2020, 6, 4, hour=12, minute=8, second=34), description='ok'),
    Opinion(id=15, user_id=1, rating=3, date=datetime(2020, 6, 4, hour=12, minute=8, second=34), description='ok'),
    Opinion(id=16, user_id=1, rating=3, date=datetime(2020, 6, 4, hour=12, minute=8, second=34), description='ok'),
    Opinion(id=17, user_id=1, rating=3, date=datetime(2020, 6, 4, hour=12, minute=8, second=34), description='ok'),

    Opinion(id=12, user_id=2, rating=3, date=datetime(2020, 6, 4, hour=12, minute=8, second=34), description='ok'),
    Opinion(id=13, user_id=2, rating=3, date=datetime(2020, 6, 4, hour=12, minute=8, second=34), description='ok'),
    Opinion(id=14, user_id=2, rating=3, date=datetime(2020, 6, 4, hour=12, minute=8, second=34), description='ok'),
    Opinion(id=15, user_id=2, rating=3, date=datetime(2020, 6, 4, hour=12, minute=8, second=34), description='ok'),
    Opinion(id=16, user_id=2, rating=3, date=datetime(2020, 6, 4, hour=12, minute=8, second=34), description='ok'),
    Opinion(id=17, user_id=2, rating=3, date=datetime(2020, 6, 4, hour=12, minute=8, second=34), description='ok')
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

users : List[User] =[
    User(id=0, username="ms@platform", password="1234", name="Megan Three Stalion"),
    User(id=1, username="mg@platform", password="2345", name="Magda Gesler"),
    User(id=2, username="hp@platform", password="3456", name="Harry Potter")
]

revenue : List[Revenue]=[
# user 1
#   hours
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 9,23,43),n=66),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 9,22,43),n=106.74),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 9,21,43),n=100),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 9,20,43),n=909),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 9,19,43),n=0),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 9,18,43),n=20),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 9,17,43),n=10.24),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 9,16,43),n=36),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 9,15,43),n=45),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 9,14,43),n=40),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 9,13,43),n=36),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 9,12,43),n=56),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 9,11,43),n=0),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 9,10,43),n=87),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 9,9,43),n=90),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 9,8,43),n=66),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 9,7,43),n=55),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 9,6,43),n=0),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 9,5,43),n=0),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 9,4,43),n=0),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 9,2,43),n=6),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 9,1,43),n=10),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 9,0,43),n=12),

#   days
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 1,0,0),n=1000),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 1,0,0),n=147),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 2,0,0),n=234),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 3,0,0),n=578),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 4,0,0),n=90),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 4,0,0),n=100),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 5,0,0),n=123),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 6,0,0),n=367),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 7,0,0),n=286),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 8,0,0),n=121),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 9,0,0),n=200),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 10,0,0),n=200),
#     months
    Revenue(id=0,user_id=0,date=datetime(2021, 1, 7,0,0),n=667),
    Revenue(id=0,user_id=0,date=datetime(2021, 2, 7,0,0),n=740),
    Revenue(id=0,user_id=0,date=datetime(2021, 3, 7,0,0),n=157),
    Revenue(id=0,user_id=0,date=datetime(2021, 4, 7,0,0),n=357),
    Revenue(id=0,user_id=0,date=datetime(2021, 5, 7,0,0),n=299),
    Revenue(id=0,user_id=0,date=datetime(2021,6, 7,0,0),n=500),
    Revenue(id=0,user_id=0,date=datetime(2021, 7, 6,0,0),n=333),
    Revenue(id=0,user_id=0,date=datetime(2021, 8, 5,0,0),n=833),
    Revenue(id=0,user_id=0,date=datetime(2021, 9, 4,0,0),n=456),
    Revenue(id=0,user_id=0,date=datetime(2021, 10, 3,0,0),n=233),
    Revenue(id=0,user_id=0,date=datetime(2021, 11, 2,0,0),n=833),
    Revenue(id=0,user_id=0,date=datetime(2021, 12, 1,0,0),n=733),


# user 2
#   hours
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 9,23,43),n=66),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 9,22,43),n=10),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 9,21,43),n=100),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 9,20,43),n=16),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 9,19,43),n=0),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 9,18,43),n=0),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 9,17,43),n=0),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 9,16,43),n=36),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 9,15,43),n=5),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 9,14,43),n=4),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 9,13,43),n=36),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 9,12,43),n=56),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 9,11,43),n=0),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 9,10,43),n=7),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 9,9,43),n=29),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 9,8,43),n=46),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 9,7,43),n=52),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 9,6,43),n=0),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 9,5,43),n=47),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 9,4,43),n=0),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 9,2,43),n=6),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 9,1,43),n=20),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 9,0,43),n=12),

#   days
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 1,0,0),n=1000),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 1,0,0),n=237),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 2,0,0),n=94),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 3,0,0),n=58),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 4,0,0),n=290),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 4,0,0),n=170),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 5,0,0),n=823),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 6,0,0),n=87),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 7,0,0),n=286),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 8,0,0),n=441),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 9,0,0),n=230),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 10,0,0),n=100),
#     months
    Revenue(id=0,user_id=1,date=datetime(2021, 1, 7,0,0),n=777),
    Revenue(id=0,user_id=1,date=datetime(2021, 2, 7,0,0),n=540),
    Revenue(id=0,user_id=1,date=datetime(2021, 3, 7,0,0),n=457),
    Revenue(id=0,user_id=1,date=datetime(2021, 4, 7,0,0),n=357),
    Revenue(id=0,user_id=1,date=datetime(2021, 5, 7,0,0),n=123),
    Revenue(id=0,user_id=1,date=datetime(2021,6, 7,0,0),n=499),
    Revenue(id=0,user_id=1,date=datetime(2021, 7, 6,0,0),n=373),
    Revenue(id=0,user_id=1,date=datetime(2021, 8, 5,0,0),n=233),
    Revenue(id=0,user_id=1,date=datetime(2021, 9, 4,0,0),n=756),
    Revenue(id=0,user_id=1,date=datetime(2021, 10, 3,0,0),n=933),
    Revenue(id=0,user_id=1,date=datetime(2021, 11, 2,0,0),n=333),
    Revenue(id=0,user_id=1,date=datetime(2021, 12, 1,0,0),n=433),


    # user 3
    #   hours
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 9,23,43),n=10),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 9,22,43),n=70),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 9,21,43),n=34),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 9,20,43),n=57),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 9,19,43),n=13),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 9,18,43),n=86),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 9,17,43),n=22),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 9,16,43),n=57),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 9,15,43),n=74),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 9,14,43),n=49),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 9,13,43),n=97),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 9,12,43),n=35),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 9,11,43),n=24),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 9,10,43),n=24),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 9,9,43),n=25),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 9,8,43),n=14),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 9,7,43),n=45),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 9,6,43),n=23),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 9,5,43),n=46),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 9,4,43),n=23),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 9,2,43),n=45),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 9,1,43),n=0),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 9,0,43),n=23),

    #   days
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 1,0,0),n=340),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 1,0,0),n=73),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 2,0,0),n=321),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 3,0,0),n=456),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 4,0,0),n=0),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 4,0,0),n=199),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 5,0,0),n=223),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 6,0,0),n=567),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 7,0,0),n=486),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 8,0,0),n=321),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 9,0,0),n=290),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 10,0,0),n=150),
    #     months
        Revenue(id=0,user_id=2,date=datetime(2021, 1, 7,0,0),n=787),
        Revenue(id=0,user_id=2,date=datetime(2021, 2, 7,0,0),n=600),
        Revenue(id=0,user_id=2,date=datetime(2021, 3, 7,0,0),n=457),
        Revenue(id=0,user_id=2,date=datetime(2021, 4, 7,0,0),n=157),
        Revenue(id=0,user_id=2,date=datetime(2021, 5, 7,0,0),n=799),
        Revenue(id=0,user_id=2,date=datetime(2021,6, 7,0,0),n=444),
        Revenue(id=0,user_id=2,date=datetime(2021, 7, 6,0,0),n=133),
        Revenue(id=0,user_id=2,date=datetime(2021, 8, 5,0,0),n=433),
        Revenue(id=0,user_id=2,date=datetime(2021, 9, 4,0,0),n=756),
        Revenue(id=0,user_id=2,date=datetime(2021, 10, 3,0,0),n=333),
        Revenue(id=0,user_id=2,date=datetime(2021, 11, 2,0,0),n=333),
        Revenue(id=0,user_id=2,date=datetime(2021, 12, 1,0,0),n=533),


]

turnover : List[Turnover]=[

# user 1
#   hours
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 9,23,43),n=66),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 9,22,43),n=90),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 9,21,43),n=10),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 9,20,43),n=89),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 9,19,43),n=0),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 9,18,43),n=20),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 9,17,43),n=10),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 9,16,43),n=36),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 9,15,43),n=45),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 9,14,43),n=40),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 9,13,43),n=36),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 9,12,43),n=56),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 9,11,43),n=0),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 9,10,43),n=87),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 9,9,43),n=90),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 9,8,43),n=66),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 9,7,43),n=55),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 9,6,43),n=0),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 9,5,43),n=0),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 9,4,43),n=0),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 9,2,43),n=6),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 9,1,43),n=10),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 9,0,43),n=12),

#   days
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 1,0,0),n=1000),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 1,0,0),n=147),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 2,0,0),n=234),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 3,0,0),n=578),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 4,0,0),n=90),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 4,0,0),n=100),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 5,0,0),n=123),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 6,0,0),n=367),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 7,0,0),n=286),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 8,0,0),n=121),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 9,0,0),n=200),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 10,0,0),n=200),
#     months
    Turnover(id=0,user_id=0,date=datetime(2021, 1, 7,0,0),n=667),
    Turnover(id=0,user_id=0,date=datetime(2021, 2, 7,0,0),n=740),
    Turnover(id=0,user_id=0,date=datetime(2021, 3, 7,0,0),n=157),
    Turnover(id=0,user_id=0,date=datetime(2021, 4, 7,0,0),n=357),
    Turnover(id=0,user_id=0,date=datetime(2021, 5, 7,0,0),n=299),
    Turnover(id=0,user_id=0,date=datetime(2021,6, 7,0,0),n=500),
    Turnover(id=0,user_id=0,date=datetime(2021, 7, 6,0,0),n=333),
    Turnover(id=0,user_id=0,date=datetime(2021, 8, 5,0,0),n=833),
    Turnover(id=0,user_id=0,date=datetime(2021, 9, 4,0,0),n=456),
    Turnover(id=0,user_id=0,date=datetime(2021, 10, 3,0,0),n=233),
    Turnover(id=0,user_id=0,date=datetime(2021, 11, 2,0,0),n=833),
    Turnover(id=0,user_id=0,date=datetime(2021, 12, 1,0,0),n=733),


# user 2
#   hours
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 9,23,43),n=66),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 9,22,43),n=10),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 9,21,43),n=100),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 9,20,43),n=16),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 9,19,43),n=0),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 9,18,43),n=0),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 9,17,43),n=0),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 9,16,43),n=36),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 9,15,43),n=5),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 9,14,43),n=4),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 9,13,43),n=36),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 9,12,43),n=56),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 9,11,43),n=0),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 9,10,43),n=7),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 9,9,43),n=29),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 9,8,43),n=46),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 9,7,43),n=52),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 9,6,43),n=0),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 9,5,43),n=47),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 9,4,43),n=0),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 9,2,43),n=6),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 9,1,43),n=20),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 9,0,43),n=12),

#   days
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 1,0,0),n=1000),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 1,0,0),n=237),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 2,0,0),n=94),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 3,0,0),n=58),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 4,0,0),n=290),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 4,0,0),n=170),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 5,0,0),n=823),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 6,0,0),n=87),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 7,0,0),n=286),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 8,0,0),n=441),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 9,0,0),n=230),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 10,0,0),n=100),
#     months
    Turnover(id=0,user_id=1,date=datetime(2021, 1, 7,0,0),n=777),
    Turnover(id=0,user_id=1,date=datetime(2021, 2, 7,0,0),n=540),
    Turnover(id=0,user_id=1,date=datetime(2021, 3, 7,0,0),n=457),
    Turnover(id=0,user_id=1,date=datetime(2021, 4, 7,0,0),n=357),
    Turnover(id=0,user_id=1,date=datetime(2021, 5, 7,0,0),n=123),
    Turnover(id=0,user_id=1,date=datetime(2021,6, 7,0,0),n=499),
    Turnover(id=0,user_id=1,date=datetime(2021, 7, 6,0,0),n=373),
    Turnover(id=0,user_id=1,date=datetime(2021, 8, 5,0,0),n=233),
    Turnover(id=0,user_id=1,date=datetime(2021, 9, 4,0,0),n=756),
    Turnover(id=0,user_id=1,date=datetime(2021, 10, 3,0,0),n=933),
    Turnover(id=0,user_id=1,date=datetime(2021, 11, 2,0,0),n=333),
    Turnover(id=0,user_id=1,date=datetime(2021, 12, 1,0,0),n=433),


    # user 3
    #   hours
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 9,23,43),n=10),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 9,22,43),n=70),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 9,21,43),n=34),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 9,20,43),n=57),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 9,19,43),n=13),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 9,18,43),n=86),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 9,17,43),n=22),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 9,16,43),n=57),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 9,15,43),n=74),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 9,14,43),n=49),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 9,13,43),n=97),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 9,12,43),n=35),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 9,11,43),n=24),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 9,10,43),n=24),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 9,9,43),n=25),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 9,8,43),n=14),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 9,7,43),n=45),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 9,6,43),n=23),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 9,5,43),n=46),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 9,4,43),n=23),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 9,2,43),n=45),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 9,1,43),n=0),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 9,0,43),n=23),

    #   days
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 1,0,0),n=340),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 1,0,0),n=73),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 2,0,0),n=321),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 3,0,0),n=456),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 4,0,0),n=0),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 4,0,0),n=199),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 5,0,0),n=223),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 6,0,0),n=567),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 7,0,0),n=486),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 8,0,0),n=321),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 9,0,0),n=290),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 10,0,0),n=150),
    #     months
        Turnover(id=0,user_id=2,date=datetime(2021, 1, 7,0,0),n=787),
        Turnover(id=0,user_id=2,date=datetime(2021, 2, 7,0,0),n=600),
        Turnover(id=0,user_id=2,date=datetime(2021, 3, 7,0,0),n=457),
        Turnover(id=0,user_id=2,date=datetime(2021, 4, 7,0,0),n=157),
        Turnover(id=0,user_id=2,date=datetime(2021, 5, 7,0,0),n=799),
        Turnover(id=0,user_id=2,date=datetime(2021,6, 7,0,0),n=444),
        Turnover(id=0,user_id=2,date=datetime(2021, 7, 6,0,0),n=133),
        Turnover(id=0,user_id=2,date=datetime(2021, 8, 5,0,0),n=433),
        Turnover(id=0,user_id=2,date=datetime(2021, 9, 4,0,0),n=756),
        Turnover(id=0,user_id=2,date=datetime(2021, 10, 3,0,0),n=333),
        Turnover(id=0,user_id=2,date=datetime(2021, 11, 2,0,0),n=333),
        Turnover(id=0,user_id=2,date=datetime(2021, 12, 1,0,0),n=533),


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
    print('monday'+str(monday))
    days =  [0 for i in range(7)]
    print(today)
    for i in l:
        print(str(i.date)+'>'+str(monday)+str(i.date >= monday))
        if (i.date.weekday() >= monday.weekday()) & (i.date.weekday() <=today.weekday()):
            days[i.date.weekday()] += i.n
    d = {i+1 : days[i] for i in range(7)}
    return d



def getRevenueById(id :int):
    a = list()
    for i in revenue:
        if i.user_id == id:
            a.append(i)
    return a

def getTurnoverById(id :int):
    a = list()
    for i in turnover:
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
    revenue = getTurnoverById(id)
    revenue = getChartDataCurrentYear(turnover,date)
    return revenue

@app.get("/chart/revenue/week/")
def root(id :int, date :datetime):
    turnover = getRevenueById(id)
    turnover = getChartDataCurrentWeek(revenue,date)
    return turnover

@app.get("/chart/turnover/week/")
def root(id :int, date :datetime):
    turnover = getTurnoverById(id)
    turnover = getChartDataCurrentWeek(turnover,date)
    return turnover


@app.get("/chart/revenue/day/")
def root(id :int, date :datetime):
    revenue = getRevenueById(id)
    revenue = getChartDataCurrentDay(revenue,date)
    return revenue

@app.get("/chart/turnover/day/")
def root(id :int, date :datetime):
    turnover = getTurnoverById(id)
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
    
@app.get("/user")
async def root():
    return users
