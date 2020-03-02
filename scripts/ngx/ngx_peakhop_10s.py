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
  counts: 30
  detector: L5
  mass: 34.05
  settling_time: 5.0
  integration_time: 10.0
default_fits: nominal
equilibration:
  eqtime: 1.0
  inlet: 0
  inlet_delay: 3
  outlet: 12
  use_extraction_eqtime: true
multicollect:
  counts: 70
  detector: L5
  isotope: Ar40
peakcenter:
  after: false
  before: false
  detector: H3
  detectors:
  - H3
  - H1
  - L1
  - L3
  - L5
  integration_time: 0.262144
  isotope: Ar40
peakhop:
  hops_name: single_detector_peak_hop
  ncycles: 50
'''
ACTIVE_DETECTORS=('L5',)
    
def main():
    info('unknown measurement script')
    
    activate_detectors(*ACTIVE_DETECTORS)
   
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
    
    sniff(eqt)    
    set_fits()
    set_baseline_fits()
    
    set_integration_time(10)
    hops=load_hops('hops/{}.yaml'.format(mx.peakhop.hops_name))
    define_hops(hops)
    peak_hop(ncycles=mx.peakhop.ncycles, hops=hops)
    
    if mx.baseline.after:
        baselines(ncounts=mx.baseline.counts, integration_time=mx.baseline.integration_time, mass=mx.baseline.mass, detector=mx.baseline.detector, settling_time=mx.baseline.settling_time)
       
    info('finished measure script')
    