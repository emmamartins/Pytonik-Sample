from pytonik import Web
                              
m = Web.App()
                              
def index():
                              
  m.header()
                              
  print("do work here") 

                            
def page400 ():

    data = {'title': 'pytonik 400 '}

    m.views('400', data)

def page404 ():

    data = {'title': 'pytonik 404 '}

    m.views('404', data)

def page405 ():

    data = {'title': 'pytonik 405 '}

    m.views('405', data)
