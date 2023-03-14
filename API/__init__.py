
from ui import cultivo,departamento,municipio

#!/ usr/bin/env python

# make sure to install these packages before running :
# pip install pandas
# pip install sodapy

import pandas as pd
from sodapy import Socrata



# Unauthenticated client only works with public data sets . Note ’None ’
# in place of application token , and no username or password :
client = Socrata ("www.datos.gov.co", None )

# Example authenticated client ( needed for non - public datasets ):
# client = Socrata (www.datos.gov.co ,
# MyAppToken ,
# username =" user@example . com" ,
# password =" AFakePassword ")

# First 2000 results , returned as JSON from API / converted to Python list of
# dictionaries by sodapy.
results = client.get ("ch4u-f3i5", limit =2000)

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

pd.set_option('display.max_columns', None)



def consulta():
    return results_df[(results_df["departamento"] == departamento) & (results_df["municipio"] == municipio) & (results_df["cultivo"] == cultivo)]



def imprimir_tabla(resultado, mediana_edafica):
    tabla = pd.concat([resultado.loc[:, ["departamento", "municipio", "cultivo", "topografia"]], mediana_edafica], axis=1 )
    print(tabla)





def calcular_mediana(resultado):
    mediana_ph = resultado["ph_agua_suelo_2_5_1_0"].median()
    mediana_fosforo = resultado["f_sforo_p_bray_ii_mg_kg"].median()
    mediana_potasio = resultado["potasio_k_intercambiable_cmol_kg"].median()
    mediana_edafica = pd.DataFrame([{ mediana_ph, mediana_fosforo,  mediana_potasio}],
        columns=['mediana_ph',"mediana_fosforo","mediana_potasio"])
    return mediana_edafica
