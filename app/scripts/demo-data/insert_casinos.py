import pandas as pd
from pathlib import Path
from app.db.crud import create_casino

PATH = Path(__file__).parent / 'demo-data' / 'casino_demo.csv'

df = pd.read_csv(PATH)
df = df.drop(columns=['id', 'created_at', 'updated_at'])


for row in df.to_dict(orient="records"):
    print(row)
    create_casino(**row)