shippingCostDict = {"Premium Ground Shipping":125}

def askWeight():
    print("please input package weight")
    weight = input()

    return float(weight)


def groundShipping(weight):
    price_per_pound = 0
    flatCharge = 20.0
    if weight <= 2.0:
        price_per_pound = 1.5
    elif 6.0 >= weight > 2.0:
        price_per_pound = 3.00
    elif 10 >= weight > 6.0:
        price_per_pound = 4.00
    else:
        price_per_pound = 4.75
    shippingCostDict.update({"Ground Shipping":price_per_pound + flatCharge})
    return price_per_pound + flatCharge


def droneShipping(weight):
    price_per_pound = 0

    if weight <= 2.0:
        price_per_pound = 4.5
    elif 6.0 >= weight > 2.0:
        price_per_pound = 9.00
    elif 10 >= weight > 6.0:
        price_per_pound = 12.00
    else:
        price_per_pound = 14.25

    shippingCostDict.update({"Drone Shipping":price_per_pound})
    return price_per_pound


def compair():
    weight = askWeight()
    groundShipping(weight)
    droneShipping(weight)
    minPrice = min([shippingCostDict["Ground Shipping"], shippingCostDict["Drone Shipping"], shippingCostDict["Premium Ground Shipping"]])
    print(shippingCostDict.items[minPrice])

compair()
