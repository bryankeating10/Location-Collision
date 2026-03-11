from app.db.db import get_session
from app.db.crud import create_account
from sqlalchemy import text
from random import randint

# Create a random username
def gen_username(name):
    return f"{name}_{randint(1000,9999)}"

# Create demo accounts
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

    testers = sesh.execute(text('SELECT * FROM testers;'))
    casinos = sesh.execute(text('SELECT * FROM casinos;'))

    main(testers,casinos)

    print('Success! green checkmark')