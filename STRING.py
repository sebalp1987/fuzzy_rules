from string import ascii_uppercase

ascii_uppercase = [i for i in ascii_uppercase]
PATH_root = 'U:\\fuzzy_rules\\'
PATH_source = PATH_root + 'source\\'
PATH_censo = PATH_root +'source\\TRAMOS-NAL.F180312'
PATH_censo_processed = PATH_root +'source\\censo_processed.csv'
PATH_hogar_processed = PATH_root +'source\\hogares.csv'
PATH_final_output = PATH_root +'source\\final_file.csv'
PATH_by_cp = PATH_root +'source\\final_file_cp.csv'

symbols = "!@#$.,-]'()º/?¿"
symbols_number = "ºª@|#~$.,?¿"
stop = ascii_uppercase + ['DE', 'DEL', 'LA', 'EL', 'LAS', 'LO', 'LOS', 'CL', 'AVDA', 'AVD']
