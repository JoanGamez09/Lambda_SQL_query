# AWS Lambda - Conexión a MySQL

## Descripción del Proyecto
Esta AWS Lambda está diseñada para conectarse a una base de datos **MySQL** alojada en AWS RDS, ejecutar una consulta para obtener los primeros registros de la tabla `clientes` y devolver los resultados en formato JSON.

---

## Tecnologías Utilizadas
- **AWS Lambda** (para ejecución sin servidor)
- **Amazon RDS / MySQL** (base de datos relacional)
- **PyMySQL** (librería para conectar Python con MySQL)

---

## Flujo de la Lambda

### 1️⃣ **Entrada de Datos**
La Lambda recibe parámetros por medio de un evento como el endpoint de la base de datos, usuario, contraseña, nombre de la base de datos y el puerto.

### 2️⃣ **Conexión a la Base de Datos**
Se establece una conexión con MySQL utilizando las credenciales proporcionadas y se ejecuta una consulta para obtener registros de la tabla `clientes`.

### 3️⃣ **Respuesta de la Lambda**
Los resultados se devuelven en un JSON con un código de estado indicando éxito o error.

---



