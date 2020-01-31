from pytonik.Web import App
        
m = App()
        
def index():

  data = {
    'title': 'Pytonik MVC',
     'note': 'Our New Website '


          }
            
  m.views('index', data)
            


        