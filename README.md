# Pydantic

Pydantic es una **biblioteca de Python** para **validar datos** y realizar **conversiones de tipo** usando *type hints*.  
Permite definir **esquemas de datos** como clases con atributos tipados, donde automáticamente se validan y convierten los datos al tipo correcto.  

Es muy popular en el desarrollo de **APIs con FastAPI**, ya que este framework lo utiliza nativamente para definir modelos de datos.

---

## Beneficios principales

### Validación de datos
- Garantiza que los datos recibidos cumplan con un esquema definido.  
- Evita errores comunes al recibir información inválida.  

### Conversión automática de tipos
- Convierte datos de entrada al tipo correcto siempre que sea posible.  
- Ejemplo: convertir `"123"` en `int(123)`.  

### Documentación de API
- Facilita la documentación automática de APIs al integrarse con FastAPI.  

###  Modelos de datos claros
- Define la estructura de datos de forma limpia y concisa.  

---

## Ventajas de usar Pydantic

- **Código más limpio:** elimina la necesidad de múltiples `if isinstance()` o validaciones manuales.  
- **Mayor seguridad:** evita errores relacionados con datos inválidos.  
- **Desarrollo rápido:** la validación y conversión automática agilizan el trabajo.  
- **Sintaxis intuitiva:** fácil de leer y mantener.  
- **Integración con FastAPI:** hace que crear APIs sea sencillo, robusto y bien documentado.  
