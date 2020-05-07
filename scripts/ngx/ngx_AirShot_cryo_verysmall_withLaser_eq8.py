#===============================================================================
# EXTRACTION SCRIPT ngx_AirShot_cryo_verysmall_withLaser_eq8.py
#===============================================================================

'''
modifier: 01
eqtime: 8
'''

def main():

    info('NGX Air Shot')

    gosub('util:PrepareForAirShot')

    gosub('util:AirShot_cryo_verysmall_withLaser')
    

#===============================================================================
# POST EQUILIBRATION SCRIPT ngx_pump_extraction_line.py
#===============================================================================


def main():

    info('Pump after equilibration')
    
    close(description='MS In')
    close(description='Laser Pump')
    close(description='Ion Pump')
    open(description='Turbo')
    
    sleep(2)
    
    open(description='Hex In')
    open(description='Cryo')
    open(description='Getter')
    open(description='Air Port')
    open(description='Laser Port')
    open(description='Laser Pump')


#===============================================================================
# POST MEASUREMENT SCRIPT ngx_pump_ms.py
#===============================================================================
def main():

    info('Pumping spectrometer')

    open(description='MS Ion Pump')
    
    open(description='Ion Pump')
    
    #if delay_after>0:
    #    sleep(delay_after)
    