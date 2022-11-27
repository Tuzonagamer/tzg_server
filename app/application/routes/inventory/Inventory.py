from flask import render_template, flash, redirect, url_for
from flask import jsonify
from flask import Flask, request, Response, json

from app.application.controlers.inventory.InventoryCT import InventoryCT
from app.application.routes.tools.ResponseContainer import ResponseContainer

class Inventory():
    def __init__(self, app):
        self.controler = InventoryCT()
        self.response = ResponseContainer(self.__class__.__name__.lower())
        print('/{0}/'.format(self.__class__.__name__.lower()) )

        
        @app.route('/{0}/'.format(self.__class__.__name__.lower()), methods=['GET'])
        def InventoryIndex():
            """container 
            :return: render_template index.html
            """
            self.response.alertCallContext( "/")
            self.response.restarObject() 
            self.getAllInventory()

            return Response(response=json.dumps(self.response.getObject()), status=self.response.status, mimetype="application/json")

    #with delete registrys by any user.    
    def getAllInventory(self):
        self.response.object_ = self.controler.getAll()
    
    def create(self, obj):
        pass