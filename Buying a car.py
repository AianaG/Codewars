def nbMonths(startPriceOld, startPriceNew, savingperMonth, percentLossByMonth):
    # your code
    month = 0
    available = startPriceOld - startPriceNew
    savings = 0
    while available <0:
        month += 1
        if month%2 ==0:
            percentLossByMonth += 0.5
#         print(percentLossByMonth)
        
        startPriceOld = startPriceOld*(1- percentLossByMonth*0.01)
        startPriceNew = startPriceNew*(1- percentLossByMonth*0.01)
        savings += savingperMonth
        available = (savings + startPriceOld) - startPriceNew
        
    return [month, round(available, 0)]