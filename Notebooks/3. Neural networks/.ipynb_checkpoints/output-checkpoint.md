Machine  Learning  Vs  Deep  Learning 
en la detección del cáncer de hígado 

 
Juan Armario Muñoz

1.

Introducción 

1.1. Contexto del cáncer de hígado 

1.2. La importancia de la detección temprana 

1.3. Jus>ﬁcación del estudio: Uso de IA para mejorar la predicción 

1.4. Explicación del PLCO dataset y su origen 

1.5. Deﬁnición de la variable liver_cancer como target principal 

2. Metodología general del estudio 

2.1. Explicación de los dos bloques del estudio 

2.1.1. Machine Learning 

2.1.2. Deep Learning, redes neuronales 

2.2. Estrategia de comparación entre ambos enfoques 

3. Técnicas de preprocesamiento aplicadas 

3.1. Feature Engineering y selección de variables 

3.2. Imputación de valores faltantes 

3.2.1. Imputación simple 

3.2.2. Imputación múl>ple 

3.2.3. Procedimiento en el estudio 

3.2.4. Conclusión 

3.4. Data transforma>on 

3.5. Balanceo de datos (SMOTE, Undersampling, Oversampling) 

3.5.1. Procedimiento en el estudio 

3.5.2. Conclusión 

4. Algoritmos de Machine Learning 

4.1. Creación de modelo y comparación de algoritmos 

4.1.1. Métricas claves 

4.2. Resultados iniciales y op>mización de hiperparámetros 

4.3. Conclusiones 

5. Algoritmos de Deep Learning 

5.1. Creación de redes neuronales ar>ﬁciales (ANN) 

5.1.1. Deﬁnición de la Arquitectura de la Red 

2

 4

 4

 4

 5

 5

 6

 7

 7

 7

 8

 8

 9

 9

 10

 10

 10

 10

 11

 12

 13

 13

 14

 15

 15

 15

 16

 16

 17

 17

 17

Juan Armario Muñoz

5.2. Op>mización con Keras Tuner 

5.3. Evaluación del modelo con métricas avanzadas 

5.4. Evaluación, comparación y conclusiones 

6. Comparación Machine Learning vs. Deep Learning 

6.1. Comparación de los resultados de ambos enfoques. 

6.2. Interpretabilidad vs. Precisión: ¿Qué modelo es más ú>l en la clínica? 

7. Discusión y Aplicabilidad del Modelo en Medicina 

7.1. ¿Cómo ayudaría este modelo a los médicos en la prác>ca? 

7.2. Desafos en la implementación real (é>ca, sesgo, conﬁanza médica) 

7.3. Posibles mejoras futuras: integración con imágenes médicas, modelos más avanzados 

8. Conclusiones y futuro trabajo 

8.1. Resumen de los hallazgos más importantes 

8.2. Sugerencias para futuros estudios 

9. Anexos 

9.1. Código 

9.2. Referencias 

9.3. Glosario de términos 

 18

 18

 18

 20

 20

 20

 22

 22

 22

 23

 24

 24

 24

 25

 25

 25

25

3

Juan Armario Muñoz

1.

Introducción 

1.1.  Contexto del cáncer de hígado 

El  cáncer  de  hígado,  par>cularmente  el  carcinoma  hepatocelular  (CHC),  es  el  >po  más  común  de  cáncer  hepá>co,  y 

representa  un  importante  problema  de  salud  pública,  debido  a  su  alta  mortalidad  y  su  diagnós>co  tardío.  Según  la 

Organización Mundial de la Salud (OMS), es el tercer cáncer más letal en el mundo, con una tasa de supervivencia a 5 años 

inferior al 20% en la mayoría de los casos, ya que, a pesar de los avances médicos, la mayoría de los diagnós>cos, se realizan 

en etapas avanzadas, cuando las opciones terapéu>cas son limitadas. 

El desarrollo del cáncer de hígado, está fuertemente asociado con enfermedades hepá>cas crónicas y es>los de vida 

poco saludables, destacando entre los factores de riesgo más importantes: 

HepaOOs B y C crónica: La infección crónica por los virus Hepa>>s B (VHB) y Hepa>>s C (VHC), es el factor de riesgo 

más  importante  para  el  desarrollo  del  hepatocarcinoma,  llegando  al  80%  de  los  casos  según  la  OMS.  Estos  virus,  causan 

inﬂamación crónica del hígado, lo que provoca ﬁbrosis y, en muchos casos, cirrosis hepá>ca. 

Consumo excesivo de alcohol: El alcoholismo crónico, contribuye signiﬁca>vamente al desarrollo del cáncer de hígado, 

principalmente a través de la enfermedad hepá>ca alcohólica, ya que, el metabolismo del alcohol en el hígado genera estrés 

oxida>vo,  provocando  daño  celular,  inﬂamación  y  ﬁbrosis  hepá>ca.  Además,  pacientes  con  VHB  o  VHC  que  consumen 

alcohol, >enen un riesgo 10 veces mayor de desarrollar CHC, en comparación con personas sin estos factores. Un consumo 

superior a 40 g/día en hombres y 20 g/día en mujeres, aumenta signiﬁca>vamente el riesgo de cirrosis y cáncer hepá>co. 

Obesidad y diabetes Mellitus: El hígado graso no alcohólico, (NAFLD, por sus siglas en inglés), y su forma avanzada, la 

esteatohepa>>s no alcohólica (NASH), se han conver>do en una de las principales causas emergentes de cáncer de hígado, 

especialmente  en  países  desarrollados.  La  obesidad  y  la  diabetes  generan  resistencia  a  la  insulina,  lo  que  promueve  la 

acumulación de grasa en el hígado y el desarrollo de inﬂamación crónica. 

Evolución: NAFLD → NASH → Fibrosis → Cirrosis → Cáncer de hígado. 

Actualmente, el 25-30% de la población mundial >ene hígado graso, y de estos, un 20% desarrolla ﬁbrosis avanzada, 

aumentando el riesgo de CHC. 

Impacto  del  tabaquismo  en  el  desarrollo  del  cáncer  de  hígado:  El  tabaquismo,  es  un  factor  de  riesgo  bien 

documentado en el desarrollo de múl>ples >pos de cáncer. Aunque su impacto es menos directo que el de la hepa>>s viral, 

el alcoholismo o la obesidad, existen estudios que han demostrado una asociación signiﬁca>va entre el consumo de tabaco y 

el riesgo de CHC, debido a que, el tabaco, contribuye al desarrollo de inﬂamación crónica en el hígado, aumentando el riesgo 

de ﬁbrosis y cirrosis, condiciones que predisponen al CHC. 

1.2.  La importancia de la detección temprana 

El  diagnós>co  temprano  del  cáncer  de  hígado  es  uno  de  los  mayores  desafos  en  oncología,  ya  que  en  sus  primeras 

fases es asintomá>co o presenta síntomas no especíﬁcos como fa>ga, pérdida de peso y malestar abdominal. El problema 

central, es que, más del 80% de los casos se diagnos>can en estadios avanzados, cuando las opciones de tratamiento son 

limitadas y la mortalidad es alta. Las estrategias actuales de detección incluyen: 

Método
Método

Descripción

Ventajas

Limitaciones

Biomarcadores en sangre 
(Ej: AFP, DCP)

Detección de proteínas 
asociadas al cáncer en el 
suero

Prueba sencilla y no invasiva

Baja sensibilidad en etapas 
tempranas

4

Juan Armario Muñoz

Método

Descripción

Ventajas

Limitaciones

Imágenes médicas 
(Ecografa, TAC, RMN)

Biopsia hepá>ca

Principales desventajas: 

Visualización de tumores 
hepá>cos mediante 
radiología

Obtención de tejido 
hepá>co para análisis 
histológico

Alta especiﬁcidad en 
tumores avanzados

Alto costo y no es accesible 
en todas las regiones

Diagnós>co deﬁni>vo

Invasivo, costoso y con 
riesgo de complicaciones

• Costo elevado: Las pruebas de imagen y biopsias hepá>cas son costosas y requieren infraestructura especializada. 

• Disponibilidad  limitada:  No  todos  los  hospitales  >enen  acceso  a  resonancias  magné>cas  o  equipos  de  biopsia 
hepá>ca guiada por imagen. 

• Sesgo en la interpretación: La evaluación de imágenes médicas depende de la experiencia del radiólogo. 

Conclusión,  no  existe  un  método  de  detección  temprana  altamente  efec>vo  y  accesible.  Por  ello,  el  desarrollo  de 

herramientas  basadas  en  Inteligencia  Ar>ﬁcial  (IA)  representa  una  alterna>va  innovadora  y  prometedora  para  mejorar  el 

diagnós>co del cáncer de hígado. 

1.3. 

JusOﬁcación del estudio: Uso de IA para mejorar la predicción 

Debido  a  las  limitaciones  indicadas  anteriormente,  los  métodos  tradicionales  de  detección  no  son  suﬁcientes  para 

garan>zar  una  detección  temprana.  Estos  desafos,  han  llevado  a  una  necesidad  urgente  de  nuevas  herramientas 

diagnós>cas que sean precisas, accesibles y automa>zadas. Es aquí, donde entra en juego, la Inteligencia Ar>ﬁcial (IA), que 

ha demostrado ser capaz de detectar patrones ocultos en los datos médicos y mejorar la precisión del diagnós>co. 

La IA, especialmente los modelos de Machine Learning y Deep Learning, automa>za el análisis de grandes volúmenes 

de datos médicos y permite, idenOﬁcar correlaciones ocultas entre variables clínicas, que pueden ser ignoradas en análisis 

convencionales,  opOmizar  la  precisión  del  diagnósOco,  reduciendo  falsos  posi>vos,  (pacientes  sanos  diagnos>cados 

erróneamente  con  cáncer)  y  falsos  nega>vos,  (casos  de  cáncer  no  detectados  a  >empo),  y  desarrollar  herramientas 

predicOvas  basadas  en  tablas,  lo  que  hace  que  los  modelos  sean  más  accesibles  y  aplicables  en  hospitales  con  menos 

recursos.  Esto  lleva,  al  desarrollo  de  modelos  predic>vos  accesibles  y  eﬁcientes,  que  pueden  complementar  los  métodos 

tradicionales y mejorar la detección temprana del cáncer de hígado. 

1.4.  Explicación del PLCO dataset y su origen 

El  PLCO,  (Prostate,  Lung,  Colorectal,  and  Ovarian)  Cancer  Screening  Trial  Dataset,  es  una  base  de  datos  de  acceso 

restringido, desarrollada por los Na>onal Ins>tutes of Health (NIH) de EE.UU. Este conjunto de datos con>ene información 

detallada  de  cánceres  de  próstata,  pulmón,  colorrectal  y  ovario,  pero  también  incluye  datos  sobre  otros  >pos  de  cáncer, 

como el de hígado. 

Este  dataset,  se  recopiló  como  parte  de  un  estudio  poblacional  diseñado,  para  evaluar  la  eﬁcacia  de  diferentes 

estrategias  de  detección  temprana  de  cáncer.  El  dataset,  no  se  basa  en  registros  hospitalarios  tradicionales,  sino  que  se 

construyó, a par>r de formularios voluntarios completados por miles de pacientes en un seguimiento a largo plazo. 

Los  par>cipantes,  rellenaban  encuestas  médicas  periódicas  que  incluían;  Información  demográﬁca,  (edad,  género, 

etnia),  es>los  de  vida,  (tabaquismo,  consumo  de  alcohol,  ac>vidad  fsica),  antecedentes  médicos,  (historial  de  cáncer, 

enfermedades hepá>cas, cirrosis), resultados de análisis clínicos y biomarcadores. El obje>vo del estudio, era monitorear a 

