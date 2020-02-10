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
  counts: 12
  detector: H3
  mass: 34.05
  settling_time: 5.0
  integration_time: 10.0
default_fits: nominal
equilibration:
  eqtime: 1.0
  inlet: 0
  inlet_delay: 3
  outlet: 12
  use_extraction_eqtime: false
multicollect:
  counts: 20
  detector: H3
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
  generate_ic_table: false
  hops_name: ''
  ncycles: 0
  use_peak_hop: false
'''
ACTIVE_DETECTORS=('H3','H1','L1','L3','L5')
    
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
    
    sniff(eqt)    
    set_fits()
    set_baseline_fits()

    #multicollect on active detectors
    multicollect(ncounts=mx.multicollect.counts, integration_time=10)
    
    if mx.baseline.after:
        baselines(ncounts=mx.baseline.counts, integration_time=mx.baseline.integration_time, mass=mx.baseline.mass, detector=mx.baseline.detector, settling_time=mx.baseline.settling_time)
    if mx.peakcenter.after:
        activate_detectors(*mx.peakcenter.detectors, **{'peak_center':True})
        peak_center(detector=mx.peakcenter.detector,isotope=mx.peakcenter.isotope,
        integration_time=mx.peakcenter.integration_time) 
       
    info('finished measure script')
    