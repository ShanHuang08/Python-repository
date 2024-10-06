def my_beeramid(bonus, price):
    bottles = bonus // price
    total = 0
    digit = 1
    while True:
        total += digit*digit
        if total > bottles:
            digit-=1
            break
        digit+=1
    return digit

def AI_beeramid(bonus, price):
    bottles = bonus // price
    total = 0
    digit = 0
    while total + (digit + 1) ** 2 <= bottles:
        digit += 1
        total += digit ** 2
    return digit

def beeramid(bonus, price):
    beers  = bonus // price
    levels = 0
    
    while beers >= (levels + 1) ** 2:
        levels += 1
        beers  -= levels ** 2
    
    return levels

def beeramid2(bonus, price, level=1):
    return 0 if bonus < price * level**2 else 1 + beeramid2(bonus - price * level**2, price, level + 1)


