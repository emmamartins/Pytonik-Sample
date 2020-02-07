# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 1/18/20.

from pytonik import Web
from pytonik.Core import File
from pytonik.Core import Helpers
from pytonik.Functions.validation import validation

m = Web.App()

validate = validation()
file  = File
def index(Request):
     
    msg = ""
    if Request.method == "POST":
        upload_dir = upload_dir = Helpers.mvc_dir('public/uploads/file')
        fileupload = Request.file('uploadfile')

        if fileupload.filename == "":
            msg = "Select File"
        else:
            response = file.upload(fileupload, upload_dir)
            if response == True:
                msg = "File Upload Successfully "
            else:
                msg = "Unable to Upload file "



    data = {

        'title' : 'Upload Controller',
        'text': 'Welcome to My pytonik Upload File Page',
        'msg' : msg
    }

    m.views('upload', data)

def multiple(Request):
     
    msg = ""
    if Request.method == "POST":
        upload_dir = upload_dir = Helpers.mvc_dir('public/uploads/file/multiple')
        multifileupload = Request.file('uploadfile')
        for fileupload in multifileupload:
            if fileupload.filename != "":
                response = file.upload(fileupload, upload_dir)
                if response == True:
                    msg = "File Upload Successfully "
                else:
                    msg = "Unable to Upload file "



    data = {

        'title' : 'Upload Controller',
        'text': 'Welcome to My pytonik Multiple Upload File Page',
        'msg' : msg
    }

    m.views('multiple', data)



def image(Request):
  
    msg = ""
    if Request.method == "POST":
        upload_dir = upload_dir = Helpers.mvc_dir('public/uploads/img')
        fileupload = Request.file('uploadimage')
        ext = file.ext(fileupload.filename)
        list_ext = ['png', 'jpg', 'JPG', 'jpeg']
        
        if fileupload.filename == "":

            msg = "Select an image File"

        elif ext not in list_ext :
            msg = "Invalid Image Formate"
        else:
            
            response = file.Image(upload_dir, fileupload).upload()
           
            if bool(response) == True :
                msg = "Image Upload Successfully "
            else:
                msg = "Unable to Upload Image "



    data = {

        'title' : 'Upload Controller',
        'text': 'Welcome to My pytonik Upload Image Page',
        'msg' : msg
    }

    m.views('image', data)


def resize(Request):
   
    msg = ""
    if Request.method == "POST":
        upload_dir = upload_dir = Helpers.mvc_dir('public/uploads/resize')
        fileupload = Request.file('uploadimage')
        ext = file.ext(fileupload.filename)
        dimension = {64: 64, 128: 128}
        list_ext = ['png', 'jpg', 'JPG', 'jpeg']
        
        if fileupload.filename == "":

            msg = "Select an image File"

        elif ext not in list_ext :
            msg = "Invalid Image Formate"
        else:
            response = ""
            image = file.Image(upload_dir, fileupload)
            for w, h in dimension.items():
                response = image.resize(w, h)
          
            if response == None:
                msg = "Image Upload Successfully "
            else:
                msg = "Unable to Upload Image "



    data = {

        'title' : 'Upload Controller',
        'text': 'Welcome to My pytonik Upload Image / Resize Page',
        'msg' : msg
    }

    m.views('resize', data)



def rename(Request):
   
    msg = ""
    if Request.method == "POST":
        upload_dir = upload_dir = Helpers.mvc_dir('public/uploads/resize/rename')
        fileupload = Request.file('uploadimage')
        ext = file.ext(fileupload.filename)
        rename = "pytonk_rees"
        dimension = {64: 64, 128: 128}

        list_ext = ['png', 'jpg', 'JPG', 'jpeg']
        
        if fileupload.filename == "":

            msg = "Select an image File"

        elif ext not in list_ext :
            msg = "Invalid Image Formate"
        else:
            response = ""
            image = file.Image(upload_dir, fileupload)
            for w, h in dimension.items():
                response = image.resize(w, h, rename)
          
            if response == None:
                msg = "Image Upload Successfully "
            else:
                msg = "Unable to Upload Image "



    data = {

        'title' : 'Upload Controller',
        'text': 'Welcome to My pytonik Upload Image / Resize / Rename Page',
        'msg' : msg
    }

    m.views('rename', data)



