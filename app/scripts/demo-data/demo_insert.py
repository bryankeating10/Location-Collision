from app.db.crud import create_quant, create_tester, \
    create_casino, create_account, create_location, \
    create_action

# Add quant
quant1 = create_quant(name='Bryan')

# Add tester
tester1 = create_tester(name='Moses', quant_id=quant1.id)

# Add casino
casino1 = create_casino("DraftKings", "DK")

# Add account
account1 = create_account(tester_id=tester1.id, casino_id=casino1.id, username='moses3242')

# Add location
location1 = create_location(name='Starbucks', address='123 Main St, Butler, NJ', longitude=-75.3210242893, latitude=40.8530201337)

# Add action
action1 = create_action(category='signup', account_id=account1.id, location_id=location1.id)