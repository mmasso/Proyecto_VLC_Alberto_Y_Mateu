from add_order_songs import order_canciones
from random import randint

def random_assign(order_canciones):
    numerosRandom = []
    for key in order_canciones:
        num_random = randint(1, len(order_canciones))

        numerosRandom.append(num_random)
    return numerosRandom

print(random_assign(order_canciones))
