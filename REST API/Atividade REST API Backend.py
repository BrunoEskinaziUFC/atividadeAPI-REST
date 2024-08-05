import traceback
import requests
import os
import psycopg2
import json

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
CORS(app)

CURRENT_FOLDER = os.getcwd()

def data_centers():
    response = requests.get('https://universalis.app/api/v2/data-centers')
    if response.status_code == 200:
        #print(response.json().get('operations'))
        return response.json()
    else:
        raise Exception(f"Erro ao listar os data centers: {response.status_code}")

def worlds():
    response = requests.get('https://universalis.app/api/v2/worlds')
    if response.status_code == 200:
        #print(response.json().get('operations'))
        return response.json()
    else:
        raise Exception(f"Erro ao listar os mundos: {response.status_code}")

def get_data_centers():
    response = data_centers()
    #text = ''

    #data = []
    data_centers_list = [(w.get('name'), w.get('region'), w.get('worlds')) for w in response] 
    text = '\n'.join([w.get('name') for w in response])
    print(text)
    
    try:
        connection = psycopg2.connect(dbname="Universalis-API", user="postgres", password="Elefante123", host="localhost", port="5432")
        cursor = connection.cursor()
        print(data_centers_list)
        cursor.executemany('INSERT INTO "DataCenters" ("Name", Region, Worlds) VALUES (%s, %s, %s)', data_centers_list)
        connection.commit()
        return jsonify(data_centers_list)
    except(Exception, psycopg2.Error) as error:
            #print("DataCenters já inseridos no banco de dados!")
            traceback.print_exc()
    finally:
        if connection:
            cursor.close()
            connection.close()

    f = open(r'{}\DataCenters.txt'.format(CURRENT_FOLDER), "w", encoding='utf-8')
    #print(f)
    f.write(str(text))
    f.close()

def get_worlds():
    response = worlds()
    worlds_list = [(w.get('id'), w.get('name')) for w in response]
    #print(response)
    text = ''

    #print(worlds_list)
    try:
        connection = psycopg2.connect(dbname="Universalis-API", user="postgres", password="Elefante123", host="localhost", port="5432")
        cursor = connection.cursor()
        #print(worlds_list)
        cursor.executemany('INSERT INTO "Worlds" (id, Name) VALUES (%s, %s)', worlds_list)
        connection.commit()
    except(Exception, psycopg2.Error) as error:
            #print("DataCenters já inseridos no banco de dados!")
            traceback.print_exc()
    finally:
        if connection:
            cursor.close()
            connection.close()

class DC(object):
    pass

def get_DC_BD():
    results = []
    try:
        try:
            get_data_centers()
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
        finally:
            pass
        connection = psycopg2.connect(dbname="Universalis-API", user="postgres", password="Elefante123", host="localhost", port="5432")
        cursor = connection.cursor()
        cursor.execute('SELECT "Name", region, worlds FROM public."DataCenters";')
        DataCenters = cursor.fetchall()
        
        for dc in DataCenters:
            d = {'name': 'a', 'region': 'b'}
            #print(d)
            d['name'] = dc[0]
            d['region'] = dc[1]
            results.append(d)

    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
            connection.close()
    return results

def get_worlds_by_DC():
    results = []
    try:
        connection = psycopg2.connect(dbname="Universalis-API", user="postgres", password="Elefante123", host="localhost", port="5432")
        cursor = connection.cursor()
        cursor.execute('SELECT DISTINCT DC."Name", DC.region, w.name, w.id FROM "DataCenters" as DC, "Worlds" as w WHERE w.id = ANY(DC.worlds)')
        worldsDC = cursor.fetchall()

        for w in worldsDC:
            d = {'DCname': 'a', 'region': 'b','WORLDname': 'c', 'WORLDid': 'd'}
            d['DCname'] = w[0]
            d['region'] = w[1]
            d['WORLDname'] = w[2]
            d['WORLDid'] = w[3]
            results.append(d)
        
    except (Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
            connection.close()
    return results



def set_character(name, world):
    try:
        connection = psycopg2.connect(dbname="Universalis-API", user="postgres", password="Elefante123", host="localhost", port="5432")
        cursor = connection.cursor()
        #print(worlds_list)
        cursor.execute('INSERT INTO "Character" (name, world) VALUES (%s, %s)', [name, world])
        connection.commit()
    except(Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
            connection.close()





class DC(Resource):
    def get(self):
        dc_list = jsonify(get_DC_BD())
        return dc_list

class World(Resource):
    def get(self):
        world_list = jsonify(get_worlds_by_DC())
        return world_list
    
class Character(Resource):
    def post(self, name, world):
        set_character(name, world)


api.add_resource(DC, '/data_centers')
api.add_resource(World, '/worlds')
@app.route('/set_characters', methods=['POST'])
def set_character_API():
    #print("AOBA")
    #data = jsonify(request.json)
    #print(data)
    data = request.json
    name = data['name']
    world = data['WORLDid']
    set_character(name, world)
    response = {'response': 'Character registered!'}
    return jsonify(response)
@app.route('/delete_DCs', methods=['DELETE'])
def delete_DCs():
    print("OLHA A BOMBA")
    try:
        connection = psycopg2.connect(dbname="Universalis-API", user="postgres", password="Elefante123", host="localhost", port="5432")
        cursor = connection.cursor()
        cursor.execute('DELETE FROM public."DataCenters"')
        connection.commit()
    except(Exception, psycopg2.Error) as error:
        traceback.print_exc()
    finally:
        if connection:
            cursor.close()
            connection.close()
    response = {'response': 'Bomba!!'}
    return jsonify(response)


def main():
    #get_data_centers()
    #get_worlds()
    #set_character("Guarc'a", 37)
    pass

if __name__ == "__main__":
    #main()
    app.run(debug=True)