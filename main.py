import STRING
import preprocess.preprocess_hogar as prep
import pandas as pd
import utils.map_hogar as mapping
import time

# Load File
hogar = pd.read_csv(STRING.PATH_source + 'hogares.csv', sep=';', encoding='utf-8')

# Clean data hogar
hogar = prep.hogar_clean(hogar)

# Map values
t_0 = time.time()
hogar_cleaned, hogar_cp = mapping.hogar_mapping(hogar, range_acceptance=75, separate_odd=True, separate_number=True,
                                                cp=False)
t_1 = time.time()
print("This took %.2f seconds" % (t_1 - t_0))

# Remain go through CP
t_0 = time.time()
hogar_cleaned, _ = mapping.hogar_mapping(hogar_cp, range_acceptance=75, separate_odd=False, separate_number=False,
                                         cp=True)
t_1 = time.time()
print("This took %.2f seconds" % (t_1 - t_0))
