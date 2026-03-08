from db import get_session
from datetime import datetime

# Add quant
from models import Quants

def create_quant(name: str):
    sesh = get_session()

    new_quant = Quants(
        name=name,
        created_at=datetime.now()
    )

    sesh.add(new_quant)
    sesh.commit()
    sesh.refresh(new_quant)
    sesh.close()

    return new_quant

# Add tester
from models import Testers

def create_tester(name: str, quant_id: int):
    sesh = get_session()

    new_tester = Testers(
        name=name,
        assigned_quant=quant_id,
        created_at=datetime.now()
    )

    sesh.add(new_tester)
    sesh.commit()
    sesh.refresh(new_tester)
    sesh.close()

    return new_tester

# Add casino
from models import Casinos

def create_casino(
        name: str,
        network: str = None,
        signup_rest: bool = False,
        deposit_rest: bool = False,
        play_rest: bool = False,
        withdrawal_rest: bool = False,
        network_rest: bool = False):
    
    sesh = get_session()

    new_casino = Casinos(
        name=name,
        network=network,
        signup_rest=signup_rest,
        deposit_rest=deposit_rest,
        play_rest=play_rest,
        withdrawal_rest=withdrawal_rest,
        network_rest=network_rest,
        created_at=datetime.now()
    )