los par>cipantes, para iden>ﬁcar quiénes desarrollaban cáncer y quiénes no. 

Este dataset, es único en comparación con otras bases de datos médicas tradicionales porque: 

5

Juan Armario Muñoz

Es  un  estudio  poblacional  de  seguimiento,  que  no  se  limita  a  datos  de  hospitales,  sino  que  rastrea  la  salud  de  los 

pacientes a lo largo del >empo. Esto permite, estudiar la evolución de factores de riesgo antes del desarrollo del cáncer. 

Incluye, datos detallados sobre múl>ples cánceres, incluyendo el de hígado, haciendo posible la posibilidad de analizar 

patrones comunes, en pacientes con diferentes >pos de cáncer, y permite evaluar, cómo los factores de riesgo evolucionan a 

lo largo del >empo. 

Es un dataset de alta calidad y validado. Los datos provienen de una ins>tución médica de pres>gio (NIH), que se han 

u>lizado en múl>ples inves>gaciones cienrﬁcas publicadas en revistas médicas. 

Aun  así,  el  dataset,  presenta  numerosos  desafos,  como  por  ejemplo,  la  existencia  de  valores  faltantes,  debido  a 

respuestas  voluntarias  incompletas,  y,  también,  puede  presentar  desbalanceamiento  de  clases,  (más  par>cipantes  sanos 

que enfermos). 

1.5.  Deﬁnición de la variable liver_cancer como target principal 

El obje>vo central de esta inves>gación, es predecir la presencia de cáncer de hígado, y para ello, se deﬁne la variable 

‘liver_cancer’, como el target principal en los modelos de Machine Learning y Deep Learning. 

Deﬁnición de la variable: 

•  liver_cancer = 1 → Paciente ha sido diagnos>cado con cáncer de hígado. 

•  liver_cancer = 0 → Paciente sin diagnós>co de cáncer de hígado. 

Esta variable, permite formular el problema como una tarea de clasiﬁcación binaria, en la que los modelos de IA, deben 

aprender a dis>nguir entre pacientes con y sin cáncer hepá>co. 

6

Juan Armario Muñoz

2. Metodología general del estudio 

En  este  contexto,  este  estudio  busca  comparar  dos  enfoques  dis>ntos  dentro  de  la  Inteligencia  Ar>ﬁcial  para  la 

detección del cáncer de hígado: Machine Learning y Deep Learning.  

El enfoque de Machine Learning, se basa en algoritmos supervisados que aprenden de patrones en los datos y generan 

predicciones  a  par>r  de  relaciones  iden>ﬁcadas  entre  las  variables  clínicas.  En  contraste,  el  enfoque  de  Deep  Learning, 

u>liza  redes  neuronales  ar>ﬁciales,  para  analizar  los  datos  de  una  manera  más  compleja,  siendo  capaz  de  descubrir 

correlaciones profundas que pueden ser difciles de captar con modelos tradicionales. 

Ambos  enfoques,  presentan  caracterís>cas  únicas,  ventajas  y  limitaciones  que  los  hacen  adecuados  en  dis>ntos 

contextos. Mientras que Machine Learning es más fácil de interpretar y requiere menos datos, Deep Learning es capaz de 

capturar  patrones  más  complejos,  aunque  a  expensas  de  una  mayor  demanda  computacional  y  una  menor  facilidad  de 

interpretación. La meta de este estudio, es determinar cuál de los dos enfoques ofrece mejores resultados en la predicción 

del cáncer de hígado a par>r de datos clínicos, evaluando su rendimiento a través de métricas estandarizadas. 

2.1.  Explicación de los dos bloques del estudio 

2.1.1.  Machine Learning 

Los algoritmos de Machine Learning, han sido ampliamente u>lizados en la medicina para la clasiﬁcación y predicción 

de enfermedades. En este estudio, se emplean modelos de aprendizaje supervisado, para analizar la presencia de cáncer de 

hígado, a par>r de datos clínicos obtenidos en el PLCO Dataset. 

El principio fundamental de Machine Learning, es el uso de modelos estadís>cos y matemá>cos que pueden iden>ﬁcar 

patrones  en  los  datos  sin  necesidad  de  una  programación  explícita  de  reglas.  Estos  modelos,  se  entrenan  con  datos 

históricos en los que se conoce el diagnós>co de los pacientes y, posteriormente, pueden predecir la probabilidad de que un 

nuevo paciente desarrolle cáncer de hígado. 

Para  este  estudio,  se  han  seleccionado  varios  algoritmos  de  Machine  Learning  ampliamente  u>lizados  en  la 

clasiﬁcación  médica:  regresión  logís>ca,  Random  Forest,  Support  Vector  Machines  (SVM)  y  Gradient  Boos>ng  (XGBoost). 

Cada  uno  de  estos  algoritmos  >ene  sus  propias  caracterís>cas  y  es  evaluado  en  función  de  su  precisión,  capacidad  de 

generalización y facilidad de interpretación. 

La regresión logís>ca, es el modelo más simple y es u>lizado como línea base en este estudio, ya que proporciona una 

forma rápida de evaluar la relación entre las variables clínicas y la variable obje>vo ‘liver_cancer’. Por otro lado, Random 

Forest,  es  un  modelo  basado  en  árboles  de  decisión  que  permite  capturar  relaciones  no  lineales  y  reducir  el  riesgo  de 

sobreajuste,  mediante  la  combinación  de  múl>ples  árboles.  Support  Vector  Machines  (SVM),  es  un  modelo  que  busca 

encontrar un hiperplano óp>mo, para separar las clases de pacientes con y sin cáncer, siendo par>cularmente ú>l cuando 

los datos >enen una estructura compleja. Finalmente, los modelos basados en boos>ng, como XGBoost, u>lizan un enfoque 

itera>vo,  para  mejorar  progresivamente  la  capacidad  predic>va  del  modelo,  permi>endo  una  mejor  precisión  en 

comparación con otros algoritmos tradicionales. 

Uno  de  los  aspectos  clave,  del  uso  de  Machine  Learning  en  este  estudio,  es  la  necesidad  de  realizar  un 

preprocesamiento adecuado de los datos. Aplicaré técnicas como normalización de variables, eliminación de valores arpicos 

y  balanceo  de  clases,  con  el  ﬁn  de  garan>zar  que  los  modelos  no  se  vean  afectados  por  sesgos  en  la  distribución  de  los 

datos. Además, realizaré una selección de caracterís>cas para descartar variables redundantes y mejorar la eﬁciencia de los 

algoritmos. 

A pesar de sus ventajas, el uso de Machine Learning en la detección del cáncer de hígado también presenta desafos. La 

necesidad  de  deﬁnir  manualmente  las  caracterís>cas  más  relevantes  para  la  clasiﬁcación,  puede  ser  una  limitación  en 

comparación  con  el  Deep  Learning,  que  es  capaz  de  aprender  estas  representaciones  de  manera  automá>ca.  Además, 

7

 
Juan Armario Muñoz

algunos  modelos  de  Machine  Learning  pueden  no  capturar  relaciones  altamente  complejas  en  los  datos,  lo  que  puede 

afectar su capacidad de generalización. 

2.1.2. Deep Learning, redes neuronales 

El Deep Learning, es una rama del aprendizaje automá>co, que u>liza redes neuronales ar>ﬁciales, para analizar datos 

de  una  manera  más  avanzada.  A  diferencia  de  los  algoritmos  de  Machine  Learning  tradicionales,  las  redes  neuronales 

pueden  aprender  automá>camente  representaciones  complejas  de  los  datos  sin  necesidad  de  deﬁnir  manualmente  las 

caracterís>cas a considerar en el modelo. 

En  este  estudio,  se  ha  implementado  una  Red  Neuronal  Ar>ﬁcial  (ANN),  para  la  predicción  del  cáncer  de  hígado, 

u>lizando  la  biblioteca  TensorFlow/Keras.  La  arquitectura  de  la  red  neuronal  está  compuesta  por  varias  capas  densas 

interconectadas, donde cada capa transforma los datos de entrada en representaciones más abstractas antes de producir 

una salida ﬁnal. 

Una de las principales ventajas del Deep Learning, es su capacidad para manejar datos complejos y detectar patrones 

ocultos  que  pueden  no  ser  evidentes  para  los  modelos  tradicionales  de  Machine  Learning.  Sin  embargo,  esta  mayor 

capacidad predic>va también conlleva mayores requerimientos computacionales y una menor facilidad de interpretación, lo 

que puede ser un obstáculo en aplicaciones médicas, donde la transparencia del modelo es crucial. 

Para  mejorar  el  rendimiento  de  la  red  neuronal,  en  este  estudio  se  han  aplicado  técnicas  avanzadas  como  Batch 

Normaliza>on  y  Dropout,  que  permiten  estabilizar  el  entrenamiento  y  reducir  el  riesgo  de  sobreajuste.  Además,  se  ha 

u>lizado Keras Tuner para op>mizar la arquitectura del modelo, ajustando parámetros como el número de neuronas, la tasa 

de aprendizaje y la can>dad de capas ocultas. 

A  pesar  de  sus  beneﬁcios,  el  uso  de  Deep  Learning  en  este  estudio  también  presenta  limitaciones.  Dado  que  los 

modelos de redes neuronales requieren grandes volúmenes de datos para su entrenamiento, su rendimiento puede verse 

afectado si los datos disponibles no son suﬁcientes. Además, la falta de interpretación en las decisiones del modelo puede 

hacer  que  su  aplicación  en  entornos  clínicos  sea  más  complicada,  en  comparación  con  los  modelos  de  Machine  Learning 

tradicionales. 

2.2.  Estrategia de comparación entre ambos enfoques 

Dado que tanto Machine Learning como Deep Learning >enen sus propias fortalezas y debilidades, este estudio, busca 

comparar  ambos  enfoques  de  manera  rigurosa,  para  determinar  cuál  ofrece  un  mejor  rendimiento  en  la  predicción  del 

cáncer de hígado. 

Para  realizar  esta  comparación,  se  ha  diseñado  una  estrategia  basada  en  métricas  de  evaluación  estandarizadas  en 

clasiﬁcación  binaria.  Entre  las  métricas  u>lizadas  se  encuentran  precisión  (accuracy),  sensibilidad  (recall),  especiﬁcidad  y 

ROC-AUC Score, cada una proporcionando información clave sobre la capacidad predic>va de los modelos. 

El análisis de resultados, no solo se centrará en la precisión del modelo, sino también en su capacidad para detectar 

correctamente los casos posi>vos de cáncer de hígado, sensibilidad (Recall), lo cual es crucial en aplicaciones médicas. Un 

modelo con una precisión alta pero una sensibilidad baja, podría no ser ú>l en la prác>ca, ya que podría fallar en iden>ﬁcar 

pacientes enfermos. 

Además,  se  considerará  la  interpretabilidad  del  modelo,  ya  que  en  aplicaciones  médicas,  es  fundamental,  que  los 

especialistas puedan entender cómo el modelo llega a sus decisiones. En este sen>do, los modelos de Machine Learning, 

como Random Forest, permiten obtener la importancia de cada variable en la predicción, mientras que en Deep Learning se 

explorarán métodos como SHAP (Shapley Addi>ve Explana>ons), para mejorar la explicabilidad del modelo. 

Con esta estrategia de comparación, se busca no solo determinar cuál modelo >ene mejor rendimiento, sino también 

