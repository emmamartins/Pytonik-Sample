from pytonik.Web import App, Load
from pytonik.Session import Session
from pytonik.Request import Request as Req

m = App()
s = Session()
Cart = Load('Cart')

def index(Request):
  #m.header()
  msg =""
  #s.destroy()

  #print(s.find('shopping_cart', 'id'))
  if Request.method == "POST":

      action = Request.params('action')

      if action == "add":
          getid = Request.params('id')
          id = Request.post('vid')
          name = Request.post('name')
          price = Request.post('price')
          vquantity = Request.post('vquantity')
          quantity = Request.post('quantity')
          currency = Request.post('currency')



          if s.get('shopping_cart') is not "":

              if id not in Cart.find('shopping_cart', 'id'):

                    items_dict = {
                        'id': id,
                        'name': name,
                        'price': price,
                        'quantity': vquantity,
                        'currency': currency,
                    }

                    session_cart = s.get('shopping_cart')
                    session_cart.append(items_dict)
                    s.set('shopping_cart', session_cart)

                    msg = "Updated Cart"
              else:
                    msg = "Item Already Added "
          else:

              items_dict = [{
                  'id': id,
                  'name': name,
                  'price': price,
                  'quantity': vquantity,
                  'currency': currency,
              }]
              s.set('shopping_cart', items_dict)


  items = [
      dict(id=1, name="Bag", price= 80, quantity = 20, currency  = "USD"),
      dict(id=2, name="Gold", price= 1440, quantity = 20, currency  = "USD"),
      dict(id=3, name="Phone", price= 120, quantity = 20, currency  = "USD"),
      dict(id=4, name="Camera", price= 630, quantity = 20, currency  = "USD"),
      dict(id=5, name="car", price= 4500, quantity = 10, currency  = "USD")
  ]

  data = {
    'title': 'Pytonik MVC',
     'note': 'List of Items',
      'items': items,
      'msg': msg,
      'list': s.get('shopping_cart'),
      'cartcount': len(s.get('shopping_cart'))

          }

  m.views('index', data)



        