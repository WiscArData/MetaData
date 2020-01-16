

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