iden>ﬁcar cuál sería más fac>ble para su implementación en la prác>ca médica. 

8

 
Juan Armario Muñoz

3. Técnicas de preprocesamiento aplicadas 

El  preprocesamiento  de  datos,  es  una  fase  crí>ca  en  cualquier  proyecto  de  Machine  Learning  o  Deep  Learning, 

especialmente cuando se trabaja con datos clínicos, como los del PLCO Dataset. En este estudio, el preprocesamiento, no 

solo se enfoca en limpiar y transformar los datos, sino también en op>mizar la calidad de la información para garan>zar que 

los modelos puedan aprender de manera eﬁciente y precisa. 

Se han implementado, diversas técnicas para mejorar la representa>vidad y la u>lidad del dataset, incluyendo Feature 

Engineering,  imputación  de  valores  faltantes,  balanceo  de  clases  y  la  creación  de  múl>ples  versiones  del  dataset  para 

evaluar el impacto de diferentes transformaciones. 

Sin embargo, antes de preprocesar nuestro dataset, dividí mi dataset en conjuntos de entrenamiento y prueba debido 

a las siguientes razones: 

• Evitar  data  leakage  o  fuga  de  información,  que  ocurre  cuando  la  información  del  conjunto  de  prueba  se  u>liza 

indirectamente  durante  el  entrenamiento.  Esto  puede  llevar,  a  una  evaluación  op>mista  e  irreal  del  rendimiento  del 

modelo.  Al  dividir  los  datos  al  principio,  aseguramos  que  el  conjunto  de  prueba  permanezca  completamente 

independiente del proceso de entrenamiento. 

• Evaluar el rendimiento real del modelo. La división temprana entre entrenamiento y prueba, asegura que el modelo 

solo  vea  los  datos  de  entrenamiento,  durante  el  proceso  de  ajuste.  El  conjunto  de  prueba,  debe  usarse  solo,  para  la 

evaluación  ﬁnal  del  modelo,  de  modo  que  reﬂeje  el  rendimiento  del  modelo  en  datos  “nuevos”  e  invisibles  para  el 

modelo durante el entrenamiento. 

• Prevenir  sesgos  en  el  modelo.  Si  se  realiza  el  preprocesamiento  y  balanceo  antes  de  la  división  de  los  datos,  los 

parámetros  calculados  en  los  datos  de  entrenamiento,  (medias,  transformaciones,…),  podrían  verse  afectados  por  los 

datos de prueba. Esto sesgaría el modelo, ya que tendría acceso a información sobre el conjunto de prueba. 

3.1.  Feature Engineering y selección de variables 

El  proceso  de  feature  engineering  en  este  estudio,  se  centró  en  seleccionar  y  descartar  variables  con  el  obje>vo  de 

mejorar la capacidad predic>va del modelo para la detección del cáncer de hígado. Para ello, se realizó un análisis detallado 

de cada sección del dataset proporcionado por la NIH, clasiﬁcando las variables según su relevancia, eliminando información 

redundante o irrelevante y generando nuevas representaciones de datos cuando fue necesario. 

El  primer  paso  en  el  proceso  consis>ó,  en  explorar  el  dataset  original,  iden>ﬁcando  el  número  de  observaciones  y 

variables disponibles. Se realizó una clasiﬁcación de las variables en diferentes secciones basadas en la documentación del 

PLCO dataset, permi>endo un análisis sistemá>co de cada grupo de caracterís>cas. Se examinó la distribución de los valores, 

la  can>dad  de  datos  faltantes  y  la  correlación  entre  variables,  asegurando  que  solo  aquellas  caracterís>cas  con  valor 

informa>vo signiﬁca>vo fueran consideradas en el modelo ﬁnal. Además, se eliminaron variables con valores únicos o con 

altos porcentajes de valores nulos, ya que estas no aportaban información relevante para la predicción del cáncer de hígado. 

A lo largo del análisis, se tomó la decisión de descartar variables redundantes o que no proporcionaban información 

adicional signiﬁca>va. Por ejemplo, en la sección de datos demográﬁcos, se encontró una alta correlación entre las variables 

“age” y “agelevel”, ambas representando la edad de los par>cipantes. Se optó por conservar “agelevel”, ya que representaba 

la  edad  de  manera  categórica  y  contenía  menos  valores  dis>ntos,  facilitando  su  tratamiento  en  modelos  de  Machine 

Learning.  De  manera  similar,  en  la  sección  de  caracterís>cas  del  cáncer,  se  eliminaron  variables  como  “liver_behavior”, 

“liver_grade” y “liver_morphology”, ya que este estudio se enfoca en la predicción de la aparición de cáncer de hígado, y no 

en la clasiﬁcación de la enfermedad una vez diagnos>cada. 

Otro aspecto clave del proceso fue la eliminación de datos no relevantes para la predicción, como los iden>ﬁcadores 

(plco_id),  variables  administra>vas  (bq_returned,  bq_compdays)  y  variables  de  consen>miento  (reconsent_outcome). 

9

Juan Armario Muñoz

También  se  eliminaron  registros  con  información  incompleta,  como  aquellos  donde  el  formulario  de  salud  fue  rechazado 

debido  a  un  diagnós>co  previo  de  cáncer,  garan>zando  que  el  análisis  estuviera  basado  en  datos  representa>vos  de  la 

población en riesgo. 

Como resultado del proceso de feature engineering y selección de variables, se construyó una versión op>mizada del 

dataset,  que  contenía  solo  las  variables  relevantes  para  la  predicción  de  liver_cancer.  Este  preprocesamiento  permi>ó 

reducir  la  dimensionalidad  del  dataset  y  mejorar  la  eﬁciencia  de  los  modelos  de  machine  learning  y  deep  learning, 

asegurando  que  los  datos  u>lizados  en  el  entrenamiento  sean  de  alta  calidad  y  libres  de  redundancias  o  información 

irrelevante. 

3.2. 

Imputación de valores faltantes 

La  presencia  de  valores  faltantes  en  datasets  clínicos,  es  un  desafo  común,  que  puede  afectar  signiﬁca>vamente  la 

calidad  de  los  modelos  predic>vos.  En  el  caso  del  PLCO  dataset,  los  datos  fueron  recolectados  a  lo  largo  de  varios  años 

mediante  formularios  voluntarios,  lo  que  incrementa  la  posibilidad,  de  que  existan  variables  incompletas,  debido  a 

respuestas omi>das o errores en la recopilación. 

Dado  que  el  obje>vo  de  este  estudio,  es  la  predicción  del  cáncer  de  hígado  a  par>r  de  la  variable  ‘liver_cancer’,  es 

fundamental, que los datos estén lo más completos posible para mejorar la precisión de los modelos de Machine Learning y 

Deep Learning. Para ello, se han aplicado dis>ntas técnicas de imputación de valores faltantes, las cuales pueden clasiﬁcarse 

en imputación simple e imputación múl>ple.  

Cada uno de estos métodos se estudió, creando y entrenando diversos modelos, para analizar y seleccionar la técnica 

que arrojó mejores resultados. Para la toma de esa decisión, se crearon matrices de confusión y se analizaron métricas como 

el error cuadrá>co, 

, y la raíz de la desviación cuadrá>ca media, RMSE. 

R2

3.2.1. Imputación simple 

La imputación simple, es una de las estrategias más u>lizadas para tratar valores faltantes, que consiste en reemplazar 

los valores ausentes, con un único es>mador basado en la distribución de los datos observados. Este método, es adecuado, 

cuando  la  can>dad  de  valores  faltantes  es  baja  y  cuando  la  variable  afectada,  no  >ene  una  fuerte  dependencia  con  otras 

variables. Aunque es una solución rápida y sencilla, >ene la limitación de no capturar la incer>dumbre en la imputación ni la 

relación entre variables. 

3.2.2. Imputación múlOple  

Se han explorado, diversas técnicas de imputación simple. Sin embargo, cada uno de estos métodos, ha demostrado 

ser  ú>l  en  dis>ntos  escenarios,  pero  comparten  una  limitación  clave.  Todas  estas  técnicas,  generan  un  único  valor  de 

imputación para cada observación faltante, sin considerar la incer>dumbre de la predicción. 

Para  abordar  esta  limitación,  se  aplicó  imputación  múl>ple  mediante  ecuaciones  encadenadas  (MICE,  Mul>ple 

Imputa>on by Chained Equa>ons). Este método, permite, es>mar múl/ples valores posibles para cada celda faltante, lo que 

ayuda a reﬂejar mejor la variabilidad y la estructura subyacente de los datos. 

3.2.3. Procedimiento en el estudio 

Antes de aplicar cualquier método de imputación, se realizó un análisis exploratorio para determinar el porcentaje de 

valores faltantes en cada variable. Este análisis permi>ó clasiﬁcar las variables en función del porcentaje de datos ausentes y 

seleccionar la técnica de imputación más adecuada. 

Los  resultados  mostraron  que  algunas  variables  contenían  un  porcentaje  elevado  de  valores  faltantes,  mientras  que 

otras  presentaban  ausencias  en  menos  del  1%  de  las  observaciones.  A  par>r  de  estos  resultados,  se  implementaron 

diferentes estrategias de imputación. 

10

 
 
 
Juan Armario Muñoz

Tras  aplicar  diferentes  métodos  de  imputación  a  los  valores  faltantes  en  el  PLCO  dataset,  se  realizó  una  evaluación 

detallada del impacto de cada técnica en la estructura de los datos y en el rendimiento de los modelos de Machine Learning. 

Para ello, se analizaron los cambios en la correlación entre variables tras la imputación y se compararon los resultados en 

términos de error cuadrá>co medio (RMSE) y coeﬁciente de determinación (

) en varios modelos de predicción. 

R2

El primer aspecto que se evaluó, fue cómo la imputación afectó la relación 

entre las variables del dataset. Se observó, que la imputación basada en MICE, 

generó la mayor variación en la matriz de correlación, lo que sugiere, que este 

método,  reestructuró  en  mayor  medida,  la  relación  entre  las  variables  en 

comparación con las demás técnicas. Por otro lado, la imputación mediante KNN 

y  regresión  lineal,  produjo  un  menor  grado  de  alteración  en  la  estructura  de 

correlaciones,  mientras  que  la  imputación  por  media  y  mediana  mantuvo  las 

correlaciones más cercanas al dataset original. Este hallazgo es relevante, ya que 

cambios  signiﬁca>vos  en  la  estructura  de  correlaciones  pueden  afectar  la 

capacidad de los modelos para aprender patrones relevantes en los datos. 

En  la  evaluación  del  rendimiento  de  los  modelos  predic>vos,  se  encontró 

que  las  diferencias  en  RMSE  y  R²  entre  los  métodos  de  imputación  fueron 

mínimas  en  modelos  lineales  como  regresión  lineal  y  KNN  regression,  lo  que 

indica que ninguno de los métodos tuvo un impacto drás>co en la precisión de 

la  predicción  de  liver_cancer.  Sin  embargo,  en  modelos  más  avanzados  como 

Random  Forest  y  XGBoost,  se  observó  que  el  rendimiento  fue  idén>co 

independientemente del método de imputación empleado, con valores de RMSE 

de 0.0058 y R² de 0.9743 en todas las imputaciones. Este resultado sugiere que, 

en modelos más complejos y robustos, la imputación de valores faltantes no tuvo un impacto signiﬁca>vo en la capacidad 

del modelo para predecir la variable obje>vo. 

Otro  aspecto  importante  a  considerar  fue  el  costo  computacional  de  cada  técnica.  Mientras  que  MICE  y  KNN, 

