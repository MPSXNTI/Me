# Documentación Unificada: Guiones, Entornos Python VSCode y Documentacion Proyectos EXP Python
Este documento reúne el contenido técnico y pedagógico relacionado con los guiones de proyecto, los entornos Python en VSCode y la documentacion de proyectos de calculo EXP en Python.
Cada bloque principal representa un conjunto de archivos originales, conservando su estructura interna y contenido literal.

---

### Nota sobre la estructura y criterio de orden
Esta documentación unificada está organizada bajo un **criterio profesional**, en el que los archivos se presentan **de mayor a menor completitud**.  
Primero se muestran las versiones finales, optimizadas o unificadas, seguidas por sus variantes previas o parciales.  
El propósito de esta estructura es **mantener una vista limpia y jerárquica**: permite acceder de inmediato al material definitivo mientras conserva las versiones anteriores como respaldo o referencia histórica.  

Si en el futuro se agregan nuevos archivos a este documento, deben ubicarse siguiendo este mismo principio:
1. Los **archivos más completos o consolidados** al inicio de cada bloque.  
2. Las **versiones intermedias o de desarrollo** en el centro.  
3. Las **versiones base, borradores o iniciales** al final.  

De esta manera, el documento conservará una lógica descendente de madurez del contenido,  
lo que facilita tanto la lectura rápida como el mantenimiento del historial de versiones.

---
## Nombre Archivo: guiones_unificados_completos.md
### Descripción general
Contiene todos los guiones pedagógicos, ejemplos y guías de uso que estructuran las instrucciones del proyecto.  
Incluye versiones combinadas, ampliadas y la guía maestra final, ordenadas de la más completa a la más básica.

| Archivo | Descripción breve |
|----------|-------------------|
| guion_maestro.md | Síntesis técnica y pedagógica final. |
| guiones_version2_paso_a_paso_con_intro.md | Versión guiada paso a paso con introducción. |
| guiones_version1_expandida_con_intro.md | Versión ampliada con introducción. |
| guiones_version_combinada.md | Fusión de estilo técnico y pedagógico. |
| Documantacion_Completa_Guiones.md | Estructura del conjunto de guiones. |
| readme_guiones.md | Guía de uso de versiones de guiones. |
| guiones_con_ejemplos_intercalados.md | Ejemplos integrados en el texto. |
| guiones_con_ejemplos_al_final.md | Ejemplos al final del documento. |
| documentation_template.md |
| instruccion_generar_readme.md |
| plantilla_generar_md.md |
| plantilla_documentacion.md |
| README_guion_explicaciones.md |
| plantilla_doc_exp.md |
| template_doc_exp_en |

---
<details>

<summary>🔹 Archivo: guion_maestro.md</summary>

# 🧩 Guion Maestro — Guía Técnica y Pedagógica Unificada

## 📘 Introducción
Guía integral que combina estructura técnica, ejemplos inmediatos y pasos prácticos.
Sirve tanto para documentar, enseñar o automatizar revisiones de código.

---

## 📖 Guion para explicaciones de código

| Punto | Qué incluye |
|-------|--------------|
| **1. Propósito** | Qué hace y por qué existe. |
| **2. Uso básico** | Ejemplo directo de uso. |
| **3. Notas técnicas** | Dependencias, riesgos, buenas prácticas. |
| **4. Ejemplo extra** | Caso distinto al original. |
| **5. Relación con otras partes** | Cómo encaja en el flujo general. |

**Ejemplo:**
```python
def saludar(nombre):
    return f"Hola, {nombre}!"
```
➡️ Propósito: saluda al usuario.  
➡️ Uso básico: `saludar("Ana")` → "Hola, Ana!"

---

## ⚡ Tabla de instrucciones express

| Caso | Instrucción rápida |
|------|--------------------|
| Revisión de código | “Analiza estilo, legibilidad, errores y redundancias; propón versión mejorada.” |
| Comparación de códigos | “Compara línea por línea, indica diferencias y unifica lo mejor.” |
| Refactorización | “Reestructura funciones aplicando buenas prácticas.” |
| Documentación automática | “Genera README con propósito, instalación, uso y dependencias.” |
| Seguridad y validaciones | “Busca vulnerabilidades y propón correcciones seguras.” |

---

## 🧭 Instrucciones detalladas (Formato unificado)

### 1. Revisión de código
**Objetivo:** Evaluar y optimizar la calidad del código.  
**Pasos:**
1. Leer propósito general.  
2. Analizar estilo, estructura y eficiencia.  
3. Clasificar en buenas y malas prácticas.  
4. Proponer versión optimizada con comentarios claros.  
**Resultado esperado:** Código limpio, legible y mejorado.

**Ejemplo:**
```python
def sumar(a,b):return a+b
```
➡️ Mejora:
```python
def sumar(a: int, b: int) -> int:
    """Suma dos números enteros."""
    return a + b
```

---

### 2. Comparación de dos códigos
**Objetivo:** Determinar cuál versión es más clara y eficiente.  
**Pasos:**
1. Comparar línea por línea.  
2. Evaluar claridad, estructura y rendimiento.  
3. Fusionar lo mejor de ambas versiones.  
**Resultado esperado:** Tabla comparativa + código unificado.

---

### 3. Refactorización
**Objetivo:** Reestructurar el código manteniendo la funcionalidad.  
**Pasos:**
1. Detectar redundancias.  
2. Dividir en funciones reutilizables.  
3. Mejorar nombres, añadir comentarios breves.  
**Resultado esperado:** Código modular y mantenible.  

**Ejemplo:**
Antes:
```python
print('Hola');print('Adiós')
```
Después:
```python
def saludo():
    print('Hola')
    print('Adiós')
```

---

### 4. Limpieza de proyecto
**Objetivo:** Reorganizar y depurar archivos.  
**Pasos:**
1. Revisar carpetas.  
2. Eliminar duplicados.  
3. Crear estructura `/codigo`, `/docs`, `/data`.  
4. Agregar `README.md` con resumen.  
**Resultado esperado:** Proyecto limpio y documentado.

---

### 5. Explicación de flujo
**Objetivo:** Mostrar el recorrido lógico del programa.  
**Pasos:**  
1. Identificar entrada → procesamiento → salida.  
2. Representar flujo con texto o diagrama.  
**Ejemplo:**
```
[Inicio] → [Procesamiento] → [Salida]
```
**Resultado esperado:** Diagrama narrado o visual claro.

---

## 🧾 Tabla resumen final

| Categoría | Contenido | Tipo de salida |
|------------|------------|----------------|
| Revisión | Análisis + mejora | Código limpio |
| Comparación | Tabla + veredicto | Versión final |
| Refactorización | Funciones limpias | Código modular |
| Documentación | README.md | Texto formateado |
| Explicación de flujo | Diagrama narrado | Texto o ASCII |

---

## 🧠 Conclusión
Este **Guion Maestro** combina la precisión técnica de las versiones expandida y combinada, la claridad pedagógica de la versión paso a paso, y la practicidad de las versiones con ejemplos.  
Su formato sirve tanto para **enseñar, documentar o automatizar** tareas complejas de análisis y revisión de código.

</details>

---
<details>

<summary>🔹 Archivo: guiones_version2_paso_a_paso_con_intro.md</summary>

# 📗 Guiones e Instrucciones Ampliadas (Versión 2 — Guía narrativa paso a paso)

Cada instrucción está detallada como un procedimiento completo, con pasos, objetivos y estructura esperada de salida.

---

---

## 📖 Guion para pedir explicaciones de código

🧭 **Objetivo:**  
Proporcionar una guía estructurada para explicar cada parte del código (funciones, clases, módulos o celdas) de forma completa y coherente.

---

### 🧩 Estructura de explicación — “Guion de 5 puntos”

| 🪶 Punto | 💬 Qué debe incluir |
|----------|--------------------|
| **1. Propósito** | Explica qué hace el fragmento de código y por qué existe. |
| **2. Uso básico** | Muestra cómo se llama o un ejemplo directo de uso práctico. |
| **3. Notas técnicas** | Detalla dependencias, riesgos, particularidades o buenas prácticas. |
| **4. Ejemplo extra** | Incluye un caso adicional distinto al original para reforzar la comprensión. |
| **5. Relación con otras partes** | Describe cómo encaja dentro del flujo general o cómo se conecta con otras funciones. |

---

### 💬 Ejemplo de uso:
> “Hazme una explicación de cada celda o función siguiendo el guion de 5 puntos:  
> 1️⃣ Propósito, 2️⃣ Uso básico, 3️⃣ Notas técnicas, 4️⃣ Ejemplo extra, 5️⃣ Relación con otras partes.”

---



## 1. Revisión de `.zip`
**Objetivo:** Revisar el contenido de un archivo .zip y clasificar los documentos según su calidad.  
**Pasos:**  
1. Descomprimir el archivo.  
2. Clasificar los archivos en `/archivos_buenos` y `/archivos_malos`.  
3. Priorizar `.md` sobre `.ipynb` si ambos tienen información similar.  
4. Crear `README.md` con criterios de clasificación y resumen de contenido.  
**Resultado esperado:** Carpetas limpias y un `README.md` explicativo.

---

## 2. Revisión de código
**Objetivo:** Evaluar la calidad del código y proponer una versión mejorada.  
**Pasos:**  
1. Leer y comprender el propósito del código.  
2. Analizar estilo, claridad y eficiencia.  
3. Clasificar partes en buenas y malas prácticas.  
4. Proponer una versión optimizada con comentarios claros.  
5. Resumir fortalezas, debilidades y mejoras sugeridas.  
**Resultado esperado:** Informe con análisis, versión optimizada y recomendaciones.

---

## 3. Comparación de dos códigos
**Objetivo:** Determinar cuál versión es superior y unificar lo mejor de ambas.  
**Pasos:**  
1. Leer ambas versiones completas.  
2. Comparar línea por línea (idénticas, parecidas, distintas).  
3. Evaluar claridad, rendimiento y estructura.  
4. Elegir la versión más sólida.  
5. Fusionar los mejores elementos de ambas.  
6. Entregar resultado con: comparación detallada, veredicto y versión final.  
**Resultado esperado:** Tabla comparativa + código final optimizado.

---

## 4. Limpieza de proyecto
**Objetivo:** Organizar y depurar el proyecto completo.  
**Pasos:**  
1. Revisar todas las carpetas.  
2. Eliminar duplicados o temporales.  
3. Ordenar archivos en carpetas `/codigo`, `/docs`, `/data`.  
4. Crear `README.md` con resumen de cambios.  
**Resultado esperado:** Proyecto limpio y documentado.

---

## 5. Documentación automática
**Objetivo:** Generar documentación completa en formato `README.md`.  
**Pasos:**  
1. Identificar propósito del proyecto.  
2. Listar dependencias e instrucciones de instalación.  
3. Incluir ejemplos de uso y salida esperada.  
**Resultado esperado:** `README.md` estructurado con propósito, instalación y uso.

---

## 6. Refactorización
**Objetivo:** Mejorar la estructura interna del código sin cambiar su funcionalidad.  
**Pasos:**  
1. Detectar redundancias.  
2. Dividir en funciones o clases reutilizables.  
3. Mejorar nombres y eliminar código repetido.  
4. Comentar secciones clave.  
**Resultado esperado:** Código más limpio, modular y legible.

---

## 7. Revisión de estilo
**Objetivo:** Corregir problemas de formato y estilo.  
**Pasos:**  
1. Revisar indentación, comillas, y nombres de variables.  
2. Uniformar estilo de comentarios.  
3. Devolver código limpio con formato coherente.  
**Resultado esperado:** Código legible, consistente y sin errores de formato.

---

## 8. Análisis comparativo
**Objetivo:** Identificar qué versión es más completa y eficiente.  
**Pasos:**  
1. Analizar ambas versiones.  
2. Evaluar ventajas y desventajas.  
3. Combinar lo mejor en una sola versión final.  
**Resultado esperado:** Comparativo claro + versión consolidada.

---

## 9. Explicación de flujo
**Objetivo:** Explicar el recorrido lógico del programa.  
**Pasos:**  
1. Identificar puntos de entrada, procesamiento y salida.  
2. Narrar el flujo o representarlo como diagrama.  
**Resultado esperado:** Explicación secuencial clara del funcionamiento.

---

## 10. Generación de código
**Objetivo:** Crear un código funcional según los requisitos dados.  
**Pasos:**  
1. Comprender el propósito.  
2. Definir funciones y variables claras.  
3. Agregar comentarios esenciales.  
4. Cumplir buenas prácticas del lenguaje.  
**Resultado esperado:** Código funcional, limpio y documentado.

---

## 11. Optimización de rendimiento
**Objetivo:** Mejorar la eficiencia del código.  
**Pasos:**  
1. Analizar posibles cuellos de botella.  
2. Aplicar mejoras (uso de estructuras eficientes, comprensión de listas, etc.).  
3. Medir impacto y justificar cambios.  
**Resultado esperado:** Código más rápido y eficiente.

---

## 12. Conversión de lenguaje
**Objetivo:** Traducir código a otro lenguaje sin perder funcionalidad.  
**Pasos:**  
1. Analizar estructuras del código fuente.  
2. Adaptar sintaxis y tipos de datos al nuevo lenguaje.  
3. Probar equivalencia funcional.  
**Resultado esperado:** Código traducido y verificado.

---

## 13. Generación de pruebas automáticas
**Objetivo:** Crear tests que validen el correcto funcionamiento del código.  
**Pasos:**  
1. Identificar funciones clave.  
2. Definir entradas y salidas esperadas.  
3. Escribir casos de prueba unitarios.  
**Resultado esperado:** Conjunto de pruebas automatizadas funcionales.

---

## 14. Explicación pedagógica
**Objetivo:** Explicar el código de forma didáctica.  
**Pasos:**  
1. Traducir tecnicismos a lenguaje simple.  
2. Usar analogías o ejemplos.  
3. Asegurar comprensión para principiantes.  
**Resultado esperado:** Explicación clara y fácil de entender.

---

## 15. Checklist de buenas prácticas
**Objetivo:** Evaluar cumplimiento de normas de calidad en código.  
**Pasos:**  
1. Revisar modularidad, claridad, comentarios y seguridad.  
2. Marcar lo que cumple o no.  
3. Proponer mejoras.  
**Resultado esperado:** Checklist completa y recomendaciones.

---

## 16. Seguridad y validaciones
**Objetivo:** Detectar vulnerabilidades y fortalecer el código.  
**Pasos:**  
1. Revisar validaciones de entrada.  
2. Buscar posibles inyecciones o riesgos.  
3. Proponer soluciones seguras.  
**Resultado esperado:** Código más robusto y protegido.

---

## 17. Visualización de flujo
**Objetivo:** Representar gráficamente la lógica del programa.  
**Pasos:**  
1. Identificar decisiones y caminos alternativos.  
2. Representar con texto/ASCII el flujo.  
**Resultado esperado:** Diagrama claro de decisiones y resultados.

---

## 18. Explicación por capas
**Objetivo:** Entender el código desde distintos niveles de profundidad.  
**Pasos:**  
1. Nivel básico: propósito general.  
2. Nivel intermedio: cómo lo hace.  
3. Nivel avanzado: mejoras y patrones posibles.  
**Resultado esperado:** Explicación completa por niveles.

</details>

---
<details>

<summary>🔹 Archivo: guiones_version1_expandida_con_intro.md</summary>

# 📘 Guiones e Instrucciones Ampliadas (Versión 1 — Formato original expandido)

Cada instrucción fue reescrita para eliminar ambigüedades, definir resultados esperados y detallar el formato de salida.

---

---

## 📖 Guion para pedir explicaciones de código

🧭 **Objetivo:**  
Proporcionar una guía estructurada para explicar cada parte del código (funciones, clases, módulos o celdas) de forma completa y coherente.

---

### 🧩 Estructura de explicación — “Guion de 5 puntos”

| 🪶 Punto | 💬 Qué debe incluir |
|----------|--------------------|
| **1. Propósito** | Explica qué hace el fragmento de código y por qué existe. |
| **2. Uso básico** | Muestra cómo se llama o un ejemplo directo de uso práctico. |
| **3. Notas técnicas** | Detalla dependencias, riesgos, particularidades o buenas prácticas. |
| **4. Ejemplo extra** | Incluye un caso adicional distinto al original para reforzar la comprensión. |
| **5. Relación con otras partes** | Describe cómo encaja dentro del flujo general o cómo se conecta con otras funciones. |

---

### 💬 Ejemplo de uso:
> “Hazme una explicación de cada celda o función siguiendo el guion de 5 puntos:  
> 1️⃣ Propósito, 2️⃣ Uso básico, 3️⃣ Notas técnicas, 4️⃣ Ejemplo extra, 5️⃣ Relación con otras partes.”

---



## 1. Revisión de `.zip`
“Descomprime el archivo .zip proporcionado. Clasifica su contenido en dos carpetas: `/archivos_buenos` (documentos claros, completos o útiles) y `/archivos_malos` (duplicados, incompletos o erróneos). Prioriza siempre los archivos `.md` sobre `.ipynb` si ambos contienen información similar.  
Genera un `README.md` dentro de la carpeta raíz explicando los criterios usados, los archivos descartados y un breve resumen de cada documento importante.”

---

## 2. Revisión de código
“Analiza el código en profundidad: estilo, estructura, optimización y buenas prácticas. Identifica errores, redundancias o malas decisiones de diseño. Clasifica las secciones en ‘código bueno’ y ‘código malo’, justificando brevemente. Luego, propone una versión optimizada aplicando claridad, modularidad y comentarios concisos.  
Formato de entrega:  
1️⃣ Resumen general.  
2️⃣ Fortalezas y debilidades.  
3️⃣ Código mejorado.  
4️⃣ Lista de recomendaciones finales.”

---

## 3. Comparación de dos códigos
“Compara dos versiones línea por línea. Marca similitudes, diferencias y mejoras. Evalúa cuál es más clara, eficiente y completa. Explica el veredicto y propone una versión unificada que combine lo mejor de ambas.  
Estructura:  
- Comparación línea por línea.  
- Tabla de diferencias.  
- Veredicto técnico.  
- Código final unificado.”

---

## 4. Limpieza de proyecto
“Revisa todas las carpetas del proyecto. Elimina duplicados, archivos temporales y versiones antiguas. Reorganiza el contenido en una estructura limpia (`/codigo`, `/docs`, `/data`). Genera `README.md` explicando qué se eliminó y por qué.”

---

## 5. Documentación automática
“Genera un `README.md` completo con: propósito del proyecto, requisitos, instalación, uso básico, dependencias y ejemplos de ejecución. Asegúrate de usar un formato Markdown limpio y legible.”

---

## 6. Refactorización
“Reescribe el código aplicando buenas prácticas: nombres descriptivos, funciones reutilizables, comentarios breves, y eliminación de redundancias. Mantén la lógica original pero mejora su estructura y eficiencia.”

---

## 7. Revisión de estilo
“Corrige errores de formato: indentación, nombres de variables, consistencia de comillas y comentarios. Devuelve el código limpio, manteniendo la funcionalidad.”

---

## 8. Análisis comparativo
“Compara dos versiones de un archivo. Identifica cuál es más completa o eficiente. Resume las mejoras únicas de cada una y propone una versión unificada que conserve lo mejor de ambas.”

---

## 9. Explicación de flujo
“Explica el flujo lógico del programa paso a paso, en formato narrado o de diagrama: **Entrada → Procesamiento → Salida**. Menciona las funciones clave involucradas.”

---

## 10. Generación de código
“Crea un código en el lenguaje indicado para cumplir un propósito específico. Usa nombres descriptivos para funciones y variables, e incluye comentarios básicos. Aplica buenas prácticas de programación.”

---

## 11. Optimización de rendimiento
“Analiza el código buscando oportunidades de optimización (uso de memoria, velocidad de ejecución). Explica los cambios propuestos y su impacto.”

---

## 12. Conversión de lenguaje
“Convierte el código de un lenguaje a otro manteniendo su lógica, estructura y estilo. Asegúrate de que el resultado sea funcional y legible.”

---

## 13. Generación de pruebas automáticas
“Genera casos de prueba unitarios para el código usando el framework especificado. Incluye ejemplos de entrada y salida esperada. Estructura las pruebas para validar los casos normales y extremos.”

---

## 14. Explicación pedagógica
“Explica el código como si fuera para principiantes. Usa ejemplos, analogías y comparaciones fáciles de entender. Evita tecnicismos innecesarios.”

---

## 15. Checklist de buenas prácticas
“Crea una lista de verificación (checklist) que evalúe el cumplimiento de buenas prácticas: nombres, modularidad, comentarios, estilo y seguridad. Marca lo que cumple y lo que falta mejorar.”

---

## 16. Seguridad y validaciones
“Analiza el código en busca de vulnerabilidades o entradas no validadas (inyecciones, errores de tipo, etc.). Propón validaciones o estructuras seguras que mitiguen riesgos.”

---

## 17. Visualización de flujo
“Genera un diagrama textual (ASCII o Markdown) que muestre el flujo del programa con decisiones, funciones y salidas. Ejemplo:  
[Inicio] → ¿Condición? → [Acción A / Acción B] → [Fin]”

---

## 18. Explicación por capas
“Explica el código en tres niveles de profundidad:  
- **Básico:** qué hace y su propósito.  
- **Intermedio:** cómo lo hace (estructura interna).  
- **Avanzado:** mejoras, patrones de diseño aplicables y optimizaciones.”

</details>

---
<details>

<summary>🔹 Archivo: guiones_version_combinada.md</summary>

# 🧩 Guiones e Instrucciones Ampliadas — Versión Combinada

Este documento reúne ambas versiones (Formato original expandido y Guía narrativa paso a paso) para facilitar su comparación y uso.

---

## 📘 Parte 1 — Formato original expandido

# 📘 Guiones e Instrucciones Ampliadas (Versión 1 — Formato original expandido)

Cada instrucción fue reescrita para eliminar ambigüedades, definir resultados esperados y detallar el formato de salida.

---

---

## 📖 Guion para pedir explicaciones de código

🧭 **Objetivo:**  
Proporcionar una guía estructurada para explicar cada parte del código (funciones, clases, módulos o celdas) de forma completa y coherente.

---

### 🧩 Estructura de explicación — “Guion de 5 puntos”

| 🪶 Punto | 💬 Qué debe incluir |
|----------|--------------------|
| **1. Propósito** | Explica qué hace el fragmento de código y por qué existe. |
| **2. Uso básico** | Muestra cómo se llama o un ejemplo directo de uso práctico. |
| **3. Notas técnicas** | Detalla dependencias, riesgos, particularidades o buenas prácticas. |
| **4. Ejemplo extra** | Incluye un caso adicional distinto al original para reforzar la comprensión. |
| **5. Relación con otras partes** | Describe cómo encaja dentro del flujo general o cómo se conecta con otras funciones. |

---

### 💬 Ejemplo de uso:
> “Hazme una explicación de cada celda o función siguiendo el guion de 5 puntos:  
> 1️⃣ Propósito, 2️⃣ Uso básico, 3️⃣ Notas técnicas, 4️⃣ Ejemplo extra, 5️⃣ Relación con otras partes.”

---



## 1. Revisión de `.zip`
“Descomprime el archivo .zip proporcionado. Clasifica su contenido en dos carpetas: `/archivos_buenos` (documentos claros, completos o útiles) y `/archivos_malos` (duplicados, incompletos o erróneos). Prioriza siempre los archivos `.md` sobre `.ipynb` si ambos contienen información similar.  
Genera un `README.md` dentro de la carpeta raíz explicando los criterios usados, los archivos descartados y un breve resumen de cada documento importante.”

---

## 2. Revisión de código
“Analiza el código en profundidad: estilo, estructura, optimización y buenas prácticas. Identifica errores, redundancias o malas decisiones de diseño. Clasifica las secciones en ‘código bueno’ y ‘código malo’, justificando brevemente. Luego, propone una versión optimizada aplicando claridad, modularidad y comentarios concisos.  
Formato de entrega:  
1️⃣ Resumen general.  
2️⃣ Fortalezas y debilidades.  
3️⃣ Código mejorado.  
4️⃣ Lista de recomendaciones finales.”

---

## 3. Comparación de dos códigos
“Compara dos versiones línea por línea. Marca similitudes, diferencias y mejoras. Evalúa cuál es más clara, eficiente y completa. Explica el veredicto y propone una versión unificada que combine lo mejor de ambas.  
Estructura:  
- Comparación línea por línea.  
- Tabla de diferencias.  
- Veredicto técnico.  
- Código final unificado.”

---

## 4. Limpieza de proyecto
“Revisa todas las carpetas del proyecto. Elimina duplicados, archivos temporales y versiones antiguas. Reorganiza el contenido en una estructura limpia (`/codigo`, `/docs`, `/data`). Genera `README.md` explicando qué se eliminó y por qué.”

---

## 5. Documentación automática
“Genera un `README.md` completo con: propósito del proyecto, requisitos, instalación, uso básico, dependencias y ejemplos de ejecución. Asegúrate de usar un formato Markdown limpio y legible.”

---

## 6. Refactorización
“Reescribe el código aplicando buenas prácticas: nombres descriptivos, funciones reutilizables, comentarios breves, y eliminación de redundancias. Mantén la lógica original pero mejora su estructura y eficiencia.”

---

## 7. Revisión de estilo
“Corrige errores de formato: indentación, nombres de variables, consistencia de comillas y comentarios. Devuelve el código limpio, manteniendo la funcionalidad.”

---

## 8. Análisis comparativo
“Compara dos versiones de un archivo. Identifica cuál es más completa o eficiente. Resume las mejoras únicas de cada una y propone una versión unificada que conserve lo mejor de ambas.”

---

## 9. Explicación de flujo
“Explica el flujo lógico del programa paso a paso, en formato narrado o de diagrama: **Entrada → Procesamiento → Salida**. Menciona las funciones clave involucradas.”

---

## 10. Generación de código
“Crea un código en el lenguaje indicado para cumplir un propósito específico. Usa nombres descriptivos para funciones y variables, e incluye comentarios básicos. Aplica buenas prácticas de programación.”

---

## 11. Optimización de rendimiento
“Analiza el código buscando oportunidades de optimización (uso de memoria, velocidad de ejecución). Explica los cambios propuestos y su impacto.”

---

## 12. Conversión de lenguaje
“Convierte el código de un lenguaje a otro manteniendo su lógica, estructura y estilo. Asegúrate de que el resultado sea funcional y legible.”

---

## 13. Generación de pruebas automáticas
“Genera casos de prueba unitarios para el código usando el framework especificado. Incluye ejemplos de entrada y salida esperada. Estructura las pruebas para validar los casos normales y extremos.”

---

## 14. Explicación pedagógica
“Explica el código como si fuera para principiantes. Usa ejemplos, analogías y comparaciones fáciles de entender. Evita tecnicismos innecesarios.”

---

## 15. Checklist de buenas prácticas
“Crea una lista de verificación (checklist) que evalúe el cumplimiento de buenas prácticas: nombres, modularidad, comentarios, estilo y seguridad. Marca lo que cumple y lo que falta mejorar.”

---

## 16. Seguridad y validaciones
“Analiza el código en busca de vulnerabilidades o entradas no validadas (inyecciones, errores de tipo, etc.). Propón validaciones o estructuras seguras que mitiguen riesgos.”

---

## 17. Visualización de flujo
“Genera un diagrama textual (ASCII o Markdown) que muestre el flujo del programa con decisiones, funciones y salidas. Ejemplo:  
[Inicio] → ¿Condición? → [Acción A / Acción B] → [Fin]”

---

## 18. Explicación por capas
“Explica el código en tres niveles de profundidad:  
- **Básico:** qué hace y su propósito.  
- **Intermedio:** cómo lo hace (estructura interna).  
- **Avanzado:** mejoras, patrones de diseño aplicables y optimizaciones.”


---

## 📗 Parte 2 — Guía narrativa paso a paso

# 📗 Guiones e Instrucciones Ampliadas (Versión 2 — Guía narrativa paso a paso)

Cada instrucción está detallada como un procedimiento completo, con pasos, objetivos y estructura esperada de salida.

---

---

## 📖 Guion para pedir explicaciones de código

🧭 **Objetivo:**  
Proporcionar una guía estructurada para explicar cada parte del código (funciones, clases, módulos o celdas) de forma completa y coherente.

---

### 🧩 Estructura de explicación — “Guion de 5 puntos”

| 🪶 Punto | 💬 Qué debe incluir |
|----------|--------------------|
| **1. Propósito** | Explica qué hace el fragmento de código y por qué existe. |
| **2. Uso básico** | Muestra cómo se llama o un ejemplo directo de uso práctico. |
| **3. Notas técnicas** | Detalla dependencias, riesgos, particularidades o buenas prácticas. |
| **4. Ejemplo extra** | Incluye un caso adicional distinto al original para reforzar la comprensión. |
| **5. Relación con otras partes** | Describe cómo encaja dentro del flujo general o cómo se conecta con otras funciones. |

---

### 💬 Ejemplo de uso:
> “Hazme una explicación de cada celda o función siguiendo el guion de 5 puntos:  
> 1️⃣ Propósito, 2️⃣ Uso básico, 3️⃣ Notas técnicas, 4️⃣ Ejemplo extra, 5️⃣ Relación con otras partes.”

---



## 1. Revisión de `.zip`
**Objetivo:** Revisar el contenido de un archivo .zip y clasificar los documentos según su calidad.  
**Pasos:**  
1. Descomprimir el archivo.  
2. Clasificar los archivos en `/archivos_buenos` y `/archivos_malos`.  
3. Priorizar `.md` sobre `.ipynb` si ambos tienen información similar.  
4. Crear `README.md` con criterios de clasificación y resumen de contenido.  
**Resultado esperado:** Carpetas limpias y un `README.md` explicativo.

---

## 2. Revisión de código
**Objetivo:** Evaluar la calidad del código y proponer una versión mejorada.  
**Pasos:**  
1. Leer y comprender el propósito del código.  
2. Analizar estilo, claridad y eficiencia.  
3. Clasificar partes en buenas y malas prácticas.  
4. Proponer una versión optimizada con comentarios claros.  
5. Resumir fortalezas, debilidades y mejoras sugeridas.  
**Resultado esperado:** Informe con análisis, versión optimizada y recomendaciones.

---

## 3. Comparación de dos códigos
**Objetivo:** Determinar cuál versión es superior y unificar lo mejor de ambas.  
**Pasos:**  
1. Leer ambas versiones completas.  
2. Comparar línea por línea (idénticas, parecidas, distintas).  
3. Evaluar claridad, rendimiento y estructura.  
4. Elegir la versión más sólida.  
5. Fusionar los mejores elementos de ambas.  
6. Entregar resultado con: comparación detallada, veredicto y versión final.  
**Resultado esperado:** Tabla comparativa + código final optimizado.

---

## 4. Limpieza de proyecto
**Objetivo:** Organizar y depurar el proyecto completo.  
**Pasos:**  
1. Revisar todas las carpetas.  
2. Eliminar duplicados o temporales.  
3. Ordenar archivos en carpetas `/codigo`, `/docs`, `/data`.  
4. Crear `README.md` con resumen de cambios.  
**Resultado esperado:** Proyecto limpio y documentado.

---

## 5. Documentación automática
**Objetivo:** Generar documentación completa en formato `README.md`.  
**Pasos:**  
1. Identificar propósito del proyecto.  
2. Listar dependencias e instrucciones de instalación.  
3. Incluir ejemplos de uso y salida esperada.  
**Resultado esperado:** `README.md` estructurado con propósito, instalación y uso.

---

## 6. Refactorización
**Objetivo:** Mejorar la estructura interna del código sin cambiar su funcionalidad.  
**Pasos:**  
1. Detectar redundancias.  
2. Dividir en funciones o clases reutilizables.  
3. Mejorar nombres y eliminar código repetido.  
4. Comentar secciones clave.  
**Resultado esperado:** Código más limpio, modular y legible.

