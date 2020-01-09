#===============================================================================
# EXTRACTION SCRIPT ngx_pause.py
#===============================================================================

'''
modifier: 01
eqtime: 15
'''

def main():

    info('NGX pause script')
    
    sleep(cleanup)

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


#===============================================================================
# POST MEASUREMENT SCRIPT ngx_pump_ms.py
#===============================================================================
def main():

    info('Pumping spectrometer')

    open(description='MS Ion Pump')
    
    open(description='Ion Pump')
    
    if delay_after>0:
        sleep(delay_after)
    