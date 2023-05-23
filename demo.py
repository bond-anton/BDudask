from udask import lib, check_error

print('Check new module', lib)
card = lib.UD_Register_Card(1, 1)
print('Registered card:', card)
if card < 0:
    print('ERROR:', check_error(card)['description'])
else:
    card = lib.UD_Release_Card(card)
    print('Released card:', card)