requirieron un >empo considerable para la imputación, debido a su naturaleza itera>va y dependiente de múl>ples cálculos, 

la  imputación  con  media  y  mediana  fue  la  más  eﬁciente  en  términos  de  procesamiento.  Esta  diferencia,  en  >empos  de 

cómputo,  se  vuelve  relevante  cuando  se  trabaja  con  datasets  grandes,  donde  métodos  más  avanzados  pueden  volverse 

computacionalmente costosos sin aportar mejoras sustanciales en el rendimiento del modelo. 

Finalmente,  el  análisis  demostró  que  la  imputación  mediante  media  y  mediana  preservó  mejor  la  estructura  de  los 

datos sin generar grandes variaciones en la distribución original de las variables. Aunque MICE se basa en un enfoque más 

soﬁs>cado y estadís>camente sólido, su aplicación en este caso par>cular no ofreció ventajas signiﬁca>vas en términos de 

precisión  predic>va.  Además,  al  generar  mayores  cambios  en  la  correlación  entre  variables,  introdujo  una  mayor 

incer>dumbre en la estructura del dataset, lo que podría afectar la hora de interpretar los modelos en un contexto clínico. 

3.2.4. Conclusión 

Tras  evaluar  los  diferentes  métodos  de  imputación  en  términos  de  estabilidad  de  los  datos,  impacto  en  las 

correlaciones, rendimiento en modelos de Machine Learning y eﬁciencia computacional, se concluyó que la imputación con 

media y mediana era la opción más adecuada para este estudio. 

Una  de  las  principales  razones  que  jus>ﬁcaron  esta  elección  fue  su  simplicidad  y  eﬁciencia,  lo  que  permi>ó  una 

imputación rápida y efec>va sin alterar signiﬁca>vamente la estructura original de los datos. Este aspecto es especialmente 

relevante en estudios de Machine Learning en medicina, donde los >empos de cómputo pueden ser un factor limitante al 

trabajar con grandes volúmenes de datos clínicos. 

11

 
Juan Armario Muñoz

Otro  factor  importante  fue  el  análisis  del  error  cuadrá>co  medio  (RMSE)  y  el  coeﬁciente  de  determinación  (R²)  en 

modelos  de  Machine  Learning.  Se  encontró  que  las  diferencias  en  rendimiento  entre  los  métodos  de  imputación  eran 

prác>camente  insigniﬁcantes,  especialmente  en  modelos  avanzados  como  Random  Forest  y  XGBoost,  donde  todos  los 

métodos generaron resultados idén>cos en términos de precisión. Esto sugiere que u>lizar una técnica más compleja como 

MICE no ofrecía ventajas signiﬁca>vas en este caso y que métodos más simples podían lograr el mismo nivel de precisión sin 

la complejidad adicional. 

Finalmente, desde una perspec>va de aplicabilidad clínica, la imputación con media y mediana ofrece un enfoque más 

estable y replicable, lo que facilita su implementación en futuros estudios o sistemas de predicción. En entornos médicos, es 

fundamental que las técnicas u>lizadas para el tratamiento de datos sean transparentes y fáciles de interpretar, ya que los 

resultados del modelo pueden inﬂuir en decisiones clínicas crí>cas. 

En  conclusión,  se  decidió  u>lizar  la  imputación  con  media  y  mediana  como  método  ﬁnal,  ya  que  demostró  ser  una 

técnica eﬁciente, estable y conﬁable que preserva mejor la estructura de los datos sin introducir cambios signiﬁca>vos en las 

correlaciones  entre  variables.  La  decisión  ﬁnal  se  basó  en  un  equilibrio  entre  precisión,  estabilidad  y  eﬁciencia 

computacional,  priorizando  una  solución  que  op>mice  la  calidad  de  los  datos  sin  comprometer  la  robustez  del  modelo 

predic>vo. 

3.4.  Data transformaOon 

La transformación de datos es una fase esencial en la preparación del conjunto de datos para el modelado de Machine 

Learning.  Su  propósito  es  mejorar  la  calidad  de  los  datos,  op>mizar  la  capacidad  predic>va  del  modelo  y  garan>zar  la 

coherencia  entre  los  conjuntos  de  entrenamiento  y  prueba.  En  este  estudio,  se  implementaron  diversas  estrategias  para 

seleccionar y transformar caracterís>cas, asegurando que los modelos predic>vos fueran más precisos, estables y eﬁcientes. 

Uno  de  los  primeros  pasos  consis>ó  en  la  selección  de  caracterís>cas,  donde  se  iden>ﬁcaron  las  variables  más 

relevantes mediante técnicas como Mutual Informa>on, Pearson y Spearman correla>on. Estas métricas permi>eron evaluar 

la relación de cada variable con la variable obje>vo, eliminando aquellas con baja importancia o alta redundancia. Al reducir 

el número de caracterís>cas irrelevantes, se consiguió mejorar la eﬁciencia computacional del modelo sin comprometer su 

rendimiento,  evitando  el  sobreajuste  y  asegurando  que  el  modelo  se  enfocara  en  las  variables  con  mayor  impacto  en  la 

predicción del cáncer de hígado. 

Además de la selección de variables, se aplicaron diversas transformaciones matemá>cas para mejorar la distribución 

de  los  datos  y  hacerlos  más  adecuados  para  los  algoritmos  de  Machine  Learning.  Algunas  variables  fueron  some>das  a 

transformaciones logarítmicas para reducir la asimetría en su distribución, mientras que otras fueron elevadas al cuadrado o 

a la cuarta potencia para resaltar patrones no lineales. En otros casos, la raíz cuadrada y la raíz cuarta fueron u>lizadas para 

suavizar la variabilidad de ciertas caracterís>cas. Estas transformaciones ayudaron a que los modelos captaran de manera 

más efec>va las relaciones complejas en los datos, mejorando la estabilidad del entrenamiento y reduciendo la inﬂuencia de 

valores extremos. 

Para  evaluar  la  efec>vidad  de  estas  transformaciones,  se  compararon  dos  enfoques  dis>ntos:  uno  en  el  que  se 

eliminaron  las  caracterís>cas  con  menor  importancia  y  otro  en  el  que  se  aplicaron  transformaciones  a  todas  las  variables 

relevantes. Ambos conjuntos de datos fueron u>lizados para entrenar modelos de Random Forest, analizando métricas clave 

como precisión, F1-score, recall y AUC-ROC. Los resultados indicaron que ambas estrategias tenían un rendimiento similar en 

términos de predicción, pero el modelo que u>lizaba un menor número de variables era más eﬁciente computacionalmente. 

Esto sugiere que una transformación adecuada de los datos permite obtener modelos más ligeros sin perder precisión en las 

predicciones. 

Un  aspecto  fundamental  del  proceso  de  transformación  fue  garan>zar  la  coherencia  entre  el  conjunto  de 

entrenamiento  y  el  conjunto  de  prueba.  Para  evitar  sesgos  y  asegurar  que  los  modelos  fueran  evaluados  en  condiciones 

12

Juan Armario Muñoz

realistas,  se  aplicaron  las  mismas  transformaciones  a  los  datos  de  prueba.  Esta  estrategia  evitó  problemas  como  data 

leakage, donde el modelo puede beneﬁciarse inadver>damente de información que no estaría disponible en un escenario 

real. Gracias a esta consistencia en el preprocesamiento, los resultados obtenidos en la fase de prueba reﬂejan con mayor 

ﬁdelidad la capacidad de generalización del modelo. 

Los resultados de esta etapa demostraron que la transformación de datos no solo op>mizó el rendimiento del modelo, 

sino  que  también  facilitó  su  implementación  al  reducir  la  complejidad  del  conjunto  de  datos.  La  eliminación  de  variables 

irrelevantes permi>ó construir modelos más eﬁcientes, mientras que la aplicación de transformaciones matemá>cas mejoró 

la estabilidad del entrenamiento y la capacidad de los modelos para iden>ﬁcar patrones en los datos. En úl>ma instancia, 

este enfoque permi>ó desarrollar un sistema predic>vo más robusto, con mayor capacidad para detectar casos de cáncer de 

hígado y mejorar su aplicabilidad en entornos médicos. 

3.5.  Balanceo de datos (SMOTE, Undersampling, Oversampling) 

Uno de los desafos más importantes en el desarrollo de modelos de Machine Learning para la predicción del cáncer de 

hígado  es  el  desbalanceamiento  en  el  dataset.  En  problemas  médicos,  es  común  que  los  datos  de  pacientes  con  la 

enfermedad  sean  signiﬁca>vamente  menores  en  comparación  con  los  pacientes  sanos.  Este  desequilibrio  puede  generar 

modelos que favorezcan la clasiﬁcación de la clase mayoritaria (no cáncer) y disminuyan la capacidad de detección de casos 

posi>vos (cáncer). 

Para abordar este problema, en este estudio se implementaron tres técnicas principales de balanceo de datos. Cada 

método fue aplicado y evaluado mediante la creación de modelos de Machine Learning, con el obje>vo de determinar que 

técnica mejoraba la capacidad del modelo para detectar el cáncer de hígado, sin introducir sesgos en los datos. 

• SMOTE  (SyntheOc  Minority  Over-sampling  Technique):  técnica  de  oversampling  que  genera  nuevas  instancias 

sinté>cas de la clase minoritaria en lugar de simplemente duplicar observaciones existentes. U>liza la interpolación de 

caracterís>cas  entre  ejemplos  reales  de  la  clase  minoritaria,  lo  que  ayuda  a  mejorar  la  capacidad  del  modelo  para 

generalizar. 

• Oversampling: Duplica aleatoriamente observaciones de la clase minoritaria para aumentar su representación. 

• Undersampling (NearMiss): Reduce la can>dad de ejemplos de la clase mayoritaria para alcanzar un equilibrio  en la 

distribución de clases. 

3.5.1. Procedimiento en el estudio 

Para abordar este problema, se implementaron técnicas de balanceo de datos u>lizando herramientas de la biblioteca 

imblearn (imbalanced-learn). Se aplicaron las técnicas anteriormente mencionadas, con el obje>vo de determinar cuál de 

estos  métodos  lograba  mejorar  la  capacidad  predic>va  del  modelo  sin  introducir  sobreajuste  ni  pérdida  de  información 

valiosa.  Se  diseñó  una  metodología  basada  en  el  uso  de  validación  cruzada  estra>ﬁcada,  garan>zando  que  cada  modelo 

fuera evaluado en diferentes par>ciones del dataset y no en un único conjunto de entrenamiento y prueba, lo que permi>ó 

obtener métricas más conﬁables y generalizables. 

El procedimiento de balanceo se desarrolló en varios pasos. Primero, se separaron las caracterís>cas del dataset (X) y la 

variable obje>vo (y). Luego, se aplicaron las diferentes técnicas de balanceo al dataset de entrenamiento, lo que permi>ó 

generar un nuevo conjunto de datos con una distribución de clases equita>va. Para asegurar, que los cambios introducidos 

por el balanceo, no afectaran la estructura de los datos, se realizaron comparaciones visuales y estadís>cas entre el dataset 

original  y  los  datasets  balanceados.  Esto  incluyó  análisis  de  correlaciones,  histogramas  de  distribución  y  comparación  de 

métricas en modelos entrenados con cada método de balanceo. 

El  código  implementado  permi>ó  automa>zar  la  comparación  entre  los  métodos  de  balanceo  y  seleccionar  el  más 

adecuado en función de métricas clave como accuracy, balanced accuracy, precision, recall y F1-score. Se u>lizó un modelo 

