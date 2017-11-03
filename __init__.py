# Imports
import pandas as pd
# Necessary to work. If not installed, try " pip3 install xlrd "
import xlrd
from UtilsFunctions import pt

# Paths
path_to_filter = "D:\\Machine_Learning\\DataSets\\VF\\CARMONA_1_SEMANA_OCTUBRE_(200_REGISTROS).xlsx"
path_with_filters = "D:\\Machine_Learning\\DataSets\\VF\\neba.xlsx"

to_filter_municipality = "POBLACION"
with_filters_municipality = "MUNICIPIO"
to_filter_sheet = "Hoja1"
with_filters_sheet = "neba"

def read_from_xlsx_by_municipality(path, sheet, municipality):
    """Read from a path and """

    excel = pd.read_excel(path, str(sheet))
    pt(excel)

read_from_xlsx_by_municipality(path_to_filter, to_filter_sheet, to_filter_municipality)