from pytonik.Web import App
        
m = App()
        
def index():

  data = {
    'title': 'Pytonik MVC',
     'note': 'Our Send Email'



          }
            
  m.views('index', data)
            


        