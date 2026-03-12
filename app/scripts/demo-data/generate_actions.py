from sqlalchemy import select
from random import choices

from app.db.db import get_session
from app.db.crud import create_action
from app.db.models import Accounts, Locations

# Actions and their rough relative frequencies
actions = ['signup','deposit','play','withdraw']
weights = [3,4,7,2]

def main(accounts,locations):
    for acc in accounts:
        act = choices(actions,weights=weights,k=1)[0]
        create_action(
            category=act,
            account_id=acc.id,
            location=choices(locations,k=1)[0]
        )

if __name__ == '__main__':
    sesh = get_session()

    accounts = sesh.scalars(select(Accounts)).all()
    locations = sesh.scalars(select(Locations)).all()

    main(accounts=accounts,locations=locations)