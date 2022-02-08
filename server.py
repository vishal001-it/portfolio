
# from urllib import requests
from email import message
from lib2to3.pgen2.token import NEWLINE
from tokenize import Name
from flask import Flask, render_template, redirect, request
import csv

app = Flask(__name__)
@app.route("/")
def home():
   return render_template('home.html')

@app.route('/<string:page_name>')
def html_page(page_name):
   return render_template(page_name)

def write_to_csv(data):
   with open ('database.csv', mode='a') as database:
      name = data["fname"]
      mail = data["email"]
      message = data["message"]
      csv_writer = csv.writer(database, delimiter=',' , quotechar='"', quoting=csv.QUOTE_MINIMAL)
      csv_writer.writerow([name,mail,message])

@app.route('/submit_form', methods=['POST','GET'])
def submit_form():
   if request.method == 'POST':
      data = request.form.to_dict()
      write_to_csv(data);
      return redirect('/thankyou.html')
   else:
      return redirect('/error.html')
