import requests


valute_lod = {
    "Австралійський долар":"AUD",
    "Канадський долар":"CAD",
    "Юань":"CNY",
    "Чеська крона":"CZK",
    "Данська крона":"DKK",
    "Гонконгівський долар":"HKD",
    "Угорський форинт":"HUF",
    "Індійська рупія":"INR",
    "Індонезійська рупія":"IDR",
    "Ізраїльський шекель":"ILS",
    "Японська єна":"JPY",
    "Казахстанський тенге":"KZT",
    "Південнокорейський вон":"KRW",
    "Мексиканське песо":"MXN",
    "Молдовський лей":"MDL",
    "Новозеландський долар":"NZD",
    "Норвезька крона":"NOK",
    "Сінгапурський долар":"SGD",
    "Південноафриканський ренд":"ZAR",
    "Шведська крона":"SEK",
    "Швейцарський франк":"CHF",
    "Єгипетський фунт":"EGP",
    "Фунт стерлінгів":"GBP",
    "Долар США":"USD",
    "Азербайджанський манат":"AZN",
    "Румунський лей":"RON",
    "Турецька ліра":"TRY",
    "СПЗ ":"XDR",
    "Болгарський лев":"BGN",
    "Євро":"EUR",
    "Польський злотий":"PLN",
    "Алжирський динар":"DZD",
    "Бангладеська така":"BDT",
    "Вірменський драм":"AMD",
    "Домініканське песо":"DOP",
    "Іранський ріал":"IRR",
    "Іракський динар":"IQD",
    "Киргизький сом":"KGS",
    "Ліванський фунт":"LBP",
    "Лівійський динар":"LYD",
    "Малайзійський ринггіт":"MYR",
    "Марокканський дирхам":"MAD",
    "Пакистанська рупія":"PKR",
    "Саудівський ріял":"SAR",
    "Вєтнамський донг":"VND",
    "Тайський бат":"THB",
    "Дирхам ОАЕ":"AED",
    "Туніський динар":"TND",
    "Узбецький сум":"UZS",
    "Тайванський долар":"TWD",
    "Туркменський манат":"TMT",
    "Сербський динар":"RSD",
    "Таджитський сомоні":"TJS",
    "Грузинський ларі":"GEL",
    "Бразильський реал":"BRL",
    "Золото":"XAU",
    "Срібло":"XAG",
    "Платина":"XPT",
    "Паладій":"XPD",

}



valcode = input("Введіть валюту:")
valdata = input("Введіть дату:")



if valcode in valute_lod:
    valcode = valute_lod[valcode]


response = requests.get(
    f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valcode}&date={valdata}&json")

data = response.json()

print(data)
print(data[0]["rate"])


























