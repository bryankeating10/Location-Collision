from app.db.crud import create_quant
import pandas as pd
from pathlib import Path

# DATA PATH
PATH = Path(__file__).parent / 'quant_demo.csv'

# Read to dataframe
df = pd.read_csv(PATH)

# Insert quants into db
for quant in df["quant"]:
    print(quant)
    create_quant(name=quant)