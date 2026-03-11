from sqlalchemy import text
from random import randint

from app.db.db import get_session
from app.db.crud import create_account


def gen_username(name):
    return f"{name}_{randint(1000,9999)}"


def main(testers, casinos):
    for tester in testers:
        for casino in casinos:
            username = gen_username(tester["name"])

            create_account(
                tester_id=tester["id"],
                casino_id=casino["id"],
                username=username
            )


if __name__ == "__main__":
    sesh = get_session()

    testers = list(sesh.execute(text("SELECT id, name FROM testers")).mappings())
    casinos = list(sesh.execute(text("SELECT id FROM casinos")).mappings())

    main(testers, casinos)

    print("Success! ✅")