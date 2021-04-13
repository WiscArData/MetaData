#===============================================================================
# EXTRACTION SCRIPT ngx_AirShot_GP50_small.py
#===============================================================================

'''
modifier: 01
eqtime: 12
'''

def main():

    info('NGX Air Shot')

    gosub('util:PrepareForAirShotLaser')

    gosub('util:AirShot_GP50_small')
    

#===============================================================================
# POST MEASUREMENT SCRIPT ngx_pump_ms.py
#===============================================================================
def main():

    info('Pumping spectrometer')

    open(description='MS Ion Pump')
    
    open(description='Ion Pump')
    
    #if delay_after>0:
    #    sleep(delay_after)
    