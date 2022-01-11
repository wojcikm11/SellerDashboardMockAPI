from datetime import datetime
from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Offer, Opinion, Orders, DailyTip
import base64


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
    Offer(id=2, photoBytes=convertImgToString("chiken.png"), name="Spaghetti prosto z Włoch", sold=100, turnover=2, views=42),
    Offer(id=3, photoBytes=convertImgToString("kaczka.jpg"), name="Sushi z tego dobrego miejsca gdzie są zniżki", sold=101, turnover=103, views=13),
    Offer(id=4, photoBytes=convertImgToString("kaczka.jpg"), name="Chińczyk", sold=6, turnover=12, views=399)
]

tipsEng : List[DailyTip] =[
    DailyTip(id=0,tip="Avoid selling low quality items."),
    DailyTip(id=1,tip="Send orders on time. Buyers will surely appreciate your dedication and discipline."),
    DailyTip(id=2,tip="Offer a Fair Return Policy. Buyers  look for sellers who offer a return policy as this builds trust.")

]

@app.get("/tips/eng")
async def root():
    return tipsEng


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