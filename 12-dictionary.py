computer_lab = {
    'table': 'wood','amount':5000 , 'floting':'plastic'
}
currency_rates={
    'PKR':80 , 'CAD':250 , 'JPY':77
}
# if 'catogeries' not in computer_lab:
#     print("product not found")
# print('table' in computer_lab)
# print('catogeries' in computer_lab)
# print(computer_lab)
is_in_dict_1='amount'in computer_lab
is_in_dict_2='PKR' in currency_rates

if is_in_dict_1:
    copyright= computer_lab['amount']
    print(copyright)

if is_in_dict_2:
    heyjerry= currency_rates['PKR']
    print(heyjerry)

if is_in_dict_1 and is_in_dict_2:
    converted_price=copyright*heyjerry
    print(converted_price)