13

 
Juan Armario Muñoz

base de Random Forest como clasiﬁcador estándar para evaluar cada técnica. La función de evaluación desarrollada en el 

código  no  solo  permi>ó  obtener  los  resultados  de  cada  modelo,  sino  que  también  incluyó  la  generación  de  matrices  de 

confusión,  lo  que  facilitó  la  interpretación  visual  del  desempeño  de  cada  método  en  términos  de  clasiﬁcación  correcta  e 

incorrecta de las clases. 

En resumen, el procedimiento aplicado en este estudio se enfocó en: iden>ﬁcar el problema de desbalanceo, aplicar y 

evaluar diferentes estrategias de corrección y comparar los modelos resultantes para seleccionar la mejor técnica. Gracias a 

este enfoque estructurado, se logró mejorar la capacidad del modelo para detectar casos de cáncer de hígado, asegurando 

que los resultados obtenidos sean conﬁables y aplicables en la predicción de enfermedades mediante machine learning y 

deep learning. 

3.5.2. Conclusión 

Tras la aplicación de SMOTE, oversampling y undersampling, así como la evaluación de su impacto en el rendimiento de 

los modelos de machine learning, se obtuvieron resultados altamente posi>vos en términos de accuracy, balanced accuracy, 

precision, recall y F1-score. 

El análisis de los resultados obtenidos en la evaluación de los modelos balanceados reveló que SMOTE fue la técnica 

más efec>va para corregir el desbalanceamiento de clases en el dataset y mejorar la capacidad predic>va del modelo en la 

detección  de  pacientes  con  cáncer  de  hígado.  Aunque  oversampling  y  undersampling  también  lograron  mejorar  el 

rendimiento  del  modelo,  SMOTE  destacó  principalmente  por  su  impacto  en  la  sensibilidad  (Recall),  que  es  una  de  las 

métricas más importantes en problemas médicos. 

Los resultados mostraron que, tras aplicar SMOTE, el recall alcanzó el 100%, lo que indica que el modelo pudo detectar 

absolutamente todos los casos posi>vos sin errores. Esto es fundamental, ya que antes del balanceo, el modelo mostraba un 

sesgo hacia la clase mayoritaria (liver_cancer = 0), resultando en una detección ineﬁcaz de los pacientes con cáncer. 

El aumento en la sensibilidad se debe a la manera en que SMOTE genera ejemplos sinté>cos. En lugar de simplemente 

duplicar  observaciones  existentes,  SMOTE  crea  nuevos  datos  sinté>cos  interpolando  entre  puntos  reales  de  la  clase 

minoritaria. Esto permite que el modelo aprenda patrones más representa>vos de los casos posi>vos sin caer en problemas 

de sobreajuste. 

En comparación con undersampling, SMOTE no eliminó datos valiosos. La técnica de undersampling redujo el tamaño 

del dataset, eliminando instancias de la clase mayoritaria, lo que puede llevar a una pérdida de información crí>ca. Aunque 

undersampling logró también resultados perfectos en este estudio, su impacto en datasets más grandes, podría ser nega>vo 

debido a la reducción de datos de entrenamiento. 

En conclusión, SMOTE fue la mejor técnica de balanceo para este estudio, ya que permi>ó crear un modelo predic>vo 

más  robusto,  con  una  mejor  capacidad  para  detectar  casos  posi>vos  de  liver_cancer,  sin  comprometer  la  estabilidad  y 

generalización del modelo, preservando la estructura del dataset sin eliminar información valiosa ni generar sobreajuste. 

14

 
Juan Armario Muñoz

4. Algoritmos de Machine Learning 

El desarrollo del modelo, para la predicción del cáncer de hígado, se llevó a cabo mediante la evaluación compara>va 

de  varios  algoritmos  de  Machine  Learning,  con  el  obje>vo  de  iden>ﬁcar,  cuál  tenía  un  mejor  desempeño  en  términos  de 

precisión, sensibilidad y área bajo la curva ROC. Se u>lizaron algoritmos como regresión logís>ca, Random Forest, XGBoost, 

decision  tree,  AdaBoost  y  SVM,  aplicando  técnicas  de  validación  cruzada  para  asegurar  que  los  resultados  fueran 

representa>vos y generalizables. 

4.1.  Creación de modelo y comparación de algoritmos 

El primer paso fue deﬁnir una serie de algoritmos de Machine Learning para evaluar su desempeño en la predicción del 

cáncer  de  hígado.  Se  seleccionaron  modelos  de  dis>ntos  enfoques,  incluyendo  modelos  lineales,  árboles  de  decisión  y 

métodos de ensemble learning. Los modelos probados inicialmente fueron: 

• Regresión LogísOca (LogisOcRegression): Modelo lineal clásico u>lizado en clasiﬁcación binaria. 

• Árbol de Decisión (DecisionTreeClassiﬁer): Modelo basado en reglas de decisión. 

• Random Forest (RandomForestClassiﬁer): Ensamble de múl>ples árboles de decisión para mejorar la generalización. 

• SVM  (Support  Vector  Machine)  (LinearSVC):  Modelo  lineal  que  encuentra  el  hiperplano  óp>mo  para  separar  las 

clases. 

• AdaBoost (AdaBoostClassiﬁer): Algoritmo de boos>ng que mejora la predicción combinando modelos débiles. 

• XGBoost (XGBClassiﬁer): Algoritmo de boos>ng basado en árboles de decisión op>mizado para grandes volúmenes 

de datos. 

El  entrenamiento  de  los 

modelos se realizó, u>lizando el 

dataset  donde  los  datos  habían 

sido  previamente  procesados 

para  eliminar  el  problema  de 

desbalanceamiento  de  clases. 

Se  u>lizó  un  esquema  de 

validación cruzada estra>ﬁcada, 

asegurando  que  los  datos  de 

e n t r e n a m i e n t o  y  p r u e b a 

c o n s e r v a r a n 

l a  m i s m a 

proporción de clases en cada iteración y se evaluaron varias métricas clave, incluyendo accuracy, recall, precision y F1-score, 

con énfasis en la sensibilidad (recall), dado que el obje>vo del modelo es maximizar la detección de pacientes con cáncer de 

hígado. 

4.1.1. Métricas claves 

En problemas de clasiﬁcación binaria como la detección del cáncer de hígado, la elección de las métricas adecuadas es 

fundamental  para  evaluar  la  calidad  del  modelo.  No  todas  las  métricas  >enen  el  mismo  peso,  y  su  interpretación  puede 

cambiar dependiendo de si el dataset está balanceado o desbalanceado. 

Para  este  estudio,  se  priorizaron  tres  métricas  clave:  Accuracy  (precisión  global),  recall  (sensibilidad  o  tasa  de 

verdaderos posi>vos), ROC-AUC (área bajo la curva ROC). Cada una de estas métricas ofrece información diferente sobre el 

desempeño del modelo, y su correcta interpretación permite tomar decisiones sobre qué modelo es más adecuado para la 

detección del cáncer de hígado. 

15

 
Juan Armario Muñoz

Accuracy (Precisión Global): Mide la proporción de predicciones correctas en relación con el total de casos. Aunque 

accuracy  es  una  métrica  estándar  en  problemas  de  clasiﬁcación,  puede  ser  engañosa  en  datasets  desbalanceados.  Si  la 

mayoría de los pacientes no >enen cáncer, un modelo puede obtener una accuracy alta simplemente prediciendo siempre la 

clase mayoritaria (liver_cancer = 0), sin iden>ﬁcar correctamente los casos posi>vos. 

Recall  (Sensibilidad  o  Tasa  de  Verdaderos  PosiOvos):  Es  la  métrica  más  importante  en  este  estudio,  ya  que  mide  la 

capacidad  del  modelo  para  detectar  correctamente  los  casos  posi>vos  de  cáncer.  En  términos  médicos,  un  recall  bajo 

signiﬁcaría que el modelo está fallando en iden>ﬁcar a pacientes enfermos, lo que puede ser crí>co. 

ROC-AUC (Área Bajo la Curva ROC): Evalúa la capacidad del modelo para diferenciar entre clases (liver_cancer = 0 y 

liver_cancer  =  1).  Un  valor  alto  de  AUC  cercano  a  1  indica  que  el  modelo  >ene  una  alta  capacidad  para  dis>nguir 

correctamente entre pacientes sanos y enfermos. 

4.2.  Resultados iniciales y opOmización de hiperparámetros  

Antes de ajustar los hiperparámetros, se evaluaron los modelos en su conﬁguración estándar para establecer una línea 

base  de  comparación.  Los  resultados  iniciales  de  la  evaluación  mostraron  que  decision  tree  tuvo  un  desempeño  decente, 

pero mostró mayor varianza en los resultados, lo que sugiere sobreajuste y regresión logís>ca y SVC no lograron capturar la 

complejidad del problema, presentando menor recall. Random forest y XGBoost tenían los mejores valores en precisión y 

recall, por lo que se decidió realizar un ajuste de hiperparámetros para op>mizar estos modelos. 

Para Random Forest, se ajustaron parámetros como: Número de árboles, profundidad máxima, peso de clases. 

En el caso de XGBoost, se op>mizaron parámetros como: learning_rate, n_esOmators, scale_pos_weight. 

Tras  la  aplicación  de  RandomizedSearchCV  y  GridSearchCV  para  aﬁnar  los  hiperparámetros,  se  observaron  mejoras 

signiﬁca>vas  en  las  métricas  clave,  par>cularmente  en  recall  y  AUC-ROC.  La  op>mización  permi>ó  que  ambos  modelos 

fueran más eﬁcientes en la iden>ﬁcación de casos posi>vos sin comprometer la precisión general del modelo.  

XGBoost  mejoró  El  recall  aumentó  un  7%,  lo  que  signiﬁca  que  el  modelo  detectó  más  casos  posi>vos,  sin  aumentar 

signiﬁca>vamente  los  falsos  posi>vos.  A  su  vez,  el  AUC-ROC  mejoró  un  5%,  conﬁrmando  que  fue  el  modelo  más  efec>vo 

para diferenciar entre pacientes sanos y enfermos.  

Random forest, por su parte, aumentó el recall un 6%, lo que indica que el modelo mejoró en la detección de pacientes 

con cáncer de hígado y se mantuvo con un buen balance entre precisión y recall se op>mizó, logrando un mejor rendimiento 

general sin comprometer la estabilidad del modelo. 

Ambos  modelos  demostraron  ser  adecuados  para  la  detección  de  cáncer  de  hígado,  con  ventajas  dis>ntas  en 

interpretabilidad y capacidad predic>va. 

4.3.  Conclusiones 

Random  Forest  y  XGBoost  fueron  los  modelos  con  mejor  desempeño,  destacando  por  su  capacidad  para  detectar 

correctamente los casos posi>vos sin sacriﬁcar precisión. Se demostró que la sensibilidad es un factor clave en la evaluación 

de  estos  modelos,  ya  que  en  problemas  médicos  es  más  importante  detectar  correctamente  los  casos  posi>vos  que 

minimizar falsos posi>vos. 

El  uso  de  validación  cruzada  permi>ó  garan>zar  que  los  resultados  fueran  estables  y  reproducibles,  evitando 

sobreajuste en el modelo seleccionado. XGBoost emergió como el mejor modelo, con una combinación óp>ma de recall y 

AUC-ROC,  asegurando  una  mejor  detección  de  pacientes  con  cáncer  de  hígado.  Sin  embargo,  random  forest  sigue  siendo 