---

## 7. Revisión de estilo
**Objetivo:** Corregir problemas de formato y estilo.  
**Pasos:**  
1. Revisar indentación, comillas, y nombres de variables.  
2. Uniformar estilo de comentarios.  
3. Devolver código limpio con formato coherente.  
**Resultado esperado:** Código legible, consistente y sin errores de formato.

---

## 8. Análisis comparativo
**Objetivo:** Identificar qué versión es más completa y eficiente.  
**Pasos:**  
1. Analizar ambas versiones.  
2. Evaluar ventajas y desventajas.  
3. Combinar lo mejor en una sola versión final.  
**Resultado esperado:** Comparativo claro + versión consolidada.

---

## 9. Explicación de flujo
**Objetivo:** Explicar el recorrido lógico del programa.  
**Pasos:**  
1. Identificar puntos de entrada, procesamiento y salida.  
2. Narrar el flujo o representarlo como diagrama.  
**Resultado esperado:** Explicación secuencial clara del funcionamiento.

---

## 10. Generación de código
**Objetivo:** Crear un código funcional según los requisitos dados.  
**Pasos:**  
1. Comprender el propósito.  
2. Definir funciones y variables claras.  
3. Agregar comentarios esenciales.  
4. Cumplir buenas prácticas del lenguaje.  
**Resultado esperado:** Código funcional, limpio y documentado.

---

## 11. Optimización de rendimiento
**Objetivo:** Mejorar la eficiencia del código.  
**Pasos:**  
1. Analizar posibles cuellos de botella.  
2. Aplicar mejoras (uso de estructuras eficientes, comprensión de listas, etc.).  
3. Medir impacto y justificar cambios.  
**Resultado esperado:** Código más rápido y eficiente.

---

## 12. Conversión de lenguaje
**Objetivo:** Traducir código a otro lenguaje sin perder funcionalidad.  
**Pasos:**  
1. Analizar estructuras del código fuente.  
2. Adaptar sintaxis y tipos de datos al nuevo lenguaje.  
3. Probar equivalencia funcional.  
**Resultado esperado:** Código traducido y verificado.

---

## 13. Generación de pruebas automáticas
**Objetivo:** Crear tests que validen el correcto funcionamiento del código.  
**Pasos:**  
1. Identificar funciones clave.  
2. Definir entradas y salidas esperadas.  
3. Escribir casos de prueba unitarios.  
**Resultado esperado:** Conjunto de pruebas automatizadas funcionales.

---

## 14. Explicación pedagógica
**Objetivo:** Explicar el código de forma didáctica.  
**Pasos:**  
1. Traducir tecnicismos a lenguaje simple.  
2. Usar analogías o ejemplos.  
3. Asegurar comprensión para principiantes.  
**Resultado esperado:** Explicación clara y fácil de entender.

---

## 15. Checklist de buenas prácticas
**Objetivo:** Evaluar cumplimiento de normas de calidad en código.  
**Pasos:**  
1. Revisar modularidad, claridad, comentarios y seguridad.  
2. Marcar lo que cumple o no.  
3. Proponer mejoras.  
**Resultado esperado:** Checklist completa y recomendaciones.

---

## 16. Seguridad y validaciones
**Objetivo:** Detectar vulnerabilidades y fortalecer el código.  
**Pasos:**  
1. Revisar validaciones de entrada.  
2. Buscar posibles inyecciones o riesgos.  
3. Proponer soluciones seguras.  
**Resultado esperado:** Código más robusto y protegido.

---

## 17. Visualización de flujo
**Objetivo:** Representar gráficamente la lógica del programa.  
**Pasos:**  
1. Identificar decisiones y caminos alternativos.  
2. Representar con texto/ASCII el flujo.  
**Resultado esperado:** Diagrama claro de decisiones y resultados.

---

## 18. Explicación por capas
**Objetivo:** Entender el código desde distintos niveles de profundidad.  
**Pasos:**  
1. Nivel básico: propósito general.  
2. Nivel intermedio: cómo lo hace.  
3. Nivel avanzado: mejoras y patrones posibles.  
**Resultado esperado:** Explicación completa por niveles.

</details>

---
<details>

<summary>🔹 Archivo: Documantacion_Completa_Guiones.md</summary>

# 📘 README de Documentación Completa de Guiones.zip

Este README explica el contenido del archivo `Guiones.zip` y cómo utilizar cada parte.  
Incluye ejemplos prácticos para sacar el máximo provecho.

---

## 📁 Estructura general

```
Guiones/
├── README.md
├── Documentacion/
│   ├── readme_guiones.md
│   ├── guiones_con_ejemplos_al_final.md
│   └── guiones_con_ejemplos_intercalados.md
├── Recursos/
│   ├── ejemplos_extra.md
│   └── plantillas_para_proyectos.md
└── versiones/
    ├── v1_original/
    ├── v2_mejorada/
    └── v3_personalizada/
```

---

## 🗂️ Carpetas y contenido

### 📘 1. Documentacion/
Contiene todos los manuales y versiones del documento principal.

- **readme_guiones.md** → guía básica sobre los guiones y su uso.  
- **guiones_con_ejemplos_al_final.md** → versión con todos los ejemplos agrupados al final.  
- **guiones_con_ejemplos_intercalados.md** → versión con ejemplos debajo de cada instrucción.

**Ejemplo de uso:**  
Usa `guiones_con_ejemplos_intercalados.md` para enseñar o practicar, y `guiones_con_ejemplos_al_final.md` para documentar o imprimir.

---

### 🧩 2. Recursos/
Material complementario.

- **ejemplos_extra.md** → agrega ejemplos personalizados o avanzados.  
  _Ejemplo:_ cómo aplicar el guion de revisión de código a un script Python real.  
- **plantillas_para_proyectos.md** → espacio para definir estructuras de carpetas o esquemas de proyectos (lo dejamos vacío para que agregues tus propias plantillas).

---

### 🧱 3. versiones/
Carpeta pensada para mantener diferentes iteraciones o versiones de tus guiones.

