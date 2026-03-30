




######################################################################

def get_signal_properties_from_ptu(ptu):
    '''
    This copies some properties from the PTU file to the signal_properties parameter.
    '''
    
    signal_properties = {}
    
    for key in dir(ptu):
        # if it's a parameter, add it to the dictionary
        if not callable(getattr(ptu, key)) and not key.startswith("__"):
            signal_properties[key] = getattr(ptu, key)
            
    # Additionally, add dt
    signal_properties['dt'] = ptu.global_resolution / ptu.number_bins_in_period
            # signal_properties['global_resolution'] / signal_properties['number_bins_in_period']
            # signal_properties['global_resolution'] / signal_properties['number_bins_in_period']
            
    # Other convenient ones:
    #signal_properties['frequency'] # ptu.frequency
    #signal_properties['global_resolution'] # ptu.global_resolution
    
    return signal_properties