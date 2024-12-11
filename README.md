# videogames-local-admin-py

You need python for this proyect

verify it with
python --version

then
pip install -r requirements.txt

to run use:
python main.py

Explicacion:
Entrada de datos JSON e ID:

Un área de texto (Text) para introducir el cuerpo de las solicitudes en formato JSON.
Un campo de entrada (Entry) para introducir el ID, utilizado en las operaciones GET by ID.
Botones CRUD:

Cada botón llama a la función execute_request con el método HTTP (GET, POST, PUT, DELETE) y el endpoint correspondiente.
Botones de eliminación (Delete) verifican si el endpoint pertenece a categories o game-info y, de ser así, muestran un error.
TextArea para resultados:

El resultado de las solicitudes HTTP se muestra en el área de texto (Text), que es de solo lectura para evitar modificaciones accidentales.
Dependencias prohibidas:

Si se intenta eliminar una categoría o información de juegos (game-info), se muestra un error directamente en un messagebox.
