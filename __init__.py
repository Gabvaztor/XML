# Imports
# Necessary to work. If not installed, try " pip3 install pandas"
import pandas as pd
# Necessary to work. If not installed, try " pip3 install xlrd"
import xlrd
from UtilsFunctions import pt
import numpy as np


# Paths
path_origin = "D:\\Machine_Learning\\DataSets\\VF\\CARMONA_1_SEMANA_OCTUBRE_(200_REGISTROS).xlsx"
path_technology = "D:\\Machine_Learning\\DataSets\\VF\\neba.xlsx"
paths = [path_origin, path_technology]

origin_column = "POBLACION"
technology_column = "MUNICIPIO"
origin_municipality = "CARMONA"
technology_municipality = "CARMONA"
origin_sheet = "Hoja1"
technology_sheet = "neba"

def algorithm(paths):
    #1: optional
    municipalities_list = municipalies_filter(paths[0], paths[1])
    #2
    dict_origin_mun_pos, dict_technology_mun_pos = create_dicts_municipaly_position(municipalities_list)

def create_dicts_municipaly_position(municipalities_list=None):
    """
    2º. Método que retorne un diccionario que tenga la siguiente forma: {key="Municipio" : value [x,y]}. "x" e "y" son
    las posiciones donde empiezan (x) y acaban (y) los registros del "Municipio" en cuestión. Esto debe hacerse por 
    cada archivo. Es decir, debe retornar dos diccionarios, uno por cada archivo.
    :param municipalities_list: list optional
    :return: Retorna dos diccionarios, uno por cada archivo, con la forma comentada.
    """
    if municipalities_list is not None:
        pass
    else: # If not municipalities_list
        pass

def municipalies_filter(origin, technology):
    """
    1º. Opcional: Filtro de municipios en orden de ambos archivos. Esto es, retornar una lista con los municipios que
    # existen realmente en ambos archivos (es opcional porque no se sabe a priori si van a tener los mismos municipios).
    :param origin: excel origen
    :param technology: excel tecnología
    :return: municipalities_list = lista de municipios filtrados
    """
    origin_ = pd.read_excel(origin, origin_sheet)
    municipality_column_origin = origin_[[origin_column]]
    # This line-code get the no-repeated values in municipality_column_origin
    municipalities_list = list(set(np.squeeze(np.asarray(municipality_column_origin.iloc[:]))))
    return municipalities_list

def read_from_xlsx_by_municipality(path, sheet, column, municipality=None):
    """Read from a path, a sheet and a column. Optionally a municipality."""

    excel = pd.read_excel(path, str(sheet))
    municipality_column = excel[[column]]
    pt(excel.head())
    if municipality is not None:
        rows = municipality_column.shape[0]
        municipalities = []
        for i in range(rows):
            if municipality_column.iloc[i][0] == municipality:
                municipalities.append(municipality_column.iloc[i][0])
        pt(len(municipalities))
    else:
        pass
    pt(municipality_column.shape)

algorithm(paths)