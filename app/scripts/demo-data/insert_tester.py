from app.db.crud import create_tester
import pandas as pd
from pathlib import Path
from sqlalchemy import text
from app.db.db import get_session

# DATA PATH
PATH = Path(__file__).parent / 'tester_demo.csv'
df = pd.read_csv(PATH)

def rand_quant(session):
    result = session.execute(
        text('SELECT id FROM quants ORDER BY RANDOM() LIMIT 1;')
    )
    
    return result.fetchone()[0]

sesh = get_session()

for _,row in df.iterrows():
    quant_id = rand_quant(sesh)
    create_tester(
        name=row['tester'],
        quant_id=quant_id
    )
sesh.commit()
sesh.close()