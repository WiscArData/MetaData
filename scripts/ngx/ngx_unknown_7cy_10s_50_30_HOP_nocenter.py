#!Measurement
# all of this is configuration info that can be used in the script.
# you refer to these values using mx.<group>.<attribute>
# e.g
#   mx.baseline.counts is 180
#   mx.multicollect.detector is H1
'''
baseline:
  after: true
  before: false
  counts: 15
  detector: H4
  mass: 37.6
  settling_time: 10.0
  integration_time: 1.0
default_fits: nominal
equilibration:
  eqtime: 1.0
  inlet: 0
  inlet_delay: 3
  outlet: 12
  use_extraction_eqtime: true
multicollect:
  counts: 30
  detector: H4
  isotope: Ar40
peakcenter:
  after: false
  before: false
  detector: H4
  detectors:
  - H4
  - H3
  - H2
  - H1
  - Ax
  - L1
  - L2
  - L3
  - L4
  - L5
  integration_time: 0.262144
  isotope: Ar40
peakhop:
  generate_ic_table: false
  hops_name: L4_IC_50_30_hops
  ncycles: 7
  use_peak_hop: true
'''
ACTIVE_DETECTORS=('H4','H3','H2','H1','Ax','L1','L2','L3','L4','L5')
    
def main():
    info('unknown measurement script')
    
    activate_detectors(*ACTIVE_DETECTORS)
   
    
    if mx.peakcenter.before:
        peak_center(detector=mx.peakcenter.detector,isotope=mx.peakcenter.isotope)
    
    if mx.baseline.before:
        baselines(ncounts=mx.baseline.counts,mass=mx.baseline.mass, detector=mx.baseline.detector,
                  settling_time=mx.baseline.settling_time)
    
    position_magnet(mx.multicollect.isotope, detector=mx.multicollect.detector)

    #sniff the gas during equilibration
    if mx.equilibration.use_extraction_eqtime:
        eqt = eqtime
    else:
        eqt = mx.equilibration.eqtime
    '''
    Equilibrate is non-blocking so use a sniff or sleep as a placeholder
    e.g sniff(<equilibration_time>) or sleep(<equilibration_time>)
    '''
    
    set_integration_time(1)

    equilibrate(eqtime=eqt, inlet=mx.equilibration.inlet, outlet=mx.equilibration.outlet, 
               delay=mx.equilibration.inlet_delay)

    set_time_zero()
    
    #sniff(eqt)    
    #instead of recording eq gas. just wait eq time.
    sleep(eqt)
    

    set_integration_time(10)
    hops=load_hops('hops/{}.yaml'.format(mx.peakhop.hops_name))
    define_hops(hops)
    set_fits()
    set_baseline_fits()
    peak_hop(ncycles=mx.peakhop.ncycles, hops=hops)

    if mx.baseline.after:
        
        #necessary if peak hopping
        #define_detectors('Ar40','H4')
        #define_detectors('Ar39','H2')
        #define_detectors('Ar38','AX')
        #define_detectors('Ar37','L2')
        #define_detectors('Ar36','L4')
        #define_detectors('Ar40','H3')
        #define_detectors('Ar39','H1')
        #define_detectors('Ar38','L1')
        #define_detectors('Ar37','L3')
        #define_detectors('Ar36','L5')
        
        #define_detectors('Ar40H4','H4')
        #define_detectors('Ar39H2','H2')
        #define_detectors('Ar38AX','AX')
        #define_detectors('Ar37L2','L2')
        #define_detectors('Ar36L4','L4')
        #define_detectors('Ar40','H3')
        #define_detectors('Ar39','H1')
        #define_detectors('Ar38','L1')
        #define_detectors('Ar37','L3')
        #define_detectors('Ar36','L5')
        
        set_integration_time(1)
        
        baselines(ncounts=mx.baseline.counts, integration_time=mx.baseline.integration_time, mass=mx.baseline.mass, detector=mx.baseline.detector, settling_time=mx.baseline.settling_time)
 
       
    info('finished measure script')
    
    