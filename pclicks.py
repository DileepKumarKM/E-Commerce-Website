from flask import Blueprint,jsonify, request

from sqlalchemy.sql import text

from db import db

import datetime

 

pclicks_blueprint = Blueprint('pclicks_blueprint',__name__)

 

@pclicks_blueprint.route('/prod-clicks')

def pClicks():

 

    currentDate = datetime.datetime.today().strftime('%Y-%m-%d')

 

    sql = text('SELECT * FROM pclicks WHERE date = "'+currentDate+'"')

    result = db.engine.execute(sql)

    rawdata = result.fetchall()

 

    #check if its first click for the day or not

    rawdatalength = len(rawdata)

 

    # if fisrt click

    if rawdatalength == 0:

        sqlins = text('INSERT INTO pclicks (date,clicks) VALUES ("'+currentDate+'",1)')

        db.engine.execute(sqlins)

    else:

        # fetch the old count

        newclickvalue = rawdata[0].clicks + 1

 

        sqlupd = text('UPDATE pclicks SET clicks = '+str(newclickvalue)+' WHERE date = "'+currentDate+'"')

        db.engine.execute(sqlupd)

   

    return "Prod Click was logged"