import requests
import pandas as pd
from datetime import datetime,timedelta
def createData():
    #temp maxima e minima,velocidade maxima do vento, umidade, chance de chuva e o content
    
    temp_max = list()
    temp_min = list()
    vel_max = list()
    umidade = list()
    chance_chuva = list()
    content = list()
    date = datetime.today()
    key= "f2aa47a175bb4c2da3103809260301"
    for i in range(0,9):
        today = date - timedelta(days=i)
        url = f"http://api.weatherapi.com/v1/history.json?key={key}&q=Brazil&dt={today.year}-{today.month}-{today.day}&lang=pt"

        url_conteudo = requests.get(url)
        print("\n\n",url_conteudo.json())
        temp_max.append(url_conteudo.json()["forecast"]["forecastday"][0]["day"]["maxtemp_c"])
        temp_min.append(url_conteudo.json()["forecast"]["forecastday"][0]["day"]["mintemp_c"])

        vel_max.append(url_conteudo.json()["forecast"]["forecastday"][0]["day"]["maxwind_kph"])

        umidade.append(url_conteudo.json()["forecast"]["forecastday"][0]["day"]["avghumidity"])

        chance_chuva.append(url_conteudo.json()["forecast"]["forecastday"][0]["day"]["daily_chance_of_rain"])

        content.append(url_conteudo.json()["forecast"]["forecastday"][0]["day"]["condition"]["text"])

    data ={
        "temp_max": temp_max,
        "temp_min": temp_min,
        "vel_max": vel_max,
        "umidade": umidade,
        "chance_chuva": chance_chuva,
        "content": content
    }
        
    df = pd.DataFrame(data)
    df.to_csv("data.csv",sep="\t",encoding="utf-8")

createData()