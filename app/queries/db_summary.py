from sqlalchemy import text
from app.db.db import get_session

def get_summary():
    sesh = get_session()

    quant_count = sesh.execute(
        text('SELECT COUNT(*) FROM quants')
    )

    tester1_name = sesh.execute(
        text('SELECT name FROM testers WHERE id = 1')
    )

    casino1_name = sesh.execute(
        text('SELECT name FROM casinos WHERE id = 1')
    )

    long1 = sesh.execute(
        text('SELECT longitude FROM locations WHERE id = 1')
    )

    lat1 = sesh.execute(
        text('SELECT latitude FROM locations WHERE id = 1')
    )

    account1_user = sesh.execute(
        text('''SELECT username FROM accounts
             WHERE id = 1''')
    )

    action1_cat = sesh.execute(
        text('''SELECT category FROM actions
             WHERE id = 1''')
    )

    result = (
        quant_count.fetchone()[0],
        tester1_name.fetchone()[0],
        casino1_name.fetchone()[0],
        long1.fetchone()[0],
        lat1.fetchone()[0],
        account1_user.fetchone()[0]
    )

    print(sesh.execute(text("SELECT * FROM actions")).fetchall())

    sesh.close()
    return result


summary = get_summary()

print(f'There are {summary[0]} quants, the first tester is named {summary[1]}, playing on {summary[2]} casino.')
print(f'The coordinates are {summary[3]}, {summary[4]}')



# print(f'The first account username is {summary[5]} and the first action category is {summary[6]}.')