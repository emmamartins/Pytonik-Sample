# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 2/6/20.
from pytonik.Web import App, url
from pytonik.Session import Session


m = App()
s = Session()

def index():
  msg =""



  data = {
    'title': 'Pytonik MVC',
     'note': 'List Items in Cart',
      'items': s.get('shopping_cart'),
      'cartcount': len(s.get('shopping_cart')),
      'msg': msg,

          }

  m.views('cart', data)


def delete(Request):

    if Request.params('id') is not "":
        if Request.params('id') == "all":
            response = s.delete('shopping_cart', 'id')
        else:
            response = s.delete('shopping_cart', 'id', Request.params('id'))
        if response is True:
            m.redirect(url('/cart/'))
            m.header()
    else:
        m.redirect(url('/'))
        m.header()


def update(Request):
    if Request.method == "POST":
        vid = Request.post('idv')
        vquantity = Request.post('quantityv')
        upitem = {'quantity': vquantity}

        response = s.update('shopping_cart', "id", vid, upitem)
        if response is True:
            m.redirect(url('/cart/'))
            m.header()
    else:
        m.redirect(url('/'))
        m.header()


