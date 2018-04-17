import pandas as pd
import numpy as np 
import STRING
import unidecode
# from algorithm_rules import repeated_same


def hogar_clean(hogar_df: pd.DataFrame, variables=['hogar_tipo_via', 'hogar_nombre_via', 'hogar_numero_via', 'hogar_cp']):
    """
    Clean the original datalake DDBB

    :param hogar_df: file dataframe
    :param variables: Variables to take from the dataframe
    :return: cleaned hogar_df
    """
    print('número de hogares :', len(hogar_df.index))
    hogar_df = hogar_df[variables]
    hogar_df = hogar_df.replace('?', np.NaN)
    
    hogar_df = hogar_df.dropna(axis=0, how='any')

    # Str variables clean
    for i in STRING.symbols:
        hogar_df['hogar_nombre_via'] = hogar_df['hogar_nombre_via'].str.replace(i, '')

    # Numero de via clean
    hogar_df['hogar_numero_via'] = hogar_df['hogar_numero_via'].apply(unidecode.unidecode)

    for i in STRING.symbols_number:
        hogar_df['hogar_numero_via'] = hogar_df['hogar_numero_via'].str.replace(i, '')
        hogar_df['hogar_numero_via'] = [x.split('-')[0] for x in hogar_df['hogar_numero_via']]
        hogar_df['hogar_numero_via'] = hogar_df['hogar_numero_via'].str.extract('(\d+)', expand=False)
        # hogar_df['numero_via'] = hogar_df['numero_via'] algorithm_rules.init_finish_bad_typo(numero_via, '-')

    # Clean String Variables
    for i in variables:
        if i != 'hogar_cp' and i != 'hogar_numero_via':

            hogar_df[i] = hogar_df[i].map(str)
            hogar_df[i] = hogar_df[i].apply(unidecode.unidecode)
            hogar_df[i] = hogar_df[i].str.upper()
            hogar_df[i] = hogar_df[i].str.replace('\d+', '')
            hogar_df[i] = hogar_df[i].str.lstrip()
            # hogar_df[i] = repeated_same(hogar_df[i])

        else:
            hogar_df[i] = hogar_df[i].map(int)

        # Delete words that are useless
        hogar_df['hogar_nombre_via'] = hogar_df['hogar_nombre_via'].apply(
        lambda x: ' '.join([word for word in x.split() if word not in (STRING.stop)]))

    # Remove empty rows
    hogar_df = hogar_df[hogar_df['hogar_nombre_via'] != '']

    # Even or Odd
    hogar_df['number_odd'] = pd.Series(0, index=hogar_df.index)
    hogar_df.loc[hogar_df['hogar_numero_via'] % 2 != 0, 'number_odd'] = 1

    hogar_df = hogar_df.reset_index(drop=True)

    print('número de hogares procesados: ', len(hogar_df.index))

    return hogar_df
    

if __name__ == '__main__':
    
    hogar = pd.read_csv(STRING.PATH_source + 'hogares.csv', sep=';', encoding='utf-8')
    hogar_clean(hogar)
