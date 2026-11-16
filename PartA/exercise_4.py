def movie_ticket_price(
        num_children: int,
        num_adults: int,
        num_seniors: int,
        show_time: int
    ) -> float | None: # float or none (| is or)

    adult_price = 15
    senior_price = 12
    half_senior_price = senior_price / 2
    child_price = 5

    # No negative inputs
    if num_children < 0 or num_adults < 0 or num_seniors < 0 or show_time < 0:
        return None

    if show_time < 15:
        discount = 0.05 
    else:
        discount = 0.0
        
    paying_children = num_children
    paying_seniors = num_seniors
    senior_cost = 0.0

    if num_adults >= 2:
        paying_children -= min(paying_children, 2)

        if num_seniors >= 1:
            paying_seniors -= 1
            senior_cost = half_senior_price

    elif num_seniors >= 1:
        paying_children -= min(paying_children, 1)

    senior_cost += paying_seniors * senior_price

    price_before_discount = (num_adults * adult_price + senior_cost + paying_children * child_price)
    price = price_before_discount * (1 - discount)

    return round(price, 2)
