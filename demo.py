from udask import lib, check_error

print('Check new module', lib)
card_type = lib.USB_1902  # You can also use USB_1903 or USB_1901
card_num = 0
card = lib.UD_Register_Card(card_type, card_num)
print('Registered card:', card)
if card < 0:
    print('ERROR:', check_error(card)['description'])
else:
    card = lib.UD_Release_Card(card)
    print('Released card:', card)
