def movie_ticket_price(
        num_children: int,
        num_adults: int,
        num_seniors: int,
        show_time: int
    ) -> float:
    # No negative inputs
    if num_children < 0 or num_adults < 0 or num_seniors < 0 or show_time < 0:
        return None

    full_cost_children = num_children
    full_cost_adults = num_adults
    full_cost_seniors = num_seniors
    
    discount: float = 0.0
    if 0 <= show_time < 15:
        discount = 0.05

    if num_adults >= 2:
        if full_cost_children >= 2:
            full_cost_children -= 2
        else:
            full_cost_children = 0

    if num_seniors >= 1:
        if full_cost_children >= 1:
            full_cost_children -= 1
        else:
            full_cost_children = 0

    if num_seniors == 1 and num_adults >= 2:
        if full_cost_children >= 2:
            full_cost_children -= 2
        else:
            full_cost_children = 0

        full_cost_seniors = 0.5


    price_before_discount = (full_cost_adults * 15 + full_cost_seniors * 12 + full_cost_children * 5)
    real_discount = (price_before_discount * discount)
    price = price_before_discount - real_discount

    return price