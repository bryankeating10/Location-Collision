from sqlalchemy import select
import pandas as pd

from app.db.db import get_session
from app.db.models import Testers, Casinos, Accounts, Locations, Actions

default_location = "McDonald's - 99 Washington St"


def main(select_tester: str, select_location: str = default_location):

    sesh = get_session()

    tester = sesh.scalars(
        select(Testers).where(Testers.name == select_tester)
    ).first()

    location = sesh.scalars(
        select(Locations).where(Locations.name == select_location)
    ).first()

    casinos = sesh.scalars(select(Casinos)).all()

    # Get all actions that happened at this location
    actions = sesh.scalars(
        select(Actions).where(Actions.location_id == location.id)
    ).all()

    # Find casinos that were used at this location
    used_casino_ids = set()

    for action in actions:

        account = sesh.scalars(
            select(Accounts).where(Accounts.id == action.account_id)
        ).first()

        used_casino_ids.add(account.casino_id)

    # Build dataframe
    rows = []

    for casino in casinos:

        availability = "Unavailable" if casino.id in used_casino_ids else "Available"

        rows.append({
            "Casino": casino.name,
            "Availability": availability
        })

    avail_df = pd.DataFrame(rows)

    sesh.close()

    return avail_df


if __name__ == '__main__':

    tester = input('\nTester:\n')
    location = input('Location:\n')

    df = main(tester, location)

    print(df)