import requests
import pandas as pd
import json

# metadata del bulk de Scryfall
bulk_url = "https://api.scryfall.com/bulk-data/default_cards"
bulk_info = requests.get(bulk_url).json()

#Descargar archivo json de mtg
download_uri = bulk_info["download_uri"]
print("Descargando dataset desde:", download_uri)
cards = requests.get(download_uri).json()

#Guardar como json local
with open("cartas.json", "w", encoding="utf-8") as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)
print("✅ Archivo cartas.json generado")

#Convertir json a csv usando pandas
df = pd.json_normalize(cards)
df.to_csv("cartas.csv", index=False, encoding="utf-8")
print("Archivo cartas.csv generado con", len(df), "cartas")