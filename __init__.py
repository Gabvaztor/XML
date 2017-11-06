# Imports
# Necessary to work. If not installed, try " pip3 install pandas"
import pandas as pd
# Necessary to work. If not installed, try " pip3 install xlrd"
import xlrd
from UtilsFunctions import pt
import numpy as np
# To delete nan values
import math

# Paths
path_origin = "D:\\Machine_Learning\\DataSets\\VF\\CARMONA_1_SEMANA_OCTUBRE_(200_REGISTROS).xlsx"
path_technology = "D:\\Machine_Learning\\DataSets\\VF\\neba.xlsx"
paths = [path_origin, path_technology]

#Columns
origin_column_municipality = "POBLACION"
technology_column_municipality = "MUNICIPIO"
origin_column_address = "DIRECCION"
technology_column_address = "Direccion"


origin_municipality = "CARMONA"
technology_municipality = "CARMONA"
origin_sheet = "Hoja1"
technology_sheet = "neba"

def algorithm(paths):
    origin = pd.read_excel(paths[0], origin_sheet)
    technology = pd.read_excel(paths[1], technology_sheet)
    #1: optional
    municipalities_list = municipalies_filter(origin, technology)
    #2
    dict_origin_mun_pos, dict_technology_mun_pos = create_dicts_municipaly_position(origin, technology, municipalities_list)

def create_dicts_municipaly_position(origin, technology, municipalities_list=None):
    """
    2º. Método que retorne un diccionario que tenga la siguiente forma: {key="Municipio" : value [x,y]}. "x" e "y" son
    las posiciones donde empiezan (x) y acaban (y) los registros del "Municipio" en cuestión. Esto debe hacerse por 
    cada archivo. Es decir, debe retornar dos diccionarios, uno por cada archivo.
    :param municipalities_list: list optional
    :return: Retorna dos diccionarios, uno por cada archivo, con la forma comentada.
    """
    dict_origin = {}
    dict_technology = {}
    municipality_column_origin = origin[[origin_column_municipality]]
    municipality_column_technology = technology[[technology_column_municipality]]
    address_column_origin = origin[[origin_column_address]]
    address_column_technology = technology[[technology_column_address]]

    municipalities_list_origin = list(np.squeeze(np.asarray(municipality_column_origin.iloc[:])))
    municipalities_list_technology = list(np.squeeze(np.asarray(municipality_column_technology.iloc[:])))
    address_list_origin = list(np.squeeze(np.asarray(address_column_origin.iloc[:])))
    address_list_technology = list(np.squeeze(np.asarray(address_column_technology.iloc[:])))

    if municipalities_list is not None:
        dict_origin = phase_2(municipalities_list_origin, address_list_origin, municipalities_list)
        dict_technology = phase_2(municipalities_list_technology, address_list_technology, municipalities_list)
    else: # If not municipalities_list
        pass

    return dict_origin, dict_technology

def phase_2(municipalities_list_file, address_list_origin, municipalities_list=None):
    dict = {}
    must_upload_municipality = True
    actual_municipality = ""
    last_municipality = ""
    range_ = len(address_list_origin)
    # File origin
    for i in range(range_):
        if i == 0 or municipalities_list_file[i] != actual_municipality and municipalities_list_file[i] \
                and type(municipalities_list_file[i]) != np.float:
            actual_municipality = municipalities_list_file[i]
            must_upload_municipality = True
            if municipalities_list_file[
                        i - 1] != actual_municipality and i != 0 and last_municipality in municipalities_list:
                dict[last_municipality] = [dict.get(last_municipality), i - 1]
        if municipalities_list_file[i] in municipalities_list:
            if i == range_ - 1 and actual_municipality in municipalities_list:
                dict[municipalities_list_file[i]] = [dict[actual_municipality], i]
            if must_upload_municipality:
                dict.update({municipalities_list_file[i]: i})
                must_upload_municipality = False
                last_municipality = actual_municipality
    pt(dict)
    return dict
def municipalies_filter(origin, technology):
    """
    1º. Opcional: Filtro de municipios en orden de ambos archivos. Esto es, retornar una lista con los municipios que
    # existen realmente en ambos archivos (es opcional porque no se sabe a priori si van a tener los mismos municipios).
    :param origin: excel origen
    :param technology: excel tecnología
    :return: municipalities_list = lista de municipios filtrados
    """
    pt("STEP 1/5...")
    municipality_column_origin = origin[[origin_column_municipality]]
    # This line-code get the no-repeated values in municipality_column_origin
    municipalities_list_origin = set(np.squeeze(np.asarray(municipality_column_origin.iloc[:])))
    municipality_column_technology = technology[[technology_column_municipality]]
    municipalities_list_technology = set(np.squeeze(np.asarray(municipality_column_technology.iloc[:])))
    municipalities_list = municipalities_list_origin.intersection(municipalities_list_technology)
    pt("STEP 1/5 Complete")
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