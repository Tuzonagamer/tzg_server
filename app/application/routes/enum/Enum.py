from flask import render_template, flash, redirect, url_for
from flask import jsonify
from flask import Flask, request, Response, json


from app.application.controlers.enum.Enum import Enum as EnumCT

from app.application.routes.tools.ResponseContainer import ResponseContainer

class Enum():
    def __init__(self, app):
        self.controler = EnumCT()
        
        self.response = ResponseContainer(self.__class__.__name__.lower())
        print('/{0}/'.format(self.__class__.__name__.lower()) )

        
        @app.route('/{0}/'.format(self.__class__.__name__.lower()), methods=['GET'])
        def EnumIndex():
            """container 
            :return: render_template index.html
            """
            self.response.alertCallContext( "/")
            self.response.restarObject() 
            self.getAllEnums()
            

            return Response(response=json.dumps(self.response.getObject()), status=self.response.status, mimetype="application/json")
        
        @app.route('/{0}/update'.format(self.__class__.__name__.lower()), methods=['POST'])
        def EnumAdd():
            """container 
            :return: render_template index.html
            """
            req = request.get_json()
            self.response.alertCallContext( "/create")
            self.response.restarObject() 
            self.create(req)

            return Response(response=json.dumps(self.response.getObject()), status=self.response.status, mimetype="application/json")

    #with delete registrys by any user.    
    def getAllEnums(self):
        self.response.object_ = self.controler.getAll()
    
    def update(self, obj):
        # se gestiona la creacion del objeto         
        trassaction = self.controler.add(obj )
        
        #se procede a realizar el registro del producto e inventario
        valuePrice = self.controlerPrice.assiggendValuePrice(obj["PRICE"], trassaction, obj )
        trassaction[1]["message"] += valuePrice[1]['message']

        self.response.object_ = trassaction[0]
        self.response.object_["price"] = obj["PRICE"]
        self.response.object_["detail_price"] = valuePrice[0]

        # se prepara la respuesta
        if(trassaction[1]["act"]):
            self.response.status = 200
        else:
            self.response.status = 201     
        self.response.is_ok = trassaction[1]["act"]
        self.response.message = trassaction[1]["message"]