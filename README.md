# Stationary-Vortices
Análisis del campo de velocidades en  vórtices estacionarios para distintas  soluciones de agua y glicerina.

# Resumen
  En este trabajo se estudió el campo de velocidades de un vórtice estacionario, y su decaimiento con el radio, mediante en procesamiento de imágenes con PIV lab. Se realizó este procedimiento para una solución de 1000 ml de agua y con 200 ml, 300 ml y 400 ml de glicerina. Se ajustaron los datos obtenidos con los modelos de Rankine y Burguers, con el objeto de compararlos.

# Fluidos y Vórtices 
  La mecánica de fluidos es de notable importancia en diversas áreas de la física así como también en las ciencias de la atmósfera, la oceanografía y la aeronáutica. En particular el estúdio de la dinámica de vórtices es fundamental en fluidos incompresibles pues se puede considerar una primera aproximación a la turbulencia además, proporciona un ejemplo físico de un sistema fuertemente no lineal el cual tiene conexión con fenómenos caóticos.

 La vorticidad es una magnitud que cuantifica la rotación local de una partícula de fluido alrededor de un cierto eje. Definida matemáticamente como el rotor del campo de velocidades $\vec{v}$ , es decir:
 $\vec{\Omega} = \vec{\nabla} \times \vec{v}$. 
 
 En este trabajo son de interés dos modelos para describir el campo de velocidades: el modelo de Rankine y el modelo de Burgers. 

 ## Modelo de Rankie 
  Consiste en un flujo central (de viscosidad nula) que rota como un sólido rígido conteniendo una vorticidad constante dentro de un radio c y un flujo potencial exterior sin vorticidad. El campo de velocidades crece linealmente hasta un valor máximo y a continuación decrece como 1/r. En este caso la velocidad depende únicamente del radio medido respecto al eje de rotación rígida y tiene componente solo en la dirección azimutal. Laexpresión de la velocidad es:

  $$ \vec{v}=\left\lbrace\begin{array}{l} \Omega r ~~~~~~~si~~~~~r\lt c\\\\ \frac{\Omega c^{2}}{r} ~~~~~si~~~~~r\gt c \end{array}\right. $$
  
donde Ω es una constante que contiene información sobre la circulación del fluido.

 ## Modelo de Burgers
  El modelo de Burgers propone un fluido con viscosidad no nula (ν>0), lo que modifica el campo de velocidades ya que ahora la vorticidad no está distribuida de forma homogénea en el recinto, en este caso el campo de velocidades presenta componentes en las direcciones r y z de la siguiente manera:
  
$$\vec{v_{r}}=-\frac{2 \nu }{c^{2}}r$$

$$\vec{v_{\theta}}=\frac{\Omega c^{2}}{r}(1-e^{-\frac{r^{2}}{c^{2}}})$$
  
| Esquema de Rankie | Modelo de Rankie y Burgers   |
| ----------------------------------- | ----------------------------------- |
| <img src="https://github.com/hnatiuksanti/Stationary-Vortices/blob/main/im%C3%A1genes/rankie.jpg" width="600" /> | <img src="https://github.com/hnatiuksanti/Stationary-Vortices/blob/main/im%C3%A1genes/modelos.png" width="600" />  |

