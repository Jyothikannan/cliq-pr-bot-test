def apply_coupon(price, coupon):
    """Apply coupon code to price."""
    coupons = {
        "SAVE10": 0.10,
        "SAVE20": 0.20,
        "FESTIVE30": 0.30
    }

    if coupon not in coupons:
        return price

    return price - (price * coupons[coupon])


def calculate_discount(price, discount_percent):
    """Return final price after discount"""
    if discount_percent < 0 or discount_percent > 100:
        return price
    return price - (price * (discount_percent / 100))