una alterna>va conﬁable y más interpretable, aspecto fundamental en entornos médicos, aunque con una ligera desventaja 

en recall. 

16

Juan Armario Muñoz

5. Algoritmos de Deep Learning 

El uso de redes neuronales ar>ﬁciales, en la predicción del cáncer de hígado, permite capturar patrones complejos y 

relaciones no lineales en los datos médicos, mejorando la precisión diagnós>ca con respecto a los modelos tradicionales de 

Machine Learning. 

En  esta  sección,  exploraremos  el  desarrollo  de  un  modelo  de  Deep  Learning,  detallando  el  proceso  desde  la 

construcción  de  la  arquitectura  de  la  red  hasta  su  evaluación  con  métricas  avanzadas.  Mediante  este  enfoque,  buscamos 

construir  un  modelo  robusto,  capaz  de  mejorar  la  detección  temprana  del  cáncer  de  hígado  y  contribuir  al  desarrollo  de 

herramientas de apoyo en el diagnós>co médico. 

5.1.  Creación de redes neuronales arOﬁciales (ANN) 

Las redes neuronales ar>ﬁciales (ANN), son modelos computacionales inspirados en la estructura del cerebro humano, 

capaces de aprender patrones complejos a par>r de los datos. En este estudio, se ha desarrollado, un modelo basado en una 

ANN, para predecir la aparición del cáncer de hígado a par>r de un conjunto de caracterís>cas clínicas y demográﬁcas. 

5.1.1. Deﬁnición de la Arquitectura de la Red 

El  modelo  u>lizado  en  este  estudio  sigue  una 

arquitectura  mul>capa,  implementada  con  TensorFlow  y 

Keras. La red consta de varias capas densamente conectadas 

(Dense Layers), con la siguiente estructura: 

• Capa  de  entrada:  Número  de  neuronas  igual  al 

número de caracterís>cas del dataset de entrada. 

• Capas  ocultas:  Se  u>lizan  múl>ples  capas  densas, 

variando  el  número  de  neuronas  para  op>mizar  la 

capacidad  de  representación.  Se  incorporan  técnicas  de 

regularización  como  Batch  Normaliza>on,  para 

estabilizar el entrenamiento y acelerar la convergencia y 

Dropout,  para  evitar  el  sobreajuste  al  eliminar 

conexiones aleatorias durante el entrenamiento. 

• Capa  de  salida:  Una  única  neurona  con  ac>vación 

sigmoide, ya que se trata de un problema de clasiﬁcación 

binaria (cáncer/no cáncer). 

Cada capa oculta emplea la función de ac>vación ReLU, 

(Rec>ﬁed Linear Unit), que es ampliamente u>lizada debido 

a  su  capacidad  para  mi>gar  el  problema  del  gradiente 

desaparecido  y  acelerar  el  aprendizaje.  La  capa  de  salida 

u>liza una función sigmoide, que transforma las salidas en probabilidades. 

El modelo se compila con los siguientes parámetros: 

• Función de pérdida: binary_crossentropy, u>lizada para problemas de clasiﬁcación binaria. 

• OpOmizador: Adam, un op>mizador eﬁciente que ajusta dinámicamente la tasa de aprendizaje. 

• Métrica de evaluación principal: recall, dado que en aplicaciones médicas es crí>co minimizar la can>dad de casos 

no detectados. 

17

 
Juan Armario Muñoz

5.2.  OpOmización con Keras Tuner 

La op>mización de hiperparámetros en redes neuronales es un proceso fundamental para mejorar el rendimiento del 

modelo  sin  necesidad  de  realizar  pruebas  manuales  exhaus>vas.  Keras  Tuner  es  una  herramienta  que  permite  explorar 

múl>ples combinaciones de hiperparámetros de manera eﬁciente, encontrando la mejor conﬁguración para lograr una alta 

precisión y generalización. 

En el contexto de la detección de cáncer de hígado, la op>mización se ha centrado en maximizar el Recall, asegurando 

que la red neuronal pueda detectar la mayor can>dad posible de casos posi>vos. Para ello, se han ajustado parámetros clave 

como el número de capas y neuronas, la tasa de aprendizaje, el tamaño de los lotes y los valores de Dropout, entre otros. 

El  proceso  de  búsqueda  se  ha  realizado  u>lizando  el  algoritmo  Hyperband,  que  permite  asignar  recursos  de  manera 

eﬁciente  evaluando  solo  aquellas  combinaciones  de  hiperparámetros  con  mayor  potencial.  Al  ﬁnalizar  el  proceso,  se 

selecciona la mejor conﬁguración y se construye el modelo deﬁni>vo con los valores óp>mos. 

La op>mización con Keras Tuner ha permi>do reducir el >empo de experimentación y mejorar la capacidad predic>va 

del modelo, obteniendo una arquitectura más robusta y eﬁciente para la detección de cáncer de hígado. 

5.3.  Evaluación del modelo con métricas avanzadas 

Una vez entrenado el modelo, es esencial evaluar su desempeño u>lizando métricas avanzadas que permitan medir su 

efec>vidad en la clasiﬁcación de casos posi>vos y nega>vos de cáncer de hígado. La evaluación no solo consideró la accuracy 

del modelo, sino métricas más especíﬁcas como Recall, Precisión, F1-Score y AUC-ROC, las cuales ofrecen un análisis más 

detallado del rendimiento. Además, se ha u>lizado una matriz de confusión para analizar visualmente los errores come>dos 

por el modelo y comprender en qué casos se generan más confusiones. 

5.4.  Evaluación, comparación y conclusiones 

Se han desarrollado dos modelos de redes neuronales para la detección de cáncer de hígado. Un modelo entrenado 

con  el  dataset  completo  (sin  preprocesamiento  signiﬁca>vo)  y  otro  entrenado  con  el  dataset  preprocesado  (con 

transformación de variables, balanceo de datos y normalización). 

A con>nuación, analizamos y comparamos los resultados obtenidos en ambos enfoques para determinar cuál ofrece 

mejor desempeño. 

Métrica

Modelo con Dataset Completo

Modelo con Dataset Preprocesado

Precisión (Clase 1)

Recall (Clase 1)

F1-Score (Clase 1)

Precisión (Clase 0)

Recall (Clase 0)

Accuracy

AUC-ROC

0.91

0.91

0.91

1.00

1.00

1.00

Alta

0.97

1.00

0.99

1.00

1.00

1.00

Muy alta

Pérdida  (Loss):  En  ambos  modelos,  la  función  de  pérdida  desciende  bruscamente  en  las  primeras  épocas  del 

entrenamiento y luego se estabiliza cerca de cero. Sin embargo, en el modelo preprocesado, la pérdida en el conjunto de 

validación  es  aún  más  estable  y  baja,  lo  que  sugiere  que  el  modelo  experimenta  menos  overﬁ|ng  y  generaliza  mejor  a 

nuevos datos. Esta estabilidad es un indicio de que la arquitectura de la red neuronal y las técnicas de regularización han 

sido efec>vas en mejorar la ﬁabilidad del modelo. 

18

Juan Armario Muñoz

Curva  de  Recall:  El  comportamiento  del  recall  durante  el  entrenamiento  refuerza  los  hallazgos  anteriores.  En  la  red 

neuronal entrenada con el dataset completo, el recall se acerca a 1.00, pero muestra cierta ﬂuctuación, lo que indica que el 

modelo  no  es  completamente  estable  en  la  iden>ﬁcación  de  casos  posi>vos.  En  contraste,  en  la  red  neuronal  con  datos 

preprocesados,  el  recall  alcanza  rápidamente  1.00  y  se  man>ene  constante,  demostrando  una  mayor  conﬁanza  en  la 

detección de cáncer. 

El  análisis  compara>vo  entre  ambas  redes  neuronales  ha  permi>do  iden>ﬁcar  las  ventajas  y  desventajas  de  cada 

enfoque  en  la  detección  de  cáncer  de  hígado.  Cada  modelo  presenta  caracterís>cas  dis>n>vas  que  pueden  inﬂuir  en  su 

aplicabilidad según el contexto y los requisitos del problema. 

El modelo entrenado con el dataset completo destaca por su simplicidad, ya que no requiere un preprocesamiento de 

datos complejo. Además, ofrece un rendimiento sólido con un 91% de recall en la clase 1 y logra una rápida convergencia 

durante el entrenamiento, lo que lo hace eﬁciente en términos de >empo de cómputo. Sin embargo, su principal limitación 

es que no alcanza un recall perfecto, lo cual es crí>co en aplicaciones médicas, ya que un falso nega>vo podría traducirse en 

la  omisión  de  un  diagnós>co  de  cáncer.  Asimismo,  la  mayor  presencia  de  falsos  nega>vos  en  este  modelo  podría 

comprometer la conﬁabilidad del sistema de predicción. 

Por  otro  lado,  el  modelo  entrenado  con  el  dataset  preprocesado  demuestra  ser  considerablemente  más  preciso  y 

robusto.  Al  aplicar  técnicas  de  normalización,  balanceo  de  clases  y  op>mización  de  caracterís>cas,  se  logra  un  100%  de 

recall, asegurando que todos los casos posi>vos sean detectados. Además, presenta una mayor estabilidad en las curvas de 

entrenamiento y generaliza mejor, gracias al preprocesamiento aplicado. Esta mejora en las métricas sugiere que el modelo 

es  capaz  de  diferenciar  con  mayor  precisión  entre  casos  posi>vos  y  nega>vos,  reduciendo  signiﬁca>vamente  los  falsos 

posi>vos y nega>vos. 

No  obstante,  este  modelo  también  presenta  algunas  desventajas.  Su  alto  desempeño  en  las  métricas  podría  indicar 

cierto grado de sobreajuste, lo que signiﬁca que su capacidad de generalización en nuevos conjuntos de datos aún debe ser 

validada. Además, el >empo necesario para el preprocesamiento de datos es mayor, lo que podría ser un factor limitante en 

aplicaciones que requieran respuestas en >empo real o procesamiento a gran escala. 

En  conclusión,  el  modelo  basado  en  datos  preprocesados  demuestra  ser  superior,  ya  que  garan>za  la  detección  de 

todos los casos posi>vos sin comprometer la precisión. Dado que en problemas médicos la omisión de un diagnós>co puede 

tener consecuencias graves, este modelo sería la opción más recomendable. 

19

Juan Armario Muñoz

6. Comparación Machine Learning vs. Deep Learning 

La aplicación de Inteligencia Ar>ﬁcial en la detección del cáncer de hígado ha permi>do evaluar dos enfoques dis>ntos: 

Machine Learning y Deep Learning. Ambos presentan ventajas y limitaciones, por lo que resulta fundamental compararlos 

para determinar cuál ofrece mejor rendimiento en la clasiﬁcación de pacientes con cáncer hepá>co. 

6.1.  Comparación de los resultados de ambos enfoques. 

Los modelos de Machine Learning, como Random Forest, XGBoost y Regresión Logís>ca, fueron entrenados sobre un 

dataset preprocesado y balanceado con técnicas como SMOTE, lo que permi>ó mejorar la detección de casos posi>vos. Los 

resultados mostraron que XGBoost fue el modelo más eﬁciente dentro de este grupo, alcanzando un recall cercano al 96%, 

seguido  por  Random  Forest  con  un  94%.  Estas  cifras  indican  una  alta  capacidad  de  los  modelos  para  iden>ﬁcar 

correctamente  a  los  pacientes  con  cáncer.  Sin  embargo,  ninguno  de  los  algoritmos  de  Machine  Learning  logró  eliminar 

