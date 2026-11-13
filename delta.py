import pandas as pd
from deltalake import write_deltalake

dane_gios = [
	{"stacja_id": 101, "miasto": "Poznań", "pm10": 34.5, "lat": 52.4064, "lon": 16.9252, "data": "2026-11-13"}
]

df = pd.DataFrame(dane_gios)

write_deltalake("./data_lake/gios_bronze", df, mode="append")
print("Zapisano w Delta Lake.")
