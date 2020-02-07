from pytonik.Web import App
        
m = App()
        
def index():

  data = {
    'title': 'Pytonik MVC',
     'note': 'Our File Upload'



          }
            
  m.views('index', data)
            


        