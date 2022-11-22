from flask import render_template, flash, redirect, url_for
from flask import jsonify
from flask import Flask, request, Response, json

from app.application.controlers.main.Main import Main



class Welcome:
	"""
	route class: welcome service
	:autor: Jajoya
	:date: 2021-09-13
	"""
	def __init__(self, app, msj='', title=''):
		self.msj = msj
		self.title = title
		
		@app.route('/', methods=['GET'])
		def welcomeIndex():
			"""container welcome
			:return: render_template index.html
			"""
			return render_template('index.html', title=self.title)