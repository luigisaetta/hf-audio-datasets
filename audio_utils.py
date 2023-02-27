import soundfile as sf

def check_channels(f_name, n_channels):
    v_rit = True
    
    vet, s_rate = sf.read(f_name)
    
    try:
        if vet.shape[1] != n_channels:
            v_rit = False
    except:
        # if mono it is a one dimensional array OK
        v_rit = True
    
    return v_rit

def check_max_length(f_name, max_length):
    v_rit = True
    
    vet, s_rate = sf.read(f_name)
    
    duration = vet.shape[0]/s_rate
    
    if duration > max_length:
        print(f"Duration : {round(duration, 1)} s.")
        v_rit = False
    
    return v_rit

def check_sampling_rate(f_name, sampling_rate):
    """
    return true if the sample_rate is the expected
    """
    vet, s_rate = sf.read(f_name)
    
    v_rit = True
    
    if s_rate != sampling_rate:
        v_rit = False
        
    return v_rit
