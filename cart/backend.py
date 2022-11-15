from .models import *


def get_cart_data():
    success = 0

    cart_items = [['', '', 0, 0, 0]]
    try :
        cart = CartItem()
        cartdatas = cart.object.all()
        
        for cartdata in cartdatas:
            item = cartdata['item']

            title = item['title']
            size = item['size']
            quantity = cartdata['quantity']
            price = item['price'] * cartdata['quantity']
            floor = cartdata['floor']

            cart_item = [title, size, quantity, price, floor]
            cart_items.append(cart_item)

            success = 1
            cartdata.delete()

    except Exception:
        pass

    return cart_items[success:]
