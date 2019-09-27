'''Clase con la lógica implementada, identifica si cumple indicador o no'''
from io import open
import os
from pymongo import MongoClient
from bson import ObjectId
from pymongo.errors import ConnectionFailure
from transform import Transform

class File:
    '''Clase principal'''
    @classmethod
    def main(cls, source):
        '''Metodo principal, recibe un json source contenedor de las propiedades'''

        def indicador(pedido):
            sumas = 0
            suman = 0
            totalpedido = 0
            indicador = ''
            for y in collection.find({'PurchaseOrderNumber':pedido}):
                if y['Tag03_ExternalReference'] == 'Ontime' :
                    sumas = sumas + 1
                elif y['Tag03_ExternalReference'] == 'Early' or y['Tag03_ExternalReference'] == 'Late' or y['Tag03_ExternalReference'] == 'VeryLate' :
                    suman = suman + 1
                else:
                    suman = suman + 1
                totalpedido = sumas+suman    

            if sumas > (totalpedido/2):
                indicador = 'S'
            else:
                indicador = 'N'      
            return indicador

        ######################################################

        client = MongoClient(
            f'mongodb+srv://dev:0OjsBx0wyMGRrsLx@intdev-6j7zu.azure.mongodb.net/admin?retryWrites=true')

        db_mongo = client['Agendamiento']#Name database
        collection = db_mongo['Workflow_Reservations']
        f = open ('holamundo.txt','w')

        print('INICIAMOS')
        
        cabecera2 = ['CodigoCita','LocID','VendPurchaseOrderID',
        'VendorOrgID','FechaCita','HoraCita','FechaIngreso',
        'HoraIngreso','IndCumplio']
        
        cabecerastr = ''
        for cab in cabecera2:
            cabecerastr = cabecerastr+cab+'|'

        f.write(cabecerastr[:-1]+'\n')   
        contador = 0
        for x in collection.find({'Flag':'0'}):  
            f.write(Transform.transformacion(x)+indicador(x['PurchaseOrderNumber'])+'\n')
            contador = contador+1
            print(contador)
            collection.update_one(x, { "$set": { "Flag": "1" } })

        #print(Transform.transformacion('PRUEBA'))
        f.close() 
        