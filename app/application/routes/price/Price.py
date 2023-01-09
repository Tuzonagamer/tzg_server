from flask import render_template, flash, redirect, url_for,  send_from_directory, jsonify, send_file
from flask import jsonify
from flask import Flask, request, Response, json, send_file

from app.application.routes.tools.ResponseContainer import ResponseContainer
from app.application.controlers.inventory.PriceCT import PriceCT

class Price:
    def __init__(self, app):
        self.controler = PriceCT()
        self.response = ResponseContainer(self.__class__.__name__.lower())
        print('/{0}/'.format(self.__class__.__name__.lower()) )

        @app.route('/{0}/'.format(self.__class__.__name__.lower()), methods=['GET'])
        def PriceIndex():
            """container 
            :return: render_template index.html
            """
            self.response.alertCallContext( "/")
            self.response.restarObject() 
            self.getAllprices()

            return Response(response=json.dumps(self.response.getObject()), status=self.response.status, mimetype="application/json")
        
        @app.route('/{0}/create'.format(self.__class__.__name__.lower()), methods=['POST'])
        def PriceADD():
            """container 
            :return: render_template index.html
            """
            req = request.get_json()
            self.response.alertCallContext( "/")
            self.response.restarObject() 
            self.create(req)

            return Response(response=json.dumps(self.response.getObject()), status=self.response.status, mimetype="application/json")
    
    def getAllprices(self):
        self.response.object_ = self.controler.getAll()
    
    def create(self, obj):
        self.response.object_ = self.controler.add(obj["descriminator"], obj["code"], obj["value"] )