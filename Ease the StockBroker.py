def balance_statement(lst):
    if lst == '':
        return 'Buy: 0 Sell: 0'
#     print(lst)
    orders = lst.split(', ')
    bad_formed_orders = []
    bought = 0
    sold = 0
    for i in orders:
        order_details = i.split(' ')
        if len(order_details) < 4 or '.' in order_details[1] or '.' not in order_details[2] or order_details[3] not in ['B', 'S']:
            bad_formed_orders.append(order_details)
        else:
            if order_details[3] == 'B':
                bought += float(order_details[1])*float(order_details[2])
            else:
                sold += float(order_details[1])*float(order_details[2])
                
#     print(bought, sold)
#     print(bad_formed_orders)
    return_str = 'Buy: {0} Sell: {1}'.format(round(bought), round(sold))
    if len(bad_formed_orders) ==0:
        return return_str
    else:
        bad_formed_orders_str = ' ;'.join([' '.join(a) for a in bad_formed_orders])
        return_str  += ('; Badly formed {0}: '.format(len(bad_formed_orders))) + bad_formed_orders_str
        return return_str + ' ;'