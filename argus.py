def calc_cart(*items, **discounts):
    total = 0
    for i, price, qty in items:
        cost = price * qty
        total += cost
        print(f"{i}: ${price} x {qty} = ${cost}")
    
    print(f"Subtotal: ${total}")

    if "discount" in discounts:
        d = discounts["discount"]
        print(f"Yeah... {d}% off!")
        total -= total * (d / 100)

    if "promo_code" in discounts:
        p = discounts["promo_code"]
        print(f"You get ${p} off.")
        total += p

    if "delivery_charge" in discounts:
        charge = discounts["delivery_charge"]
        if total <= 500:
            total += charge
            print(f"Delivery Charge: ${charge}")
        else:
            print("Free Delivery")

    print(f"Total Bill is: ${-total:2f}")

items = [("Apple Airbuds", 10000, 1), ("Samsung S10", 20000, 2), ("Face Wash", 500, 1)]
calc_cart(*items, discount=200, promo_code=20, delivery_charge=100)

