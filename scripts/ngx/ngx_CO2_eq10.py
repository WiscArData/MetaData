#===============================================================================
# EXTRACTION SCRIPT ngx_CO2_eq10.py
#===============================================================================

'''
modifier: 01
eqtime: 10
'''

def main():

    info('NGX CO2 laser analysis')

    gosub('util:PrepareForCO2Analysis')

    gosub('util:CO2Analysis')
    

    

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
    