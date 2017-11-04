# XML
XML Extraction

Se necesita crear un programa que a partir de dos archivos xml o xlsx y siga los siguientes pasos:

Requisitos previos:

Dos excels, uno que sea "origen" y otro que sea "tecnología". Al final, se deberá actual el archivo "origen".
Los excels deberán estar ordenados por Municipios para tener en cuenta las posiciones correctamente.
1º. Opcional: Filtro de municipios en orden de ambos archivos. Esto es, retornar una lista con los municipios que existen realmente en ambos archivos (es opcional porque no se sabe a priori si van a tener los mismos municipios).

2º. Método que retorne un diccionario que tenga la siguiente forma: {key="Municipio" : value [x,y]}. "x" e "y" son las posiciones donde empiezan (x) y acaban (y) los registros del "Municipio" en cuestión. Esto debe hacerse por cada archivo. Es decir, debe retornar dos diccionarios, uno por cada archivo.

3º. Por cada municipio de cada uno de los diccionarios del paso 2, crear un diccionario con la forma: {key=posición : value="dirección"}. Se retornan dos diccionarios.

4º. A partir de esos dos diccionarios, comparar mediante el ALGORITMO las direcciones. El ALGORITMO deberá comparar las direcciones y decidir qué direcciones son las mismas. Se deberá crear un diccionario de la siguiente forma: {key=posición : value="Gescal17"} ("Gescal17" es una columna del excel de la tecnología). La key contiene la posición del excel "origen" que el ALGORITMO ha comprobado que existe en el excel "tecnología". Se retornará ese diccionario.

5º. A partir de ese diccionario, se deberá actualizar en el excel "origen" las posiciones del diccionario creando dos nuevas columnas. Una de ellas será referida al Gescal17 y la otra que contenga la tecnología filtrada del excel "tecnología". Solo se actualizarán las posiciones que contenga el diccionario anterior.

Analizar, por la cantidad de datos, si es necesario realizar el algoritmo completo con "divide y vencerás" disminuyendo así la cantidad de registros procesados por el procesador y memoria ram (en proceso).