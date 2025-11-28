def calculate_discount(price, discount_percent):
    """
    Return the price after applying a discount.

    Args:
        price (float): Original price
        discount_percent (float): Discount percentage (0 to 100)

    Returns:
        float: Final price after discount
    """
    if not (0 <= discount_percent <= 100):
        raise ValueError("Discount percent must be between 0 and 100")

    discount_amount = price * (discount_percent / 100)
    return price - discount_amount


def apply_coupon(price, coupon_code):
    """
    Apply a coupon code and return the discounted price.

    Supported coupons:
    - SAVE10: 10%
    - SAVE20: 20%
    - FESTIVE30: 30%
    """
    coupons = {
        "SAVE10": 10,
        "SAVE20": 20,
        "FESTIVE30": 30
    }

    if coupon_code not in coupons:
        return price

    percent = coupons[coupon_code]
    return calculate_discount(price, percent)
