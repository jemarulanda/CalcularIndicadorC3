'''Clase con la lógica implementada, identifica si cumple indicador o no'''

class Transform:
    '''Clase principal'''
    @classmethod
    def transformacion(cls, source):
        response = source['ReservationId']+'|'+source['Site_ExternalReference']+'|'+source['PurchaseOrderNumber']+'|'+source['Supplier_ID']+'|'+source['ScheduledDateUTC']+'|'+source['ScheduledDateUTC']+'|'+source['StatedTimestamp13UTC']+'|'+source['StatedTimestamp13UTC']+'|'
        return response