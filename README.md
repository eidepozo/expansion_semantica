# expansión_semántica

El siguiente repositorio contiene el trabajo de tesis de pregado que lleva por nombre: *"Expansión semántica para mejorar la diversidad en la formulación de consultas"*, realizado por Elliot Ide Pozo, Ingenierio Civil en Informática de la Universidad Austral de Chile, junto al Dr. Cristian Olivares-Rodríguez como profesor patrocinante.

Cabe mencionar que existen multiples cambios desde el origen de la idea hasta el producto final. Por ejemplo, inicialmente se hablaba de recomendar terminos, lo cual abarca la intención de la idea, pero puede asociarse erroneamente a los sistemas de recomendación. 

La motivación de este trabajo es mejorar la diversidad de los resultados, para que el usuario logre satisfacer con mayor extensión su necesidad de información. Se abarca este desafio apoyando al usuario, expandiendo su propia consulta con terminos que son semánticamente relevantes a esta.

**Resumen del artículo**

*"Aunque la diversidad de los resultados ha sido estudiada desde los primeros sistemas de recuperación de información, existen pocos estudios que exploren la diversidad y su representación en un contexto educacional. Inherentemente los enfoques que buscan apoyar las dificultades en la búsqueda web, tales como la sugerencia y la expansión de consultas, se enfocan en maximizar la relevancia de los resultados de la consulta original.
En este trabajo se presenta un método que integra relaciones semánticas mediante Word Embedding para la expansión con retroalimentación ciega. Utilizando un corpus basado en los registros de consultas de estudiante, se entrenan 3 modelos Word2vec para obtener términos semánticamente relevantes a cada consulta. Se estudia la arquitectura propuesta en una tarea de búsqueda puntual, acotando el número de términos candidatos en cada modelo según la frecuencia mínima de palabras. Finalmente se compara la diversidad en dos grupos de consultas, midiendo la similitud léxica de los snippets de los resultados antes y después de la expansión. Los resultados indican la posibilidad de mejorar la diversidad mostrando además que una menor similitud semántica puede conducir a una mayor diversidad."*

***
**Backlog**

10-09-21
- Cambios mayores a la presentación del proceso, eliminando archivos .csv innecesarios, renombrando y reordenando cuadernillos para clarificar las etapas del producto final. Se modulariza el código puntual para 
- Paso de recomendacion_de_terminos a expansion_semantica. Técnicamente solo se evalua la diversidad obtenida, escogiendo los terminos para la expansión de consultas (rama del EA donde se ubica el proyecto) según su similitud semántica a la consulta. 

11-03-21
- Incluye la evaluación de metricas de diversidad para los nuevos resultados emitidos, segun la definición de los modelos y la metodologia establecida parcialmente.

03-11-20
- Solo se permite la entrega como articulos independientes, la concatenación puede producir conexiones ilogicas de similaridad segun la proximidad que se escoja. 

02-11-20
- Se sube la sistematización realizada junto a una serie de mejoras para la creación flexible de modelos. Queda pendiente 
permitir la entrega como articulos o corpus al modelo (actualmente solo como corpus). Ademas de evaluar los parametros propiamente tales del modelo.
