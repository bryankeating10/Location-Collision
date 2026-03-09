from app.db.db import get_session
from datetime import datetime

# Add quant
from .models import Quants

def create_quant(name: str):
    sesh = get_session()

    quant = Quants(
        name=name,
        created_at=datetime.now()
    )

    sesh.add(quant)
    sesh.commit()
    sesh.refresh(quant)
    sesh.close()

    return quant

# Add tester
from .models import Testers

def create_tester(name: str, quant_id: int):
    sesh = get_session()

    tester = Testers(
        name=name,
        assigned_quant=quant_id,
        created_at=datetime.now()
    )

    sesh.add(tester)
    sesh.commit()
    sesh.refresh(tester)
    sesh.close()

    return tester

# Add casino
from .models import Casinos

def create_casino(
        name: str,
        network: str = None,
        signup_rest: bool = False,
        deposit_rest: bool = False,
        play_rest: bool = False,
        withdrawal_rest: bool = False,
        network_rest: bool = False):
    
    sesh = get_session()

    casino = Casinos(
        name=name,
        network=network,
        signup_rest=signup_rest,
        deposit_rest=deposit_rest,
        play_rest=play_rest,
        withdrawal_rest=withdrawal_rest,
        network_rest=network_rest,
        created_at=datetime.now()
    )

    sesh.add(casino)
    sesh.commit()
    sesh.refresh(casino)
    sesh.close()

    return casino

# Add account
from .models import Accounts

def create_account(tester_id, casino_id, username: str = None):
    sesh = get_session()

    account = Accounts(
        tester_id=tester_id,
        casino_id=casino_id,
        username=username,
        created_at=datetime.utcnow()
    )

    sesh.add(account)
    sesh.commit()
    sesh.refresh(account)

    sesh.close()
    return account

# Add location
from .models import Locations

def create_location(name, address, longitude, latitude):
    sesh = get_session()

    location = Locations(
        name=name,
        address=address,
        longitude=longitude,
        latitude=latitude,
        created_at=datetime.now()
    )

    sesh.add(location)
    sesh.commit()
    sesh.refresh(location)

    sesh.close()
    return location

# Add action
from .models import Actions

def create_action(category, account_id, location_id):
    sesh = get_session()

    action = Actions(
        category=category,
        account_id=account_id,
        location_id=location_id,
        timestamp=datetime.now()
    )

    sesh.add(action)
    sesh.commit()
    sesh.refresh(action)
    sesh.close()

    return action