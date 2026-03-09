from app.db.crud import create_location
import pandas as pd
from pathlib import Path

# DATA PATH
PATH = Path(__file__).parent / 'location_demo.csv'
df = pd.read_csv(PATH)
print(df.head())

for _,row in df.iterrows():
    create_location(
        name=row['name'],
        address=row['address'],
        longitude=row['longitude'],
        latitude=row['latitude']
    )