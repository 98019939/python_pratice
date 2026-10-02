# **Q4. Shopping cart with quantity limits (\~12 min)**
#  Write `add_to_cart(cart, item, qty, stock)` where `cart` is a dict. Add `item: qty` to cart only if `qty <= stock`; otherwise print "Not enough stock" and don't add it.

# ```
# 1. Check: is qty <= stock?
#    - If yes: check if item already in cart.
#      - If yes, add qty to existing value.
#      - If no, create new key with qty.
#    - If no: print "Not enough stock" and do nothing.
# 2. Return the updated cart.
# 3. Call it a few times with different qty/stock combinations and print cart after each call.
# ```


def add_to_cart(cart, item, qty, stock):
   
    if qty <= stock:

        
        if item in cart:
            cart[item] += qty
        else:
            cart[item] = qty

    else:
        print("Not enough stock")

    return cart



cart = {}

print(add_to_cart(cart, "Apple", 2, 10))
print(add_to_cart(cart, "Banana", 3, 5))
print(add_to_cart(cart, "Apple", 4, 10))
print(add_to_cart(cart, "Mango", 8, 5))