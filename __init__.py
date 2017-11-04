# Imports
# Necessary to work. If not installed, try " pip3 install pandas"
import pandas as pd
# Necessary to work. If not installed, try " pip3 install xlrd"
import xlrd
from UtilsFunctions import pt

# Paths
path_to_filter = "D:\\Machine_Learning\\DataSets\\VF\\CARMONA_1_SEMANA_OCTUBRE_(200_REGISTROS).xlsx"
path_with_filters = "D:\\Machine_Learning\\DataSets\\VF\\neba.xlsx"

to_filter_column = "POBLACION"
with_filters_column = "MUNICIPIO"
to_filter_municipality = "CARMONA"
with_filters_municipality = "CARMONA"
to_filter_sheet = "Hoja1"
with_filters_sheet = "neba"

def read_from_xlsx_by_municipality(path, sheet, column, municipality=None):
    """Read from a path and a sheet"""

    excel = pd.read_excel(path, str(sheet))
    municipality_column = excel[[column]]
    if municipality is not None:
        rows = municipality_column.shape[0]
        municipalities = []
        for i in range(rows):
            if municipality_column.iloc[i][0] == municipality:
                municipalities.append(municipality_column.iloc[i][0])
        pt(municipalities)
    pt(municipality_column.shape)

read_from_xlsx_by_municipality(path_to_filter, to_filter_sheet, to_filter_column, to_filter_municipality)