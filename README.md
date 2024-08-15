# Stationary-Vortices
Análisis del campo de velocidades en  vórtices estacionarios para distintas  soluciones de agua y glicerina.

# Resumen
  $~~~~$  En este trabajo se estudió el campo de velocidades de un vórtice estacionario, y su decaimiento con el radio, mediante en procesamiento de imágenes con PIV lab. Se realizó este procedimiento para una solución de 1000 ml de agua y con 200 ml, 300 ml y 400 ml de glicerina. Se ajustaron los datos obtenidos con los modelos de Rankine y Burguers, con el objeto de compararlos.

# Fluidos y Vórtices 
  $~~~~$ La mecánica de fluidos es de notable importancia en diversas áreas de la física así como también en las ciencias de la atmósfera, la oceanografía y la aeronáutica. En particular el estúdio de la dinámica de vórtices es fundamental en fluidos incompresibles pues se puede considerar una primera aproximación a la turbulencia además, proporciona un ejemplo físico de un sistema fuertemente no lineal el cual tiene conexión con fenómenos caóticos.

$~~~~$ La vorticidad es una magnitud que cuantifica la rotación local de una partícula de fluido alrededor de un cierto eje. Definida matemáticamente como el rotor del campo de velocidades $\vec{v}$ , es decir:
 $\vec{\Omega} = \vec{\nabla} \times \vec{v}$. 
 
 En este trabajo son de interés dos modelos para describir el campo de velocidades: el modelo de Rankine y el modelo de Burgers. 

 ## Modelo de Rankie 
 $~~~~$ Consiste en un flujo central (de viscosidad nula) que rota como un sólido rígido conteniendo una vorticidad constante dentro de un radio c y un flujo potencial exterior sin vorticidad. El campo de velocidades crece linealmente hasta un valor máximo y a continuación decrece como 1/r. En este caso la velocidad depende únicamente del radio medido respecto al eje de rotación rígida y tiene componente solo en la dirección azimutal. Laexpresión de la velocidad es:

  $$ \vec{v}=\left\lbrace\begin{array}{l} \Omega r ~~~~~~~si~~~~~r\lt c\\\\ \frac{\Omega c^{2}}{r} ~~~~~si~~~~~r\gt c \end{array}\right. $$
  
donde Ω es una constante que contiene información sobre la circulación del fluido.

 ## Modelo de Burgers
 $~~~~$ El modelo de Burgers propone un fluido con viscosidad no nula (ν>0), lo que modifica el campo de velocidades ya que ahora la vorticidad no está distribuida de forma homogénea en el recinto, en este caso el campo de velocidades presenta componentes en las direcciones r y z de la siguiente manera:
  
$$\vec{v_{r}}=-\frac{2 \nu }{c^{2}}r$$

$$\vec{v_{\theta}}=\frac{\Omega c^{2}}{r}(1-e^{-\frac{r^{2}}{c^{2}}})$$

$$\vec{v_{z}}=\frac{4 \nu }{c^{2}}z$$
  
| Esquema de Rankie | Modelo de Rankie y Burgers   |
| ----------------------------------- | ----------------------------------- |
| <img src="https://github.com/hnatiuksanti/Stationary-Vortices/blob/main/im%C3%A1genes/rankie.jpg" width="600" /> | <img src="https://github.com/hnatiuksanti/Stationary-Vortices/blob/main/im%C3%A1genes/modelos.png" width="600" />  |

# Montaje experimental
$~~~~$ El montaje experimental empleado es sencillo y de facil reproducción. Se utilizó un recipiente cilíndrico en el cual se colocó un agitador magnético Decalab-FBR el cual contaba con 5 niveles de frecuencias distintas. Se filmó con un celular y se exportó cada video para realizar el análisis mediante PIVlab. Para poder caracterizar el campo de velocidades del fluido se utilizó gliter azul como partículas trazadoras y se agregó colorante vegetal negro FLEIBOR para generar mayor contraste. 
<p align="center">
  <img src="https://github.com/hnatiuksanti/Stationary-Vortices/blob/main/im%C3%A1genes/montaje%20exp.png" width="550" />
</p>

# PIVlab Image Analysis
$~~~~$ Un Análisis PIV consiste principalmente en tres pasos: Pre-procesamiento de imágenes, análisis de imágenes y post-procesamiento. El preprocesamiento consiste en determinar un área de interés para las imágenes sobre la cual se realizará el análisis esto para descartar zonas donde no hay fluido o simplemente eliminar brillos indeseados. En el post-procesamiento en cambio, se filtran los resultados insatisfactorios y se puede realizar un tratamiento estadístico de los datos para obtener valores medios. La parte más importante del análisis PIV es el análisis de imágenes, para realizarlo se utiliza un algoritmo de correlación cruzada. Para ello se crea un cuadro pequeño que encierre a una partícula dentro de un área determinada y se la compara con la siguiente imagen para determinar cuan correlacionadas están las imágenes.  Del análisis del video realizado con PIVlab se obtuvieron las posiciones y velocidades de las partículas trazadoras en coordenadas cartesianas. 
<p align="center">
  <img src="https://github.com/hnatiuksanti/Stationary-Vortices/blob/main/im%C3%A1genes/Campo_velocidades_sin_glic.png" width="550" />
</p>

$~~~~$ Una vez se obtuvo el centro, se lo resto alas coordenadas x e y para hacer una transformación a coordenadas polares, y de esta manera obtener la velocidad tangencial en función del radio. Finalmente se realizó un promedio de los datos debido a la dispersión significativa que presentaron. 

| Resultados sin promediar | Resultados para todas las concentraciones|
| ----------------------------------- | ----------------------------------- |
| <img src="https://github.com/hnatiuksanti/Stationary-Vortices/blob/main/im%C3%A1genes/agua%20vels.png" width="600" /> | <img src="https://github.com/hnatiuksanti/Stationary-Vortices/blob/main/im%C3%A1genes/glicerina%20vels.png" width="600" />  |

$~~~~$ Una vez obtenidos los datos promediados, se procedió a realizar los ajustes empleando el modelo de Burgers y de Rankine. A continuacion, en la figura, se observa el ajuste realizado para los datos correspondiente a la solución de agua con 400 ml de glicerina, donde en linea punteada amarilla se presenta el ajuste realizado por el modelo de Rankine y en linea punteada azul el ajuste realizado por el modelo de Burgers. Como era de esperar el modelo de Rankine no ajusta correctamente los datos obtenidos y en contraparte el modelo Burguers ajusta satisfactoriamente los datos obtenidos, ya que éste toma en cuenta la viscosidad del fluido. El error asociado a cada punto corresponde a la desviación estándar de haber promediado los datos originales.
 
<p align="center">
  <img src="https://github.com/hnatiuksanti/Stationary-Vortices/blob/main/im%C3%A1genes/ajustes.png" width="550" />
</p>