completamente  los  falsos  nega>vos,  lo  que  signiﬁca  que,  aunque  el  rendimiento  es  alto,  aún  existe  la  posibilidad  de  que 

algunos pacientes enfermos no sean iden>ﬁcados por el modelo. 

Por otro lado, el enfoque de Deep Learning, basado en redes neuronales ar>ﬁciales, presentó una mejora signiﬁca>va 

en la detección de casos posi>vos. En el modelo entrenado con el dataset completo sin preprocesamiento avanzado, la red 

neuronal alcanzó un 91% de recall, lo que indica que su capacidad de detección fue comparable a la de los modelos de ML, 

aunque con cierta inestabilidad en el entrenamiento. En el segundo, con un dataset preprocesado, el rendimiento mejoró 

notablemente, logrando un 100% de recall y una mayor estabilidad en las curvas de entrenamiento. 

El  hecho  de  que  la  red  neuronal  op>mizada  haya  alcanzado  un  recall  perfecto  es  un  aspecto  crí>co  en  el  ámbito 

médico, donde la prioridad es minimizar la can>dad de falsos nega>vos. En la prác>ca clínica, un diagnós>co erróneo que 

deje  sin  detectar  un  caso  de  cáncer  puede  tener  consecuencias  fatales,  por  lo  que  contar  con  un  modelo  que  iden>ﬁque 

todos los casos posi>vos representa una ventaja signiﬁca>va frente a los enfoques tradicionales de Machine Learning. 

A  pesar  de  este  alto  desempeño,  también  es  importante  considerar  las  posibles  limitaciones  del  modelo  de  Deep 

Learning. Aunque los resultados indican una mejor generalización y menor riesgo de sobreajuste, el alto rendimiento del 

modelo  sugiere  que  podría  estar  ajustándose  demasiado  a  los  datos  de  entrenamiento,  lo  que  requeriría  pruebas 

adicionales con datos externos para garan>zar su capacidad de predicción en otros entornos clínicos. Además, el >empo de 

entrenamiento  y  el  costo  computacional  de  las  redes  neuronales  es  considerablemente  mayor  en  comparación  con  los 

modelos de ML, lo que podría ser una limitación en contextos donde la eﬁciencia computacional es un factor determinante. 

En términos generales, los resultados sugieren que el modelo de Deep Learning con preprocesamiento es el enfoque 

más eﬁcaz para la detección del cáncer de hígado, ya que ofrece la máxima sensibilidad sin comprometer la precisión. No 

obstante, los modelos de Machine Learning como XGBoost siguen siendo una alternaOva sólida, especialmente cuando se 

busca una solución más interpretable y eﬁciente en términos de computación. La elección entre ambos enfoques dependerá 

en gran medida del contexto de aplicación. 

6.2. 

Interpretabilidad vs. Precisión: ¿Qué modelo es más úOl en la clínica? 

La  implementación  de  modelos  de  inteligencia  ar>ﬁcial  en  el  ámbito  médico  no  solo  depende  de  su  capacidad 

predic>va, sino también de su interpretabilidad y aplicabilidad en la prác>ca clínica. En este estudio, se han comparado dos 

enfoques  dis>ntos  y  cada  uno  presenta  ventajas  y  desventajas  que  pueden  inﬂuir  en  su  adopción  dentro  del  sector  de  la 

salud. 

Uno de los principales criterios de evaluación en modelos de diagnós>co médico es la sensibilidad, ya que la prioridad 

es  detectar  la  mayor  can>dad  posible  de  casos  posi>vos  de  cáncer,  minimizando  el  riesgo  de  falsos  nega>vos.  En  este 

aspecto,  los  modelos  de  Deep  Learning  entrenados  con  datos  preprocesados  lograron  un  recall  del  100%,  asegurando  la 

20

Juan Armario Muñoz

detección de todos los casos de cáncer en el dataset de prueba. Este resultado es crucial en aplicaciones clínicas, donde la 

omisión de un diagnós>co podría signiﬁcar la pérdida de una oportunidad de tratamiento. 

Sin  embargo,  aunque  la  precisión  de  un  modelo  es  fundamental,  en  entornos  clínicos  también  es  crí>co  que  los 

médicos  puedan  interpretar  y  conﬁar  en  las  predicciones  del  sistema.  Aquí  es  donde  los  modelos  de  Machine  Learning 

>enen una ventaja signiﬁca>va sobre las redes neuronales profundas. 

Modelos  como  Random  Forest  y  XGBoost  permiten  evaluar  la  importancia  de  cada  variable  en  la  predicción,  lo  que 

facilita la iden>ﬁcación de los factores de riesgo más relevantes en el desarrollo del cáncer de hígado. Por ejemplo, se puede 

determinar si variables como el consumo de alcohol, la obesidad o antecedentes familiares >enen un peso signiﬁca>vo en la 

predicción  del  cáncer.  Esta  capacidad  de  interpretación  es  clave  en  medicina,  ya  que  los  médicos  pueden  respaldar  sus 

decisiones en un análisis lógico basado en las variables más relevantes. 

En contraste, las redes neuronales ar>ﬁciales son modelos de caja negra, lo que signiﬁca que su proceso de toma de 

decisiones  es  difcil  de  interpretar.  Aunque  técnicas  como  SHAP  (Shapley  Addi>ve  Explana>ons)  pueden  proporcionar 

información sobre la contribución de cada variable a la predicción, la interpretación de los modelos de Deep Learning sigue 

siendo un desafo. Esto puede generar resistencia entre los profesionales de la salud, quienes pueden dudar en conﬁar en un 

sistema que no pueden entender completamente. 

¿Qué modelo es más úOl en la clínica? 

La elección entre Machine Learning y Deep Learning en un contexto clínico dependerá de las prioridades y necesidades 

especíﬁcas  del  entorno  médico;  si  la  prioridad  es  la  máxima  sensibilidad  en  la  detección  del  cáncer,  el  modelo  de  Deep 

Learning es la mejor opción. Su capacidad para detectar todos los casos posi>vos de cáncer es un argumento clave en su 

favor, especialmente en situaciones donde la detección temprana es fundamental para mejorar las tasas de supervivencia. 

Sin embargo, su aplicabilidad en la clínica dependerá de la capacidad del sistema para ser validado en diferentes poblaciones 

y de la conﬁanza que los médicos depositen en sus predicciones. 

Si, por el contrario, se busca un modelo que combine precisión con interpretabilidad, los modelos de Machine Learning 

como XGBoost y Random Forest son más adecuados. Aunque su sensibilidad es ligeramente inferior a la de la red neuronal, 

su capacidad para explicar las predicciones y destacar los factores de riesgo los hace más conﬁables desde la perspec>va de 

los  médicos.  Además,  su  menor  demanda  computacional  y  mayor  facilidad  de  implementación  los  convierte  en  una 

alterna>va viable para hospitales con menos recursos tecnológicos. 

En conclusión, ambos enfoques >enen su lugar en la medicina, y la mejor elección dependerá del contexto de uso. En 

una fase inicial, los modelos de Machine Learning pueden ser más prác>cos por su facilidad de interpretación y validación, 

permi>endo que los médicos los u>licen como herramientas de apoyo en la toma de decisiones. Sin embargo, a medida que 

las técnicas de interpretabilidad en Deep Learning avancen, es probable que las redes neuronales se conviertan en la mejor 

opción a largo plazo, gracias a su capacidad superior para detectar patrones complejos en los datos clínicos. 

21

Juan Armario Muñoz

7. Discusión y Aplicabilidad del Modelo en Medicina 

El uso de modelos de inteligencia ar>ﬁcial en la detección del cáncer de hígado representa una innovación que podría 

mejorar  signiﬁca>vamente  los  métodos  tradicionales  de  diagnós>co.  Sin  embargo,  la  integración  de  estos  modelos  en  la 

prác>ca  clínica  plantea  desafos  técnicos,  é>cos  y  opera>vos  que  deben  abordarse  para  garan>zar  su  efec>vidad  y 

aceptación dentro del sistema de salud. 

7.1.  ¿Cómo ayudaría este modelo a los médicos en la prácOca? 

La  implementación  de  modelos  de  Machine  Learning  y  Deep  Learning  en  la  prác>ca  clínica  podría  revolucionar  la 

detección temprana del cáncer de hígado. En par>cular, los modelos analizados en este estudio pueden asis>r a los médicos 

en varias áreas clave: 

  Detección temprana y apoyo en el diagnósOco: Los modelos pueden analizar grandes volúmenes de datos clínicos y 

encontrar  patrones  que  pueden  pasar  desapercibidos  para  los  médicos.  La  capacidad  de  iden>ﬁcar  factores  de  riesgo  y 

predecir  la  probabilidad  de  desarrollar  cáncer  de  hígado  podría  permi>r  intervenciones  preven>vas  en  pacientes  de  alto 

riesgo.  Su  uso  en  hospitales  y  centros  de  atención  primaria  permi>ría  realizar  una  primera  evaluación  automa>zada, 

iden>ﬁcando pacientes que requieren estudios más avanzados. 

  Reducción  de  la  carga  de  trabajo  médico:  Un  sistema  de  IA  puede  preclasiﬁcar  a  los  pacientes  según  su  nivel  de 

riesgo, permi>endo que los especialistas enfoquen su >empo en los casos más crí>cos. Al automa>zar el análisis de datos, 

los  médicos  pueden  reducir  el  >empo  necesario  para  revisar  historiales  médicos  y  tomar  decisiones  más  informadas  en 

menos >empo. 

  Mejora en la precisión diagnósOca: La inteligencia ar>ﬁcial ha demostrado reducir la tasa de falsos nega>vos, lo que 

podría  evitar  diagnós>cos  tardíos  y  mejorar  la  tasa  de  supervivencia.  En  comparación  con  métodos  convencionales  como 

biopsias hepá>cas o estudios de imagen, los modelos pueden ofrecer una evaluación rápida y no invasiva, lo que disminuye 

la necesidad de procedimientos costosos. 

  Personalización  de  tratamientos:  Los  modelos  pueden  proporcionar  una  evaluación  individualizada  del  riesgo, 

permi>endo tratamientos personalizados según las caracterís>cas del paciente. Al integrar datos clínicos con IA, los médicos 

pueden evaluar cómo diferentes factores (edad, hábitos de vida, antecedentes familiares) impactan el desarrollo del cáncer 

de  hígado  y  ajustar  las  estrategias  de  prevención  y  tratamiento.  A  pesar  de  estas  ventajas,  la  adopción  de  modelos 

predic>vos en la prác>ca médica depende de múl>ples factores, incluyendo conﬁanza médica, interpretabilidad y regulación 

legal, los cuales se exploran a con>nuación. 

7.2.  Desapos en la implementación real (éOca, sesgo, conﬁanza médica) 

A pesar de sus beneﬁcios, la integración de modelos de IA en la detección del cáncer de hígado presenta importantes 

desafos que deben abordarse antes de su aplicación a gran escala en hospitales y clínicas. 

Conﬁanza médica y resistencia al cambio:  Uno de los principales desafos en la implementación de IA en medicina es 

la conﬁanza de los médicos en las predicciones del modelo. Dado que los modelos de Deep Learning funcionan como cajas 

negras, es difcil para los médicos comprender cómo se llega a una decisión especíﬁca, lo que puede generar desconﬁanza y 

resistencia a su uso. 

La falta de interpretabilidad puede hacer que los médicos duden en basar sus decisiones en las recomendaciones de un 

modelo de IA, especialmente en casos crí>cos donde la vida del paciente está en riesgo. La solución a este problema radica 