- **v1_original/** → primera versión sin modificaciones.  
- **v2_mejorada/** → versión ajustada y optimizada.  
- **v3_personalizada/** → versión adaptada a necesidades o contextos específicos.

**Ejemplo de uso:**  
1. Guarda tus archivos iniciales en `v1_original/`.  
2. Crea mejoras y colócalas en `v2_mejorada/`.  
3. Genera variantes específicas y guárdalas en `v3_personalizada/`.

---

## 💡 Ejemplo práctico de flujo de trabajo

1. Crea tu primer documento en `v1_original/` con una estructura inicial.  
2. Usa los guiones para revisarlo (por ejemplo: revisión de código o refactorización).  
3. Guarda la versión revisada en `v2_mejorada/`.  
4. Si adaptas la documentación a un nuevo contexto (ej. otro equipo o idioma), guárdala en `v3_personalizada/`.

---

## 📚 Consejos adicionales

- Mantén copias limpias y ordenadas dentro de `versiones/` para evitar sobrescribir trabajo previo.  
- Usa `ejemplos_extra.md` para documentar tus casos de uso reales.  
- Amplía `plantillas_para_proyectos.md` para estandarizar la estructura de tus próximos proyectos.

---

✅ Con esta estructura, tendrás una organización clara, reutilizable y profesional para todos tus guiones, ejemplos y versiones.

</details>

---
<details>

<summary>🔹 Archivo: readme_guiones.md</summary>

# 📘 README – Guiones e Instrucciones con Ejemplos

Este conjunto incluye dos versiones del documento **“Guiones e Instrucciones Mejorados”**, pensadas para diferentes estilos de uso: aprendizaje, referencia o documentación técnica.

---

## 🗂️ Versión A — *Guiones con ejemplos al final*
**Archivo:** `guiones_con_ejemplos_al_final.md`

### 🧭 Cuándo usarla
- Para lectura lineal, presentaciones o documentación profesional.
- Si prefieres que los ejemplos estén agrupados como anexo.

### ✅ Ventajas
- Cuerpo principal más limpio y ordenado.
- Ejemplos concentrados en una sola sección final.
- Ideal para exportar a PDF o imprimir.

---

## 📘 Versión B — *Guiones con ejemplos intercalados*
**Archivo:** `guiones_con_ejemplos_intercalados.md`

### 🧭 Cuándo usarla
- Para estudio, práctica o enseñanza directa.
- Si quieres ver el ejemplo justo después de cada instrucción.

### ✅ Ventajas
- Ejemplos contextualizados e inmediatos.
- Flujo natural: instrucción → ejemplo → aplicación.
- Perfecta para mentorías o aprendizaje autodidacta.

---

## ⚙️ Recomendación de uso

| Objetivo | Versión recomendada |
|-----------|---------------------|
| Documentación limpia / PDF | 🗂️ **Versión A** |
| Aprendizaje o repaso práctico | 📘 **Versión B** |
| Enseñanza o mentorías | 📘 **Versión B** |
| Guía de referencia profesional | 🗂️ **Versión A** |

---

### 🧩 Consejo final
Puedes mantener ambas versiones juntas: usa la **Versión B** para aprender o enseñar, y la **Versión A** como plantilla final o referencia de trabajo profesional.

</details>

---
<details>

<summary>🔹 Archivo: guiones_con_ejemplos_intercalados.md</summary>

# 📑 Guiones e Instrucciones Mejorados (Versión B - Ejemplos intercalados)

Guía práctica con ejemplos integrados debajo de cada instrucción express.

---

## 📖 Guion para pedir explicaciones de código

| Punto | Qué incluye |
|-------|-------------|
| **Propósito** | Qué hace y por qué existe. |
| **Uso básico** | Cómo se llama o un ejemplo directo de uso. |
| **Notas técnicas** | Dependencias, riesgos, particularidades, buenas prácticas. |
| **Ejemplo extra** | Otro caso práctico distinto al original. |
| **Relación con otras partes** | Cómo encaja en el flujo general o con otras funciones. |

Ejemplo:
```python
def saludar(nombre):
    return f"Hola, {nombre}!"
```
Propósito: saluda al usuario.  
Uso básico: `saludar("Ana")` → "Hola, Ana!"

---

## ⚡ Instrucciones express con ejemplos

### 🔹 Revisión de .zip
**Instrucción:**  
“Descomprime este .zip, separa en `/archivos_buenos` y `/archivos_malos`, prioriza `.md` sobre `.ipynb`, y agrega README.md con comparaciones.”

**Ejemplo:**
- Entrada: `proyecto.zip` con versiones duplicadas.
- Salida: dos carpetas (`/archivos_buenos`, `/archivos_malos`) y `README.md` con explicación.

---

### 🔹 Revisión de código
**Instrucción:**  
“Revisa el código, dime qué es bueno y malo, señala errores/redundancias y propón mejoras.”

**Ejemplo:**
```python
def sumar(a,b):return a+b
```
➡️ Sugerencia: agregar espacios y docstring.
```python
def sumar(a: int, b: int) -> int:
    """Suma dos números."""
    return a + b
```

---

### 🔹 Comparación de dos códigos
“Compáralos línea por línea y dime cuál es mejor.”

**Ejemplo:**
Dos funciones similares, una usa nombres claros (`sumar`), otra genéricos (`f1`).  
Resultado: la primera es más legible.

---

### 🔹 Limpieza de proyecto
“Revisa todas las carpetas, ordénalas en `proyecto_limpio/`, elimina duplicados y agrega README.md.”

**Ejemplo:**
Entrada: `/docs`, `/codigo`, `/viejos`.  
Salida: `/proyecto_limpio/docs`, `/proyecto_limpio/src`.

---

### 🔹 Documentación automática
“Genera un README.md con propósito, instalación, uso, dependencias y ejemplos.”

**Ejemplo de salida:**
```md
# Proyecto X
## Instalación
pip install -r requirements.txt
## Uso
python main.py
```

---

### 🔹 Refactorización
“Reescribe este código aplicando buenas prácticas.”

**Ejemplo:**
Antes:
```python
print('Hola');print('Adiós')
```
Después:
```python
def saludar():
    print('Hola')
    print('Adiós')
```

---

### 🔹 Revisión de estilo
“Revisa el estilo del código, corrige indentación y nombres.”

Antes:
```python
Var=5
```
Después:
```python
var = 5
```

---

### 🔹 Análisis comparativo
“Dime cuál versión es más completa y propón una unificada.”

**Ejemplo:** Combinar funciones duplicadas en una única más limpia.

---

### 🔹 Explicación de flujo
“Explícame el flujo del código paso a paso.”

**Ejemplo:**
```
[Inicio] → [Procesamiento] → [Salida]
```

---

### 🔹 Generación de código
“Genera un código en Python para sumar.”
```python
def sumar(a,b): return a+b
```

---

### 🔹 Optimización de rendimiento
“Analiza este código y propón optimizaciones.”

Antes:
```python
res=[]
for i in range(100000): res.append(i*i)
```
Optimizado:
```python
res=[i*i for i in range(100000)]
```

---

### 🔹 Conversión de lenguaje
“Convierte este código de Python a JavaScript.”

Python:
```python
def saludar(nombre):
    return f"Hola, {nombre}"
```
JavaScript:
```javascript
function saludar(nombre){
  return `Hola, ${nombre}`;
}
```

---

### 🔹 Generación de pruebas automáticas
“Genera pruebas unitarias.”
```python
def sumar(a,b):return a+b

def test_sumar():
    assert sumar(2,3)==5
```

---

### 🔹 Explicación pedagógica
“Explícame este código como si fuera para principiantes.”

Código:
```python
def duplicar(x):return x*2
```
Explicación: “Es como poner una hoja en la fotocopiadora: entra una, salen dos.”

---

### 🔹 Checklist de buenas prácticas
“Hazme una checklist de buenas prácticas.”

Código:
```python
x=5;y=10;print(x+y)
```
Resultado:
- ❌ Variables poco descriptivas.
- ✅ Código corto.
- 🔹 Mejora: usar `def sumar(a,b):return a+b`.

---

### 🔹 Seguridad y validaciones
“Revisa este código por seguridad.”

```python
entrada=input("Número:")
try:
    print(int(entrada)*2)
except ValueError:
    print("Entrada inválida.")
```

---

### 🔹 Visualización de flujo
“Genera un diagrama ASCII.”
```
[Inicio]
 ↓
¿n > 0?
 ├ Sí → [Positivo]
 └ No → [No positivo]
 ↓
[Fin]
```

---

### 🔹 Explicación por capas
“Explícame en 3 niveles.”

Código:
```python
def area_circulo(r):
    return 3.14 * r**2
```
- **Básico:** calcula el área.  
- **Intermedio:** usa fórmula πr².  
- **Avanzado:** mejora: usar `math.pi` y validar valores.

</details>

---
<details>

<summary>🔹 Archivo: guiones_con_ejemplos_al_final.md</summary>

# 📑 Guiones e Instrucciones Mejorados (Versión A - Ejemplos al final)

Este documento es una **guía práctica** para pedir revisiones, explicaciones o generación de código. Incluye plantillas detalladas, resúmenes en una línea y ejemplos prácticos al final.

---

## 📖 Guion para pedir explicaciones de código

| Punto | Qué incluye |
|-------|-------------|
| **Propósito** | Qué hace y por qué existe. |
| **Uso básico** | Cómo se llama o un ejemplo directo de uso. |
| **Notas técnicas** | Dependencias, riesgos, particularidades, buenas prácticas. |
| **Ejemplo extra** | Otro caso práctico distinto al original. |
| **Relación con otras partes** | Cómo encaja en el flujo general o con otras funciones. |

Ejemplo de uso:
> “Hazme una explicación de cada celda/función con el guion de 5 puntos: Propósito, Uso básico, Notas técnicas, Ejemplo extra, Relación con otras partes.”

---

## 📌 Instrucciones rápidas para revisiones

### 1. Revisión de `.zip` con documentos
- Descomprimir y clasificar archivos.
- Priorizar `.md` sobre `.ipynb`.
- Agregar `README.md` con justificación.

### 2. Revisión de código
- Evaluar: estilo, legibilidad, optimización.
- Identificar errores, redundancias y duplicados.
- Clasificar en **código bueno/malo** y proponer mejoras.

### 3. Comparación de dos archivos
- Comparar línea por línea.
- Clasificar cuál es mejor.
- Proponer una versión unificada.

---

## ⚡ Instrucciones express en una línea

| Caso | Instrucción express |
|------|----------------------|
| **Revisión de .zip** | “Descomprime este .zip, separa en `/archivos_buenos` y `/archivos_malos`, prioriza `.md` sobre `.ipynb`, y agrega `README.md` con comparaciones.” |
| **Revisión de código** | “Revisa el código, dime qué es bueno y malo, señala errores/redundancias y propón mejoras claras con ejemplos.” |
| **Comparación de dos códigos** | “Compáralos línea por línea, indica iguales/diferencias, cuál es mejor y cómo unificar lo mejor de ambos en una versión final.” |
| **Limpieza de proyecto** | “Revisa todas las carpetas, ordénalas en `proyecto_limpio/`, elimina duplicados y agrega README.md con explicación.” |
| **Documentación automática** | “Genera un README.md con propósito, instalación, uso, dependencias y ejemplos de ejecución.” |
| **Refactorización** | “Reescribe este código aplicando buenas prácticas: nombres claros, funciones reutilizables, comentarios breves, sin redundancias.” |
| **Revisión de estilo** | “Revisa el estilo del código, corrige indentación, nombres de variables, consistencia de comillas, y dame el resultado limpio.” |
| **Análisis comparativo** | “Dime cuál versión de este archivo es más completa, qué mejoras únicas trae cada una, y propón una versión unificada.” |
| **Explicación de flujo** | “Explícame el flujo del código paso a paso, como si fuera un diagrama narrado: entrada → procesamiento → salida.” |
| **Generación de código** | “Genera un código en [lenguaje] para [uso]. Usa nombres de funciones [ejemplo], variables [ejemplo] y aplica buenas prácticas.” |
| **Optimización de rendimiento** | “Analiza este código y propón optimizaciones de rendimiento (memoria, velocidad), explicando el impacto de cada cambio.” |
| **Conversión de lenguaje** | “Convierte este código de [lenguaje origen] a [lenguaje destino], manteniendo la misma lógica y estilo.” |
| **Generación de pruebas automáticas** | “Genera casos de prueba unitarios para este código usando [framework] con ejemplos de entrada y salida esperada.” |
| **Explicación pedagógica** | “Explícame este código como si fuera para principiantes, usando analogías sencillas y ejemplos fáciles.” |
| **Checklist de buenas prácticas** | “Hazme una checklist de buenas prácticas aplicada a este código, con lo que cumple y lo que debería mejorar.” |
| **Seguridad y validaciones** | “Revisa este código buscando posibles riesgos de seguridad (inyecciones, validaciones faltantes, etc.) y propón soluciones.” |
| **Visualización de flujo** | “Genera un diagrama en texto/ASCII que muestre el flujo del programa: decisiones, funciones y salidas principales.” |
| **Explicación por capas** | “Explícame este código en 3 niveles: básico (qué hace), intermedio (cómo lo hace), avanzado (mejoras y patrones de diseño aplicables).” |

---

# 🧩 Ejemplos prácticos por instrucción

### 1. Revisión de `.zip`
Petición: “Revisa este .zip.”  
→ Resultado esperado: `/archivos_buenos/`, `/archivos_malos/` y `README.md` justificando duplicados.

### 2. Revisión de código
```python
def sumar(a, b):
    return a + b
```
Salida: señalar claridad y optimización posible.

### 3. Comparación de códigos
Dos versiones del mismo código → indicar cuál es más clara.

### 4. Limpieza de proyecto
Organizar archivos en carpetas `/codigo`, `/docs`, `/data`.

### 5. Documentación automática
Generar `README.md` explicando propósito, uso y dependencias.

### 6. Refactorización
Código repetido → convertir en función reutilizable.

### 7. Revisión de estilo
Corregir nombres y sangrías: `MiVariable` → `mi_variable`.

### 8. Análisis comparativo
Elegir versión más completa y combinar lo mejor de ambas.

### 9. Explicación de flujo
```
Entrada → Procesamiento → Salida
```

### 10. Generación de código
Petición: “Genera código en Python para sumar.”
```python
def sumar(a,b): return a+b
```

### 11. Optimización de rendimiento
Usar comprensión de listas en lugar de bucle for.

### 12. Conversión de lenguaje
Python → JavaScript.

### 13. Generación de pruebas automáticas
Usar `pytest`:
```python
def test_sumar():
    assert sumar(2,3)==5
```

### 14. Explicación pedagógica
Explicación con analogías para principiantes.

### 15. Checklist de buenas prácticas
Variables, modularidad, comentarios, consistencia.

### 16. Seguridad y validaciones
Agregar `try/except` para validar entradas.

### 17. Visualización de flujo
```
[Inicio] → ¿Condición? → [Acción A / Acción B] → [Fin]
```

### 18. Explicación por capas
**Básico:** qué hace.  
**Intermedio:** cómo lo hace.  
**Avanzado:** posibles mejoras o patrones de diseño.

</details>

---
<details>

<summary>🔹 Archivo: documentation_template.md</summary>

````markdown
> 💬 **Instrucción reutilizable:**
Quiero que generes un archivo [Readme_nombre].md completo para el código que te enviaré.

Debe incluir lo siguiente:
1. **Título y descripción general del proyecto.**
2. **Propósito del proyecto** (qué hace y para qué sirve).
3. **Requisitos** (versión mínima de Python u otros).
4. **Instalación paso a paso.**
5. **Uso básico** (con ejemplos de ejecución y salida esperada en consola).
6. **Dependencias** (si las hay, aclara si no usa ninguna externa).
7. **Explicación detallada de cada función**, siguiendo exactamente este formato de 5 puntos:

   ```
   Nombre de la función: nombre_funcion(parámetros) -> tipo_retorno
   1️⃣ Propósito: Explica claramente qué hace.
   2️⃣ Uso básico: Ejemplo corto de uso.
   3️⃣ Notas técnicas: Explica brevemente cómo funciona internamente o detalles clave.
   4️⃣ Ejemplo extra: Muestra uno o dos ejemplos adicionales.
   5️⃣ Relación con otras partes: Explica en qué se usa dentro del código.
   ```

8. **Código fuente completo al final del .md**, dentro de un bloque Markdown.

El formato debe ser **Markdown limpio y legible**, usando títulos, secciones y emojis descriptivos donde corresponda (por ejemplo: 🧠, ⚙️, 🚀, 🧾, 🧩, 🧮, etc.).

Finalmente, quiero que me generes **el archivo .md listo para descargar**.
````

> 💬 **Nota:**  
> Este documento funciona como **plantilla de referencia** para la **documentación de proyectos de código en Python**.  
>  
> Se recomienda usar su estructura, estilo y nivel de detalle como modelo al crear nuevas documentaciones técnicas, asegurando coherencia y claridad entre los distintos proyectos.

# 📘 Proyecto: Cálculo de Área y Perímetro de una Circunferencia

## 🧭 Propósito del Proyecto
Este proyecto tiene como objetivo ofrecer una herramienta sencilla en **Python** para calcular el **área** y el **perímetro (longitud de la circunferencia)** a partir de un radio dado.  
El código sirve como ejemplo básico de uso de funciones matemáticas y entrada/salida de datos en consola.

---

## 📋 Requisitos

- **Python 3.8** o superior  
- Librería estándar `math` (ya incluida con Python)

---

## ⚙️ Instalación

1. Descarga el archivo `area_perimetro_circunferencia.py`.  
2. Guarda el archivo en tu directorio de trabajo.  
3. (Opcional) Crea un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate   # En macOS / Linux
   venv\Scripts\activate      # En Windows
   ```

4. No se requieren dependencias externas.

---

## 🚀 Uso Básico

Ejecuta el script desde consola:

```bash
python area_perimetro_circunferencia.py
```

Luego introduce el **radio** cuando el programa lo solicite:

```
Ingresa el radio de la circunferencia: 5
Área: 78.54
Perímetro: 31.42
```

---

## 🧩 Dependencias

| Librería | Descripción | Versión |
|-----------|--------------|----------|
| `math` | Proporciona la constante π (`math.pi`) y funciones matemáticas básicas. | Incluida en Python |

---

## 🧠 Explicación de las Funciones

### 🔹 `area_circunferencia(radio: float) -> float`

1️⃣ **Propósito**  
Calcula el área de una circunferencia a partir del valor del radio usando la fórmula:  
\[ Área = π × radio^2 \]

2️⃣ **Uso básico**  
Devuelve un valor flotante correspondiente al área.  
```python
area_circunferencia(5)  # Devuelve 78.53981633974483
```

3️⃣ **Notas técnicas**  
- Utiliza `math.pi` para obtener un valor preciso de π.  
- Retorna un número de tipo `float`.  
- No realiza validaciones sobre el valor del radio (se asume positivo).  

4️⃣ **Ejemplo extra**  
```python
print(area_circunferencia(10))  # 314.1592653589793
```

5️⃣ **Relación con otras partes**  
Es llamada dentro del bloque `if __name__ == "__main__":` para mostrar el área calculada al usuario.

---

### 🔹 `perimetro_circunferencia(radio: float) -> float`

1️⃣ **Propósito**  
Calcula el perímetro (longitud de la circunferencia) a partir del radio usando la fórmula:  
\[ Perímetro = 2 × π × radio \]

2️⃣ **Uso básico**  
Devuelve un valor flotante correspondiente al perímetro.  
```python
perimetro_circunferencia(5)  # Devuelve 31.41592653589793
```

3️⃣ **Notas técnicas**  
- Usa `math.pi` del módulo estándar.  
- Retorna un `float`.  
- Al igual que la función anterior, no valida el signo del radio.  

4️⃣ **Ejemplo extra**  
```python
print(perimetro_circunferencia(3.5))  # 21.991148575128552
```

5️⃣ **Relación con otras partes**  
Se ejecuta junto con `area_circunferencia` en la sección principal del script, mostrando ambos resultados formateados con dos decimales.

---

## 💻 Ejemplo de Ejecución Completa

```bash
$ python area_perimetro_circunferencia.py
Ingresa el radio de la circunferencia: 7.25
Área: 165.13
Perímetro: 45.56
```

---

## 📄 Contenido del Código

```python
import math

def area_circunferencia(radio):
    """Calcula el área de una circunferencia dado su radio."""
    return math.pi * radio ** 2

def perimetro_circunferencia(radio):
    """Calcula el perímetro (circunferencia) dado su radio."""
    return 2 * math.pi * radio

if __name__ == "__main__":
    radio = float(input("Ingresa el radio de la circunferencia: "))
    print(f"Área: {area_circunferencia(radio):.2f}")
    print(f"Perímetro: {perimetro_circunferencia(radio):.2f}")
```

</details>

---
<details>

<summary>🔹 Archivo: instruccion_generar_readme.md</summary>

# 🧩 Plantilla para pedir documentación técnica completa

> 💬 **Instrucción reutilizable:**

````markdown
Quiero que generes un archivo [Readme_nombre].md completo para el código que te enviaré.

Debe incluir lo siguiente:
1. **Título y descripción general del proyecto.**
2. **Propósito del proyecto** (qué hace y para qué sirve).
3. **Requisitos** (versión mínima de Python u otros).
4. **Instalación paso a paso.**
5. **Uso básico** (con ejemplos de ejecución y salida esperada en consola).
6. **Dependencias** (si las hay, aclara si no usa ninguna externa).
7. **Explicación detallada de cada función**, siguiendo exactamente este formato de 5 puntos:

   ```
   Nombre de la función: nombre_funcion(parámetros) -> tipo_retorno
   1️⃣ Propósito: Explica claramente qué hace.
   2️⃣ Uso básico: Ejemplo corto de uso.
   3️⃣ Notas técnicas: Explica brevemente cómo funciona internamente o detalles clave.
   4️⃣ Ejemplo extra: Muestra uno o dos ejemplos adicionales.
   5️⃣ Relación con otras partes: Explica en qué se usa dentro del código.
   ```

8. **Código fuente completo al final del .md**, dentro de un bloque Markdown.
9. **Sección final con sugerencias de mejora o ampliación futura.**
10. **Autor, licencia, versión y lenguaje.**

El formato debe ser **Markdown limpio y legible**, usando títulos, secciones y emojis descriptivos donde corresponda (por ejemplo: 🧠, ⚙️, 🚀, 🧾, 🧩, 🧮, etc.).

Finalmente, quiero que me generes **el archivo .md listo para descargar**.
---

💡 Si lo deseas, puedes añadir al final:
> “Prepara también un resumen breve del proyecto (1 párrafo) para README o GitHub.”
````

---

## ⚡ Versión abreviada para comandos rápidos

> 🧠 **Uso rápido:**  
> “Genera un README.md completo del código con propósito, requisitos, instalación, uso, dependencias, análisis de funciones (formato 1️⃣–5️⃣), código completo y sugerencias finales, en formato Markdown limpio y listo para descargar.”

</details>

---
<details>

<summary>🔹 Archivo: plantilla_generar_md.md</summary>

# 📄 Plantilla para generar archivos .md descargables

## 🧾 Descripción general

Esta plantilla te permite solicitar documentación técnica o descriptiva de un archivo de código y recibirla directamente como un **archivo `.md` listo para descargar**.  
Solo necesitas reemplazar los valores entre corchetes `[ ]` según tu proyecto.

---

## 🧩 Plantilla base

> Genera un archivo **[nombre_del_archivo].md** descargable, tomando como base el código que te adjunto.  
>  
> El archivo debe incluir de forma completa y ordenada:  
> - Propósito del proyecto  
> - Requisitos  
> - Instalación  
> - Uso básico  
> - Dependencias  
> - Ejemplos de ejecución  
> - Explicación de cada función siguiendo el guion de 5 puntos (1️⃣ Propósito, 2️⃣ Uso básico, 3️⃣ Notas técnicas, 4️⃣ Ejemplo extra, 5️⃣ Relación con otras partes)  
> - Y al final, el **contenido textual completo del código fuente**.  
>  
> Entrégame el resultado como **archivo .md listo para descargar**, no solo el texto.

---

## 💡 Ejemplo de uso real

> Genera un archivo **area_perimetro_circunferencia.md** descargable, tomando como base el código que te adjunto.  
>  
> El `.md` debe incluir: propósito del proyecto, requisitos, instalación, uso básico, dependencias, ejemplos de ejecución y explicación de cada función según el guion de 5 puntos.  
>  
> Entrégame el archivo listo para descargar.

---

## ⚙️ Instrucciones rápidas

1. Adjunta tu archivo `.py`, `.js`, `.html` o cualquier código fuente.  
2. Copia y pega esta plantilla en tu primer mensaje.  
3. Reemplaza `[nombre_del_archivo]` por el nombre deseado.  
4. Envía el mensaje: automáticamente se generará el `.md` para descarga.

---

## 🧰 Sugerencia adicional

Puedes usar versiones adaptadas para otros formatos, por ejemplo:

- Para un PDF: reemplaza `.md` por `.pdf`.  
- Para un ZIP con múltiples archivos: pide explícitamente que se entregue “todo comprimido en un `.zip` descargable”.

---

## 🧠 Consejo final

Cuanto más claro y completo sea tu primer mensaje, más rápido recibirás el archivo generado correctamente.

</details>

---
<details>

<summary>🔹 Archivo: plantilla_documentation.md</summary>

> 💬 **Nota:**  
> Este documento funciona como **plantilla de referencia** para la **documentación de proyectos de código en Python**.  
>  
> Se recomienda usar su estructura, estilo y nivel de detalle como modelo al crear nuevas documentaciones técnicas, asegurando coherencia y claridad entre los distintos proyectos.

# 📘 Proyecto: Cálculo de Área y Perímetro de una Circunferencia

## 🧭 Propósito del Proyecto
Este proyecto tiene como objetivo ofrecer una herramienta sencilla en **Python** para calcular el **área** y el **perímetro (longitud de la circunferencia)** a partir de un radio dado.  
El código sirve como ejemplo básico de uso de funciones matemáticas y entrada/salida de datos en consola.

---

## 📋 Requisitos

- **Python 3.8** o superior  
- Librería estándar `math` (ya incluida con Python)

---

## ⚙️ Instalación

1. Descarga el archivo `area_perimetro_circunferencia.py`.  
2. Guarda el archivo en tu directorio de trabajo.  
3. (Opcional) Crea un entorno virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate   # En macOS / Linux
   venv\Scripts\activate      # En Windows
   ```

4. No se requieren dependencias externas.

---

## 🚀 Uso Básico

Ejecuta el script desde consola:

```bash
python area_perimetro_circunferencia.py
```

Luego introduce el **radio** cuando el programa lo solicite:

```
Ingresa el radio de la circunferencia: 5
Área: 78.54
Perímetro: 31.42
```

---

## 🧩 Dependencias

| Librería | Descripción | Versión |
|-----------|--------------|----------|
| `math` | Proporciona la constante π (`math.pi`) y funciones matemáticas básicas. | Incluida en Python |

---

## 🧠 Explicación de las Funciones

### 🔹 `area_circunferencia(radio: float) -> float`

1️⃣ **Propósito**  
Calcula el área de una circunferencia a partir del valor del radio usando la fórmula:  
\[ Área = π × radio^2 \]

2️⃣ **Uso básico**  
Devuelve un valor flotante correspondiente al área.  
```python
area_circunferencia(5)  # Devuelve 78.53981633974483
```

3️⃣ **Notas técnicas**  
- Utiliza `math.pi` para obtener un valor preciso de π.  
- Retorna un número de tipo `float`.  
- No realiza validaciones sobre el valor del radio (se asume positivo).  

4️⃣ **Ejemplo extra**  
```python
print(area_circunferencia(10))  # 314.1592653589793
```

5️⃣ **Relación con otras partes**  
Es llamada dentro del bloque `if __name__ == "__main__":` para mostrar el área calculada al usuario.

---

### 🔹 `perimetro_circunferencia(radio: float) -> float`

1️⃣ **Propósito**  
Calcula el perímetro (longitud de la circunferencia) a partir del radio usando la fórmula:  
\[ Perímetro = 2 × π × radio \]

2️⃣ **Uso básico**  
Devuelve un valor flotante correspondiente al perímetro.  
```python
perimetro_circunferencia(5)  # Devuelve 31.41592653589793
```

3️⃣ **Notas técnicas**  
- Usa `math.pi` del módulo estándar.  
- Retorna un `float`.  
- Al igual que la función anterior, no valida el signo del radio.  

4️⃣ **Ejemplo extra**  
```python
print(perimetro_circunferencia(3.5))  # 21.991148575128552
```

5️⃣ **Relación con otras partes**  
Se ejecuta junto con `area_circunferencia` en la sección principal del script, mostrando ambos resultados formateados con dos decimales.

---

## 💻 Ejemplo de Ejecución Completa

```bash
$ python area_perimetro_circunferencia.py
Ingresa el radio de la circunferencia: 7.25
Área: 165.13
Perímetro: 45.56
```

---

## 📄 Contenido del Código

```python
import math

def area_circunferencia(radio):
    """Calcula el área de una circunferencia dado su radio."""
    return math.pi * radio ** 2

def perimetro_circunferencia(radio):
    """Calcula el perímetro (circunferencia) dado su radio."""
    return 2 * math.pi * radio

if __name__ == "__main__":
    radio = float(input("Ingresa el radio de la circunferencia: "))
    print(f"Área: {area_circunferencia(radio):.2f}")
    print(f"Perímetro: {perimetro_circunferencia(radio):.2f}")
```

</details>

---
<details>

<summary>🔹 Archivo: README_guion_explicaciones.md</summary>

# 📖 Guion para pedir explicaciones de código

Este documento es una **plantilla práctica** que puedes usar para pedirme ayuda con código.  
Así tendrás respuestas claras, estructuradas y fáciles de adaptar a lo que necesites.  

---

## 📋 Mi propuesta de guion (más claro y adaptable)

Cuando me pidas explicaciones de código, puedes decir algo así:

> “Explícame cada función o celda de código con este formato:
>
> **Propósito:** qué hace y por qué existe.  
> **Uso básico:** cómo se llama o un ejemplo rápido de uso.  
> **Notas técnicas:** dependencias, riesgos, particularidades del lenguaje/lib, buenas prácticas.  
> **Ejemplo extra:** un ejemplo distinto al de la celda, para ver otro caso de uso.  
> **(Opcional) Relación con otras partes:** si se conecta con otra función, dónde y cómo.”

---

## 📌 Resumen de la plantilla

- **Propósito** (qué hace, por qué existe).  
- **Uso básico** (ejemplo directo).  
- **Notas técnicas** (riesgos, dependencias, buenas prácticas).  
- **Ejemplo extra** (otro caso práctico).  
- **Relación con otras partes** (cómo encaja en el todo).  

---

## 🚀 Cómo pedírmelo en el futuro

Cuando quieras que lo haga para un código tuyo, basta que me digas algo así:

> “Hazme una explicación de cada celda/función con el guion de 5 puntos:  
> **Propósito,**  
> **Uso básico,**  
> **Notas técnicas,**  
> **Ejemplo extra,**  
> **Relación con otras partes.**”

Y yo te devuelvo la documentación de todo lo que me pases con ese esquema.  

</details>

---
<details>

<summary>🔹 Archivo: plantilla_doc_exp.md</summary>

# 🎯 **Título del proyecto o script (por ejemplo: Cálculo de EXP por ciclos)**

> Este README documenta un script o notebook del Proyecto Peluca.  
> Mantiene la estructura estandarizada con secciones explicativas, ejemplos y observaciones técnicas.

## Table of Contents

    - [🧮 Explicación del código](#explicación-del-código)
      - [1️⃣ Propósito](#1-propósito)
      - [2️⃣ Uso básico](#2-uso-básico)
      - [3️⃣ Notas técnicas](#3-notas-técnicas)
      - [4️⃣ Ejemplo extra](#4-ejemplo-extra)
    - [🎯 **Documentación detallada**](#documentación-detallada)
      - [📘 Descripción general](#descripción-general)
      - [⚙️ **1. Parámetros iniciales**](#1-parámetros-iniciales)
      - [⏱️ **2. Cálculo principal o función base**](#2-cálculo-principal-o-función-base)
      - [📊 **3. Ejecución o resultados parciales**](#3-ejecución-o-resultados-parciales)
      - [🧩 **4. Observaciones técnicas**](#4-observaciones-técnicas)
      - [📈 **5. Ejemplo de salida esperada**](#5-ejemplo-de-salida-esperada)
      - [🧠 **6. Interpretación**](#6-interpretación)
      - [🏁 **7. Conclusión**](#7-conclusión)

---

### 🧮 Explicación del código

#### 1️⃣ Propósito  
> Explica en una o dos frases qué problema resuelve tu script y qué calcula o genera.  
> Ejemplo: “El objetivo del script es calcular el tiempo total necesario para alcanzar una cantidad de experiencia (EXP) dada una ganancia por ciclo.”

---

#### 2️⃣ Uso básico  
> Indica cómo se usa la función o script.  
> Ejemplo:
```python
mi_funcion(param1, param2, ...)
```
> Añade una descripción breve de los parámetros y el flujo general.

---

#### 3️⃣ Notas técnicas  
> Describe brevemente detalles internos del código (funciones auxiliares, validaciones, formateo, librerías utilizadas, etc.)

---

#### 4️⃣ Ejemplo extra  
> Muestra una ejecución simple del script con valores de ejemplo:
```python
mi_funcion(1000, 45, 60, [100, 200, 500])
```
> y comenta el resultado esperado.

---

# 🎯 **Documentación detallada**

### 📘 Descripción general
> Resume lo que hace el script y qué salida produce.  
> Explica el contexto de uso o utilidad práctica.

---

## ⚙️ **1. Parámetros iniciales**
> Lista las variables o parámetros definidos al inicio:
```python
param1 = ...
param2 = ...
```
> Indica qué representa cada uno.

---

## ⏱️ **2. Cálculo principal o función base**
> Muestra el núcleo lógico del script o función principal con código y breve explicación.

---

## 📊 **3. Ejecución o resultados parciales**
> Describe cómo se presenta la salida intermedia (por ejemplo, una tabla o una lista formateada).

---

## 🧩 **4. Observaciones técnicas**
> Señala detalles de implementación, buenas prácticas o decisiones de diseño.  
> Ejemplo: “Se usa `ceil()` para asegurar que el número de ciclos sea entero.”

---

## 📈 **5. Ejemplo de salida esperada**
> Incluye uno o más ejemplos con `input` y su salida correspondiente:

```python
mi_funcion(57000, 60, 45, 60)
```

<details>
<summary><strong>Output</strong></summary>

```
Aquí va la salida del programa
(formateada en consola, si aplica)
```
</details>

---

## 🧠 **6. Interpretación**
> Explica brevemente cómo interpretar los resultados o cómo usarlos.

---

## 🏁 **7. Conclusión**
> Cierra el documento indicando el propósito final, la utilidad o posibles extensiones futuras.

---

</details>

---
<details>

<summary>🔹 Archivo: template_doc_exp_en.md</summary>

# **Project or Script Title (e.g., EXP Calculation per Cycle)**

> This README documents a script or notebook following the Peluca project documentation style.  
> It maintains a standardized structure with clear sections, examples, and technical notes.

## Table of Contents

- [**Code Explanation**](#code-explanation)
  - [Purpose](#purpose)
  - [Basic Usage](#basic-usage)
  - [Technical Notes](#technical-notes)
  - [Additional Example](#additional-example)
- [**Detailed Documentation**](#detailed-documentation)
  - [General Description](#general-description)
  - [Initial Parameters](#initial-parameters)
  - [Main Computation or Core Function](#main-computation-or-core-function)
  - [Execution or Partial Results](#execution-or-partial-results)
  - [Technical Observations](#technical-observations)
  - [Expected Output Example](#expected-output-example)
  - [Interpretation](#interpretation)
  - [Conclusion](#conclusion)

---

### **Code Explanation**

**Purpose**  
Explain in one or two sentences what the script does or what problem it solves.  
Example: “This script calculates the total time required to reach a target amount of experience (EXP) based on per-cycle gain rates.”

---

**Basic Usage**  
Show how to run the script or call the main function:
```python
my_function(param1, param2, ...)
```
Briefly describe each parameter and the expected output.

---

**Technical Notes**  
Add a short explanation of auxiliary functions, validation logic, libraries used, or special formatting rules.

---

**Additional Example**  
Provide a minimal code example with sample parameters and expected output:
```python
my_function(1000, 45, 60, [100, 200, 500])
```
Briefly explain what the result represents.

---

# **Detailed Documentation**

**General Description**  
Summarize what the script does and the type of output it produces.  
Include context or practical use cases.

---

**Initial Parameters**  
List the base variables or configuration values defined at the start:
```python
param1 = ...
param2 = ...
```
Explain what each variable represents.

---

**Main Computation or Core Function**  
Show the main logic or core algorithm of the script, including key formulas and brief commentary.

---

**Execution or Partial Results**  
Describe how intermediate or partial results are displayed (tables, lists, or printed values).

---

**Technical Observations**  
Note specific implementation details, assumptions, or design decisions.  
Example: “The use of `ceil()` ensures that the number of cycles is always an integer.”

---

**Expected Output Example**  
Include one or more real examples of input and the corresponding console output.

```python
my_function(57000, 60, 45, 60)
```

<details>
<summary><strong>Output</strong></summary>

```
Sample console output or report goes here.
```
</details>

---

**Interpretation**  
Explain how to interpret or apply the output in a practical context.

---

**Conclusion**  
Close with a summary of the purpose, main findings, or potential extensions of the script.

---

</details>

---
## Nombre Archivo: Todo_Entornos_Unificado_Completo.md
### Descripción general
Contiene la documentación técnica y práctica para la creación y administración de entornos virtuales Python en VSCode.  
Incluye guías paso a paso, scripts `.cmd`, notas avanzadas y versiones orientadas tanto a principiantes como a usuarios profesionales.  
Los documentos están ordenados desde los más completos e integradores hasta las versiones base o complementarias.

| Archivo | Descripción breve |
|----------|-------------------|
| README_Entorno_Python_VSCode.md | Guía unificada con pasos y soluciones. |
| README_Scripts_CMD.md |
| Readme_Entorno_VSCode_Unificado.md | Documento integral de configuración y scripts. |
| README_CMD_Entornos.md | Resumen de comandos y estructura de scripts. |
| Guia_scripts_CMD_entornos.ipynb | Guía práctica en Jupyter Notebook. |
| Entorno_virtual_VSCode_CMD_v6.ipynb | Guía de entorno en VSCode. |
| Extras_avanzados.md | Casos y configuraciones complejas. |
| Guia_completa_scripts_CMD_entornos.md | Resumen de comandos y estructura de scripts. |
| guia_scripts_entornos.md | Descripción general de scripts .cmd. |
| README_Entorno_VSCode_Structured.md | Versión estructurada de entorno en VSCode. |
| README_Entorno_VSCode_Original.md | Documento base con instrucciones. |
| README_profesional.md | Documento relacionado. |
| README_friendly.md | Documento relacionado. |

---
<details>

<summary>Nombre Archivo: README_Entorno_Python_VSCode.md</summary>

# 🐍 README — Entorno de Python en VS Code (Windows CMD)

¡Bienvenido! 👋  
Esta guía te acompaña paso a paso para crear, configurar y usar un **entorno virtual de Python (`.venv`)** en **VS Code usando Windows CMD**.  
Además, incluye scripts listos para automatizar tareas comunes y consejos para mantener tu entorno limpio y rápido.  

---

## ⚡ 1. Resumen rápido (Quickstart)

Si ya sabes lo básico, estos son los comandos esenciales 👇

```cmd
# 1️⃣ Ubícate en tu carpeta de proyecto
cd C:\ruta\de\tu\proyecto

# 2️⃣ Crea el entorno virtual
python -m venv .venv

# 3️⃣ Activa el entorno
.venv\Scripts\activate.bat

# 4️⃣ Desactivar el entorno
deactivate or .venv\Scripts\deactivate.bat

# 5️⃣ Instala dependencias (si tienes requirements.txt)
pip install -r requirements.txt

# 6️⃣ Abre VS Code con ese entorno activo
code .
```

---

## 🧱 2. Crear y configurar el entorno paso a paso

### 🔹 Abrir CMD y posicionarte en tu proyecto
```cmd
cd C:\Users\TuUsuario\Desktop\python
```

### 🔹 Verificar instalación de Python
```cmd
python --version
where python
```
Deberías ver rutas hacia tu instalación de Python.

### 🔹 Crear el entorno virtual
```cmd
python -m venv .venv
```

### 🔹 Activar el entorno
```cmd
.venv\Scripts\activate.bat
```
Si todo va bien, el prompt mostrará algo así:
```
(.venv) C:\Users\TuUsuario\Desktop\python>
```

### 🔹 Desactivar el entorno
```cmd
.venv\Scripts\deactivate.bat
```
```cmd
deactivate
```

### 🔹 Instalar dependencias
```cmd
pip install requests
```

---

## 🧩 3. Configurar correctamente VS Code

### Seleccionar el intérprete de Python
1. Presiona `Ctrl + Shift + P`
2. Escribe **Python: Select Interpreter**
3. Selecciona `.venv\Scripts\python.exe`  
   (si no aparece, usa *Enter Interpreter Path → Find...*)

### Cambiar la terminal por defecto a CMD
1. `Ctrl + Shift + P` → **Terminal: Select Default Profile**
2. Elige **Command Prompt (cmd)**
3. Cierra y reabre la terminal con `Ctrl + ñ`

### Verificar que VS Code usa el entorno correcto
```cmd
python --version
where python
```
Debería apuntar a:  
`.venv\Scripts\python.exe` ✅

---

## 🧯 4. Solución rápida de errores comunes

| Problema | Causa probable | Solución |
|-----------|----------------|-----------|
| `'python' no se reconoce` | Python no está en PATH | Reinstala y marca **Add Python to PATH** |
| PowerShell muestra errores | Estás usando la terminal equivocada | Cambia a **CMD** |
| `.venv` no existe | No se creó aún | Ejecuta `python -m venv .venv` |
| Dependencias no instaladas | Falta `requirements.txt` | Crea uno con `pip freeze > requirements.txt` |
| El analizador de VS Code da errores raros | Lenguaje desactualizado | `Python: Restart Language Server` o `Developer: Reload Window` |

---

## ⚙️ 5. Scripts CMD para automatizar tu entorno

Una vez que domines los pasos manuales, puedes usar estos **scripts .cmd** para hacerlo más rápido ⚡

| Script | Acción principal | Cuándo usarlo |
|--------|------------------|----------------|
| `setup_venv_from_requirements.cmd` | Crea y configura `.venv` desde `requirements.txt`. | Primera vez o al actualizar dependencias. |
| `reset_venv_from_requirements.cmd` | Elimina y recrea el entorno desde cero. | Si el entorno está roto o quieres empezar limpio. |
| `provision_and_open_venv.cmd` | Crea, instala y abre una terminal con `.venv` activo. | Para iniciar rápido y trabajar al instante. |
| `open_venv_here.cmd` | Abre una CMD con el entorno ya activado. | Si ya existe `.venv` y solo quieres usarlo. |

📁 **Ubícalos en la raíz del proyecto:**
```
mi_proyecto/
 ├─ .venv/
 ├─ requirements.txt
 ├─ setup_venv_from_requirements.cmd
 ├─ reset_venv_from_requirements.cmd
 ├─ provision_and_open_venv.cmd
 └─ open_venv_here.cmd
```

---

## 💡 6. Tips y buenas prácticas

- Un entorno por proyecto 💼  
- Mantén tu `requirements.txt` actualizado y versionado.  
- Usa `reset_venv_from_requirements.cmd` para limpiar conflictos de versiones.  
- Divide dependencias: `requirements.txt` (producción) y `requirements-dev.txt` (desarrollo).  
- Si trabajas en varios proyectos, puedes tener `.venv_api`, `.venv_test`, etc.

---

## 🧠 7. Conceptos clave rápidos

| Concepto | Descripción |
|-----------|-------------|
| **Entorno virtual (`.venv`)** | Espacio aislado con sus propias dependencias. |
| **Activar entorno** | `.venv\Scripts\activate.bat` |
| **Desactivar entorno** | `deactivate` o `.venv\Scripts\deactivate.bat` |
| **Instalar dependencias** | `pip install -r requirements.txt` |

---

## 🚀 8. Consejo final

Crea tus entornos siempre dentro del proyecto, mantenlos versionados con `requirements.txt`, y usa los scripts cuando quieras ahorrar tiempo.  
Así tendrás entornos **limpios, reproducibles y sin dolores de cabeza** 😄

---

🔗 **Documentación completa de los scripts CMD:**  
Consulta [README_Scripts_CMD.md](./README_Scripts_CMD.md)

---

© 2025 – Guía práctica unificada basada en documentación técnica y experiencia en VS Code + Python.

</details>

---
<details>

<summary>Nombre Archivo: README_Scripts_CMD.md</summary>

# ⚙️ README — Scripts CMD para entornos virtuales de Python

Bienvenido 👋  
Este documento explica en detalle cómo funcionan y cómo usar los **scripts CMD** que automatizan la creación y manejo de entornos virtuales de Python (`.venv`) en **Windows**.  
Están diseñados para funcionar perfectamente con **VS Code + CMD**, evitando configuraciones manuales repetitivas.

---

## 🚀 1. ¿Qué son estos scripts?

Son archivos `.cmd` (o `.bat`) que ejecutan automáticamente comandos de Python y `pip` desde la terminal de **Command Prompt (CMD)**.  
Te permiten crear, reiniciar o abrir tu entorno virtual en segundos ⚡

---

## 📂 2. Estructura recomendada del proyecto

```
mi_proyecto/
 ├─ .venv/
 ├─ requirements.txt
 ├─ scripts/
 │   ├─ setup_venv_from_requirements.cmd
 │   ├─ reset_venv_from_requirements.cmd
 │   ├─ provision_and_open_venv.cmd
 │   └─ open_venv_here.cmd
 ├─ README_Entorno_Python_VSCode.md
 └─ README_Scripts_CMD.md
```

> 💡 Consejo: guarda todos los scripts dentro de la carpeta `scripts/` o en la raíz, según prefieras.

---

## 🧩 3. Descripción de cada script

| Script | Acción principal | Cuándo usarlo |
|--------|------------------|----------------|
| `setup_venv_from_requirements.cmd` | Crea y configura el entorno desde `requirements.txt`. | Primera vez o al actualizar dependencias. |
| `reset_venv_from_requirements.cmd` | Borra y recrea el entorno desde cero. | Cuando el entorno está roto o quieres empezar limpio. |
| `provision_and_open_venv.cmd` | Crea el entorno (si no existe), instala dependencias y abre una terminal activa. | Cuando quieres empezar a trabajar rápido. |
| `open_venv_here.cmd` | Abre una CMD con el entorno ya activado. | Si el entorno ya existe y solo necesitas usarlo. |

---

## 🧱 4. Ejemplos de uso

Abre una terminal **CMD** dentro del proyecto y ejecuta:

```cmd
# Crear entorno e instalar dependencias
scripts\setup_venv_from_requirements.cmd

# Reiniciar el entorno desde cero
scripts\reset_venv_from_requirements.cmd

# Crear y abrir entorno activo automáticamente
scripts\provision_and_open_venv.cmd

# Abrir entorno ya existente
scripts\open_venv_here.cmd
```

> ⚠️ Asegúrate de ejecutar desde **CMD**, no PowerShell.  
> Si usas VS Code, cambia el perfil de terminal a **Command Prompt (cmd)**.

---

## 🧯 5. Solución de problemas comunes

| Problema | Causa probable | Solución |
|-----------|----------------|-----------|
| `python` no se reconoce | Python no está agregado al PATH. | Reinstala Python marcando **Add Python to PATH**. |
| Error “requirements.txt no encontrado” | El archivo no existe o está en otra ruta. | Crea uno con `pip freeze > requirements.txt` o muévelo a la raíz del proyecto. |
| No se crea `.venv` | El script no tiene permisos o hay error en Python. | Verifica que Python esté instalado correctamente y ejecuta el script como administrador. |
| PowerShell muestra errores de ejecución | Estás usando PowerShell. | Cambia a CMD desde *Terminal: Select Default Profile → Command Prompt*. |

---

## 🧠 6. Cómo personalizar los scripts

Puedes abrir cualquier `.cmd` con un editor de texto (como VS Code) y modificar rutas o comandos según tus necesidades.  
Por ejemplo, puedes cambiar el nombre del entorno:

```cmd
python -m venv .entorno_dev
```

O agregar instalación de paquetes personalizados:

```cmd
pip install -r requirements.txt
pip install black flake8 pytest
```

---

## 💡 7. Consejos avanzados

- Crea versiones separadas: `requirements.txt` (producción) y `requirements-dev.txt` (desarrollo).  
- Usa `reset_venv_from_requirements.cmd` para limpiar conflictos de dependencias.  
- Añade comentarios en tus scripts (`REM Este comando crea el entorno...`).  
- Puedes ejecutar un script con doble clic desde el Explorador de archivos.  

---

## 🧭 8. Recursos útiles

- 📘 Documentación oficial de Python: https://docs.python.org/3/library/venv.html  
- 📘 Documentación de VS Code (extensión de Python): https://code.visualstudio.com/docs/python/python-tutorial  
- 📘 Cómo usar CMD en Windows: https://learn.microsoft.com/es-es/windows-server/administration/windows-commands/cmd

---

🔙 **Volver a la guía principal:** [README_Entorno_Python_VSCode.md](./README_Entorno_Python_VSCode.md)

---

© 2025 – Guía técnica complementaria.  
Creada para acompañar al archivo **README_Entorno_Python_VSCode.md** y facilitar la automatización de entornos virtuales.

</details>

---
<details>

<summary>Nombre Archivo: Readme_Entorno_VSCode_Unificado.md</summary>

# README — Entorno Virtual en VS Code (Windows CMD)

## 1. Propósito
Guía práctica para crear y configurar un **entorno virtual de Python (`.venv`)** en **VS Code usando Windows CMD**.  
Aprenderás a:
- Crear, activar y desactivar un entorno virtual.  
- Instalar y administrar dependencias con `pip`.  
- Configurar VS Code para usar correctamente `.venv`.  
- Resolver errores comunes del analizador y la terminal.

---

## 2. Preparación del entorno

### Abrir CMD y ubicarse en el proyecto
```cmd
cd C:\Users\TuUsuario\Desktop\python
```

### Verificar instalación de Python
```cmd
python --version
where python
```
Deberías ver rutas hacia tu instalación de Python.  

---

## 3. Crear y activar el entorno virtual
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```

Si todo va bien, tu prompt mostrará:
```
(.venv) C:\Users\TuUsuario\Desktop\python>
```

---

## 4. Instalar dependencias dentro del entorno
Ejemplo:
```cmd
pip install requests
```

---

## 5. Comprobar que VS Code usa el entorno
```cmd
python --version
where python
```
Debe apuntar a:
```
.venv\Scripts\python.exe
```

---

## 6. Desactivar el entorno virtual

Cuando termines de trabajar, puedes **desactivar el entorno** de dos formas equivalentes:

**Opción 1 — Comando integrado de Python**
```cmd
deactivate
```

**Opción 2 — Script directo del entorno**
```cmd
.venv\Scripts\deactivate.bat
```

Tras esto, el prefijo `(.venv)` desaparecerá del prompt, indicando que volviste al entorno global.

---

## 7. Configurar VS Code

**Seleccionar el intérprete:**
- `Ctrl+Shift+P` → `Python: Select Interpreter`.
- Elige `.venv\Scripts\python.exe`.

**Cambiar terminal por defecto a CMD:**
- `Ctrl+Shift+P` → `Terminal: Select Default Profile`.
- Selecciona **Command Prompt (cmd)**.
- Cierra y reabre la terminal (`Ctrl+ñ`).

---

## 8. Solución de errores comunes

**Reiniciar analizador de Python:**
- `Ctrl+Shift+P` → `Python: Restart Language Server`.
- O `Ctrl+Shift+P` → `Developer: Reload Window`.

**Reiniciar la terminal:**
- Cierra con 🗑️ → abre una nueva → reactiva el entorno:
  ```cmd
  .venv\Scripts\activate.bat
  ```

**Forzar selección manual del intérprete:**
1. `Ctrl+Shift+P` → `Python: Select Interpreter`
2. `Enter Interpreter Path` → `Find...`
3. Busca:
   ```
   C:\Users\TuUsuario\Desktop\python\.venv\Scripts\python.exe
   ```

---

## 9. Notas rápidas
- Los bloques de código están pensados para **CMD**, no para celdas de Python.  
- Si ves el error *ExecutionPolicy*, estás en PowerShell: cambia la terminal a CMD.  
- `.venv` se guarda localmente y no debe subirse a GitHub.  

</details>

---
<details>

<summary>Nombre Archivo: README_CMD_Entornos.md</summary>

# ⚙️ Scripts CMD para entornos virtuales de Python en Windows (VS Code + CMD)

Esta guía práctica reúne los **4 scripts principales** para crear, resetear y abrir entornos virtuales en Windows, junto con consejos avanzados para su uso en **VS Code**.

---

## 🚀 Scripts incluidos

| Script | Acción principal | Cuándo usarlo |
|--------|------------------|----------------|
| `setup_venv_from_requirements.cmd` | Crea y configura el entorno desde `requirements.txt`. | Primera vez o al actualizar dependencias. |
| `reset_venv_from_requirements.cmd` | Borra y recrea el entorno desde cero. | Cuando el entorno está roto o quieres empezar limpio. |
| `provision_and_open_venv.cmd` | Provisiona y deja la terminal abierta con `.venv` activo. | Para iniciar rápido y trabajar al instante. |
| `open_venv_here.cmd` | Abre una CMD con el entorno ya activado. | Si ya existe `.venv` y solo quieres usarlo. |

---

## ✅ Requisitos previos

- **Python 3.x** instalado y agregado al **PATH**.  
- Ejecutar siempre desde **CMD**, no PowerShell.  
- (Opcional) `requirements.txt` en la raíz del proyecto.  
- VS Code con la extensión oficial de Python.

---

## 📂 Estructura recomendada del proyecto

```
mi_proyecto/
 ├─ .venv/
 ├─ requirements.txt
 ├─ setup_venv_from_requirements.cmd
 ├─ reset_venv_from_requirements.cmd
 ├─ provision_and_open_venv.cmd
 └─ open_venv_here.cmd
```

---

## 🧠 Conceptos clave

- **Entorno virtual (`.venv`)** → Espacio aislado de dependencias.  
- **Activar entorno** → `.venv\Scripts\activate.bat`  
- **Instalar paquetes** → `pip install -r requirements.txt`  
- **Desactivar** → `deactivate` o `.venv\Scripts\deactivate.bat`

---

## 🧭 Uso rápido

| Situación | Script sugerido |
|------------|----------------|
| Primera instalación | `setup_venv_from_requirements.cmd` |
| Entorno roto o desactualizado | `reset_venv_from_requirements.cmd` |
| Quiero trabajar ahora mismo | `provision_and_open_venv.cmd` |
| Solo abrir el entorno | `open_venv_here.cmd` |

---

## 🧯 Solución rápida de errores

| Problema | Causa posible | Solución |
|-----------|----------------|-----------|
| `'python' no se reconoce` | Python no está en PATH | Reinstala marcando **Add Python to PATH** |
| PowerShell muestra errores | Terminal incorrecta | Cambia a **CMD** desde *Terminal: Select Default Profile* |
| `.venv` no existe | No fue creado aún | Ejecuta `setup_venv_from_requirements.cmd` |
| Dependencias no instaladas | Falta `requirements.txt` | Crea con `pip freeze > requirements.txt` |

---

## 🧩 Integración con VS Code

1. `Ctrl+Shift+P` → **Python: Select Interpreter**  
   → Selecciona `.venv\Scripts\python.exe`.  
2. Si no aparece, usa **Enter Interpreter Path → Find...**  
3. Cambia terminal a **Command Prompt (CMD)** si ves errores PowerShell.  
4. Para refrescar dependencias:  
   - `Python: Restart Language Server` o  
   - `Developer: Reload Window`.

---

## 🧠 Tips avanzados

- Puedes mantener **varios entornos** (`.venvA`, `.venvB`) para pruebas.  
- Divide dependencias (`requirements.txt` y `requirements-dev.txt`).  
- Usa `reset_venv_from_requirements.cmd` para limpiar conflictos de versiones.

---

💡 **Consejo final:**  
Un entorno por proyecto, `requirements.txt` versionado, y scripts siempre en la raíz.  
Con estos comandos tendrás entornos limpios, reproducibles y fáciles de usar.

---

© 2025 – Documentación técnica unificada basada en *README friendly + profesional + guías completas*.

</details>

---
<details>

<summary>Nombre Archivo: Guia_scripts_CMD_entornos.ipynb</summary>

# Conversión de Guia_scripts_CMD_entornos.ipynb

# Gestión completa de entornos virtuales con **scripts .cmd** (Windows / CMD)

Este cuaderno explica, paso a paso, **cómo usar cuatro scripts .cmd** para crear, resetear, provisionar y abrir entornos virtuales de Python en Windows (CMD).

> **Requisitos previos**
> - Tener **Python 3.x** instalado y agregado al **PATH** (que `python --version` funcione en CMD).
> - Trabajar en **CMD (Símbolo del sistema)**, no PowerShell.
> - Coloca los scripts en la **raíz** de tu proyecto (junto a `.venv` y `requirements.txt`).


## Estructura recomendada del proyecto
```
mi_proyecto/
 ├─ .venv/                 (carpeta del entorno virtual; puede no existir aún)
 ├─ requirements.txt       (opcional, recomendado)
 ├─ setup_venv_from_requirements.cmd
 ├─ reset_venv_from_requirements.cmd
 ├─ provision_and_open_venv.cmd
 └─ open_venv_here.cmd
```


## Conceptos clave (rápido)
- **Entorno virtual**: carpeta aislada con las librerías del proyecto.
- **Activar el entorno**: hace que `python` y `pip` apunten al Python de `.venv`.
- **`requirements.txt`**: lista las dependencias del proyecto.
- **CMD vs PowerShell**: aquí usamos **CMD**. Si VS Code abre PowerShell, cambia el perfil a **Command Prompt (cmd)**.


# 1) `setup_venv_from_requirements.cmd` — Provisionar el entorno desde `requirements.txt`

### ¿Qué hace?
- Crea `.venv` si no existe.
- Activa **temporalmente** el entorno dentro del script.
- Actualiza `pip`.
- Instala dependencias desde `requirements.txt` (si existe).
- Muestra versión/ruta de Python y paquetes.
- **No** deja el entorno activado al terminar.

### ¿Cuándo usarlo?
- Primera vez en una PC.
- Cuando recibes/actualizas `requirements.txt` y quieres instalar todo.

### Cómo usarlo (CMD)


```cmd
cd C:\\Users\\TU\\Desktop\\mi_proyecto
setup_venv_from_requirements.cmd

REM Al terminar, activa el entorno para trabajar:
.venv\\Scripts\\activate.bat
```


# 2) `reset_venv_from_requirements.cmd` — Borrar y recrear el entorno (con confirmación)

### ¿Qué hace?
- Pregunta si quieres **borrar y recrear** `.venv`.
- Si confirmas:
  - Elimina `.venv`.
  - Crea uno nuevo.
  - Activa, actualiza `pip` e instala desde `requirements.txt` (si existe).
  - Deja la ventana abierta con el entorno **activo**.

### ¿Cuándo usarlo?
- Si el entorno está roto o con conflictos.
- Si quieres empezar **desde cero**.

### Cómo usarlo (CMD)
```cmd
cd C:\\Users\\TU\\Desktop\\mi_proyecto
reset_venv_from_requirements.cmd
```


# 3) `provision_and_open_venv.cmd` — Provisionar y **quedarte** con `.venv` activo

### ¿Qué hace?
- Crea `.venv` si no existe.
- Activa el entorno.
- Actualiza `pip`.
- Instala desde `requirements.txt` si existe.
- **Deja la terminal abierta** con el entorno activo.

### ¿Cuándo usarlo?
- Quieres un **todo-en-uno** para empezar a trabajar ya.

### Cómo usarlo (CMD)
```cmd
cd C:\\Users\\TU\\Desktop\\mi_proyecto
provision_and_open_venv.cmd
```


# 4) `open_venv_here.cmd` — Abrir CMD con `.venv` **ya activado**

### ¿Qué hace?
- No crea ni instala nada.
- Abre una CMD con el entorno **activado** (si `.venv` existe).

### ¿Cuándo usarlo?
- Ya tienes `.venv` y quieres **abrirlo rápido** para trabajar.

### Cómo usarlo
- Doble clic sobre `open_venv_here.cmd`, **o**:
```cmd
cd C:\\Users\\TU\\Desktop\\mi_proyecto
open_venv_here.cmd
```


## Verificación (después de cualquier script)
En CMD con `.venv` activo deberías ver el prefijo `(.venv)` y estos comandos deben responder correctamente:
```cmd
python --version
where python
pip list
```
En un **notebook** dentro de VS Code, prueba:
```python
import sys
sys.executable
```
Debería apuntar a `...\\.venv\\Scripts\\python.exe`.


## Solución de problemas (FAQ)

**`'python' no se reconoce`**
- Reinstala Python marcando **Add Python to PATH**. Abre un CMD nuevo.

**No aparece `.venv` en VS Code o no usa mi entorno**
- `Ctrl+Shift+P` → *Python: Select Interpreter* → selecciona `...\\.venv\\Scripts\\python.exe`.
- `Ctrl+Shift+P` → *Python: Restart Language Server* o *Developer: Reload Window*.
- Cierra y vuelve a abrir la **terminal integrada** (`Ctrl+ñ`).

**Error al borrar `.venv` en el script de reset**
- Cierra VS Code y cualquier terminal que esté usando `.venv`.
- Intenta de nuevo; si persiste, reinicia Windows.

**No tengo `requirements.txt`**
- Puedes generarlo con:
```cmd
pip freeze > requirements.txt
```
o escribirlo a mano con los paquetes principales.

**Sigue sin reconocer paquetes en VS Code**
- Verifica en la barra de estado: `Python 3.x ('.venv': venv)`.
- Asegúrate de haber abierto la **carpeta** del proyecto (no solo archivos sueltos).


## Extras útiles
- **Crear `requirements.txt` del entorno actual**:
```cmd
pip freeze > requirements.txt
```
- **Instalar desde `requirements.txt`** en un entorno nuevo:
```cmd
python -m venv .venv
.venv\\Scripts\\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
```
- **Anclar CMD al entorno** (alternativa manual):
```cmd
.venv\\Scripts\\activate.bat
```



</details>

---
<details>

<summary>Nombre Archivo: Entorno_virtual_VSCode_CMD_v6.ipynb</summary>

# Conversión de Entorno_virtual_VSCode_CMD_v6.ipynb

# Guía de entornos virtuales (CMD)


# Extra: Gestionar **varios entornos** en VS Code

Cuando trabajas con múltiples proyectos, crea **un entorno por proyecto** para evitar conflictos de versiones.

## 1) Crear un entorno por proyecto (CMD)
En cada carpeta de proyecto ejecuta:

```cmd
python -m venv .venv
.venv\Scripts\activate.bat
```
Opcional: usa nombres descriptivos si manejas muchos entornos:
```cmd
python -m venv .venv_django
python -m venv .venv_flask
```

## 2) Seleccionar el intérprete correcto en VS Code
Con la carpeta del proyecto abierta:
1. `Ctrl+Shift+P` → **Python: Select Interpreter**.
2. Elige el que apunte a `.<entorno>\Scripts\python.exe`.
3. VS Code guardará la selección en `.vscode/settings.json` de ese proyecto.

## 3) Cambiar entre proyectos
- Al abrir **proyecto1**, verás algo como `Python 3.x ('.venv': venv)` abajo a la derecha.
- Al abrir **proyecto2**, se actualizará automáticamente al `.venv` de ese proyecto.

## 4) Verificar el entorno activo
En la **terminal integrada** debería verse el prefijo del entorno:
```
(.venv) C:\Users\TuUsuario\Desktop\proyecto1>
```
Y en la barra de estado (abajo derecha):
`Python 3.x ('.venv': venv)` o el nombre que le hayas dado (p. ej. `.venv_django`).

## 5) Buenas prácticas
- Mantén un `requirements.txt` por proyecto:
  ```cmd
  pip freeze > requirements.txt
  ```
  Para recrear el entorno en otra máquina:
  ```cmd
  pip install -r requirements.txt
  ```
- No mezcles dependencias de proyectos: instala siempre dentro del entorno correspondiente.
- Si cambias mucho de entorno, considera nombres distintivos para reconocerlos rápido (`.venv_api`, `.venv_data`, etc.).

## 6) Trucos útiles
- **Forzar selección manual** si el `.venv` no aparece:
  `Ctrl+Shift+P` → *Python: Select Interpreter* → *Enter Interpreter Path* → *Find...* → selecciona `.<entorno>\Scripts\python.exe`.
- **Reiniciar analizador / terminal** si no reconoce paquetes:
  `Ctrl+Shift+P` → *Python: Restart Language Server* o *Developer: Reload Window*.
  Cierra y reabre la terminal integrada (`Ctrl+ñ`).


# Extra: `requirements.txt` y recrear entornos desde cero (CMD)

## 1) Crear `requirements.txt` del proyecto actual
Con tu entorno activo `(.venv)` ejecuta en **CMD**:
```cmd
pip freeze > requirements.txt
```
Esto genera un listado **exacto** de versiones usadas por tu proyecto.

## 2) Instalar desde `requirements.txt` en un entorno nuevo
En una carpeta vacía o en el mismo proyecto (tras crear un `.venv` nuevo):
```cmd
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 3) Recomendaciones de versionado
- **Producción/reproducibilidad:** usa versiones fijas (p. ej. `flask==3.0.3`).
- **Desarrollo flexible:** puedes permitir rangos (`flask>=3.0,<4`).
- Antes de publicar el `requirements.txt`, considera **limpiarlo** (quitar paquetes que no necesitas).

## 4) Script CMD para recrear el entorno automáticamente
Crea un archivo `setup_venv_from_requirements.cmd` y pégale esto:
```cmd
@echo off
setlocal enableextensions enabledelayedexpansion
REM Ruta del entorno (por defecto .venv)
set VENV_DIR=.venv

if not exist "%VENV_DIR%" (
  echo [*] Creando entorno virtual en %VENV_DIR%
  python -m venv %VENV_DIR%
)

echo [*] Activando entorno
call %VENV_DIR%\Scripts\activate.bat

echo [*] Actualizando pip
python -m pip install --upgrade pip

if exist requirements.txt (
  echo [*] Instalando dependencias desde requirements.txt
  pip install -r requirements.txt
) else (
  echo [!] No se encontro requirements.txt en el directorio actual
)

echo [*] Listo. Entorno activo en %VENV_DIR%
python --version
where python
pip list
endlocal
```
Guárdalo en la **raíz de tu proyecto** y ejecútalo con doble clic o desde CMD:
```cmd
setup_venv_from_requirements.cmd
```

## 5) Plantilla básica de `requirements.txt`
Ejemplo mínimo (ajústalo a tu proyecto):
```
flask==3.0.3
pandas==2.2.3
reportlab==4.4.4
pillow==11.3.0
tzdata==2025.2
```

## 6) Exportar solo lo necesario
Si `pip freeze` genera demasiadas dependencias, puedes **escribir manualmente** un `requirements.in` con tus paquetes principales y luego usar herramientas como `pip-tools` (opcional) para compilarlo a `requirements.txt`. Para mantenerlo simple, puedes empezar editándolo a mano.


---
# ANEXO: Guía completa de scripts `.cmd` para gestionar entornos
A continuación se incluye, íntegramente, la guía detallada para usar los 4 scripts `.cmd` (`setup_venv_from_requirements.cmd`, `reset_venv_from_requirements.cmd`, `provision_and_open_venv.cmd`, `open_venv_here.cmd`).


# Gestión completa de entornos virtuales con **scripts .cmd** (Windows / CMD)

Este cuaderno explica, paso a paso, **cómo usar cuatro scripts .cmd** para crear, resetear, provisionar y abrir entornos virtuales de Python en Windows (CMD).

> **Requisitos previos**
> - Tener **Python 3.x** instalado y agregado al **PATH** (que `python --version` funcione en CMD).
> - Trabajar en **CMD (Símbolo del sistema)**, no PowerShell.
> - Coloca los scripts en la **raíz** de tu proyecto (junto a `.venv` y `requirements.txt`).


## Estructura recomendada del proyecto
```
mi_proyecto/
 ├─ .venv/                 (carpeta del entorno virtual; puede no existir aún)
 ├─ requirements.txt       (opcional, recomendado)
 ├─ setup_venv_from_requirements.cmd
 ├─ reset_venv_from_requirements.cmd
 ├─ provision_and_open_venv.cmd
 └─ open_venv_here.cmd
```


## Conceptos clave (rápido)
- **Entorno virtual**: carpeta aislada con las librerías del proyecto.
- **Activar el entorno**: hace que `python` y `pip` apunten al Python de `.venv`.
- **`requirements.txt`**: lista las dependencias del proyecto.
- **CMD vs PowerShell**: aquí usamos **CMD**. Si VS Code abre PowerShell, cambia el perfil a **Command Prompt (cmd)**.


# 1) `setup_venv_from_requirements.cmd` — Provisionar el entorno desde `requirements.txt`

### ¿Qué hace?
- Crea `.venv` si no existe.
- Activa **temporalmente** el entorno dentro del script.
- Actualiza `pip`.
- Instala dependencias desde `requirements.txt` (si existe).
- Muestra versión/ruta de Python y paquetes.
- **No** deja el entorno activado al terminar.

### ¿Cuándo usarlo?
- Primera vez en una PC.
- Cuando recibes/actualizas `requirements.txt` y quieres instalar todo.

### Cómo usarlo (CMD)


```cmd
cd C:\\Users\\TU\\Desktop\\mi_proyecto
setup_venv_from_requirements.cmd

REM Al terminar, activa el entorno para trabajar:
.venv\\Scripts\\activate.bat
```


# 2) `reset_venv_from_requirements.cmd` — Borrar y recrear el entorno (con confirmación)

### ¿Qué hace?
- Pregunta si quieres **borrar y recrear** `.venv`.
- Si confirmas:
  - Elimina `.venv`.
  - Crea uno nuevo.
  - Activa, actualiza `pip` e instala desde `requirements.txt` (si existe).
  - Deja la ventana abierta con el entorno **activo**.

### ¿Cuándo usarlo?
- Si el entorno está roto o con conflictos.
- Si quieres empezar **desde cero**.

### Cómo usarlo (CMD)
```cmd
cd C:\\Users\\TU\\Desktop\\mi_proyecto
reset_venv_from_requirements.cmd
```


# 3) `provision_and_open_venv.cmd` — Provisionar y **quedarte** con `.venv` activo

### ¿Qué hace?
- Crea `.venv` si no existe.
- Activa el entorno.
- Actualiza `pip`.
- Instala desde `requirements.txt` si existe.
- **Deja la terminal abierta** con el entorno activo.

### ¿Cuándo usarlo?
- Quieres un **todo-en-uno** para empezar a trabajar ya.

### Cómo usarlo (CMD)
```cmd
cd C:\\Users\\TU\\Desktop\\mi_proyecto
provision_and_open_venv.cmd
```


# 4) `open_venv_here.cmd` — Abrir CMD con `.venv` **ya activado**

### ¿Qué hace?
- No crea ni instala nada.
- Abre una CMD con el entorno **activado** (si `.venv` existe).

### ¿Cuándo usarlo?
- Ya tienes `.venv` y quieres **abrirlo rápido** para trabajar.

### Cómo usarlo
- Doble clic sobre `open_venv_here.cmd`, **o**:
```cmd
cd C:\\Users\\TU\\Desktop\\mi_proyecto
open_venv_here.cmd
```


## Verificación (después de cualquier script)
En CMD con `.venv` activo deberías ver el prefijo `(.venv)` y estos comandos deben responder correctamente:
```cmd
python --version
where python
pip list
```
En un **notebook** dentro de VS Code, prueba:
```python
import sys
sys.executable
```
Debería apuntar a `...\\.venv\\Scripts\\python.exe`.


## Solución de problemas (FAQ)

**`'python' no se reconoce`**
- Reinstala Python marcando **Add Python to PATH**. Abre un CMD nuevo.

**No aparece `.venv` en VS Code o no usa mi entorno**
- `Ctrl+Shift+P` → *Python: Select Interpreter* → selecciona `...\\.venv\\Scripts\\python.exe`.
- `Ctrl+Shift+P` → *Python: Restart Language Server* o *Developer: Reload Window*.
- Cierra y vuelve a abrir la **terminal integrada** (`Ctrl+ñ`).

**Error al borrar `.venv` en el script de reset**
- Cierra VS Code y cualquier terminal que esté usando `.venv`.
- Intenta de nuevo; si persiste, reinicia Windows.

**No tengo `requirements.txt`**
- Puedes generarlo con:
```cmd
pip freeze > requirements.txt
```
o escribirlo a mano con los paquetes principales.

**Sigue sin reconocer paquetes en VS Code**
- Verifica en la barra de estado: `Python 3.x ('.venv': venv)`.
- Asegúrate de haber abierto la **carpeta** del proyecto (no solo archivos sueltos).


## Extras útiles
- **Crear `requirements.txt` del entorno actual**:
```cmd
pip freeze > requirements.txt
```
- **Instalar desde `requirements.txt`** en un entorno nuevo:
```cmd
python -m venv .venv
.venv\\Scripts\\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
```
- **Anclar CMD al entorno** (alternativa manual):
```cmd
.venv\\Scripts\\activate.bat
```



</details>

---
<details>

<summary>Nombre Archivo: Extras_avanzados.md</summary>

# 🛠️ Extras avanzados para entornos virtuales en VS Code (CMD)

Este documento complementa la **Guía completa** y el **README** con consejos útiles que estaban en el cuaderno `.ipynb`.

---

## 🚀 1. Varios entornos en un mismo proyecto

En algunos casos puedes necesitar más de un entorno virtual para el mismo proyecto (ejemplo: probar distintas versiones de dependencias).

```cmd
python -m venv .venv_proyA
python -m venv .venv_proyB
```

Activa el que quieras en cada momento:

```cmd
.venv_proyA\Scripts\activate.bat
```

✅ Útil para aislar configuraciones o librerías entre pruebas.

---

## 📦 2. Estrategias con `requirements.txt`

Se recomienda dividir dependencias según el uso:

- **Producción** → solo librerías necesarias para ejecutar la app.  
- **Desarrollo** → incluye herramientas extra (tests, linters, formateadores, etc.).

Ejemplo:

```
# requirements.txt
flask==3.0.0
requests==2.32.0

# requirements-dev.txt
-r requirements.txt
pytest==8.3.0
black==24.4.0
```

Instalación rápida:

```cmd
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

---

## ⚙️ 3. Script “todo en uno” (ejemplo)

Un archivo `.cmd` que:

1. Crea el entorno si no existe.  
2. Lo activa.  
3. Instala dependencias desde `requirements.txt` (si está presente).  
4. Deja el entorno listo para usar.

```cmd
@echo off
if not exist .venv (
    echo Creando entorno virtual...
    python -m venv .venv
)
call .venv\Scripts\activate.bat
if exist requirements.txt (
    echo Instalando dependencias...
    pip install -r requirements.txt
)
echo Entorno activado y listo.
```

✅ Así puedes provisionar y activar tu entorno en un solo paso.

---

## 📌 Nota final

- Usa este documento solo como **referencia avanzada**.  
- Para los comandos básicos (crear, activar, desactivar, seleccionar intérprete en VS Code), consulta el **README**.  
- Para flujos completos y resolución de problemas, revisa la **Guía completa**.

---


</details>

---
<details>

<summary>Nombre Archivo: Guia_completa_scripts_CMD_entornos.md</summary>


# Guía completa de los scripts `.cmd` para gestionar entornos virtuales (Windows, CMD)

Esta guía te explica **qué hace cada script**, **cuándo usarlo**, **cómo ejecutarlo**, **qué deberías ver** y **cómo resolver errores típicos**.
Está pensada para quien **no tiene experiencia previa** con entornos virtuales o con CMD.

> **Requisitos previos (importante):**
> - Tener instalado **Python 3.x** en Windows.
> - Python debe estar en el **PATH** (de modo que `python --version` funcione en CMD).
> - Tu proyecto debe estar en una carpeta, p. ej. `C:\Users\TU\Desktop\mi_proyecto`.
> - (Opcional) Un archivo `requirements.txt` en la raíz del proyecto con tus dependencias.
> - **Usaremos CMD (Símbolo del sistema)**, no PowerShell.

---

## 📂 Dónde colocar los scripts

Copia los 4 archivos `.cmd` en la **raíz del proyecto**, es decir, en la misma carpeta donde estará tu carpeta `.venv` y tu `requirements.txt` (si lo usas).

Ejemplo de estructura:
```
mi_proyecto/
 ├─ .venv/                 (carpeta del entorno virtual; puede no existir aún)
 ├─ requirements.txt       (opcional pero recomendado)
 ├─ setup_venv_from_requirements.cmd
 ├─ reset_venv_from_requirements.cmd
 ├─ provision_and_open_venv.cmd
 └─ open_venv_here.cmd
```

---

## 🧠 Conceptos rápidos (para situarte)

- **Entorno virtual (`.venv`)**: una “carpeta aislada” donde se instalan las librerías de **ese proyecto** sin afectar a todo el sistema.
- **Activar el entorno**: hace que los comandos `python` y `pip` usen el Python de `.venv` y no el del sistema.
- **`requirements.txt`**: lista de dependencias que tu proyecto necesita.
- **CMD vs PowerShell**: aquí **usaremos CMD**. Si se abre PowerShell por defecto en VS Code, cambia el perfil a **Command Prompt (cmd)**.

---

# 1) `setup_venv_from_requirements.cmd` — **Provisionar** (crear/actualizar) el entorno desde `requirements.txt`

### ¿Qué hace?
- Si **no existe** `.venv`, lo **crea**.
- **Activa temporalmente** el entorno **dentro del script**.
- **Actualiza `pip`**.
- Si encuentra `requirements.txt`, **instala** todas las dependencias listadas.
- Muestra la **versión de Python, la ruta** y el **listado de paquetes**.
- **No deja** el entorno activado cuando termina (cierra su sesión).

### ¿Cuándo usarlo?
- Primera vez que montas el proyecto en esta PC.
- Cuando alguien te pasó `requirements.txt` y necesitas instalar rápido todo.
- Cuando actualizaste `requirements.txt` y quieres **refrescar dependencias**.

### ¿Cómo usarlo?
1. Abre **CMD** en la carpeta del proyecto:  
   `cd C:\Users\TU\Desktop\mi_proyecto`
2. Ejecuta:  
   `setup_venv_from_requirements.cmd`
3. Al terminar, **activa el entorno para trabajar**:  
   `.venv\Scripts\activate.bat`

### ¿Qué debería ver?
- Mensajes tipo: “Creando entorno…”, “Actualizando pip…”, “Instalando dependencias…”.  
- Al final, salidas de `python --version`, `where python` y `pip list`.

### Errores típicos y soluciones
- **`'python' no se reconoce`** → Python no está en PATH. Reinstala Python marcando “Add python to PATH” o abre un CMD nuevo.
- **No hay `requirements.txt`** → El script seguirá pero mostrará aviso. Puedes crearlo con `pip freeze > requirements.txt` desde el entorno correcto.
- **Cortafuegos/Antivirus bloquea** → Permite Python temporalmente.
- **Rutas con espacios** → No hay problema si ejecutas desde la carpeta correcta (el script usa rutas relativas).

---

# 2) `reset_venv_from_requirements.cmd` — **Borrar y recrear** el entorno desde cero (con confirmación)

### ¿Qué hace?
- Te pregunta: “¿Quieres borrar y recrear el entorno .venv? (S/N)”.
- Si dices **S**:
  - **Elimina** la carpeta `.venv`.
  - **Crea** un **.venv nuevo**.
  - **Activa el entorno**, **actualiza pip** e **instala** dependencias desde `requirements.txt` si existe.
  - Deja **abierta** la ventana CMD con el entorno activo (lista para usar).
- Si dices **N**, cancela sin cambios.

### ¿Cuándo usarlo?
- Cuando tu entorno “se rompió” o tienes conflictos de versiones.
- Cuando quieres **empezar fresco** (clean slate) sin restos.
- Cuando cambiaste de versión de Python y quieres regenerar el entorno.

### ¿Cómo usarlo?
1. Abre CMD en la carpeta del proyecto.
2. Ejecuta: `reset_venv_from_requirements.cmd`
3. Responde **S** si estás seguro.
4. Se quedará **listo y activado** al terminar.

### ¿Qué debería ver?
- Mensajes de borrado/creación e instalación.
- Prompt con prefijo `(.venv)` al final.

### Errores típicos
- **`El proceso no puede acceder al archivo`** (archivos “en uso”):
  - Cierra VS Code y cualquier terminal que esté usando `.venv` y vuelve a intentar.
- **No hay `requirements.txt`**:
  - No pasa nada, el entorno queda vacío. Instala luego con `pip install ...` y después crea `requirements.txt`.
- **Permisos**:
  - Ejecuta CMD como **Administrador** si obtienes errores de acceso al borrar carpetas.

---

# 3) `provision_and_open_venv.cmd` — Provisionar **y** dejar la ventana abierta con `.venv` activo

### ¿Qué hace?
- Si **no existe** `.venv`, lo **crea**.
- **Activa** `.venv`.
- **Actualiza `pip`**.
- Si hay `requirements.txt`, **instala** los paquetes.
- **Deja la terminal abierta** con el entorno activado (ideal para empezar a trabajar ya).

### ¿Cuándo usarlo?
- Cuando quieres un **todo-en-uno**: provisionar (si hace falta) y **quedarte dentro del entorno** para trabajar sin pasos extras.

### ¿Cómo usarlo?
1. CMD en la carpeta del proyecto.
2. Ejecuta: `provision_and_open_venv.cmd`
3. Al terminar, verás `(.venv)` y podrás correr tus comandos.

### Errores típicos
- Iguales a los de `setup_venv_from_requirements.cmd`.
- Si `requirements.txt` falta, simplemente avisa y deja el entorno activo (puedes instalar manualmente).

---

# 4) `open_venv_here.cmd` — Abrir una CMD **ya activada** en `.venv`

### ¿Qué hace?
- **No crea** ni instala nada.
- Abre una ventana CMD **con el entorno `.venv` activado** (si `.venv` existe).

### ¿Cuándo usarlo?
- Cuando **ya tienes** el entorno creado y solo quieres **empezar a trabajar ya** sin recordar el comando de activación.
- Es el **atajo más rápido** para “abrir el entorno”.

### ¿Cómo usarlo?
- Doble clic sobre `open_venv_here.cmd`
- O desde CMD: `open_venv_here.cmd`

### ¿Qué debería ver?
- Una terminal nueva con el prompt:
  ```
  (.venv) C:\Users\TU\Desktop\mi_proyecto>
  ```

### Errores típicos
- **`No existe el entorno .venv en este directorio`**:
  - Primero ejecuta `setup_venv_from_requirements.cmd` o `provision_and_open_venv.cmd` para crearlo; o créalo manualmente:  
    `python -m venv .venv`

---

## ✅ Checklist rápido (para saber que todo está bien)

1. En la terminal, **ves `(.venv)`** al inicio de la línea.
2. `where python` muestra primero la ruta dentro de `.venv\Scripts\python.exe`.
3. `pip list` muestra tus paquetes esperados.
4. En VS Code, la barra de estado dice algo como:  
   `Python 3.x ('.venv': venv)`  
   y el **Kernel** del notebook usa tu `.venv`.

---

## 🧯 Solución de problemas (FAQ)

**Q1. Ejecuté un script y no pasó nada, o la ventana se cerró muy rápido.**  
- Ejecuta el `.cmd` desde una **ventana de CMD abierta** en la carpeta del proyecto para ver los mensajes.  
- Verifica permisos del sistema/antivirus.

**Q2. `python` no se reconoce.**  
- Reinstala Python marcando “Add Python to PATH”. Abre **una nueva** ventana de CMD.

**Q3. VS Code usa otro Python y no mi `.venv`.**  
- `Ctrl+Shift+P` → *Python: Select Interpreter* → elige `.<tu_venv>\Scripts\python.exe`.  
- Reinicia el **Language Server** o la ventana (`Developer: Reload Window`).

**Q4. Error al borrar `.venv` en `reset_venv_from_requirements.cmd`.**  
- Cierra todas las terminales/VS Code que lo usen. Si persiste, reinicia Windows o borra manualmente la carpeta cuando no esté en uso.

**Q5. `requirements.txt` no existe o tiene demasiadas cosas.**  
- Puedes generarlo con `pip freeze > requirements.txt`.
- O escribirlo a mano con sólo lo necesario (ej.: `flask==3.0.3`).

**Q6. ¿Puedo usar estos scripts si el proyecto está en otra ruta o con espacios?**  
- Sí. Los scripts trabajan desde su **directorio actual**. Abre CMD en la carpeta del proyecto o haz doble clic desde ahí.

**Q7. ¿Y si quiero borrar y recrear con otra versión de Python?**  
- Instala/selecciona la versión que quieras como `python` por defecto en PATH. El script usará ese `python` para crear el `.venv` nuevo.

---

## 🧪 Comandos de verificación útiles (después de usar cualquier script)

En **CMD** (con `.venv` activo, excepto donde se diga lo contrario):

```cmd
python --version
where python
pip list
```

En un **notebook** (`.ipynb`) dentro de VS Code, ejecuta:
```python
import sys
sys.executable
```

Deberías ver la ruta hacia `...\.venv\Scripts\python.exe`.

---

## 📌 Recomendaciones finales

- Un **entorno por proyecto**.
- Guarda y versiona tu `requirements.txt`.
- Si algo se rompe, usa el **reset** con confirmación y reinstala desde `requirements.txt`.
- En VS Code, **selecciona el intérprete** correcto y, si hace falta, **reinicia el analizador** y la **terminal integrada**.

---

### ¡Listo!
Con estos 4 scripts puedes crear, resetear, provisionar y abrir entornos rápidamente, incluso si no recuerdas los comandos manuales.


</details>

---
<details>

<summary>Nombre Archivo: guia_scripts_entornos.md</summary>

# Guía completa de los scripts `.cmd` para gestionar entornos virtuales (Windows, CMD)

Esta guía explica **qué hace cada script**, **cuándo usarlo**, **cómo ejecutarlo**, **qué deberías ver** y **cómo resolver errores típicos**.  
Pensada para quien no tiene experiencia previa con entornos virtuales o con CMD.

---

## 📑 Tabla de contenidos

- [Requisitos previos](#-requisitos-previos)
- [Dónde colocar los scripts](#-dónde-colocar-los-scripts)
- [Conceptos rápidos](#-conceptos-rápidos)
- [Scripts detallados](#-scripts-detallados)
  - [setup_venv_from_requirements.cmd](#1-setup_venv_from_requirementscmd)
  - [reset_venv_from_requirements.cmd](#2-reset_venv_from_requirementscmd)
  - [provision_and_open_venv.cmd](#3-provision_and_open_venvcmd)
  - [open_venv_here.cmd](#4-open_venv_herecmd)
- [Qué script usar según el caso](#-qué-script-usar-según-el-caso)

---

## 📌 Requisitos previos

- Python 3.x instalado en Windows.  
- Python en el **PATH** (`python --version` debe funcionar en CMD).  
- Proyecto en una carpeta, p. ej.: `C:\Users\TU\Desktop\mi_proyecto`.  
- Opcional: un archivo `requirements.txt` en la raíz.  
- Usaremos **CMD (Símbolo del sistema)**, no PowerShell.  

---

## 📂 Dónde colocar los scripts

Copia los 4 archivos `.cmd` en la **raíz del proyecto**, junto a `.venv` y `requirements.txt`.  

Estructura recomendada:

```
mi_proyecto/
 ├─ .venv/
 ├─ requirements.txt
 ├─ setup_venv_from_requirements.cmd
 ├─ reset_venv_from_requirements.cmd
 ├─ provision_and_open_venv.cmd
 └─ open_venv_here.cmd
```

---

## 🧠 Conceptos rápidos

- **Entorno virtual (`.venv`)**: carpeta aislada con librerías solo de ese proyecto.  
- **Activar el entorno**: hace que `python` y `pip` usen el de `.venv`.  
- **`requirements.txt`**: lista de dependencias.  
- **CMD vs PowerShell**: aquí usamos CMD.  

---

## ⚙️ Scripts detallados

### 1) `setup_venv_from_requirements.cmd` — Provisionar entorno desde `requirements.txt`

```cmd
@echo off
setlocal ENABLEDELAYEDEXPANSION
if not exist ".venv" (
  echo [*] Creando entorno virtual .venv...
  python -m venv .venv || goto :error
)
call ".venv\Scripts\activate.bat" || goto :error
python -m pip install --upgrade pip || goto :error
if exist "requirements.txt" (
  pip install -r requirements.txt || goto :error
)
python --version
where python
pip list
exit /b 0
:error
exit /b 1
```

---

### 2) `reset_venv_from_requirements.cmd` — Borrar y recrear el entorno desde cero

```cmd
@echo off
set /p CONF=¿Quieres borrar y recrear el entorno .venv? (S/N) :
if /I not "%CONF%"=="S" exit /b 0
if exist ".venv" rmdir /S /Q ".venv"
python -m venv .venv || goto :error
call ".venv\Scripts\activate.bat" || goto :error
python -m pip install --upgrade pip || goto :error
if exist "requirements.txt" pip install -r requirements.txt || goto :error
cmd /k
exit /b 0
:error
exit /b 1
```

---

### 3) `provision_and_open_venv.cmd` — Provisionar y dejar el entorno abierto

```cmd
@echo off
if not exist ".venv" python -m venv .venv || goto :error
call ".venv\Scripts\activate.bat" || goto :error
python -m pip install --upgrade pip || goto :error
if exist "requirements.txt" pip install -r requirements.txt || goto :error
cmd /k
exit /b 0
:error
exit /b 1
```

---

### 4) `open_venv_here.cmd` — Abrir una CMD ya activada en `.venv`

```cmd
@echo off
set "ACT=.venv\Scripts\activate.bat"
if not exist "%ACT%" (
  echo No existe el entorno .venv en este directorio.
  exit /b 1
)
cmd /k "%ACT%"
```

---

## 🗂 Qué script usar según el caso

- ¿**Primera vez** en este proyecto? → `setup_venv_from_requirements.cmd`  
- ¿**Algo roto** o quieres empezar limpio? → `reset_venv_from_requirements.cmd`  
- ¿**Provisionar y quedarme dentro**? → `provision_and_open_venv.cmd`  
- ¿Ya tengo entorno y solo quiero **abrirlo rápido**? → `open_venv_here.cmd`  

---

✅ Con estos 4 scripts puedes crear, resetear, provisionar y abrir entornos rápidamente sin memorizar los comandos manuales.


</details>

---
<details>

<summary>Nombre Archivo: README_Entorno_VSCode_Structured.md</summary>


# Entorno Virtual en VS Code (Windows CMD)

## 1. Propósito
Esta guía muestra cómo crear y usar un **entorno virtual de Python** (`.venv`) en **Windows CMD con VS Code**.  
Está pensada como referencia práctica para:
- Crear y activar un entorno virtual.
- Instalar y administrar dependencias con `pip`.
- Configurar VS Code para usar correctamente `.venv`.
- Resolver errores comunes con el analizador o la terminal.

---

## 2. Uso básico

### Abrir CMD y ubicarse en el proyecto
```cmd
cd C:\Users\TuUsuario\Desktop\python
```

### Verificar instalación de Python
```cmd
python --version
where python
```

### Crear el entorno virtual
```cmd
python -m venv .venv
```

### Activar el entorno virtual
```cmd
.venv\Scripts\activate.bat
```
Prompt esperado:
```
(.venv) C:\Users\TuUsuario\Desktop\python>
```

### Instalar paquetes dentro del entorno
```cmd
pip install requests
```

### Comprobar que VS Code usa el entorno
```cmd
python --version
where python
```
Debe apuntar a:
```
.venv\Scripts\python.exe
```

### Desactivar el entorno virtual
```cmd
deactivate
```

---

## 3. Notas técnicas
- **Selección de intérprete en VS Code**:  
  - `Ctrl+Shift+P` → `Python: Select Interpreter` → elegir `.venv\Scripts\python.exe`.

- **Cambiar terminal predeterminada a CMD**:  
  - `Ctrl+Shift+P` → `Terminal: Select Default Profile`.  
  - Escoge **Command Prompt (cmd)**.  
  - Cierra y vuelve a abrir la terminal con `Ctrl+ñ`.

- **Reiniciar el analizador de Python**:  
  - `Ctrl+Shift+P` → `Python: Restart Language Server`.  
  - O usa `Ctrl+Shift+P` → `Developer: Reload Window`.

- **Reiniciar la terminal integrada**:  
  - Cierra la terminal con el ícono de papelera 🗑️.  
  - Abre una nueva con ➕.  
  - Reactiva el entorno con:  
    ```cmd
    .venv\Scripts\activate.bat
    ```

- **Forzar selección manual del intérprete**:  
  - `Ctrl+Shift+P` → `Python: Select Interpreter`.  
  - Opción **Enter Interpreter Path** → **Find...**.  
  - Busca y selecciona:  
    ```
    C:\Users\TuUsuario\Desktop\python\.venv\Scripts\python.exe
    ```

- **Notas rápidas**:  
  - Los bloques de código son para **CMD**, no para celdas de Python.  
  - Si ves el error *ExecutionPolicy* en PowerShell, cambia la terminal a CMD.  

---


</details>

---
<details>

<summary>Nombre Archivo: README_Entorno_VSCode_Original.md</summary>

# Creación y uso de un Entorno Virtual en VS Code (Windows **CMD**)

Este notebook es una **guía práctica** con celdas *Markdown* y bloques de **código listo para copiar/pegar** en el **Símbolo del sistema (CMD)** de Windows.

Incluye:
1. Verificar versión y ruta de Python.
2. Crear un entorno virtual `.venv`.
3. Activarlo desde **CMD**.
4. Instalar paquetes con `pip`.
5. **Desactivar** el entorno virtual.
6. Configurar VS Code para usar `.venv`.
7. (Extra) Cambiar la **terminal por defecto** a **CMD**.
8. (Extra) Reiniciar el analizador y la terminal si ves errores en rojo.
9. (Extra) Forzar selección manual del intérprete en VS Code.


## 0) Abrir CMD y ubicarse en tu proyecto
Abre **CMD** (Win+R → `cmd` → Enter) y navega a la carpeta de tu proyecto:

```cmd
cd C:\Users\TuUsuario\Desktop\python
```


## 1) Verificar instalación de Python (versión y rutas)
Comprueba que Python esté instalado y accesible en tu PATH, y mira su ubicación.

```cmd
python --version
```
```cmd
where python
```
Deberías ver una ruta hacia tu futuro entorno cuando esté activo, por ejemplo:
`C:\Users\TuUsuario\Desktop\python\.venv\Scripts\python.exe`


## 2) Crear el entorno virtual
Crea un entorno llamado `.venv` dentro de tu proyecto:

```cmd
python -m venv .venv
```


## 3) Activar el entorno virtual (**CMD**)
Activa el entorno usando el script para CMD:

```cmd
.venv\Scripts\activate.bat
```
Si todo va bien, verás el prompt con prefijo `(.venv)`:
```
(.venv) C:\Users\TuUsuario\Desktop\python>
```


## 4) Instalar paquetes dentro del entorno
Ejemplo instalando `requests` (puedes cambiarlo por lo que necesites, p. ej. `flask`, `pandas`, `django`):

```cmd
pip install requests
```


## 5) Comprobar que VS Code usa el entorno
En la terminal integrada de VS Code (con el entorno activado), verifica versión y ruta:

```cmd
python --version
```
```cmd
where python
```
La primera ruta debe apuntar a `.venv\Scripts\python.exe`.


## 6) Desactivar el entorno virtual
Cuando termines, puedes desactivarlo con:

```cmd
deactivate
```


## 7) Configurar el intérprete en VS Code
1. Abre la **paleta de comandos**: `Ctrl + Shift + P`.
2. Escribe: `Python: Select Interpreter`.
3. Selecciona el que apunte a tu `.venv`.

Deberías ver en la barra de estado (abajo a la derecha) algo como:
`Python 3.x ('.venv': venv)`


## (Extra) Cambiar la terminal por defecto a **CMD** en VS Code
Si VS Code te abre PowerShell por defecto y prefieres **CMD**:

1. `Ctrl + Shift + P` → **Terminal: Select Default Profile**.
2. Selecciona **Command Prompt (cmd)**.
3. Cierra la terminal (`Ctrl + ñ`) y vuelve a abrir una nueva (`Ctrl + ñ`).

Ahora tu terminal debería verse como:
```
C:\Users\TuUsuario\Desktop\python>
```
Y la activación funcionará con:
```cmd
.venv\Scripts\activate.bat
```


## (Extra) Reiniciar el analizador y la terminal en VS Code

Si después de instalar dependencias aún ves errores en rojo, puede ser el analizador de VS Code (Pylance).

1. **Reinicia el analizador**:
   - `Ctrl+Shift+P` → `Python: Restart Language Server`
   - o `Ctrl+Shift+P` → `Developer: Reload Window`

2. **Cierra y vuelve a abrir la terminal integrada** (`Ctrl+ñ`).

Esto fuerza a VS Code a reconocer las nuevas librerías de tu `.venv`.


## (Extra) Forzar selección manual del intérprete en VS Code
Si tu `.venv` no aparece en la lista de intérpretes:

1. Abre la **paleta de comandos**: `Ctrl+Shift+P`.
2. Escribe: `Python: Select Interpreter`.
3. Elige la opción: **Enter Interpreter Path**.
4. Haz clic en **Find...**
5. Navega hasta tu entorno virtual, normalmente en:
   ```
   C:\Users\TuUsuario\Desktop\python\.venv\Scripts\python.exe
   ```
6. Selecciónalo y confirma.

Así VS Code quedará enlazado manualmente a tu `.venv`.


---
### Notas rápidas
- Estos bloques de **código** están pensados para **copiar/pegar en CMD**, no para ejecutarlos como celdas de Python.
- Si ves el error de *ExecutionPolicy* en PowerShell, significa que estás en PowerShell, no en CMD. Cambia la terminal por defecto como se indica arriba.


</details>

---
<details>

<summary>Nombre Archivo: README_profesional.md</summary>

# Guía de scripts CMD para entornos virtuales en Windows

Este repositorio contiene 4 scripts `.cmd` para facilitar la creación, activación y gestión de entornos virtuales de Python en Windows utilizando **CMD**.

## Scripts incluidos

- **setup_venv_from_requirements.cmd**  
  Crea (si no existe) y provisiona el entorno a partir de `requirements.txt`.  

- **reset_venv_from_requirements.cmd**  
  Elimina `.venv` y lo recrea desde cero con las dependencias.  

- **provision_and_open_venv.cmd**  
  Provisiona (si hace falta) y deja la terminal abierta con `.venv` activado.  

- **open_venv_here.cmd**  
  Abre una nueva terminal CMD con `.venv` activado.  

## Requisitos

- Windows con **Python 3.x** instalado.  
- Python agregado al **PATH**.  
- Opcional: archivo `requirements.txt`.  
- Uso en **CMD (Command Prompt)**, no PowerShell.  

## Estructura del proyecto

```
mi_proyecto/
 ├─ .venv/
 ├─ requirements.txt
 ├─ setup_venv_from_requirements.cmd
 ├─ reset_venv_from_requirements.cmd
 ├─ provision_and_open_venv.cmd
 └─ open_venv_here.cmd
```

## Decisión rápida

- **Primera vez** → `setup_venv_from_requirements.cmd`  
- **Reiniciar limpio** → `reset_venv_from_requirements.cmd`  
- **Provisionar y quedarme dentro** → `provision_and_open_venv.cmd`  
- **Abrir entorno existente** → `open_venv_here.cmd`  

---

© 2025 - Documentación técnica de apoyo para proyectos en Python.


</details>

---
<details>

<summary>Nombre Archivo: README_friendly.md</summary>

# 🐍⚡ Scripts CMD para entornos virtuales en Windows

Bienvenido 👋 Esta guía trae **4 scripts mágicos** en `.cmd` para que nunca más tengas que recordar los comandos de entornos virtuales en Windows.  

## 🚀 Scripts disponibles

1. **`setup_venv_from_requirements.cmd`** → crea `.venv` y lo llena desde `requirements.txt`.  
2. **`reset_venv_from_requirements.cmd`** → borra todo y arranca de cero (con confirmación).  
3. **`provision_and_open_venv.cmd`** → provisiona y te deja listo dentro del entorno.  
4. **`open_venv_here.cmd`** → abre directo una CMD con `.venv` activado.  

## ✅ Requisitos previos

- Tener **Python 3.x** instalado en Windows.  
- Que `python --version` funcione en CMD.  
- (Opcional) `requirements.txt` en tu proyecto.  
- ⚠️ Importante: **usar CMD, no PowerShell**.  

## 📂 Cómo se ven en tu proyecto

```
mi_proyecto/
 ├─ .venv/
 ├─ requirements.txt
 ├─ setup_venv_from_requirements.cmd
 ├─ reset_venv_from_requirements.cmd
 ├─ provision_and_open_venv.cmd
 └─ open_venv_here.cmd
```

## 🤔 ¿Qué script uso?

- 🆕 Primera vez → **setup**  
- 🔄 Algo roto / empezar limpio → **reset**  
- ⚡ Quiero entrar listo ya → **provision_and_open**  
- 🎯 Ya tengo `.venv` y solo quiero abrir → **open_venv_here**  

## 🎉 Tips extra

- Un entorno por proyecto.  
- Versiona siempre tu `requirements.txt`.  
- Si algo falla → usa `reset` y reinstala.  

---

💡 Hecho para que la gestión de entornos sea **fácil, rápida y sin dolores de cabeza**.


</details>

---
## Nombre Archivo: Documentacion_Proyectos_EXP.md
### Descripción general
Contiene todos los documentos técnicos, tutoriales, ejemplos y módulos que componen el sistema **EXP Report**.  
Incluye versiones unificadas, simplificadas y de análisis, ordenadas de la más completa a la más básica.

| Archivo | Descripción breve |
|----------|-------------------|
| readme_exp_report.md | Versión final y consolidada del proyecto EXP Report. Incluye documentación completa, funciones explicadas, código íntegro y generación de reportes PDF y de consola. |
| readme_exp_report_clean.md | Variante optimizada y minimalista del generador de reportes de EXP, con el mismo cálculo base y estructura PDF simplificada. |
| readme_exp_report_tutorial_final_v2.md | Tutorial final paso a paso (v2) que explica cómo generar un PDF con tiempos y checkpoints, ideal para aprendizaje o documentación pedagógica. |
| readme_print_console_exp_report.md | Módulo centrado en la impresión de reportes en consola. Permite validar cálculos sin dependencias externas ni generación de PDF. |
| readme_debug_exp_report.md | Herramienta base para depuración de tiempos y checkpoints de EXP. Muestra resultados en consola y sirve como punto de partida para versiones posteriores. |
| readme_Análisis_de_tiempos_de_EXP_por_checkpoints.md | Documento analítico inicial convertido desde un notebook. Contiene el cálculo base de tiempos mínimos y máximos de EXP por checkpoints. |

<details><summary>extra</summary>

# Documentación de Proyectos EXP

## Descripción breve de cada archivo
- **readme_Análisis_de_tiempos_de_EXP_por_checkpoints.md**: Notebook convertido a README que calcula tiempos mínimos y máximos para alcanzar checkpoints de EXP, incluyendo explicación para mover la meta total fuera de la tabla y ejemplos de salida.
- **readme_exp_report.md**: Documentación del módulo EXP Report: genera tabla en consola y PDF; incluye explicación de funciones, README del proyecto y código completo del generador.
- **readme_exp_report_tutorial_final_v2.md**: Tutorial final (v2) para generar un PDF de tiempos para alcanzar EXP, con parámetros, ejemplos y todas las celdas de código separadas del notebook.
- **readme_print_console_exp_report.md**: Mini-módulo para imprimir en consola un reporte de EXP; explica funciones auxiliares y muestra ejemplos de uso sin dependencias externas.

---

- **readme_exp_report_clean.md**: Versión simplificada y limpia del generador de reportes de EXP; incluye documentación técnica, ejemplos y código fuente minimalista.
- **readme_debug_exp_report.md**: Herramienta de consola para depurar reportes de EXP y visualizar tiempos estimados por checkpoint.

---

## Resumen de funciones, variables y recomendaciones

### 🧩 readme_Análisis_de_tiempos_de_EXP_por_checkpoints.md
**Funciones detectadas**
- `analyze_checkpoints()`
- `calculate_time_ranges()`
- `export_table_to_md()`

**Variables relevantes**
- `min_time`, `max_time`, `checkpoints`, `exp_total`.

**Recomendaciones**
- Ideal para estimar progresión de experiencia por hitos.
- Se recomienda usarlo antes de generar reportes para verificar consistencia de datos.

---

### 🧾 readme_exp_report.md
**Funciones detectadas**
- `generate_exp_report()`
- `_compute_plan()`
- `_validate_inputs()`
- `_on_page()`
- `_ensure_dir_for()`

**Variables relevantes**
- `total_exp`, `exp_per_cycle`, `checkpoint_step`, `filename`, `tz_name`.

**Recomendaciones**
- Usar para crear reportes PDF con tabla y resumen.
- Ideal para documentación o entrega de resultados.
- Verificar permisos de escritura antes de generar el archivo.

---

### 📘 readme_exp_report_tutorial_final_v2.md
**Funciones detectadas**
- `generate_exp_report()`
- `print_console_exp_report()`
- `_register_fonts()`

**Variables relevantes**
- `detail_checkpoints`, `include_total_in_table`, `ensure_total_in_detail`.

**Recomendaciones**
- Útil como guía práctica paso a paso para nuevos usuarios.
- Puede emplearse como plantilla de aprendizaje para adaptar reportes personalizados.

---

### 💻 readme_print_console_exp_report.md
**Funciones detectadas**
- `print_console_exp_report()`
- `_print_debug_header()`
- `_print_detail_table()`

**Variables relevantes**
- `return_data`, `verbose`, `detail_checkpoints`.

**Recomendaciones**
- Ideal para depuración rápida sin generar PDFs.
- Perfecto para validar cálculos antes de ejecutar el reporte principal.

---

### 🧩 readme_exp_report_clean.md
**Funciones detectadas**
- `generate_exp_report()`
- `print_console_exp_report()`
- `_compute_plan()`
- `_validate_inputs()`
- `_on_page()`
- `format_hms()`
- `es_miles()`

**Variables relevantes**
- `FONT_NAME`, `tz_name`, `checkpoint_step`, `max_detail_rows`

**Recomendaciones**
- Ideal para generar reportes PDF minimalistas y claros.
- Perfecto para integración en entornos ligeros o notebooks.

---

### 🧩 readme_debug_exp_report.md
**Funciones detectadas**
- `debug_exp_report()`
- `_compute_plan()`
- `_validate_inputs()`
- `format_hms()`
- `_format_thousands()`

**Variables relevantes**
- `total_exp`, `exp_per_cycle`, `min_sec_per_cycle`, `max_sec_per_cycle`, `detail_checkpoints`

**Recomendaciones**
- Excelente para pruebas rápidas en consola.
- Facilita depurar cálculos de tiempos antes de generar reportes PDF.
</details>

---
<details>
<summary>Nombre Archivo: readme_exp_report.md</summary>

# EXP Report — Generador de tabla y PDF

Este proyecto calcula cuánto tiempo tardarías en alcanzar una meta de **EXP** (experiencia) dado:
- EXP ganado por ciclo
- Rango de duración (en segundos) de cada ciclo
- Checkpoints opcionales para ver avances parciales

Produce salida **en consola** y un **PDF** con una tabla de detalle.

---

## 1) Explicación de cada función (guion de 5 puntos)

> Formato: **1) Propósito, 2) Uso básico, 3) Notas técnicas, 4) Ejemplo extra, 5) Relación con otras partes.**

### ` _register_fonts() -> str`
1. **Propósito:** Registrar una tipografía TrueType (DejaVuSans) para ReportLab y devolver el nombre a usar en el PDF; si falla, usa *Helvetica*.
2. **Uso básico:** Se invoca al cargar el módulo para inicializar `FONT_NAME`.
3. **Notas técnicas:** Usa `reportlab.pdfbase.pdfmetrics.registerFont` y `TTFont`. Captura excepciones para asegurar un fallback.
4. **Ejemplo extra:** Si incluyes `DejaVuSans.ttf` junto al script, podrás renderizar caracteres latinos y símbolos sin problemas.
5. **Relación:** El valor devuelto se usa en `_on_page` para fijar la fuente del encabezado/pie del PDF.

### `format_hms(seconds: int) -> str`
1. **Propósito:** Convertir segundos enteros a formato `HH:MM:SS`.
2. **Uso básico:** `format_hms(3723)  # "01:02:03"`
3. **Notas técnicas:** Redondea a entero, usa divisiones enteras y módulos para horas, minutos y segundos.
4. **Ejemplo extra:** Formatear tiempos mínimos y máximos acumulados por checkpoint.
5. **Relación:** Utilizada en `_print_debug_header`, `_print_detail_table` y `generate_exp_report` para presentar tiempos.

### `es_miles(n: int) -> str`
1. **Propósito:** Formatear números enteros con separador de miles como punto (estilo “1.234.567”).
2. **Uso básico:** `es_miles(57000)  # "57.000"`
3. **Notas técnicas:** Usa `format(n, ",")` y reemplaza comas por puntos.
4. **Ejemplo extra:** Mostrar “ciclos necesarios” y “checkpoints” de manera legible.
5. **Relación:** Empleado en todos los resúmenes/textos donde aparecen enteros grandes.

### `_ensure_dir_for(path: str) -> None`
1. **Propósito:** Crear el directorio destino si no existe antes de escribir el PDF.
2. **Uso básico:** Internamente en `generate_exp_report`.
3. **Notas técnicas:** `os.path.dirname/os.path.abspath` y `os.makedirs(..., exist_ok=True)`.
4. **Ejemplo extra:** Si pasas `reports/out.pdf`, creará `reports/` automáticamente.
5. **Relación:** Previene errores de E/S al guardar PDFs.

### `_validate_inputs(...) -> List[int]`
Parámetros: `total_exp`, `exp_per_cycle`, `min_sec_per_cycle`, `max_sec_per_cycle`, `detail_checkpoints`

1. **Propósito:** Validar tipos y rangos; normalizar y ordenar los checkpoints si existen.
2. **Uso básico:** Llamada temprana por `_compute_plan` y `generate_exp_report`.
3. **Notas técnicas:** Exige `int` y `> 0`; asegura `min_sec_per_cycle <= max_sec_per_cycle`; convierte `detail_checkpoints` a lista ordenada única.
4. **Ejemplo extra:** Si pasas `[500, -1, 500, 999999]`, devuelve `[500]` (y el resto se filtra en `_compute_plan` si excede el total).
5. **Relación:** Base para la consistencia del plan de cálculo.

### `_on_page(canvas, doc, title_text: str, tz_name: str)`
1. **Propósito:** Dibujar encabezado y pie de página con fecha/hora y número de página en cada página del PDF.
2. **Uso básico:** Callback `onFirstPage`/`onLaterPages` de `SimpleDocTemplate.build`.
3. **Notas técnicas:** Usa `ZoneInfo` para zona horaria, `canvas.drawString/drawRightString`, y la fuente `FONT_NAME`.
4. **Ejemplo extra:** Cambia `tz_name` a `"UTC"` si necesitas hora universal.
5. **Relación:** Integrado por `generate_exp_report` durante el render del PDF.

### `_compute_plan(..., checkpoint_step=10000, max_detail_rows=300, include_total_in_table=False) -> dict`
1. **Propósito:** Calcular el plan de progreso: ciclos, tiempos mínimos/máximos y la lista final de checkpoints a mostrar.
2. **Uso básico:** Es el núcleo de cómputo para consola y PDF.
3. **Notas técnicas:** 
   - `cycles_needed = ceil(total_exp / exp_per_cycle)`  
   - Si no se pasan checkpoints, genera automáticos cada `checkpoint_step` hasta el total (“modo auto”).  
   - Limita filas a `max_detail_rows` aplicando muestreo.
   - Puede añadir el `total_exp` como fila final si `include_total_in_table=True`.
4. **Ejemplo extra:** Con `total_exp=57_000, exp_per_cycle=60` → `cycles_needed=950`.
5. **Relación:** Insumo directo para `_print_*` y `generate_exp_report`.

### `_print_debug_header(d: dict)`
1. **Propósito:** Imprimir en consola un resumen del plan (total, ciclos, tiempos, avisos).
2. **Uso básico:** Llamado por `debug_exp_report`.
3. **Notas técnicas:** Usa `es_miles` y `format_hms` para legibilidad.
4. **Ejemplo extra:** Muestra un aviso si hubo checkpoints filtrados.
5. **Relación:** Complemento textual previo a la tabla de detalle.

### `_print_detail_table(checkpoints, exp_per_cycle, min_sec_per_cycle, max_sec_per_cycle)`
1. **Propósito:** Imprimir una tabla alineada con tiempos para cada checkpoint.
2. **Uso básico:** Llamado por `debug_exp_report`.
3. **Notas técnicas:** Calcula `ceil(cp / exp_per_cycle)` para ciclos por fila; muestra tiempos acumulados min/max.
4. **Ejemplo extra:** Sirve para una “vista rápida” cuando no necesitas PDF.
5. **Relación:** Presentación en consola de los datos de `_compute_plan`.

### `debug_exp_report(..., return_data=False, verbose=True)`
1. **Propósito:** Orquestar el flujo de depuración en consola (encabezado + tabla), y opcionalmente devolver los datos.
2. **Uso básico:** `debug_exp_report(57000, 60, 35, 45, [1000, 2000])`
3. **Notas técnicas:** Pasa parámetros de granularidad (`checkpoint_step`, `max_detail_rows`) y `include_total_in_table`.
4. **Ejemplo extra:** Con `return_data=True` obtienes el diccionario para integrarlo en otra app.
5. **Relación:** Es la “API de consola”; la versión PDF es `generate_exp_report`.

### `print_console_exp_report(total_exp, exp_per_cycle, min_sec_per_cycle, max_sec_per_cycle, detail_checkpoints=None)`
1. **Propósito:** Atajo simple para imprimir el reporte en consola con valores por defecto razonables.
2. **Uso básico:** `print_console_exp_report(57000, 60, 35, 45, checkpoints)`
3. **Notas técnicas:** Llama directamente a `debug_exp_report` con `verbose=True`.
4. **Ejemplo extra:** Útil como entrypoint en scripts mínimos.
5. **Relación:** Capa de conveniencia sobre `debug_exp_report`.

### `generate_exp_report(..., filename=None, include_question=True, ..., tz_name="America/Santiago", return_data=False) -> str | (str, dict)`
1. **Propósito:** Generar el **PDF** con encabezado, resumen y tabla de checkpoints.
2. **Uso básico:** 
   ```python
   pdf = generate_exp_report(57000, 60, 35, 45, [1000,2000], question_suffix="")
   ```
3. **Notas técnicas:** 
   - Si `filename` es `None`, crea `exp_report_YYYYMMDD_HHMM.pdf` en la zona horaria dada.
   - Usa ReportLab (`SimpleDocTemplate`, `Table`, `Paragraph`) y callbacks `_on_page`.
   - `return_data=True` devuelve `(ruta_pdf, dict_resumen)`.
4. **Ejemplo extra:** Pasa `detail_checkpoints=None` para modo auto cada 10.000 EXP; ajusta `checkpoint_step`.
5. **Relación:** Es la “API PDF”; comparte la lógica de `_compute_plan` con la versión de consola.

---

## 2) README completo del proyecto

### Propósito del proyecto
Calcular y **reportar** (consola + PDF) el tiempo necesario para alcanzar una meta de EXP, mostrando además avances por checkpoints.

### Requisitos
- Python 3.10+ (se usa `zoneinfo`, parte de la librería estándar moderna).
- Paquete **ReportLab** para generar PDFs.

### Instalación
```bash
pip install reportlab
```

### Uso básico
```python
from exp_report import print_console_exp_report, generate_exp_report

# Consola
print_console_exp_report(57000, 60, 35, 45, [1000,2000,3125,4125,5125,6250,7250,8375,9375,10375])

# PDF
pdf_path = generate_exp_report(
    57000, 60, 35, 45,
    [1000,2000,3125,4125,5125,6250,7250,8375,9375,10375],
    question_suffix=""
)
print("PDF generado en:", pdf_path)
```

### Dependencias
- `reportlab`

### Ejemplos de ejecución
- **Consola:** imprimirá un resumen y una tabla con tiempos mínimos y máximos acumulados.
- **PDF:** generará `exp_report_YYYYMMDD_HHMM.pdf` con encabezado, resumen y la tabla detallada.  
  Si no existe el directorio del archivo de salida, se creará automáticamente.

---

## 3) Código completo (incluido tal cual)

```python
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas as canvas_mod
from reportlab.lib.units import mm
from zoneinfo import ZoneInfo
import os, math
from datetime import datetime
from typing import Iterable, List, Optional, Tuple, Dict, Any


from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def _register_fonts() -> str:
    try:
        pdfmetrics.registerFont(TTFont("DejaVu", "DejaVuSans.ttf"))
        return "DejaVu"
    except Exception:
        return "Helvetica"

FONT_NAME = _register_fonts()


def format_hms(seconds: int) -> str:
    seconds = int(round(seconds))
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def es_miles(n: int) -> str:
    s = f"{int(n):,}"
    return s.replace(",", ".")


def _ensure_dir_for(path: str) -> None:
    directory = os.path.dirname(os.path.abspath(path))
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

def _validate_inputs(
    total_exp: int,
    exp_per_cycle: int,
    min_sec_per_cycle: int,
    max_sec_per_cycle: int,
    detail_checkpoints: Optional[Iterable[int]]
) -> List[int]:
    for name, val in [
        ("total_exp", total_exp),
        ("exp_per_cycle", exp_per_cycle),
        ("min_sec_per_cycle", min_sec_per_cycle),
        ("max_sec_per_cycle", max_sec_per_cycle),
    ]:
        if not isinstance(val, int):
            raise TypeError(f"{name} debe ser int.")
        if val <= 0:
            raise ValueError(f"{name} debe ser > 0.")
    if min_sec_per_cycle > max_sec_per_cycle:
        raise ValueError("min_sec_per_cycle no puede ser mayor que max_sec_per_cycle.")
    if detail_checkpoints is None:
        return []
    cps = sorted({int(x) for x in detail_checkpoints if int(x) > 0})
    return cps


def _on_page(canvas: canvas_mod.Canvas, doc, title_text: str, tz_name: str):
    canvas.saveState()
    canvas.setFont(FONT_NAME, 9)
    canvas.drawString(15 * mm, 285 * mm, title_text)
    now_str = datetime.now(ZoneInfo(tz_name)).strftime("%Y-%m-%d %H:%M")
    page_str = f"Generado: {now_str}  |  Página {doc.page}"
    canvas.drawRightString(200 * mm, 10 * mm, page_str)
    canvas.restoreState()


def _compute_plan(
    total_exp: int,
    exp_per_cycle: int,
    min_sec_per_cycle: int,
    max_sec_per_cycle: int,
    detail_checkpoints: Optional[Iterable[int]],
    *,
    checkpoint_step: int = 10_000,
    max_detail_rows: int = 300,
    include_total_in_table: bool = False,
) -> Dict[str, Any]:
    _validate_inputs(total_exp, exp_per_cycle, min_sec_per_cycle, max_sec_per_cycle, detail_checkpoints)
    cycles_exact = total_exp / exp_per_cycle
    cycles_needed = math.ceil(cycles_exact)
    min_total = cycles_needed * min_sec_per_cycle
    max_total = cycles_needed * max_sec_per_cycle
    filtered_notice = None
    auto_mode = (detail_checkpoints is None)
    if auto_mode:
        last = (total_exp // checkpoint_step) * checkpoint_step
        cps = list(range(checkpoint_step, last + 1, checkpoint_step))
        if include_total_in_table and (not cps or cps[-1] != total_exp):
            cps.append(total_exp)
    else:
        cps = sorted({int(x) for x in detail_checkpoints if int(x) > 0})
        over = [x for x in cps if x > total_exp]
        if over:
            filtered_notice = f"Aviso: se ignoraron checkpoints > total ({over})"
        cps = [x for x in cps if x <= total_exp]
        if include_total_in_table and (not cps or cps[-1] != total_exp):
            cps.append(total_exp)
    if len(cps) > max_detail_rows:
        keep = max_detail_rows - (1 if include_total_in_table else 0)
        step = max(1, len(cps) // keep)
        reduced = cps[::step]
        if len(reduced) > keep:
            reduced = reduced[:keep]
        cps = reduced + ([total_exp] if include_total_in_table and (not reduced or reduced[-1] != total_exp) else [])
    return {
        "total_exp": total_exp, "exp_per_cycle": exp_per_cycle,
        "min_sec_per_cycle": min_sec_per_cycle, "max_sec_per_cycle": max_sec_per_cycle,
        "cycles_exact": cycles_exact, "cycles_needed": cycles_needed,
        "min_total_sec": min_total, "max_total_sec": max_total,
        "checkpoints": cps, "filtered_notice": filtered_notice, "auto_mode": auto_mode,
    }

def _print_debug_header(d: Dict[str, Any]):
    print("=== Debug EXP Report ===")
    print(f"total_exp: {es_miles(d['total_exp'])}")
    print(f"exp_per_cycle: {d['exp_per_cycle']}")
    print(f"Ciclos necesarios (ceil): {d['cycles_needed']}\n")
    print(f"min_sec_per_cycle: {d['min_sec_per_cycle']}")
    print(f"Tiempo total mínimo: {format_hms(d['min_total_sec'])}\n")
    print(f"max_sec_per_cycle: {d['max_sec_per_cycle']}")
    print(f"Tiempo total máximo: {format_hms(d['max_total_sec'])}\n")
    if d.get("filtered_notice"): print(d["filtered_notice"])

def _print_detail_table(checkpoints: List[int], exp_per_cycle: int, min_sec_per_cycle: int, max_sec_per_cycle: int):
    headers = ("Checkpoint", "Ciclos hasta aquí", "Tiempo mínimo", "Tiempo máximo")
    col_w = (14, 20, 16, 16)
    def fmt_row(c1, c2, c3, c4):
        return (f"{str(c1):>{col_w[0]}} {str(c2):>{col_w[1]}} {str(c3):>{col_w[2]}} {str(c4):>{col_w[3]}}")
    print(fmt_row(*headers))
    print("-" * sum(col_w) + "-" * 3)
    for cp in checkpoints:
        cycles_here = math.ceil(cp / exp_per_cycle)
        min_here = cycles_here * min_sec_per_cycle
        max_here = cycles_here * max_sec_per_cycle
        print(fmt_row(es_miles(cp), es_miles(cycles_here), format_hms(min_here), format_hms(max_here)))


def debug_exp_report(
    total_exp: int, exp_per_cycle: int, min_sec_per_cycle: int, max_sec_per_cycle: int,
    detail_checkpoints: Optional[Iterable[int]] = None, *, checkpoint_step: int = 10_000,
    max_detail_rows: int = 300, include_total_in_table: bool = False, return_data: bool = False, verbose: bool = True):
    d = _compute_plan(total_exp, exp_per_cycle, min_sec_per_cycle, max_sec_per_cycle,
                      detail_checkpoints, checkpoint_step=checkpoint_step, max_detail_rows=max_detail_rows,
                      include_total_in_table=include_total_in_table)
    if verbose:
        _print_debug_header(d)
        _print_detail_table(d["checkpoints"], d["exp_per_cycle"], d["min_sec_per_cycle"], d["max_sec_per_cycle"])
    return d if return_data else None

def print_console_exp_report(total_exp: int, exp_per_cycle: int, min_sec_per_cycle: int, max_sec_per_cycle: int,
                             detail_checkpoints: Optional[Iterable[int]] = None):
    debug_exp_report(total_exp, exp_per_cycle, min_sec_per_cycle, max_sec_per_cycle,
                     detail_checkpoints, include_total_in_table=False, return_data=False, verbose=True)


def generate_exp_report(
    total_exp: int, exp_per_cycle: int, min_sec_per_cycle: int, max_sec_per_cycle: int,
    detail_checkpoints: Optional[Iterable[int]] = None, filename: Optional[str] = None, include_question: bool = True,
    *, checkpoint_step: int = 10_000, max_detail_rows: int = 300, question_suffix: str = "Muéstralo en una tabla y en PDF.",
    tz_name: str = "America/Santiago", return_data: bool = False
) -> str | Tuple[str, Dict[str, Any]]:
    _validate_inputs(total_exp, exp_per_cycle, min_sec_per_cycle, max_sec_per_cycle, detail_checkpoints)
    d = _compute_plan(total_exp, exp_per_cycle, min_sec_per_cycle, max_sec_per_cycle, detail_checkpoints,
                      checkpoint_step=checkpoint_step, max_detail_rows=max_detail_rows, include_total_in_table=False)
    if not filename:
        now = datetime.now(ZoneInfo(tz_name)).strftime("%Y%m%d_%H%M")
        filename = f"exp_report_{now}.pdf"
    _ensure_dir_for(filename)
    styles = getSampleStyleSheet()
    style_h1 = styles["Title"]; style_p = styles["BodyText"]
    doc = SimpleDocTemplate(filename, pagesize=letter, leftMargin=18*mm, rightMargin=18*mm, topMargin=18*mm, bottomMargin=18*mm)
    elements = []
    title_text = "Reporte de EXP"; elements.append(Paragraph(title_text, style_h1)); elements.append(Spacer(1, 6))
    if include_question:
        q_text = f"Meta: {es_miles(d['total_exp'])} EXP @ {d['exp_per_cycle']} EXP/ciclo. {question_suffix}"
        elements.append(Paragraph(q_text, style_p)); elements.append(Spacer(1, 8))
    resumen = [
        f"<b>Total EXP:</b> {es_miles(d['total_exp'])}",
        f"<b>Ciclos necesarios (ceil):</b> {es_miles(d['cycles_needed'])}",
        f"<b>Tiempo total:</b> {format_hms(d['min_total_sec'])} — {format_hms(d['max_total_sec'])}",
        f"<b>Duración por ciclo (seg):</b> {min_sec_per_cycle} — {max_sec_per_cycle}",
    ]
    elements.append(Paragraph("<br/>".join(resumen), style_p)); elements.append(Spacer(1, 10))
    if d.get("filtered_notice"):
        elements.append(Paragraph(f"<i>{d['filtered_notice']}</i>", style_p)); elements.append(Spacer(1, 6))
    cps = d["checkpoints"]
    data = [["Checkpoint", "Ciclos hasta aquí", "Tiempo mínimo", "Tiempo máximo"]]
    for cp in cps:
        cycles_here = math.ceil(cp / d["exp_per_cycle"])
        min_here = cycles_here * d["min_sec_per_cycle"]; max_here = cycles_here * d["max_sec_per_cycle"]
        data.append([es_miles(cp), es_miles(cycles_here), format_hms(min_here), format_hms(max_here)])
    table = Table(data, repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("FONTSIZE", (0,0), (-1,0), 12),
        ("BOTTOMPADDING", (0,0), (-1,0), 12),
        ("BACKGROUND", (0,1), (-1,-1), colors.beige),
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    elements.append(Paragraph("<b>Detalle por checkpoints</b>", style_p)); elements.append(Spacer(1,4)); elements.append(table)
    doc.build(elements, onFirstPage=lambda c,d: _on_page(c,d,title_text,tz_name), onLaterPages=lambda c,d: _on_page(c,d,title_text,tz_name))
    if return_data:
        out = {
            "total_exp": d["total_exp"], "exp_per_cycle": d["exp_per_cycle"],
            "cycles_needed": d["cycles_needed"], "min_total_hms": format_hms(d["min_total_sec"]),
            "max_total_hms": format_hms(d["max_total_sec"]), "checkpoints": cps, "tz_name": tz_name, "filename": filename,
        }
        return filename, out
    return filename
```

---

## 4) Ambas peticiones incluidas en este README
- ✅ Explicación de cada función (sección **1** arriba).
- ✅ README completo del proyecto con propósito, requisitos, instalación, uso básico, dependencias y ejemplos (sección **2**), además del **código completo** (sección **3**).

</details>

---
<details>
<summary>Nombre Archivo: readme_exp_report_clean.md</summary>

# 🧾 exp_report_clean

Módulo minimalista para generar un **reporte PDF del progreso de EXP** (experiencia), con soporte de consola y cálculos automáticos.  
Está pensado para entornos donde se requiere calcular el avance por ciclos, tiempos mínimos/máximos y mostrar el progreso en tablas legibles o en un archivo PDF.

---

## 📌 Propósito del proyecto

Este módulo genera un **informe visual y calculado del progreso total de experiencia (EXP)** a partir de datos básicos de ciclos.  
Permite:
- Calcular tiempos totales estimados según intervalos de duración por ciclo.
- Mostrar resultados por consola o exportarlos como PDF.
- Incluir encabezado/pie dinámico con hora local.
- Validar y formatear datos de entrada automáticamente.

---

## 🧩 Requisitos

- **Python 3.9+**  
- Librerías:
  - `reportlab`
  - `tzdata` (para soporte de zonas horarias en sistemas sin zona configurada)
  - `zoneinfo` (incluida desde Python 3.9)
  - `math`, `datetime`, `os` (estándar)

---

## ⚙️ Instalación

```bash
pip install reportlab tzdata
```

Luego copia el archivo `exp_report_clean.py` a tu proyecto o entorno de trabajo.

---

## 🚀 Uso básico

Ejemplo mínimo en consola:

```python
from exp_report_clean import generate_exp_report, print_console_exp_report

# Generar reporte por consola
print_console_exp_report(57000,60,35,45,[1000,2000,3125,4125,5125,6250,7250,8375,9375,10375])

# Generar reporte en PDF
generate_exp_report(57000,60,35,45,[1000,2000,3125,4125,5125,6250,7250,8375,9375,10375],question_suffix="")
```

El PDF se guardará automáticamente como:
```
exp_report_YYYYMMDD_HHMM.pdf
```

---

## 📦 Dependencias

| Librería | Propósito |
|-----------|------------|
| **reportlab** | Creación de PDF y manejo de estilos/tablas. |
| **tzdata** | Base de datos de zonas horarias para `zoneinfo`. |
| **zoneinfo** | Manejo de zona horaria local para encabezados. |
| **math**, **os**, **datetime** | Operaciones matemáticas, de archivos y tiempo. |

---

## 🧠 Ejemplos de ejecución

### 1️⃣ En consola
```python
print_console_exp_report(10000, 100, 30, 50, [500, 1000, 2000])
```

Salida simplificada:
```
=== Debug EXP Report ===
total_exp: 10.000
exp_per_cycle: 100
Ciclos necesarios (ceil): 100
Tiempo total mínimo: 00:50:00
Tiempo total máximo: 01:23:20
Checkpoint        Ciclos hasta aquí   Tiempo mínimo   Tiempo máximo
--------------------------------------------------------------------
500                         5            00:02:30         00:04:10
...
```

### 2️⃣ En PDF
```python
generate_exp_report(15000, 75, 40, 60, [500, 1000, 2000], question_suffix="")
```

Genera un archivo con resumen y tabla de detalle sin incluir la fila total.

---

## 🔍 Explicación de funciones

A continuación se documentan las funciones principales según el guion de 5 puntos.

---

### `format_hms(seconds: int) -> str`

1️⃣ **Propósito**  
Convierte una cantidad total de segundos en una cadena formateada como `HH:MM:SS`, con ceros a la izquierda.

2️⃣ **Uso básico**  
Se utiliza para mostrar tiempos totales o parciales en formato legible dentro del reporte.

```python
format_hms(3670)  # Devuelve '01:01:10'
```

3️⃣ **Notas técnicas**  
- Redondea los segundos al entero más cercano usando `round()`.  
- Usa división entera (`//`) y módulo (`%`) para obtener horas, minutos y segundos.  
- Devuelve una cadena de longitud fija con ceros a la izquierda mediante formato f-string.

4️⃣ **Ejemplo extra**  
```python
print(format_hms(59))    # '00:00:59'
print(format_hms(3605))  # '01:00:05'
```

5️⃣ **Relación con otras partes**  
Se usa en `_print_detail_table`, `_print_debug_header`, `_compute_plan` y `generate_exp_report` para presentar tiempos de forma uniforme.

---

### `es_miles(n: int) -> str`

1️⃣ **Propósito**  
Formatea enteros con separador de miles estilo español (`12.345.678`).

2️⃣ **Uso básico**  
```python
es_miles(1234567)  # '1.234.567'
```

3️⃣ **Notas técnicas**  
Utiliza formato `:,` y reemplaza comas por puntos.

4️⃣ **Ejemplo extra**  
```python
print(es_miles(50000))  # '50.000'
```

5️⃣ **Relación con otras partes**  
Se usa en todos los reportes (consola y PDF) para mejorar la legibilidad de cifras.

---

### `_validate_inputs(...) -> List[int]`

1️⃣ **Propósito**  
Verifica tipos, rangos y normaliza la lista de checkpoints.

2️⃣ **Uso básico**  
Interna, llamada automáticamente por `_compute_plan` y `generate_exp_report`.

3️⃣ **Notas técnicas**  
Asegura que todos los valores sean enteros > 0, ordena y elimina duplicados.

4️⃣ **Ejemplo extra**  
```python
_validate_inputs(5000, 50, 30, 40, [100, 200, 200, 50])
# Devuelve [50, 100, 200]
```

5️⃣ **Relación con otras partes**  
Previene errores de cálculo o PDF por entradas inválidas.

---

### `_compute_plan(...) -> dict`

1️⃣ **Propósito**  
Calcula los ciclos totales, tiempos mínimos/máximos y genera los checkpoints finales.

2️⃣ **Uso básico**  
Interna, invocada por `print_console_exp_report` y `generate_exp_report`.

3️⃣ **Notas técnicas**  
- Admite modo automático si no se especifican checkpoints.  
- Controla el número máximo de filas (`max_detail_rows`).  
- Devuelve estructura lista para impresión o PDF.

4️⃣ **Ejemplo extra**  
```python
d = _compute_plan(57000, 60, 35, 45, [1000, 2000])
print(d["cycles_needed"])  # 950
```

5️⃣ **Relación con otras partes**  
Es el núcleo del cálculo. Todos los reportes lo usan como fuente de verdad.

---

### `print_console_exp_report(...) -> None`

1️⃣ **Propósito**  
Muestra en consola un resumen de progreso y tabla detallada de checkpoints.

2️⃣ **Uso básico**  
```python
print_console_exp_report(10000, 100, 30, 50, [500, 1000])
```

3️⃣ **Notas técnicas**  
Usa `_compute_plan`, `_print_debug_header` y `_print_detail_table`.  
No incluye la fila total al final.

4️⃣ **Ejemplo extra**  
```python
print_console_exp_report(8000, 80, 20, 30, None)
```

5️⃣ **Relación con otras partes**  
Es la contraparte visual de `generate_exp_report`, útil para depuración rápida.

---

### `generate_exp_report(...) -> str | Tuple[str, dict]`

1️⃣ **Propósito**  
Genera un archivo PDF con resumen y tabla de progreso de EXP.

2️⃣ **Uso básico**  
```python
generate_exp_report(57000, 60, 35, 45, [1000, 2000])
```

3️⃣ **Notas técnicas**  
- Usa `ReportLab` con tabla repetida en cada página.  
- Encabezado con título y hora local.  
- Opción `return_data=True` devuelve también el resumen calculado.  
- Genera automáticamente el nombre del archivo con timestamp.

4️⃣ **Ejemplo extra**  
```python
filename, data = generate_exp_report(
    10000, 100, 30, 40, [1000, 2000], return_data=True
)
print(data["min_total_hms"])  # '00:50:00'
```

5️⃣ **Relación con otras partes**  
Depende de `_compute_plan`, `format_hms`, `es_miles` y `_on_page` para cálculos, formato y estructura del PDF.

---

## 📘 Notas finales

- Todos los PDF se generan con márgenes equilibrados y fuente `DejaVuSans` si está disponible.  
- El módulo puede integrarse fácilmente en notebooks o scripts.  
- Las funciones internas (`_nombre`) están diseñadas para uso interno o depuración avanzada.

---

## 📄 Código fuente completo (`exp_report_clean.py`)

```python
# -*- coding: utf-8 -*-
"""
exp_report_clean
----------------
Módulo minimalista para generar un PDF con el progreso de EXP.
Incluye:
- Utilidades de formato
- Validación de entradas
- Cálculo común compartido
- Generación de PDF (ReportLab)
- Funciones de consola (debug + tabla) opcionales

Dependencias externas: reportlab
"""

from typing import Iterable, Optional, List, Dict, Any, Tuple
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas as canvas_mod
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from zoneinfo import ZoneInfo
from datetime import datetime
import os, math

# ==============================
# Configuración de fuente (opcional)
# ==============================

def _register_fonts() -> str:
    """Intenta registrar DejaVuSans.ttf y retorna el nombre de fuente a usar.
    Si no está disponible, usa 'Helvetica' como fallback (sin error).
    """
    try:
        pdfmetrics.registerFont(TTFont("DejaVu", "DejaVuSans.ttf"))
        return "DejaVu"
    except Exception:
        return "Helvetica"

FONT_NAME = _register_fonts()

# ==============================
# Utilidades de formato
# ==============================

def format_hms(seconds: int) -> str:
    """Convierte segundos a HH:MM:SS (con cero padding)."""
    seconds = int(round(seconds))
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def es_miles(n: int) -> str:
    """Formatea enteros con separador de miles estilo es-CL/es-ES (puntos)."""
    s = f"{int(n):,}"
    return s.replace(",", ".")

# ==============================
# Validaciones y utilidades de archivo
# ==============================

def _ensure_dir_for(path: str) -> None:
    """Crea el directorio destino del archivo si no existe."""
    directory = os.path.dirname(os.path.abspath(path))
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)

def _validate_inputs(
    total_exp: int,
    exp_per_cycle: int,
    min_sec_per_cycle: int,
    max_sec_per_cycle: int,
    detail_checkpoints: Optional[Iterable[int]],
) -> List[int]:
    """Valida tipos/rangos y normaliza detail_checkpoints (ordena/únicos, >0)."""
    for name, val in [
        ("total_exp", total_exp),
        ("exp_per_cycle", exp_per_cycle),
        ("min_sec_per_cycle", min_sec_per_cycle),
        ("max_sec_per_cycle", max_sec_per_cycle),
    ]:
        if not isinstance(val, int):
            raise TypeError(f"{name} debe ser int.")
        if val <= 0:
            raise ValueError(f"{name} debe ser > 0.")
    if min_sec_per_cycle > max_sec_per_cycle:
        raise ValueError("min_sec_per_cycle no puede ser mayor que max_sec_per_cycle.")
    if detail_checkpoints is None:
        return []
    cps = sorted({int(x) for x in detail_checkpoints if int(x) > 0})
    return cps

# ==============================
# Encabezado/pie del PDF
# ==============================

def _on_page(canvas: canvas_mod.Canvas, doc, title_text: str, tz_name: str) -> None:
    """Encabezado/pie uniforme en cada página, con hora local y número de página."""
    canvas.saveState()
    canvas.setFont(FONT_NAME, 9)
    canvas.drawString(15 * mm, 285 * mm, title_text)
    now_str = datetime.now(ZoneInfo(tz_name)).strftime("%Y-%m-%d %H:%M")
    page_str = f"Generado: {now_str}  |  Página {doc.page}"
    canvas.drawRightString(200 * mm, 10 * mm, page_str)
    canvas.restoreState()

# ==============================
# Cálculo común (fuente de verdad)
# ==============================

def _compute_plan(
    total_exp: int,
    exp_per_cycle: int,
    min_sec_per_cycle: int,
    max_sec_per_cycle: int,
    detail_checkpoints: Optional[Iterable[int]],
    *,
    checkpoint_step: int = 5_000,
    max_detail_rows: int = 300,
    include_total_in_table: bool = False,
) -> Dict[str, Any]:
    """Calcula ciclos, tiempos totales y lista final de checkpoints (sin total por defecto)."""
    _validate_inputs(total_exp, exp_per_cycle, min_sec_per_cycle, max_sec_per_cycle, detail_checkpoints)

    cycles_exact = total_exp / exp_per_cycle
    cycles_needed = math.ceil(cycles_exact)
    min_total = cycles_needed * min_sec_per_cycle
    max_total = cycles_needed * max_sec_per_cycle

    filtered_notice = None
    auto_mode = (detail_checkpoints is None)

    if auto_mode:
        last = (total_exp // checkpoint_step) * checkpoint_step
        cps = list(range(checkpoint_step, last + 1, checkpoint_step))
        if include_total_in_table and (not cps or cps[-1] != total_exp):
            cps.append(total_exp)
    else:
        cps = sorted({int(x) for x in detail_checkpoints if int(x) > 0})
        over = [x for x in cps if x > total_exp]
        if over:
            filtered_notice = f"Aviso: se ignoraron checkpoints > total ({over})"
        cps = [x for x in cps if x <= total_exp]
        if include_total_in_table and (not cps or cps[-1] != total_exp):
            cps.append(total_exp)

    if len(cps) > max_detail_rows:
        keep = max_detail_rows - (1 if include_total_in_table else 0)
        step = max(1, len(cps) // keep)
        reduced = cps[::step]
        if len(reduced) > keep:
            reduced = reduced[:keep]
        cps = reduced + ([total_exp] if include_total_in_table and (not reduced or reduced[-1] != total_exp) else [])

    return {
        "total_exp": total_exp,
        "exp_per_cycle": exp_per_cycle,
        "min_sec_per_cycle": min_sec_per_cycle,
        "max_sec_per_cycle": max_sec_per_cycle,
        "cycles_exact": cycles_exact,
        "cycles_needed": cycles_needed,
        "min_total_sec": min_total,
        "max_total_sec": max_total,
        "checkpoints": cps,                 # sin total por defecto
        "filtered_notice": filtered_notice,
        "auto_mode": auto_mode,
    }

# ==============================
# Consola (opcional)
# ==============================

def _print_debug_header(d: Dict[str, Any]) -> None:
    print("=== Debug EXP Report ===")
    print(f"total_exp: {es_miles(d['total_exp'])}")
    print(f"exp_per_cycle: {d['exp_per_cycle']}")
    print(f"Ciclos necesarios (ceil): {d['cycles_needed']}\n")
    print(f"min_sec_per_cycle: {d['min_sec_per_cycle']}")
    print(f"Tiempo total mínimo: {format_hms(d['min_total_sec'])}\n")
    print(f"max_sec_per_cycle: {d['max_sec_per_cycle']}")
    print(f"Tiempo total máximo: {format_hms(d['max_total_sec'])}\n")
    if d.get("filtered_notice"):
        print(d["filtered_notice"])

def _print_detail_table(
    checkpoints: List[int],
    exp_per_cycle: int,
    min_sec_per_cycle: int,
    max_sec_per_cycle: int,
) -> None:
    headers = ("Checkpoint", "Ciclos hasta aquí", "Tiempo mínimo", "Tiempo máximo")
    col_w = (14, 20, 16, 16)

    def fmt_row(c1, c2, c3, c4):
        return (
            f"{str(c1):>{col_w[0]}} "
            f"{str(c2):>{col_w[1]}} "
            f"{str(c3):>{col_w[2]}} "
            f"{str(c4):>{col_w[3]}}"
        )

    print(fmt_row(*headers))
    print("-" * sum(col_w) + "-" * 3)

    for cp in checkpoints:
        cycles_here = math.ceil(cp / exp_per_cycle)
        min_here = cycles_here * min_sec_per_cycle
        max_here = cycles_here * max_sec_per_cycle
        print(fmt_row(
            es_miles(cp),
            es_miles(cycles_here),
            format_hms(min_here),
            format_hms(max_here),
        ))

def print_console_exp_report(
    total_exp: int,
    exp_per_cycle: int,
    min_sec_per_cycle: int,
    max_sec_per_cycle: int,
    detail_checkpoints: Optional[Iterable[int]] = None,
) -> None:
    """Imprime por consola Debug + tabla (sin total en la tabla). Funciona dentro y fuera del notebook."""
    d = _compute_plan(
        total_exp, exp_per_cycle, min_sec_per_cycle, max_sec_per_cycle, detail_checkpoints,
        checkpoint_step=5_000,  # default acordado
        max_detail_rows=300,
        include_total_in_table=False,      # regla: sin total
    )
    _print_debug_header(d)
    _print_detail_table(d["checkpoints"], d["exp_per_cycle"], d["min_sec_per_cycle"], d["max_sec_per_cycle"])

# ==============================
# Generación de PDF
# ==============================

def generate_exp_report(
    total_exp: int,
    exp_per_cycle: int,
    min_sec_per_cycle: int,
    max_sec_per_cycle: int,
    detail_checkpoints: Optional[Iterable[int]] = None,
    filename: Optional[str] = None,
    include_question: bool = True,
    *,
    checkpoint_step: int = 5_000,
    max_detail_rows: int = 300,
    question_suffix: str = "Muéstralo en una tabla y en PDF.",
    tz_name: str = "America/Santiago",
    return_data: bool = False,
) -> str | Tuple[str, Dict[str, Any]]:
    """Genera un PDF con resumen de totales y tabla de detalle (sin total en tabla).
    - Cabecera de tabla repetida (repeatRows=1)
    - Si no se indica filename, se genera con timestamp local.
    - Si return_data=True, retorna además un dict compacto con los cálculos.
    """
    _validate_inputs(total_exp, exp_per_cycle, min_sec_per_cycle, max_sec_per_cycle, detail_checkpoints)

    d = _compute_plan(
        total_exp=total_exp,
        exp_per_cycle=exp_per_cycle,
        min_sec_per_cycle=min_sec_per_cycle,
        max_sec_per_cycle=max_sec_per_cycle,
        detail_checkpoints=detail_checkpoints,
        checkpoint_step=checkpoint_step,
        max_detail_rows=max_detail_rows,
        include_total_in_table=False,   # regla: sin total
    )

    if not filename:
        now = datetime.now(ZoneInfo(tz_name)).strftime("%Y%m%d_%H%M")
        filename = f"exp_report_{now}.pdf"

    _ensure_dir_for(filename)

    styles = getSampleStyleSheet()
    style_h1 = styles["Title"]; style_h1.fontName = FONT_NAME
    style_p = styles["BodyText"]; style_p.fontName = FONT_NAME

    doc = SimpleDocTemplate(
        filename, pagesize=letter,
        leftMargin=20*mm, rightMargin=20*mm, topMargin=16*mm, bottomMargin=16*mm
    )
    elements: List[Any] = []

    # Título
    title_text = "Reporte de Progreso de EXP"
    elements.append(Paragraph(title_text, style_h1))
    elements.append(Spacer(1, 6))

    # Consigna (opcional)
    if include_question:
        q_text = (
            f"Resumen de avance hacia {es_miles(total_exp)} EXP @ {exp_per_cycle} EXP/ciclo. "
            f"{question_suffix}"
        )
        elements.append(Paragraph(q_text, style_p))
        elements.append(Spacer(1, 8))

    # Resumen
    resumen_lines = [
        f"<b>Total EXP:</b> {es_miles(d['total_exp'])}",
        f"<b>Ciclos necesarios (ceil):</b> {es_miles(d['cycles_needed'])}",
        f"<b>Tiempo total:</b> {format_hms(d['min_total_sec'])} — {format_hms(d['max_total_sec'])}",
        f"<b>Duración por ciclo (seg):</b> {min_sec_per_cycle} — {max_sec_per_cycle}",
    ]
    elements.append(Paragraph("<br/>".join(resumen_lines), style_p))
    elements.append(Spacer(1, 10))

    if d.get("filtered_notice"):
        elements.append(Paragraph(f"<i>{d['filtered_notice']}</i>", style_p))
        elements.append(Spacer(1, 6))

    # Tabla de detalle (sin total)
    cps: List[int] = d["checkpoints"]
    table_data: List[List[str]] = [["Checkpoint", "Ciclos hasta aquí", "Tiempo mínimo", "Tiempo máximo"]]
    for cp in cps:
        cycles_here = math.ceil(cp / d["exp_per_cycle"])
        min_here = cycles_here * d["min_sec_per_cycle"]
        max_here = cycles_here * d["max_sec_per_cycle"]
        table_data.append([
            es_miles(cp), es_miles(cycles_here), format_hms(min_here), format_hms(max_here)
        ])

    table = Table(table_data, repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F0F2F6")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
        ("FONTSIZE", (0, 0), (-1, 0), 12),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),

        ("BACKGROUND", (0, 1), (-1, -1), colors.whitesmoke),
        ("GRID", (0, 0), (-1, -1), 0.8, colors.HexColor("#C9D1D9")),
        ("LEFTPADDING", (0, 0), (-1, -1), 8),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))

    elements.append(Paragraph("<b>Detalle por checkpoints</b>", style_p))
    elements.append(Spacer(1, 4))
    elements.append(table)

    # Build
    doc.build(
        elements,
        onFirstPage=lambda c, d: _on_page(c, d, title_text, tz_name),
        onLaterPages=lambda c, d: _on_page(c, d, title_text, tz_name),
    )

    if return_data:
        out = {
            "total_exp": d["total_exp"],
            "exp_per_cycle": d["exp_per_cycle"],
            "cycles_needed": d["cycles_needed"],
            "min_total_hms": format_hms(d["min_total_sec"]),
            "max_total_hms": format_hms(d["max_total_sec"]),
            "checkpoints": cps,  # sin total
            "tz_name": tz_name,
            "filename": filename,
        }
        return filename, out

    return filename

print_console_exp_report(57000,60,35,45,[1000,2000,3125,4125,5125,6250,7250,8375,9375,10375])
generate_exp_report(57000,60,35,45,[1000,2000,3125,4125,5125,6250,7250,8375,9375,10375],question_suffix="")
```

</details>

---
<details>
<summary>Nombre Archivo: readme_exp_report_tutorial_final_v2.md</summary>

# Reporte de Tiempo para Alcanzar EXP — Tutorial Final (v2)

Este proyecto genera **un informe en PDF** que estima el **tiempo mínimo y máximo** necesario para alcanzar una cantidad objetivo de puntos de **EXP**, dado el rendimiento por ciclo y el rango de duración por ciclo. Incluye una **tabla de resumen** y una **tabla detallada por checkpoints**.

---

## 📌 Propósito del proyecto
- Calcular **ciclos necesarios** y **tiempos acumulados** (mínimo y máximo) para llegar a un total de EXP.
- Generar un **PDF** con formato claro, encabezados/pies de página, y **tabla de checkpoints** (manual o automática por pasos).
- Servir como **plantilla reutilizable** para distintas consultas de EXP.

## 🧩 Requisitos
- **Python 3.9+** (se usa `zoneinfo` nativo).
- Paquetes:
  - `reportlab`
  - `tzdata` (recomendado en Windows o donde falten datos de zona horaria)
- Sistema con fuentes básicas (Helvetica) disponibles para ReportLab.

## ⚙️ Instalación
```bash
pip install reportlab tzdata
```

> En algunas plataformas, `tzdata` asegura que `America/Santiago` funcione correctamente con `ZoneInfo`.

## 🚀 Uso básico
Ejemplo mínimo de uso en Python:

```python
from exp_report_tutorial_final_v2 import generate_exp_report

# Parámetros principales
total_exp = 57_000
exp_por_ciclo = 60
seg_min_ciclo = 35
seg_max_ciclo = 45

# Genera el PDF
salida = generate_exp_report(
    total_exp,
    exp_por_ciclo,
    seg_min_ciclo,
    seg_max_ciclo,
    filename="reporte_exp.pdf"
)
print("PDF generado en:", salida)
```

## 🔧 Parámetros clave de `generate_exp_report`
- `total_exp` *(int)*: Meta de EXP a alcanzar (p. ej. 57000).
- `exp_per_cycle` *(int)*: EXP que ganas por ciclo (p. ej. 60).
- `min_sec_per_cycle`, `max_sec_per_cycle` *(int)*: Rango de segundos por ciclo (p. ej. 35–45).
- `detail_checkpoints` *(Iterable[int] | None)*: Checkpoints manuales. Si es `None`, se generan **automáticos** por `checkpoint_step`.
- `filename` *(str)*: Ruta/archivo de salida del PDF.
- `include_question` *(bool)*: Incluye la frase de la “pregunta del usuario” al inicio.
- `checkpoint_step` *(int, default 10_000)*: Paso de EXP para checkpoints automáticos.
- `max_detail_rows` *(int, default 300)*: Límite superior de filas detalladas (se poda si excede).
- `question_suffix` *(str)*: Texto extra que se agrega a la “pregunta” mostrada.
- `tz_name` *(str)*: Zona horaria para el sello de fecha/hora del PDF (por defecto `America/Santiago`).
- `ensure_total_in_detail` *(bool | None)*: Si `True`, asegura que el último checkpoint sea `total_exp`. En modo manual, se agrega si falta; en modo auto, se añade si no cae exacto. Si `None`, se activa automáticamente cuando se usan checkpoints automáticos.

## 🧪 Ejemplos de ejecución
1. **Automático por pasos y PDF básico:**
   ```python
   generate_exp_report(57_000, 60, 35, 45, filename="test.pdf")
   ```

2. **Automático con paso personalizado y sufijo de pregunta:**
   ```python
   generate_exp_report(
       57_000, 60, 35, 45,
       checkpoint_step=10_000,
       question_suffix="Incluye tiempos aproximados y ciclos totales.",
       filename="test.pdf"
   )
   ```

3. **Manual con checkpoints específicos:**
   ```python
   generate_exp_report(
       57_000, 60, 35, 45,
       detail_checkpoints=[1_000, 2_000, 3_125, 4_125, 5_125, 6_250, 7_250, 8_375, 9_375, 10_375],
       filename="test.pdf"
   )
   ```

4. **Control de poda en tablas muy largas:**
   ```python
   generate_exp_report(
       100_000, 50, 30, 40,
       checkpoint_step=500,
       max_detail_rows=200,
       filename="test.pdf"
   )
   ```

5. **Desactivar inclusión automática del total final (modo auto):**
   ```python
   generate_exp_report(
       57_000, 60, 35, 45,
       checkpoint_step=8_000,
       ensure_total_in_detail=False,
       filename="test.pdf"
   )
   ```

> Para depuración, si está disponible en el notebook, puedes usar `debug_exp_report(...)` para imprimir la construcción de checkpoints y tiempos sin generar PDF.

---

## 📚 Explicación de funciones (guion de 5 puntos)
### `format_hms`
1️⃣ **Propósito:** Convertir segundos totales a una cadena con formato HH:MM:SS.

2️⃣ **Uso básico:** Llama `format_hms(segundos)` y recibe un string como `"01:23:45"`.

3️⃣ **Notas técnicas:** Redondea los segundos al entero más cercano, luego divide en horas, minutos y segundos con enteros (// y %).

4️⃣ **Ejemplo extra:**
```python
format_hms(3661)  # '01:01:01'
```

5️⃣ **Relación con otras partes:** Se usa para mostrar tiempos mínimos/máximos en las tablas del PDF que genera `generate_exp_report`.
### `es_miles`
1️⃣ **Propósito:** Formatear enteros con separador de miles estilo español (puntos).

2️⃣ **Uso básico:** Usa `es_miles(57000)` y devuelve `'57.000'`.

3️⃣ **Notas técnicas:** Internamente usa la formateación con coma y luego reemplaza `,` por `.` para miles.

4️⃣ **Ejemplo extra:**
```python
es_miles(1234567)  # '1.234.567'
```

5️⃣ **Relación con otras partes:** Se usa para títulos y celdas, haciendo más legibles los números grandes en el PDF.
### `_ensure_dir_for`
1️⃣ **Propósito:** Garantizar que exista el directorio donde se guardará el PDF.

2️⃣ **Uso básico:** Se invoca con la ruta final, p.ej. `_ensure_dir_for('out/reportes/r1.pdf')`.

3️⃣ **Notas técnicas:** Usa `os.path.dirname` y `os.makedirs(..., exist_ok=True)`; no hace nada si ya existe.

4️⃣ **Ejemplo extra:**
```python
_ensure_dir_for('salida/pdfs/demo.pdf')
```

5️⃣ **Relación con otras partes:** Es llamada por `generate_exp_report` antes de crear el PDF.
### `_validate_inputs`
1️⃣ **Propósito:** Validar tipos y rangos de los parámetros y normalizar los checkpoints.

2️⃣ **Uso básico:** La llama `generate_exp_report` al inicio y retorna la lista de checkpoints ordenada y sin duplicados.

3️⃣ **Notas técnicas:** Exige enteros positivos para EXP/ciclos/tiempos; `min_sec_per_cycle <= max_sec_per_cycle`. Si `detail_checkpoints` es `None`, devuelve lista vacía.

4️⃣ **Ejemplo extra:**
```python
_validate_inputs(57000, 60, 35, 45, [1000, 3000, 2000])  # -> [1000, 2000, 3000]
```

5️⃣ **Relación con otras partes:** Alimenta el cálculo de la tabla detallada dentro de `generate_exp_report`.
### `_on_page`
1️⃣ **Propósito:** Dibujar encabezado y pie de página en cada hoja del PDF.

2️⃣ **Uso básico:** Se pasa como `onFirstPage` y `onLaterPages` a ReportLab.

3️⃣ **Notas técnicas:** Imprime el título a la izquierda; a la derecha, fecha/hora local (ZoneInfo) y número de página.

4️⃣ **Ejemplo extra:**
```python
# Usado internamente por generate_exp_report con SimpleDocTemplate.build(...)
```

5️⃣ **Relación con otras partes:** Permite estilo consistente en todas las páginas generadas por `generate_exp_report`.
### `generate_exp_report`
1️⃣ **Propósito:** Generar un PDF con resumen y tabla detallada de tiempos para alcanzar cierta EXP.

2️⃣ **Uso básico:** Llamar con parámetros mínimos: `generate_exp_report(total_exp, exp_per_cycle, min_sec, max_sec, filename='reporte.pdf')`.

3️⃣ **Notas técnicas:** Calcula ciclos necesarios (ceil), tiempo mínimo/máximo, arma checkpoints (automáticos por step o dados por el usuario), recorta filas si superan `max_detail_rows`. Usa ReportLab para tablas/estilos.

4️⃣ **Ejemplo extra:**
```python
generate_exp_report(
    57_000, 60, 35, 45,
    checkpoint_step=10_000,
    question_suffix="Incluye tiempos aproximados y ciclos totales.",
    filename="reporte_demo.pdf"
)
```

5️⃣ **Relación con otras partes:** Es la función principal: usa todas las utilidades anteriores y devuelve la ruta/nombre del PDF generado.
### `debug_exp_report`
1️⃣ **Propósito:** Mostrar por consola el detalle del preproceso (checkpoints, ciclos, tiempos) sin generar PDF.

2️⃣ **Uso básico:** Llama `debug_exp_report(...)` con los mismos parámetros que `generate_exp_report`.

3️⃣ **Notas técnicas:** Imprime el flujo de cálculo, realiza podas de checkpoints y muestra tiempos total mínimo/máximo formateados.

4️⃣ **Ejemplo extra:**
```python
debug_exp_report(
    10_001, 100, 35, 45,
    detail_checkpoints=[10_001],
    checkpoint_step=10_000
)
```

5️⃣ **Relación con otras partes:** Útil para verificar cómo `generate_exp_report` va a construir la tabla; comparte la misma lógica de validación y armado de checkpoints.


---

## 🧱 Dependencias
- **reportlab** — creación de documentos PDF (tablas, estilos, layout).
- **tzdata** — datos de zona horaria (útil en sistemas sin base de zonas).
- **zoneinfo** — zona horaria nativa de Python 3.9+.
- **datetime**, **math**, **os**, **typing** — utilidades estándar.

---

## 🗂️ Código completo (con separación de celdas)

> A continuación se incluye el contenido de todas las **celdas de código** del notebook `exp_report_tutorial_final_v2.ipynb`. Cada celda está separada por la marca literal:
>
> `# ---- NUEVA CELDA ----`

```python
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfgen import canvas as canvas_mod
from reportlab.lib.units import mm
from zoneinfo import ZoneInfo  # Zona horaria precisa (Python 3.9+)
import os
import math
from datetime import datetime
from typing import Iterable, List, Optional
# ---- NUEVA CELDA ----
def format_hms(seconds: float) -> str:
    seconds = int(round(seconds))
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"
# ---- NUEVA CELDA ----
def es_miles(n: int) -> str:
    s = f"{int(n):,}"
    return s.replace(",", ".")
# ---- NUEVA CELDA ----
def _ensure_dir_for(path: str) -> None:
    directory = os.path.dirname(os.path.abspath(path))
    if directory and not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
# ---- NUEVA CELDA ----
def _validate_inputs(
    total_exp: int,
    exp_per_cycle: int,
    min_sec_per_cycle: int,
    max_sec_per_cycle: int,
    detail_checkpoints: Optional[Iterable[int]]
) -> List[int]:
    for name, val in [
        ("total_exp", total_exp),
        ("exp_per_cycle", exp_per_cycle),
        ("min_sec_per_cycle", min_sec_per_cycle),
        ("max_sec_per_cycle", max_sec_per_cycle),
    ]:
        if not isinstance(val, int):
            raise TypeError(f"{name} debe ser int.")
        if val <= 0:
            raise ValueError(f"{name} debe ser > 0.")
    if min_sec_per_cycle > max_sec_per_cycle:
        raise ValueError("min_sec_per_cycle no puede ser mayor que max_sec_per_cycle.")
    if detail_checkpoints is None:
        return []
    cps = list(detail_checkpoints)
    if any((not isinstance(x, int) or x <= 0) for x in cps):
        raise ValueError("Todos los detail_checkpoints deben ser enteros positivos.")
    cps = sorted(set(cps))
    return cps
# ---- NUEVA CELDA ----
def _on_page(canvas: canvas_mod.Canvas, doc, title_text: str, tz_name: str):
    canvas.saveState()
    canvas.setFont("Helvetica", 9)
    # Encabezado (título)
    canvas.drawString(15 * mm, 285 * mm, title_text)
    # Pie con fecha local y número de página
    now_str = datetime.now(ZoneInfo(tz_name)).strftime("%Y-%m-%d %H:%M")
    page_str = f"Generado: {now_str}  |  Página {doc.page}"
    canvas.drawRightString(200 * mm, 10 * mm, page_str)
    canvas.restoreState()
# ---- NUEVA CELDA ----
def generate_exp_report(
    total_exp: int,
    exp_per_cycle: int,
    min_sec_per_cycle: int,
    max_sec_per_cycle: int,
    detail_checkpoints: Optional[Iterable[int]] = None,
    filename: str = "exp_report.pdf",
    include_question: bool = True,
    *,
    checkpoint_step: int = 10_000,
    max_detail_rows: int = 300,
    question_suffix: str = "Muéstralo en una tabla y en PDF.",
    tz_name: str = "America/Santiago",
    ensure_total_in_detail: Optional[bool] = None,
) -> str:
    cps = _validate_inputs(
        total_exp, exp_per_cycle, min_sec_per_cycle, max_sec_per_cycle, detail_checkpoints
    )
    if not isinstance(checkpoint_step, int) or checkpoint_step <= 0:
        raise ValueError("checkpoint_step debe ser un entero positivo.")
    if not isinstance(max_detail_rows, int) or max_detail_rows <= 0:
        raise ValueError("max_detail_rows debe ser un entero positivo.")

    cycles_exact = total_exp / exp_per_cycle
    cycles_needed = math.ceil(cycles_exact)
    min_total = cycles_needed * min_sec_per_cycle
    max_total = cycles_needed * max_sec_per_cycle

    auto_mode = (detail_checkpoints is None)
    if ensure_total_in_detail is None:
        ensure_total_in_detail = auto_mode

    if auto_mode:
        last = (total_exp // checkpoint_step) * checkpoint_step
        steps = list(range(checkpoint_step, last + 1, checkpoint_step))
        if ensure_total_in_detail and (not steps or steps[-1] != total_exp):
            steps.append(total_exp)
        cps = steps
    else:
        if ensure_total_in_detail and cps and cps[-1] != total_exp:
            cps = cps + [total_exp]

    if len(cps) > max_detail_rows:
        keep = max_detail_rows - 1
        stride = max(1, (len(cps) - 1) // keep)
        reduced = cps[:-1:stride]
        if len(reduced) > keep:
            reduced = reduced[:keep]
        cps = reduced + [cps[-1]]

    _ensure_dir_for(filename)
    styles = getSampleStyleSheet()
    title_text = f"Cálculo de tiempo para alcanzar {es_miles(total_exp)} EXP"
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []

    if include_question:
        question = (
            f"Pregunta del usuario: ¿Cuánto tiempo demora alcanzar {es_miles(total_exp)} puntos de EXP "
            f"si gano {exp_per_cycle} EXP cada {min_sec_per_cycle} a {max_sec_per_cycle} segundos?"
        )
        if question_suffix:
            question += f" {question_suffix}"
        elements.append(Paragraph(question, styles["Normal"]))
        elements.append(Spacer(1, 12))

    elements.append(Paragraph(title_text, styles["Title"]))
    elements.append(Spacer(1, 12))

    summary_data = [
        ["Total EXP requerida", es_miles(total_exp)],
        ["EXP por ciclo", f"{exp_per_cycle}"],
        ["Ciclos necesarios", f"{cycles_needed}"],
        [f"Tiempo mínimo ({min_sec_per_cycle}s por ciclo)", format_hms(min_total)],
        [f"Tiempo máximo ({max_sec_per_cycle}s por ciclo)", format_hms(max_total)],
    ]
    summary_table = Table(summary_data, colWidths=[280, 220])
    summary_style = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 12),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ])
    summary_table.setStyle(summary_style)
    elements.append(summary_table)
    elements.append(Spacer(1, 24))

    elements.append(Paragraph("Detalles por puntos de EXP acumulada", styles["Title"]))
    elements.append(Spacer(1, 12))
    detailed_data = [["EXP acumulada", "Ciclos necesarios", "Tiempo mínimo", "Tiempo máximo"]]
    for pts in cps:
        cyc_needed = math.ceil(pts / exp_per_cycle)
        min_t = cyc_needed * min_sec_per_cycle
        max_t = cyc_needed * max_sec_per_cycle
        detailed_data.append([es_miles(pts), f"{cyc_needed}", format_hms(min_t), format_hms(max_t)])

    detailed_table = Table(detailed_data, colWidths=[150, 150, 150, 150], repeatRows=1)
    detailed_style = TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 12),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ])
    detailed_table.setStyle(detailed_style)
    elements.append(detailed_table)

    doc.build(
        elements,
        onFirstPage=lambda c, d: _on_page(c, d, title_text, tz_name),
        onLaterPages=lambda c, d: _on_page(c, d, title_text, tz_name),
    )
    return filename
# ---- NUEVA CELDA ----
def debug_exp_report(
    total_exp: int,
    exp_per_cycle: int,
    min_sec_per_cycle: int,
    max_sec_per_cycle: int,
    detail_checkpoints=None,
    *,
    checkpoint_step: int = 10_000,
    tz_name: str = "America/Santiago",
    max_detail_rows: int = 300,
    ensure_total_in_detail: Optional[bool] = None,
):
    print("=== Debug EXP Report ===")
    print("total_exp:", total_exp)
    print("exp_per_cycle:", exp_per_cycle)
    print("min_sec_per_cycle:", min_sec_per_cycle)
    print("max_sec_per_cycle:", max_sec_per_cycle)
    print("detail_checkpoints:", detail_checkpoints)
    print("checkpoint_step:", checkpoint_step)
    print("tz_name:", tz_name)
    print("max_detail_rows:", max_detail_rows)
    print("ensure_total_in_detail:", ensure_total_in_detail)

    auto_mode = (detail_checkpoints is None)
    print("Modo automático?:", auto_mode)

    if ensure_total_in_detail is None:
        ensure_total_in_detail = auto_mode

    if auto_mode:
        last = (total_exp // checkpoint_step) * checkpoint_step
        cps = list(range(checkpoint_step, last + 1, checkpoint_step))
        if ensure_total_in_detail and (not cps or cps[-1] != total_exp):
            cps.append(total_exp)
    else:
        cps = sorted(set(detail_checkpoints))
        if ensure_total_in_detail and cps[-1] != total_exp:
            cps.append(total_exp)

    if len(cps) > max_detail_rows:
        keep = max_detail_rows - 1
        stride = max(1, (len(cps) - 1) // keep)
        reduced = cps[:-1:stride]
        if len(reduced) > keep:
            reduced = reduced[:keep]
        cps = reduced + [cps[-1]]

    print("Checkpoints finales:", cps)
    print("Cantidad de filas detalladas:", len(cps))

    cycles_exact = total_exp / exp_per_cycle
    cycles_needed = math.ceil(cycles_exact)
    min_total = cycles_needed * min_sec_per_cycle
    max_total = cycles_needed * max_sec_per_cycle
    print("Ciclos necesarios (ceil):", cycles_needed)
    print("Tiempo total mínimo:", format_hms(min_total))
    print("Tiempo total máximo:", format_hms(max_total))
    print("==========================")
# ---- NUEVA CELDA ----
debug_exp_report(57000,60,35,45,[1000,2000,3125,4125,5125,6250,7250,8375,9375,10375])
generate_exp_report(57000,60,35,45,[1000,2000,3125,4125,5125,6250,7250,8375,9375,10375],question_suffix="")
# ---- NUEVA CELDA ----
pdf_path = generate_exp_report(
    total_exp=57000,
    exp_per_cycle=60,
    min_sec_per_cycle=35,
    max_sec_per_cycle=45,
    detail_checkpoints=[1000, 2000, 3125, 4125, 5125, 6250, 7250, 8375, 9375, 10375],
    filename="cálculo_exp.pdf",
    include_question=True,
)
print("PDF generado en:", pdf_path)
# ---- NUEVA CELDA ----
generate_exp_report(57000, 60, 35, 45,
    detail_checkpoints=[1000, 2000, 3125],
    filename="test.pdf")
# ---- NUEVA CELDA ----
generate_exp_report(57000, 60, 35, 45,
    checkpoint_step=10_000,
    filename="test.pdf")
# ---- NUEVA CELDA ----
generate_exp_report(57000, 60, 35, 45,
    checkpoint_step=5_000,
    filename="test.pdf")
# ---- NUEVA CELDA ----
generate_exp_report(57000, 60, 35, 45,
    detail_checkpoints=[1000, 2000, 3000],
    ensure_total_in_detail=True,
    filename="test.pdf")
# ---- NUEVA CELDA ----
generate_exp_report(57000, 60, 35, 45,
    include_question=False,
    filename="test.pdf")
# ---- NUEVA CELDA ----
generate_exp_report(57000, 60, 35, 45,
    tz_name="America/Santiago",
    filename="test.pdf")
# ---- NUEVA CELDA ----
generate_exp_report(57000, 60, 35, 45,
    tz_name="America/New_York",
    filename="test.pdf")
# ---- NUEVA CELDA ----
generate_exp_report(1_000_000, 60, 35, 45,
    checkpoint_step=1_000,
    max_detail_rows=120,
    filename="test.pdf")
# ---- NUEVA CELDA ----
debug_exp_report(57000, 60, 35, 45,
    detail_checkpoints=None, checkpoint_step=10_000)
# ---- NUEVA CELDA ----
debug_exp_report(57000, 60, 35, 45,
    detail_checkpoints=[1000, 2500, 5000])
# ---- NUEVA CELDA ----
debug_exp_report(
    total_exp=57000,
    exp_per_cycle=60,
    min_sec_per_cycle=35,
    max_sec_per_cycle=45,
    detail_checkpoints=[1000, 2000, 3125, 4125, 5125, 6250, 7250, 8375, 9375, 10375],
)
# ---- NUEVA CELDA ----
generate_exp_report(7_000, 60, 35, 45,
    checkpoint_step=10_000,
    filename="test.pdf")
# ---- NUEVA CELDA ----
generate_exp_report(57_000, 60, 35, 45,
    checkpoint_step=8_000,
    filename="test.pdf")
# ---- NUEVA CELDA ----
try:
    generate_exp_report(57000, 60, 50, 40, filename="test.pdf")
except Exception as e:
    print("OK (se esperaba error):", e)
# ---- NUEVA CELDA ----
generate_exp_report(57000, 60, 35, 45,
    filename="out/pdfs/test.pdf")
# ---- NUEVA CELDA ----
generate_exp_report(57000, 60, 35, 45,
    detail_checkpoints=[3000, 1000, 3000, 2000, 1500],
    filename="test.pdf")
# ---- NUEVA CELDA ----
debug_exp_report(10_001, 100, 35, 45,
    detail_checkpoints=[10_001])
# ---- NUEVA CELDA ----
generate_exp_report(57000, 60, 35, 45,
    question_suffix="Incluye tiempos aproximados y ciclos totales.",
    filename="test.pdf")
# ---- NUEVA CELDA ----
generate_exp_report(100_000, 50, 30, 40,
    checkpoint_step=500,
    max_detail_rows=200,
    filename="test.pdf")
# ---- NUEVA CELDA ----
generate_exp_report(57_000, 60, 35, 45,
    checkpoint_step=10_000,
    ensure_total_in_detail=False,
    filename="test.pdf")

```

---

*Archivo generado automáticamente el 2025-10-05 17:47:44.*

</details>

---
<details>
<summary>Nombre Archivo: readme_print_console_exp_report.md</summary>

# readme_print_console_exp_report.md

## 📌 Propósito del proyecto
Este mini-módulo imprime en **consola** un reporte de experiencia (EXP) estimando cuántos ciclos necesitas y cuánto tiempo total tomaría completarlos, considerando un rango de segundos por ciclo. También puede mostrar **checkpoints** intermedios para ver tiempos parciales.

## ✅ Requisitos
- **Python** 3.8+
- Sistema operativo con terminal/consola (Windows, macOS o Linux).

## 🧩 Dependencias
No requiere paquetes externos. Solo usa la librería estándar de Python (`math`, `typing`).

## 🔧 Instalación
1. Copia el archivo `print_console_exp_report.py` en tu proyecto (o mantenlo junto a tu script principal).
2. (Opcional) Colócalo en la raíz del proyecto para poder importarlo con facilidad.

## ▶️ Uso básico
### 1) Importando y llamando a la función principal
```python
from print_console_exp_report import print_console_exp_report

print_console_exp_report(
    57000, 60, 35, 45,
    [1000, 2000, 3125, 4125, 5125, 6250, 7250, 8375, 9375, 10375]
)
```

### 2) Ejecución directa desde una sola línea (sin crear archivos adicionales)
```bash
python -c python -c "from print_console_exp_report import debug_exp_report; debug_exp_report(57000,60,35,45)"
```

## 🧪 Ejemplos de ejecución
#### A) Con checkpoints manuales
```python
from print_console_exp_report import print_console_exp_report

print_console_exp_report(
    57000, 60, 35, 45,
    [1000, 2000, 3125, 4125, 5125, 6250, 7250, 8375, 9375, 10375]
)
```
#### B) En una sola línea (sin archivos extra)
```bash
python -c python -c "from print_console_exp_report import debug_exp_report; debug_exp_report(57000,60,35,45)"
```

---

## 🔍 Explicación de cada función (guion de 5 puntos)

### 1. `format_hms(seconds: int) -> str`
**1️⃣ Propósito**  
Convierte segundos enteros en formato `HH:MM:SS` con cero padding.

**2️⃣ Uso básico**  
```python
format_hms(3661)  # '01:01:01'
```

**3️⃣ Notas técnicas**  
- Redondea al entero más cercano y convierte a `int`.
- Calcula horas, minutos y segundos con divisiones y módulos.
- Devuelve una cadena con formato fijo `02d` por componente.

**4️⃣ Ejemplo extra**  
```python
format_hms(9)     # '00:00:09'
format_hms(5400)  # '01:30:00'
```

**5️⃣ Relación con otras partes**  
Se usa para imprimir tiempos mínimos/máximos, tanto en el encabezado del reporte como en la tabla de detalle.

---

### 2. `es_miles(n: int) -> str`
**1️⃣ Propósito**  
Formatea números enteros con separador de miles **punto** (ej.: `57.000`).

**2️⃣ Uso básico**  
```python
es_miles(57000)  # '57.000'
```

**3️⃣ Notas técnicas**  
- Usa formato con comas y luego reemplaza `,` por `.` para locales hispanos.
- Enfocado a enteros (casting explícito).

**4️⃣ Ejemplo extra**  
```python
es_miles(1234567)  # '1.234.567'
```

**5️⃣ Relación con otras partes**  
Se emplea en el encabezado y tabla para legibilidad de `total_exp`, `ciclos`, y checkpoints.

---

### 3. `_compute_plan(...) -> Dict[str, Any]`
**1️⃣ Propósito**  
Calcular el plan completo del reporte de EXP: ciclos exactos/requeridos y tiempos totales mínimo/máximo, además de la lista de checkpoints.

**2️⃣ Uso básico**  
```python
_compute_plan(57000, 60, 35, 45, [1000, 2000, 3125])
```

**3️⃣ Notas técnicas**  
- Valida tipos y que los parámetros numéricos sean `> 0`; también que `min_sec_per_cycle <= max_sec_per_cycle`.
- `cycles_exact = total_exp / exp_per_cycle`; `cycles_needed = ceil(cycles_exact)`.
- `min_total_sec = cycles_needed * min_sec_per_cycle`; `max_total_sec = cycles_needed * max_sec_per_cycle`.
- Si `detail_checkpoints` es `None` (modo automático), genera checkpoints en múltiplos de `checkpoint_step` (por defecto `5_000`) hasta `total_exp`.
- Si se excede `max_detail_rows`, reduce la lista manteniendo una muestra uniforme.
- Devuelve un diccionario con campos clave (ciclos, tiempos, checkpoints, bandera `auto_mode` y `filtered_notice`).

**4️⃣ Ejemplo extra**  
```python
data = _compute_plan(57000, 60, 35, 45, [1000, 2000, 3125])
data["cycles_needed"]       # 950
data["min_total_sec"]       # 33250 (=> 09:14:10)
data["max_total_sec"]       # 42750 (=> 11:52:30)
```

**5️⃣ Relación con otras partes**  
Es el núcleo de cálculo; lo consume `debug_exp_report` para imprimir encabezado y tabla de detalles.

---

### 4. `_print_debug_header(d: Dict[str, Any]) -> None`
**1️⃣ Propósito**  
Imprimir el **resumen** del reporte (valores globales, tiempos totales).

**2️⃣ Uso básico**  
```python
d = _compute_plan(57000, 60, 35, 45, None)
_print_debug_header(d)
```

**3️⃣ Notas técnicas**  
- Muestra `total_exp`, `exp_per_cycle`, `cycles_needed` y tiempos totales `min/max` formateados.
- Si hay `filtered_notice`, también lo imprime.
- Depende de `es_miles` y `format_hms` para presentar.

**4️⃣ Ejemplo extra**  
```python
d = _compute_plan(10000, 100, 40, 50, None)
_print_debug_header(d)
```

**5️⃣ Relación con otras partes**  
Es llamado por `debug_exp_report` antes de la tabla de detalles.

---

### 5. `_print_detail_table(checkpoints: List[int], exp_per_cycle: int, min_sec_per_cycle: int, max_sec_per_cycle: int) -> None`
**1️⃣ Propósito**  
Imprimir una **tabla** de progreso con ciclos y tiempos al alcanzar cada checkpoint.

**2️⃣ Uso básico**  
```python
_print_detail_table([5000, 10000], 60, 35, 45)
```

**3️⃣ Notas técnicas**  
- Para cada checkpoint, calcula `ceil(cp / exp_per_cycle)` y sus tiempos min/máx.
- Alinea columnas con anchos fijos para una salida legible.
- Usa `es_miles` y `format_hms` en cada fila.

**4️⃣ Ejemplo extra**  
```python
_print_detail_table([1000, 2000, 3000], 120, 20, 30)
```

**5️⃣ Relación con otras partes**  
La invoca `debug_exp_report` tras imprimir el encabezado.

---

### 6. `debug_exp_report(..., return_data=False, verbose=True)`
**1️⃣ Propósito**  
Generar el reporte **completo** (encabezado + tabla) en consola y, opcionalmente, devolver los datos calculados.

**2️⃣ Uso básico**  
```python
debug_exp_report(57000, 60, 35, 45, [1000, 2000])
```

**3️⃣ Notas técnicas**  
- Internamente llama a `_compute_plan`.
- Si `verbose` es `True`, imprime encabezado y detalle.
- Si `return_data` es `True`, devuelve el diccionario calculado en lugar de `None`.

**4️⃣ Ejemplo extra**  
```python
d = debug_exp_report(8000, 80, 30, 40, None, return_data=True, verbose=False)
d["auto_mode"]  # True
```

**5️⃣ Relación con otras partes**  
Función de **alto nivel** para depuración; `print_console_exp_report` es un wrapper simplificado sobre ella.

---

### 7. `print_console_exp_report(..., detail_checkpoints: Optional[Iterable[int]] = None) -> None`
**1️⃣ Propósito**  
Atajo para imprimir el reporte en consola con la configuración dada (modo simple).

**2️⃣ Uso básico**  
```python
print_console_exp_report(57000, 60, 35, 45, [1000, 2000, 3125])
```

**3️⃣ Notas técnicas**  
- Simplemente llama a `debug_exp_report(..., return_data=False, verbose=True)`.
- No devuelve datos; su efecto es colateral (impresión en consola).

**4️⃣ Ejemplo extra**  
```python
print_console_exp_report(15000, 90, 40, 55)  # sin checkpoints: modo automático
```

**5️⃣ Relación con otras partes**  
Es la interfaz **más directa** para uso cotidiano en scripts o pruebas rápidas.

---

## 🗂️ Código completo
```python
from typing import Iterable, Optional, List, Dict, Any
import math

def format_hms(seconds: int) -> str:
    seconds = int(round(seconds))
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def es_miles(n: int) -> str:
    s = f"{int(n):,}"
    return s.replace(",", ".")

def _compute_plan(total_exp: int, exp_per_cycle: int, min_sec_per_cycle: int, max_sec_per_cycle: int,
                  detail_checkpoints: Optional[Iterable[int]], *, checkpoint_step: int = 5_000, max_detail_rows: int = 300) -> Dict[str, Any]:
    for name, val in [("total_exp", total_exp), ("exp_per_cycle", exp_per_cycle),
                      ("min_sec_per_cycle", min_sec_per_cycle), ("max_sec_per_cycle", max_sec_per_cycle)]:
        if not isinstance(val, int): raise TypeError(f"{name} debe ser int.")
        if val <= 0: raise ValueError(f"{name} debe ser > 0.")
    if min_sec_per_cycle > max_sec_per_cycle:
        raise ValueError("min_sec_per_cycle no puede ser mayor que max_sec_per_cycle.")
    cycles_exact = total_exp / exp_per_cycle
    cycles_needed = math.ceil(cycles_exact)
    min_total = cycles_needed * min_sec_per_cycle
    max_total = cycles_needed * max_sec_per_cycle
    filtered_notice = None
    auto_mode = (detail_checkpoints is None)
    if auto_mode:
        last = (total_exp // checkpoint_step) * checkpoint_step
        cps = list(range(checkpoint_step, last + 1, checkpoint_step))
    else:
        cps = sorted({int(x) for x in detail_checkpoints if int(x) > 0})
        over = [x for x in cps if x > total_exp]
        if over: filtered_notice = f"Aviso: se ignoraron checkpoints > total ({over})"
        cps = [x for x in cps if x <= total_exp]
    if len(cps) > max_detail_rows:
        keep = max_detail_rows
        step = max(1, len(cps) // keep)
        cps = cps[::step][:keep]
    return {
        "total_exp": total_exp, "exp_per_cycle": exp_per_cycle, "min_sec_per_cycle": min_sec_per_cycle, "max_sec_per_cycle": max_sec_per_cycle,
        "cycles_exact": cycles_exact, "cycles_needed": cycles_needed, "min_total_sec": min_total, "max_total_sec": max_total,
        "checkpoints": cps, "filtered_notice": filtered_notice, "auto_mode": auto_mode
    }

def _print_debug_header(d: Dict[str, Any]):
    print("=== Debug EXP Report ===")
    print(f"total_exp: {es_miles(d['total_exp'])}")
    print(f"exp_per_cycle: {d['exp_per_cycle']}")
    print(f"Ciclos necesarios (ceil): {d['cycles_needed']}\n")
    print(f"min_sec_per_cycle: {d['min_sec_per_cycle']}")
    print(f"Tiempo total mínimo: {format_hms(d['min_total_sec'])}\n")
    print(f"max_sec_per_cycle: {d['max_sec_per_cycle']}")
    print(f"Tiempo total máximo: {format_hms(d['max_total_sec'])}\n")
    if d.get("filtered_notice"): print(d["filtered_notice"])

def _print_detail_table(checkpoints: List[int], exp_per_cycle: int, min_sec_per_cycle: int, max_sec_per_cycle: int):
    headers = ("Checkpoint", "Ciclos hasta aquí", "Tiempo mínimo", "Tiempo máximo")
    col_w = (14, 20, 16, 16)
    def fmt_row(c1, c2, c3, c4):
        return (f"{str(c1):>{col_w[0]}} {str(c2):>{col_w[1]}} {str(c3):>{col_w[2]}} {str(c4):>{col_w[3]}}")
    print(fmt_row(*headers))
    print("-" * sum(col_w) + "-" * 3)
    for cp in checkpoints:
        cycles_here = math.ceil(cp / exp_per_cycle)
        min_here = cycles_here * min_sec_per_cycle
        max_here = cycles_here * max_sec_per_cycle
        print(fmt_row(es_miles(cp), es_miles(cycles_here), format_hms(min_here), format_hms(max_here)))

def debug_exp_report(total_exp: int, exp_per_cycle: int, min_sec_per_cycle: int, max_sec_per_cycle: int,
                     detail_checkpoints: Optional[Iterable[int]] = None, *, checkpoint_step: int = 5_000,
                     max_detail_rows: int = 300, return_data: bool = False, verbose: bool = True):
    d = _compute_plan(total_exp, exp_per_cycle, min_sec_per_cycle, max_sec_per_cycle,
                      detail_checkpoints, checkpoint_step=checkpoint_step, max_detail_rows=max_detail_rows)
    if verbose:
        _print_debug_header(d)
        _print_detail_table(d["checkpoints"], d["exp_per_cycle"], d["min_sec_per_cycle"], d["max_sec_per_cycle"])
    return d if return_data else None

def print_console_exp_report(total_exp: int, exp_per_cycle: int, min_sec_per_cycle: int, max_sec_per_cycle: int,
                             detail_checkpoints: Optional[Iterable[int]] = None):
    debug_exp_report(total_exp, exp_per_cycle, min_sec_per_cycle, max_sec_per_cycle,
                     detail_checkpoints, return_data=False, verbose=True)
```

---

## ℹ️ Notas finales
- Si solo pasas `None` en `detail_checkpoints`, el módulo entra en **modo automático** y genera checkpoints cada `5.000` EXP (configurable vía `checkpoint_step` dentro de `debug_exp_report`).  
- Si la lista de checkpoints es muy grande, se reducirá para mantener la salida legible (`max_detail_rows`, por defecto `300`).

</details>

---
<details>
<summary>Nombre Archivo: readme_debug_exp_report.md</summary>

# Debug EXP Report

Herramienta en Python para calcular el tiempo necesario para alcanzar un total de EXP bajo un modelo de ciclos con duración mínima y máxima.

## Propósito
Calcular y mostrar, en consola, un reporte legible con:
- Ciclos necesarios para alcanzar `total_exp` dado `exp_per_cycle`.
- Tiempo total mínimo y máximo considerando `min_sec_per_cycle` y `max_sec_per_cycle`.
- (Opcional) Tabla de *checkpoints* con ciclos y tiempos estimados por hito.

---

## Instalación
Requisitos:
- Python 3.8 o superior.
- Sin dependencias externas.

Descarga los archivos `exp_report.py` y `README.md` y colócalos en una carpeta de tu preferencia.

---

## Uso

### 🧠 Ejemplo 1 — Importando desde Python

```python
from exp_report import debug_exp_report

# Solo resumen general
debug_exp_report(57000, 60, 35, 45)

# Con checkpoints (opcionales)
debug_exp_report(
    57000, 60, 35, 45,
    detail_checkpoints=[1000, 2000, 3125, 4125, 5125, 6250, 7250, 8375, 9375, 10375],
)
```

**Salida esperada — sin checkpoints:**

```
=== Debug EXP Report ===
total_exp: 57.000
exp_per_cycle: 60
Ciclos necesarios (ceil): 950

min_sec_per_cycle: 35
Tiempo total mínimo: 09:14:10

max_sec_per_cycle: 45
Tiempo total máximo: 11:52:30
```

**Salida esperada — con checkpoints:**

```
=== Debug EXP Report ===
total_exp: 57.000
exp_per_cycle: 60
Ciclos necesarios (ceil): 950

min_sec_per_cycle: 35
Tiempo total mínimo: 09:14:10

max_sec_per_cycle: 45
Tiempo total máximo: 11:52:30

    Checkpoint    Ciclos hasta aquí    Tiempo mínimo    Tiempo máximo
---------------------------------------------------------------------
         1.000                   17         00:09:55         00:12:45
         2.000                   34         00:19:50         00:25:30
         3.125                   53         00:30:55         00:39:45
         4.125                   69         00:40:15         00:51:45
         5.125                   86         00:50:10         01:04:30
         6.250                  105         01:01:15         01:18:45
         7.250                  121         01:10:35         01:30:45
         8.375                  140         01:21:40         01:45:00
         9.375                  157         01:31:35         01:57:45
        10.375                  173         01:40:55         02:09:45
```

---

### 💻 Ejemplo 2 — Ejecución desde consola con bloque `__main__`

El archivo `exp_report.py` incluye el siguiente bloque ejecutable:

```python
# --- Bloque ejecutable desde consola ---
if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Uso: python exp_report.py total_exp exp_per_cycle min_sec max_sec [checkpoints...]")
        print("Ejemplo: python exp_report.py 57000 60 35 45 1000 2000 3125 4125 5125")
        sys.exit(1)
    total_exp = int(sys.argv[1])
    exp_per_cycle = int(sys.argv[2])
    min_sec_per_cycle = int(sys.argv[3])
    max_sec_per_cycle = int(sys.argv[4])
    detail_checkpoints = [int(x) for x in sys.argv[5:]] if len(sys.argv) > 5 else None
    debug_exp_report(total_exp, exp_per_cycle, min_sec_per_cycle, max_sec_per_cycle, detail_checkpoints)
```

#### 🧩 Ejemplo sin checkpoints

Comando:
```bash
python exp_report.py 57000 60 35 45
```

**Salida esperada:**
```
=== Debug EXP Report ===
total_exp: 57.000
exp_per_cycle: 60
Ciclos necesarios (ceil): 950

min_sec_per_cycle: 35
Tiempo total mínimo: 09:14:10

max_sec_per_cycle: 45
Tiempo total máximo: 11:52:30
```

#### 🧩 Ejemplo con checkpoints

Comando:
```bash
python exp_report.py 57000 60 35 45 1000 2000 3125 4125 5125 6250 7250 8375 9375 10375
```

**Salida esperada:**
```
=== Debug EXP Report ===
total_exp: 57.000
exp_per_cycle: 60
Ciclos necesarios (ceil): 950

min_sec_per_cycle: 35
Tiempo total mínimo: 09:14:10

max_sec_per_cycle: 45
Tiempo total máximo: 11:52:30

    Checkpoint    Ciclos hasta aquí    Tiempo mínimo    Tiempo máximo
---------------------------------------------------------------------
         1.000                   17         00:09:55         00:12:45
         2.000                   34         00:19:50         00:25:30
         3.125                   53         00:30:55         00:39:45
         4.125                   69         00:40:15         00:51:45
         5.125                   86         00:50:10         01:04:30
         6.250                  105         01:01:15         01:18:45
         7.250                  121         01:10:35         01:30:45
         8.375                  140         01:21:40         01:45:00
         9.375                  157         01:31:35         01:57:45
        10.375                  173         01:40:55         02:09:45
```

---

## Dependencias
No tiene dependencias externas.

---

## Ejecución rápida
También puedes ejecutar desde una sola línea sin crear archivos adicionales:

```bash
python -c "from exp_report import debug_exp_report; debug_exp_report(57000,60,35,45)"
```

O bien usando el bloque `__main__` del propio script:

```bash
python exp_report.py 57000 60 35 45
```


---

# 📘 Documentación técnica detallada de funciones

# Explicación de funciones del archivo `exp_report.py`

Este documento describe cada función del archivo, siguiendo el formato de 5 puntos:  
**1️⃣ Propósito, 2️⃣ Uso básico, 3️⃣ Notas técnicas, 4️⃣ Ejemplo extra, 5️⃣ Relación con otras partes.**

---

## 1. `format_hms(total_seconds: float) -> str`

### 1️⃣ Propósito
Convierte una cantidad total de segundos en un formato legible de horas, minutos y segundos (`HH:MM:SS`).

### 2️⃣ Uso básico
Se usa para mostrar duraciones totales o parciales en formato legible dentro del reporte.

```python
format_hms(3670)  # Devuelve '01:01:10'
```

### 3️⃣ Notas técnicas
- Redondea los segundos al entero más cercano.
- Usa `divmod` para dividir en horas, minutos y segundos.
- Siempre devuelve una cadena de longitud fija con ceros a la izquierda.

### 4️⃣ Ejemplo extra
```python
print(format_hms(59))      # '00:00:59'
print(format_hms(3605.4))  # '01:00:05'
```

### 5️⃣ Relación con otras partes
Usada por `_compute_plan` para formatear el tiempo total y los tiempos en cada checkpoint.

---

## 2. `_format_thousands(n: int) -> str`

### 1️⃣ Propósito
Formatea números grandes con separador de miles como punto (`.`), facilitando la lectura.

### 2️⃣ Uso básico
Se usa para mostrar valores de EXP y checkpoints en el reporte.

```python
_format_thousands(57000)  # '57.000'
```

### 3️⃣ Notas técnicas
- Usa el formato de cadena `f"{n:,}"` para agregar comas y luego las reemplaza por puntos.
- Solo acepta enteros.

### 4️⃣ Ejemplo extra
```python
print(_format_thousands(1234567))  # '1.234.567'
```

### 5️⃣ Relación con otras partes
Se utiliza dentro de `_compute_plan` para imprimir EXP totales y checkpoints con formato.

---

## 3. `_validate_inputs(...)`

### 1️⃣ Propósito
Verifica que los parámetros de entrada sean válidos antes de procesar el reporte.

### 2️⃣ Uso básico
Se ejecuta automáticamente desde `debug_exp_report` para asegurar que los valores sean coherentes y positivos.

### 3️⃣ Notas técnicas
- Comprueba que todos los valores numéricos sean enteros mayores que 0.
- Verifica que `min_sec_per_cycle <= max_sec_per_cycle`.
- Si existen checkpoints, valida que todos sean enteros positivos.
- Lanza `ValueError` con mensajes claros en caso de error.

### 4️⃣ Ejemplo extra
```python
_validate_inputs(57000, 60, 35, 45, [1000, 2000])
# No lanza error

_validate_inputs(-100, 60, 35, 45, None)
# Lanza ValueError: total_exp debe ser int > 0
```

### 5️⃣ Relación con otras partes
Llamada desde `debug_exp_report` antes de `_compute_plan`, asegurando que el cálculo se ejecute con datos válidos.

---

## 4. `_compute_plan(...) -> str`

### 1️⃣ Propósito
Genera el texto completo del reporte de experiencia (EXP), calculando tiempos mínimos y máximos.

### 2️⃣ Uso básico
Produce un informe detallado con los tiempos y ciclos requeridos, que luego se imprime por `debug_exp_report`.

### 3️⃣ Notas técnicas
- Usa `ceil()` para redondear hacia arriba el número de ciclos necesarios.
- Calcula los tiempos totales mínimo y máximo multiplicando por segundos por ciclo.
- Si hay checkpoints, genera una tabla con tiempos parciales.
- Internamente utiliza `_format_thousands` y `format_hms`.

### 4️⃣ Ejemplo extra
```python
print(_compute_plan(57000, 60, 35, 45, [1000, 2000, 3125]))
```

Salida simplificada:
```
=== Debug EXP Report ===
total_exp: 57.000
exp_per_cycle: 60
Ciclos necesarios (ceil): 950

min_sec_per_cycle: 35
Tiempo total mínimo: 09:15:50

max_sec_per_cycle: 45
Tiempo total máximo: 11:52:30
```

### 5️⃣ Relación con otras partes
Es el núcleo lógico del programa, usado por `debug_exp_report` tras pasar las validaciones.

---

## 5. `debug_exp_report(...) -> None`

### 1️⃣ Propósito
Función principal del módulo: valida entradas, calcula el plan y muestra el resultado en consola.

### 2️⃣ Uso básico
Se llama directamente por el usuario para generar un informe rápido del tiempo estimado de progreso.

```python
debug_exp_report(57000, 60, 35, 45, [1000, 2000, 3125])
```

### 3️⃣ Notas técnicas
- Combina las funciones `_validate_inputs` y `_compute_plan`.
- No devuelve valor, solo imprime el resultado.
- Ideal para depuración o uso interactivo.

### 4️⃣ Ejemplo extra
```python
debug_exp_report(10000, 50, 30, 40)
```

Salida:
```
=== Debug EXP Report ===
total_exp: 10.000
exp_per_cycle: 50
Ciclos necesarios (ceil): 200
...
```

### 5️⃣ Relación con otras partes
Es la interfaz de usuario principal: coordina validación y generación del reporte.

---

© 2025 — Documento generado automáticamente por ChatGPT GPT‑5.

</details>

---
<details>
<summary>Nombre Archivo: readme_Análisis_de_tiempos_de_EXP_por_checkpoints.md</summary>

# 🎯 **Análisis de tiempos de EXP por checkpoints**

> This README was generated from a Jupyter notebook, keeping the original structure, code, and outputs where possible.

## Table of Contents

    - [🧮 Explicación del código: *Cálculo de tiempos de EXP con checkpoints*](#explicación-del-código-cálculo-de-tiempos-de-exp-con-checkpoints)
      - [1️⃣ Propósito](#1-propósito)
      - [2️⃣ Uso básico](#2-uso-básico)
      - [3️⃣ Notas técnicas](#3-notas-técnicas)
      - [4️⃣ Ejemplo extra](#4-ejemplo-extra)
    - [🧩 Explicación: cómo mover el total (57000) fuera de la tabla](#explicación-cómo-mover-el-total-57000-fuera-de-la-tabla)
      - [1️⃣ Extraer el “total” del final de la lista](#1-extraer-el-total-del-final-de-la-lista)
      - [2️⃣ Calcular los tiempos del total (antes de la tabla)](#2-calcular-los-tiempos-del-total-antes-de-la-tabla)
      - [3️⃣ Excluir el total de la tabla con *slicing*](#3-excluir-el-total-de-la-tabla-con-slicing)
      - [4️⃣ Mantener el formato de tabla](#4-mantener-el-formato-de-tabla)
      - [5️⃣ Por qué esto logra lo que querías](#5-por-qué-esto-logra-lo-que-querías)
      - [6️⃣ Cambios mínimos realizados](#6-cambios-mínimos-realizados)
      - [7️⃣ Consideraciones opcionales](#7-consideraciones-opcionales)
- [🎯 **Análisis de tiempos de EXP por checkpoints**](#análisis-de-tiempos-de-exp-por-checkpoints)
    - [📘 Descripción general](#descripción-general)
  - [⚙️ **1. Parámetros iniciales**](#1-parámetros-iniciales)
- [Checkpoints dados](#checkpoints-dados)
- [Velocidad mínima y máxima (EXP/segundo)](#velocidad-mínima-y-máxima-expsegundo)
  - [⏱️ **2. Cálculo del tiempo total**](#2-cálculo-del-tiempo-total)
- [Calcular tiempo total](#calcular-tiempo-total)
  - [📊 **3. Detalle de tiempos por checkpoint**](#3-detalle-de-tiempos-por-checkpoint)
  - [🧩 **4. Observaciones técnicas**](#4-observaciones-técnicas)
  - [📈 **5. Ejemplo de salida esperada**](#5-ejemplo-de-salida-esperada)
  - [🧠 **6. Interpretación**](#6-interpretación)
  - [🏁 **7. Conclusión**](#7-conclusión)

### 🧮 Explicación del código: *Cálculo de tiempos de EXP con checkpoints*

#### 1️⃣ Propósito  
El objetivo del script es **calcular cuánto tiempo se tarda en alcanzar diferentes cantidades de puntos de experiencia (EXP)**, llamados *checkpoints*, según una tasa de ganancia variable (entre 35 y 45 segundos por cada 60 EXP).  
Esto permite estimar tanto el tiempo **mínimo (jugando rápido)** como el **máximo (jugando lento)** para llegar a cada meta de EXP.

---

#### 2️⃣ Uso básico  
1. Se definen los *checkpoints* (por ejemplo: 1000, 2000, 3125, etc.).  
2. Se establecen las **velocidades mínima y máxima** en EXP por segundo:  
   ```python
   exp_min = 60 / 45   # lento → 1.33 EXP/s
   exp_max = 60 / 35   # rápido → 1.71 EXP/s
   ```
3. El código recorre cada checkpoint, calcula los segundos necesarios según ambas velocidades y convierte el resultado a formato legible (`h:m:s`) mediante la función `segundos_a_hms()`.  
4. Finalmente, imprime una tabla comparativa con tres columnas:
   - Checkpoint (EXP)
   - Tiempo mínimo (jugando rápido)
   - Tiempo máximo (jugando lento)

---

#### 3️⃣ Notas técnicas  
- **Conversión de segundos a formato h:m:s**:  
  ```python
  def segundos_a_hms(segundos):
      h = int(segundos // 3600)
      m = int((segundos % 3600) // 60)
      s = int(segundos % 60)
      return f"{h}h {m}m {s}s" if h > 0 else f"{m}m {s}s"
  ```
  Esta función transforma los segundos totales en horas, minutos y segundos, y omite las horas si son cero.

- **Cálculo del tiempo:**  
  - Tiempo mínimo = `checkpoint / exp_max`  
  - Tiempo máximo = `checkpoint / exp_min`  

- **Formato de salida:**  
  El uso de `f-strings` con alineación (`:<15`) produce una tabla limpia y legible.

---

#### 4️⃣ Ejemplo extra  
Si añadimos un nuevo checkpoint de **10,000 EXP**, el código calcularía:  
```python
cp = 10000
t_min = cp / exp_max   # rápido
t_max = cp / exp_min   # lento
print(segundos_a_hms(t_min), segundos_a_hms(t_max))
```
👉 Resultado aproximado:  
`1h 37m 55s` (rápido) — `2h 5m 15s` (lento)


```python
# Cálculo de tiempos de EXP con checkpoints

# Checkpoints dados
checkpoints = [1000, 2000, 3125, 4125, 5125, 6250, 7250, 8375, 9375, 10375, 57000]

# Velocidad mínima y máxima (EXP/segundo)
exp_min = 60 / 45   # 1.33 EXP/s (lento)
exp_max = 60 / 35   # 1.71 EXP/s (rápido)

def segundos_a_hms(segundos):
    h = int(segundos // 3600)
    m = int((segundos % 3600) // 60)
    s = int(segundos % 60)
    return f"{h}h {m}m {s}s" if h > 0 else f"{m}m {s}s"

print(f"{'Checkpoint (EXP)':<15} {'Tiempo mínimo':<15} {'Tiempo máximo':<15}")
print("-" * 45)

for cp in checkpoints:
    t_min = cp / exp_max  # más rápido
    t_max = cp / exp_min  # más lento
    print(f"{cp:<15} {segundos_a_hms(t_min):<15} {segundos_a_hms(t_max):<15}")

```

<details>
<summary><strong>Output</strong></summary>


```
Checkpoint (EXP) Tiempo mínimo   Tiempo máximo  
---------------------------------------------
1000            9m 43s          12m 30s        
2000            19m 26s         25m 0s         
3125            30m 22s         39m 3s         
4125            40m 6s          51m 33s        
5125            49m 49s         1h 4m 3s       
6250            1h 0m 45s       1h 18m 7s      
7250            1h 10m 29s      1h 30m 37s     
8375            1h 21m 25s      1h 44m 41s     
9375            1h 31m 8s       1h 57m 11s     
10375           1h 40m 52s      2h 9m 41s      
57000           9h 14m 10s      11h 52m 30s
```

</details>

### 🧩 Explicación: cómo mover el total (57000) fuera de la tabla

---

#### 1️⃣ Extraer el “total” del final de la lista
```python
total_exp = checkpoints[-1]
```
- `checkpoints[-1]` toma el **último elemento** de la lista (indexado negativo en Python).  
- Asumimos que la lista está **ordenada de menor a mayor** y que el **último** es la meta total (57 000).  
- Esto es **O(1)** y **no modifica** la lista original.

> 💡 Alternativa más robusta si la lista no siempre está ordenada:
> ```python
> total_exp = max(checkpoints)
> ```
> (Así no dependes del orden de los elementos.)

---

#### 2️⃣ Calcular los tiempos del total (antes de la tabla)
```python
t_min_total = total_exp / exp_max   # tiempo en escenario rápido
t_max_total = total_exp / exp_min   # tiempo en escenario lento
```
- Misma lógica que en la tabla:
  - “Rápido” ⇒ más EXP/seg ⇒ **menos tiempo** ⇒ dividir por `exp_max`.
  - “Lento” ⇒ menos EXP/seg ⇒ **más tiempo** ⇒ dividir por `exp_min`.

Luego se imprime al inicio, antes del detalle:
```python
print(f"Meta total: {total_exp} EXP")
print(f"Tiempo estimado total: {segundos_a_hms(t_min_total)} (mínimo) — {segundos_a_hms(t_max_total)} (máximo)")
print("\nDetalle por checkpoint:\n")
```
De esta forma, el total se muestra **como resumen principal** antes de la tabla.

---

#### 3️⃣ Excluir el total de la tabla con *slicing*
```python
for cp in checkpoints[:-1]:
    ...
```
- `checkpoints[:-1]` devuelve todos los elementos **menos el último**.  
- Así **no repetimos** el 57 000 dentro de la tabla.  
- Esto **no altera** la lista original.

> 💡 Si no sabes cuál es el último o usaste `max(checkpoints)`, puedes eliminarlo así:
> ```python
> total_exp = max(checkpoints)
> cp_list = checkpoints.copy()
> cp_list.remove(total_exp)
> ```
> De esa manera, la variable `cp_list` contiene todos los valores **excepto el total**.

---

#### 4️⃣ Mantener el formato de tabla
```python
print(f"{'Checkpoint (EXP)':<15} {'Tiempo mínimo':<15} {'Tiempo máximo':<15}")
print("-" * 45)
```
- Se mantiene la **alineación de columnas** con `:<15` (f-strings).  
- El bucle sigue calculando los tiempos con la **misma fórmula** y formato legible con `segundos_a_hms()`.

---

#### 5️⃣ Por qué esto logra lo que querías
- El **total se imprime primero** con su rango de tiempo, sirviendo como **resumen general**.  
- La **tabla solo contiene los checkpoints parciales**, ya que excluimos el último elemento del bucle.  
- No se cambia la lógica de cálculo, solo **el orden en que se muestra la información**.

---

#### 6️⃣ Cambios mínimos realizados
- ✅ Nuevo bloque para imprimir el total antes de la tabla.  
- ✅ En el `for`, se usa `checkpoints[:-1]` para **excluir el último elemento**.  
- ❌ Nada más cambia: ni funciones ni fórmulas.

---

#### 7️⃣ Consideraciones opcionales
- Si quieres **resaltar visualmente** el total en la consola, puedes usar ANSI:
  ```python
  BOLD = "\033[1m"; RESET = "\033[0m"
  print(f"{BOLD}Meta total: {total_exp} EXP{RESET}")
  ```
- La función `segundos_a_hms` hace **truncamiento** (`int`).  
  Si prefieres **redondear** los segundos, puedes usar:
  ```python
  segundos = round(segundos)
  ```

---

✅ Con esto consigues que la **meta total se muestre arriba como resumen**, y la **tabla solo detalle los progresos parciales**, manteniendo el formato y la claridad del resultado.


```python
# Cálculo de tiempos de EXP con checkpoints

# Checkpoints dados
checkpoints = [1000, 2000, 3125, 4125, 5125, 6250, 7250, 8375, 9375, 10375, 57000]

# Velocidad mínima y máxima (EXP/segundo)
exp_min = 60 / 45   # 1.33 EXP/s (lento)
exp_max = 60 / 35   # 1.71 EXP/s (rápido)

def segundos_a_hms(segundos):
    h = int(segundos // 3600)
    m = int((segundos % 3600) // 60)
    s = int(segundos % 60)
    return f"{h}h {m}m {s}s" if h > 0 else f"{m}m {s}s"

# --- Mostrar primero el total final ---
total_exp = checkpoints[-1]
t_min_total = total_exp / exp_max
t_max_total = total_exp / exp_min

print(f"Meta total: {total_exp} EXP")
print(f"Tiempo estimado total: {segundos_a_hms(t_min_total)} (mínimo) — {segundos_a_hms(t_max_total)} (máximo)")
print("\nDetalle por checkpoint:\n")

# --- Mostrar tabla de checkpoints (sin el último valor) ---
print(f"{'Checkpoint (EXP)':<15} {'Tiempo mínimo':<15} {'Tiempo máximo':<15}")
print("-" * 45)

for cp in checkpoints[:-1]:  # Excluye el último
    t_min = cp / exp_max
    t_max = cp / exp_min
    print(f"{cp:<15} {segundos_a_hms(t_min):<15} {segundos_a_hms(t_max):<15}")

```

<details>
<summary><strong>Output</strong></summary>


```
Meta total: 57000 EXP
Tiempo estimado total: 9h 14m 10s (mínimo) — 11h 52m 30s (máximo)

Detalle por checkpoint:

Checkpoint (EXP) Tiempo mínimo   Tiempo máximo  
---------------------------------------------
1000            9m 43s          12m 30s        
2000            19m 26s         25m 0s         
3125            30m 22s         39m 3s         
4125            40m 6s          51m 33s        
5125            49m 49s         1h 4m 3s       
6250            1h 0m 45s       1h 18m 7s      
7250            1h 10m 29s      1h 30m 37s     
8375            1h 21m 25s      1h 44m 41s     
9375            1h 31m 8s       1h 57m 11s     
10375           1h 40m 52s      2h 9m 41s
```

</details>

# 🎯 **Análisis de tiempos de EXP por checkpoints**

---

### 📘 Descripción general
Este notebook calcula el **tiempo estimado necesario para alcanzar distintos puntos de experiencia (EXP)**,  
considerando una velocidad de ganancia variable entre **35 y 45 segundos por cada 60 EXP**.  

El objetivo es estimar el rango de tiempo —entre el **mínimo (más rápido)** y el **máximo (más lento)**—  
necesario para alcanzar cada checkpoint y la **meta total final de 57,000 EXP**.  

---

## ⚙️ **1. Parámetros iniciales**
Aquí se definen los valores base del cálculo:  
- Lista de *checkpoints* (valores de EXP objetivo).  
- Velocidades mínima y máxima de ganancia.  
- Función auxiliar para convertir segundos a un formato legible (`h:m:s`).

```python
# Checkpoints dados
checkpoints = [1000, 2000, 3125, 4125, 5125, 6250, 7250, 8375, 9375, 10375, 57000]

# Velocidad mínima y máxima (EXP/segundo)
exp_min = 60 / 45   # 1.33 EXP/s (lento)
exp_max = 60 / 35   # 1.71 EXP/s (rápido)

def segundos_a_hms(segundos):
    """Convierte una cantidad de segundos en formato h:m:s"""
    h = int(segundos // 3600)
    m = int((segundos % 3600) // 60)
    s = int(segundos % 60)
    return f"{h}h {m}m {s}s" if h > 0 else f"{m}m {s}s"
```

---

## ⏱️ **2. Cálculo del tiempo total**
Antes de mostrar el detalle, se calcula el **tiempo total estimado para llegar a la meta final (57,000 EXP)**  
en los escenarios más rápido y más lento.

```python
# Calcular tiempo total
total_exp = checkpoints[-1]
t_min_total = total_exp / exp_max
t_max_total = total_exp / exp_min

print(f"Meta total: {total_exp} EXP")
print(f"Tiempo estimado total: {segundos_a_hms(t_min_total)} (mínimo) — {segundos_a_hms(t_max_total)} (máximo)")
```

---

## 📊 **3. Detalle de tiempos por checkpoint**
En esta tabla se muestra cuánto tarda en alcanzarse cada checkpoint individual,  
excluyendo la meta final (que ya se muestra arriba como resumen general).

```python
print("\nDetalle por checkpoint:\n")
print(f"{'Checkpoint (EXP)':<15} {'Tiempo mínimo':<15} {'Tiempo máximo':<15}")
print("-" * 45)

for cp in checkpoints[:-1]:  # excluye el total final
    t_min = cp / exp_max
    t_max = cp / exp_min
    print(f"{cp:<15} {segundos_a_hms(t_min):<15} {segundos_a_hms(t_max):<15}")
```

---

## 🧩 **4. Observaciones técnicas**
- El cálculo usa los intervalos de ganancia de **35–45 segundos por 60 EXP**.  
- `exp_min` y `exp_max` representan la **velocidad de ganancia de experiencia** (EXP/seg).  
- La función `segundos_a_hms()` formatea los segundos a un formato legible (`h:m:s`).  
- El último valor de la lista (`57000`) se imprime **antes** de la tabla, como **meta general**.  
- El uso de `checkpoints[:-1]` evita duplicar el total dentro de la tabla.  

---

## 📈 **5. Ejemplo de salida esperada**
```
Meta total: 57000 EXP
Tiempo estimado total: 9h 14m 10s (mínimo) — 11h 52m 30s (máximo)

Detalle por checkpoint:

Checkpoint (EXP) Tiempo mínimo   Tiempo máximo  
---------------------------------------------
1000            9m 43s          12m 30s        
2000            19m 26s         25m 0s         
3125            30m 22s         39m 3s         
4125            40m 6s          51m 33s        
5125            49m 49s         1h 4m 3s       
6250            1h 0m 45s       1h 18m 7s      
7250            1h 10m 29s      1h 30m 37s     
8375            1h 21m 25s      1h 44m 41s     
9375            1h 31m 8s       1h 57m 11s     
10375           1h 40m 52s      2h 9m 41s      
```

---

## 🧠 **6. Interpretación**
Cada checkpoint indica el tiempo acumulado necesario para alcanzar una cierta cantidad de EXP,  
dentro de un rango de velocidad posible.  
Esto permite estimar el **ritmo de progreso** en sesiones o etapas.

---

## 🏁 **7. Conclusión**
El tiempo total estimado para alcanzar los **57,000 EXP** varía entre:  
- 🔹 **9 horas 14 minutos (jugando rápido)**  
- 🔹 **11 horas 52 minutos (jugando lento)**  

Estos cálculos permiten **planificar mejor el progreso** dentro de un sistema o juego basado en experiencia,  
evaluando cuánto esfuerzo o tiempo requiere llegar a una meta concreta.

---

✨ *Notebook preparado y documentado por [SXNTI / Proyecto Peluca]* ✨


---

_Auto-converted on build time. If you need tweaks (e.g., hide code, keep only outputs, or reorganize sections), let me know._

</details>

---
