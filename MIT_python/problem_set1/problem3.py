def item_order (order):
    count = order.count ("salad")
    result = "salad:" + str(count)
    count = order.count ("hamburger")
    result = result + " hamburger:" + str(count)
    count = order.count ("water")
    result = result + " water:" + str(count)
    
    return result[:]
    