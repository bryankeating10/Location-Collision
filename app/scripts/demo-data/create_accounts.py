from sqlalchemy import select
from random import randint

from app.db.db import get_session
from app.db.crud import create_account
from app.db.models import Testers, Casinos

def gen_username(name):
    return f"{name}_{randint(1000,9999)}"

def main(testers, casinos):
    for tester in testers:
        for casino in casinos:
            username = gen_username(tester.name)

            create_account(
                tester_id=tester.id,
                casino_id=casino.id,
                username=username
            )


if __name__ == "__main__":
    sesh = get_session()

    testers = sesh.scalars(select(Testers)).all()
    casinos = sesh.scalars(select(Casinos)).all()

    main(testers, casinos)

    print("Success! ✅")