en el desarrollo de técnicas de explicabilidad, como SHAP, que permitan interpretar las predicciones del modelo de manera 

más clara y comprensible. 

Sesgo en los datos y equidad en la predicción: La IA aprende de los datos en los que ha sido entrenada, lo que signiﬁca 

que  si  el  dataset  de  entrenamiento  es  sesgado,  las  predicciones  del  modelo  también  lo  serán.  En  el  caso  del  cáncer  de 

22

Juan Armario Muñoz

hígado, el sesgo puede surgir si la base de datos u>lizada con>ene una representación desigual de diferentes grupos étnicos, 

rangos de edad o condiciones médicas. Si el modelo no es entrenado con datos representa>vos de toda la población, podría 

presentar un peor desempeño en ciertos grupos demográﬁcos, lo que afectaría su conﬁabilidad en la prác>ca clínica. Para 

mi>gar este problema, es fundamental entrenar los modelos con datasets diversos y representa>vos, asegurando que la IA 

funcione equita>vamente para todos los pacientes. 

Regulaciones  legales  y  seguridad  de  los  datos:  La  implementación  de  IA  en  el  ámbito  médico  está  sujeta  a 

regulaciones  estrictas  de  privacidad  y  seguridad  de  los  datos.  Los  modelos  deben  cumplir  con  norma>vas  como  HIPAA 

(Health Insurance Portability and Accountability Act) en EE.UU. o el GDPR (Reglamento General de Protección de Datos) en 

Europa,  que  regulan  el  uso  de  datos  sensibles  de  los  pacientes.  Se  deben  garan>zar  medidas  de  anonimización  y 

encriptación  de  datos  para  proteger  la  privacidad  de  los  pacientes  y  evitar  el  uso  indebido  de  la  información  médica. 

Además,  el  modelo  debe  ser  validado  clínicamente  antes  de  su  implementación,  lo  que  implica  realizar  pruebas  en 

diferentes poblaciones y en múl>ples centros médicos para asegurar su robustez. 

7.3.  Posibles mejoras futuras: integración con imágenes médicas, modelos más avanzados 

A  medida  que  la  inteligencia  ar>ﬁcial  avanza,  existen  múl>ples  oportunidades  para  mejorar  los  modelos  actuales  y 

ampliar su aplicabilidad en la detección del cáncer de hígado. Algunas de las mejoras más prometedoras incluyen: 

Integración con imágenes médicas (Radiología + IA): Actualmente, el diagnós>co del cáncer de hígado se basa en una 

combinación  de  biomarcadores  clínicos,  estudios  de  laboratorio  e  imágenes  médicas  (resonancia  magné>ca,  tomografas 

computarizadas y ecografas). Un paso lógico en la evolución de los modelos predic>vos es la integración de IA con imágenes 

médicas,  u>lizando  Redes  Neuronales  Convolucionales  (CNNs)  para  analizar  imágenes  de  hígado  y  detectar  lesiones 

sospechosas de manera automa>zada. Estudios recientes han demostrado que las CNN pueden igualar o incluso superar la 

precisión de los radiólogos en la detección de cáncer en imágenes médicas, lo que podría complementar el modelo actual 

basado en datos clínicos. 

Modelos más avanzados: Deep Learning con Transformers: La implementación de Transformers en medicina, como los 

modelos  basados  en  A}en>on  Mechanisms,  ha  demostrado  ser  altamente  efec>va  en  la  interpretación  de  datos  clínicos 

complejos.  Estos  modelos  podrían  ser  aplicados  en  la  detección  del  cáncer  de  hígado  para  iden>ﬁcar  correlaciones  más 

profundas  entre 

las  variables  clínicas,  proporcionando  una  mayor  capacidad  predic>va  sin  necesidad  de  un 

preprocesamiento  extenso  de  los  datos.  A  diferencia  de  los  modelos  convencionales,  los  Transformers  pueden  analizar 

grandes  can>dades  de  información  con  múl>ples  dependencias  temporales,  lo  que  sería  par>cularmente  ú>l  en  estudios 

longitudinales del cáncer de hígado. 

Uso de modelos híbridos: Machine Learning + Deep Learning: Una alterna>va interesante sería la creación de modelos 

híbridos, donde Machine Learning sea u>lizado para la interpretación de datos clínicos y Deep Learning para la detección de 

patrones  en  imágenes  médicas.  Esta  combinación  permi>ría  obtener  lo  mejor  de  ambos  enfoques,  maximizando  la 

interpretabilidad  y  la  precisión  diagnós>ca  al  mismo  >empo.  Modelos  híbridos  han  demostrado  ser  efec>vos  en  otros 

campos  de  la  medicina,  como  la  detección  de  cáncer  de  mama  y  enfermedades  pulmonares,  lo  que  sugiere  que  podrían 

aplicarse también en la detección del cáncer de hígado. 

23

Juan Armario Muñoz

8. Conclusiones y futuro trabajo 

La  detección  temprana  del  cáncer  de  hígado  es  un  desafo  crí>co  en  oncología,  ya  que  la  mayoría  de  los  casos  se 

diagnos>can  en  etapas  avanzadas,  reduciendo  drás>camente  las  opciones  de  tratamiento  y  la  tasa  de  supervivencia.  Este 

estudio  ha  demostrado  cómo  la  inteligencia  ar>ﬁcial,  a  través  de  enfoques  de  Machine  Learning  y  Deep  Learning,  puede 

mejorar  signiﬁca>vamente  la  capacidad  de  predicción  de  la  enfermedad,  proporcionando  herramientas  de  apoyo  a  los 

médicos para op>mizar el diagnós>co. 

8.1.  Resumen de los hallazgos más importantes 

Este estudio comparó dos enfoques de IA para la detección del cáncer de hígado: Machine Learning y Deep Learning, 

aplicados  sobre  el  PLCO  dataset.  Los  resultados  obtenidos  muestran  diferencias  clave  en  la  precisión,  sensibilidad  y 

aplicabilidad clínica de ambos métodos. 

Machine  Learning:  Se  probaron  diversos  algoritmos,  incluyendo  Random  Forest  y  XGBoost,  que  demostraron  un 

desempeño sólido, con altos valores de recall y precisión en la detección de pacientes con cáncer de hígado. Los modelos 

fueron  op>mizados  mediante  técnicas  de  balanceo  de  datos  (SMOTE),  selección  de  caracterís>cas  e  hiperparámetros, 

logrando  mejorar  la  detección  de  casos  posi>vos  sin  aumentar  el  sobreajuste.  Aunque  XGBoost  fue  el  modelo  con  mejor 

rendimiento,  sigue  presentando  ciertas  limitaciones  en  cuanto  a  la  complejidad  de  relaciones  no  lineales  en  los  datos 

clínicos. 

Deep Learning: Se desarrollaron redes neuronales ar>ﬁciales, con y sin preprocesamiento de datos, demostrando que 

el  modelo  con  datos  preprocesados  alcanzó  un  recall  perfecto  del  100%,  asegurando  la  detección  de  todos  los  casos 

posi>vos.  Se  aplicaron  técnicas  avanzadas  como  Batch  Normaliza>on,  Dropout  y  op>mización  con  Keras  Tuner,  lo  que 

permi>ó  mejorar  la  estabilidad  del  modelo  y  evitar  el  sobreajuste.  En  comparación  con  Machine  Learning,  las  redes 

neuronales lograron un mayor rendimiento en recall y f1-score, aunque con la desventaja de menor interpretabilidad. 

Comparación  entre  ambos  enfoques:  Machine  Learning  es  más  interpretable  y  fácil  de  implementar  en  entornos 

clínicos,  ya  que  permite  visualizar  la  importancia  de  cada  variable  y  comprender  cómo  el  modelo  llega  a  una  predicción. 

Deep Learning ofrece mayor precisión y recall, asegurando que ningún caso posi>vo pase desapercibido, lo que lo hace más 

adecuado para aplicaciones médicas donde la detección temprana es crí>ca. Sin embargo, las redes neuronales requieren 

mayor  capacidad  computacional  y  mayor  >empo  de  entrenamiento,  lo  que  puede  ser  una  limitación  en  hospitales  con 

recursos limitados. 

En general, este estudio demuestra que ambos enfoques son viables para la detección del cáncer de hígado, pero su 

implementación dependerá del contexto en el que se apliquen y de los recursos disponibles. 

8.2.  Sugerencias para futuros estudios 

A pesar de los logros alcanzados en este estudio, existen varias áreas de mejora y expansión que podrían explorarse en 

futuras inves>gaciones para fortalecer la aplicabilidad de los modelos de IA en la medicina. 

Expansión  del  dataset  y  validación  en  otras  poblaciones:  Una  de  las  principales  limitaciones  del  estudio  es  que  el 

modelo  fue  entrenado  y  probado  en  el  PLCO  dataset,  lo  que  puede  restringir  su  aplicabilidad  a  poblaciones  con 

caracterís>cas dis>ntas. Sería ideal validar el modelo en datasets de diferentes regiones geográﬁcas y grupos étnicos, para 

garan>zar  que  funcione  de  manera  robusta  en  diversas  poblaciones.  Además,  se  podría  incluir  información  de  historial 

clínico de largo plazo, para mejorar la precisión de las predicciones y hacerlas más personalizadas. 

Integración  con  datos  de  imágenes  médicas  (ecograpas,  resonancias  magnéOcas):  Actualmente,  la  mayoría  de  los 

diagnós>cos  de  cáncer  de  hígado  se  basan  en  estudios  de  imagen,  como  resonancia  magné>ca  (RM)  y  tomografa 

computarizada  (TC).  Una  línea  de  inves>gación  futura  sería  combinar  los  modelos  actuales  con  análisis  de  imágenes 

médicas,  u>lizando  Redes  Neuronales  Convolucionales  (CNNs)  para  detectar  anomalías  hepá>cas  de  manera 

24

Juan Armario Muñoz

automa>zada.mEsta  integración  podría  mejorar  la  precisión  del  diagnós>co,  ya  que  combinaría  datos  clínicos  y 

biomarcadores con evidencia visual del estado del hígado. 

Desarrollo  de  modelos  híbridos:  Un  área  prometedora  sería  el  desarrollo  de  modelos  híbridos  que  combinen  la 

interpretabilidad de Machine Learning con la precisión de Deep Learning. Se podrían u>lizar algoritmos como XGBoost para 

predecir  factores  de  riesgo  y  una  red  neuronal  para  detectar  patrones  más  complejos  en  los  datos  clínicos.  Este  enfoque 

permi>ría  aprovechar  las  fortalezas  de  ambos  métodos,  mejorando  la  conﬁabilidad  y  la  aceptabilidad  del  modelo  en  la 

prác>ca médica. 

Implementación  en  sistemas  de  salud  reales:  Para  que  estos  modelos  sean  adoptados  en  hospitales  y  clínicas,  es 

necesario desarrollar una interfaz de usuario intui>va y accesible para los médicos. Se podrían diseñar plataformas web o 

aplicaciones móviles donde los médicos ingresen los datos de un paciente y el modelo genere una predicción de riesgo en 

>empo real. Esto permi>ría que la IA sea u>lizada como una herramienta de apoyo en la toma de decisiones, sin reemplazar 

la evaluación médica. 

En  resumen,  el  futuro  de  la  detección  del  cáncer  de  hígado  con  IA  dependerá  de  la  integración  con  tecnologías 

avanzadas y de su validación en entornos clínicos reales. 

9. Anexos 

9.1.  Código 

9.2.  Referencias 

9.3.  Glosario de términos

25

