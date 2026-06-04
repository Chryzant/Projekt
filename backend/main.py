from fastapi import FastAPI
import requests

app = FastAPI(title="Currency API")

@app.get("/currencies")
def get_currencies():
    # Odpytujemy API NBP o tabelę A (średnie kursy walut) w formacie JSON
    url = "http://api.nbp.pl/api/exchangerates/tables/A/?format=json"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    
    return {"error": "Nie udało się połączyć z NBP"}
