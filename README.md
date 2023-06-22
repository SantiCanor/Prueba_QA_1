# Prueba de Funcionalidades de Login y Registro - Documentación

Este documento proporciona instrucciones y pautas para realizar pruebas de las funcionalidades de login y registro en la página web "https://buggy.justtestit.org/".

## Requisitos previos

- Acceso a la página web "https://buggy.justtestit.org/" en entorno de pruebas.
- Credenciales de prueba proporcionadas por el equipo de desarrollo.

## Configuración del entorno de pruebas

1. Clona el repositorio del proyecto desde GitHub: [https://github.com/SantiCanor/Prueba_QA_1.git].
2. Instala las dependencias del proyecto ejecutando el siguiente comando: `npm install`.


## Casos de prueba

A continuación se detallan los casos de prueba que se deben ejecutar para las funcionalidades de login y registro:

1. **Caso de prueba 1: Registro exitoso**
   - Descripción: Verificar que un nuevo usuario pueda registrarse correctamente.
   - Pasos:
     1. Navegar a la página de registro.
     2. Completar el formulario de registro con datos válidos.
     3. Enviar el formulario.
   - Resultado esperado: El ususario debe recibir una confirmación de registro exitoso.

2. **Caso de prueba 2: Inicio de sesión válido**
   - Descripción: Verificar que un usuario registrado pueda iniciar sesión correctamente.
   - Pasos:
     1. Ingresar las credenciales válidas de un usuario registrado.
     2. Hacer clic en el botón de inicio de sesión.
   - Resultado esperado: El usuario debe ser redirigido a la página de inicio y recibir una confirmación de inicio de sesión exitoso.

## Datos de prueba

Puedes utilizar los siguientes datos de prueba durante las pruebas:

- Nombre de usuario: RamiroVelasquez
- Contraseña: Raminata123

## Configuración de ejecución de pruebas

No se requiere ninguna configuración adicional para ejecutar las pruebas. Simplemente asegúrate de tener un entorno de pruebas apropiado y las credenciales de prueba correctas.

## Resultados y reportes

Registra los resultados de las pruebas en un formato adecuado y genera informes o reportes según sea necesario. Puedes utilizar herramientas de prueba como [Allure] para generar informes detallados.

## Contacto y contribución

Para cualquier pregunta, comentario o sugerencia relacionada con estas pruebas, ponte en contacto con [Santiago Cano] en [santiagocanor@hotmail.com]. También puedes contribuir con mejoras o nuevas pruebas a través de pull requests en el repositorio del proyecto.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# JSON Placeholder API - Ejemplo de solicitud y respuesta

Este código de ejemplo demuestra cómo realizar una solicitud a la API JSON Placeholder y procesar la respuesta.

## Descripción

El código utiliza la biblioteca `requests` para hacer una solicitud GET a la URL `https://jsonplaceholder.typicode.com/todos/1`. Luego, verifica el código de estado de la respuesta para determinar si la solicitud fue exitosa o no. Si el código de estado es 200, el código imprime el mensaje "La solicitud fue exitosa" junto con el código de estado y muestra el contenido JSON de la respuesta. Si el código de estado no es 200, se imprime un mensaje de error junto con el código de estado.

## Requisitos previos

- Python 3.x instalado en tu sistema.
- La biblioteca `requests` instalada. Puedes instalarla ejecutando `pip install requests`.

## Ejecución

1. Clona el repositorio o copia el código en un archivo con extensión `.py`.
2. Abre una terminal o línea de comandos y navega hasta el directorio donde se encuentra el archivo `.py`.
3. Ejecuta el siguiente comando para ejecutar el código: EP_Prueba.py
4. También puedes hacerlo desde tu editor preferido.


## Notas adicionales

- Este código utiliza la API JSON Placeholder como ejemplo, pero puedes modificar la URL para realizar solicitudes a otras APIs según tus necesidades.
- Asegúrate de tener una conexión a Internet activa para realizar la solicitud correctamente.

## Contribución

Si tienes sugerencias de mejora o encuentras algún problema en el código, no dudes en abrir un problema o enviar una solicitud de extracción en este repositorio.
