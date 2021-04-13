#===============================================================================
# EXTRACTION SCRIPT ngx_AirShot_cryo_small_eq12.py
#===============================================================================

'''
modifier: 01
eqtime: 12
'''

def main():

    info('NGX Air Shot')

    gosub('util:PrepareForAirShot')

    gosub('util:AirShot_cryo_small')
    

#===============================================================================
# POST MEASUREMENT SCRIPT ngx_pump_ms.py
#===============================================================================
def main():

    info('Pumping spectrometer')

    open(description='MS Ion Pump')
    
    open(description='Ion Pump')
    
    #if delay_after>0:
    #    sleep(delay_after)
    