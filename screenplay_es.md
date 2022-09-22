Guión
=========

# Intro

Tradicionalmente uno crea programas que funcionan de forma síncrona que para
ciertos escenarios no es eficiente. La aplicación de asíncronismo más común es
para manejar recursos bloqueantes. Dos analogías muy citadas:

- Restaurante: Cuando un cliente pide una comida, el mesero va a la cocina a
  dejar la órden pero no se queda esperando a que la comida esté lista para
  llevarla a la mesa. Después de dejar la órden, sale a atender a los demás
  clientes mientras se preparan los platos.
- Tareas domésticas: Cuando se mete la ropa a la lavadora, no necesariamente
  tenemos que esperar a que termine de lavar. Podemos ir a hacer otra
  actividad.

El uso de la lavadora y la preparación de platos en la cocina son recursos
bloqueantes los cuales no necesitan nuestra atención.

# Conceptos básicos

Solo una comparación de dos programas que hacen lo mismo.

```bash
python m00_sync.py
python m01_sync.py
time python m00_sync.py
time python m01_sync.py
```

Al llamar la corutina su código no se ejecuta.

```python
import m01_async
m01_async.task()
# no sucede nada
import asyncio
asyncio.run(m01_async.task())

cor = m01_async.task()
asyncio.run(cor)
```

Ejemplo `m02_say_after.py` se demora 3 segundos.

```bash
python m02_say_after.py
time python m02_say_after.py
```
Ejemplo `m03_say_after.py` se demora 2 segundos. Al transformar la corutina en
`Task`, el código se prepara para ejecución.

```bash
python m03_say_after_task.py
time python m03_say_after_task.py
```

Depurar `m03...`.

Con `Task` las corutinas son gestionables, por ejemplo, se pueden cancelar.

```bash
python m04_cancel.py
```

Ejemplo `m05....` se demora 4 segundos.

```bash
time python m05_sync_blocking.py
```

Ejemplo `m06...` se demora 1 segundo.

```bash
time python m06_async_multiple.py
```

Ejemplo `m07...` para mostrar sintaxis de `async with`.

# Web App Demo

Tenemos un recurso bloqueante que puede representar un API externo o una base
de datos. El recurso se demora 5 segundos en responder cada petición.

```
/blocking_resource$ ./run.sh
time curl localhost:8000/blocking-resource
```

Flask corre de manera síncrona. Un solo worker solo es capaz de procesar una
petición a la vez.

```
/sync_flask$ ./run.sh 1
time curl localhost:8001/resource
# x2 time curl...
```

`run_clients.py` realizara n peticiones en "paralelo" con un límite de tiempo
de 7 segundo. Cada petición respresenta un usuario/cliente. El código se
mostrará después.

```
./run_clients.py 8001 -n 1  # pasa
./run_clients.py 8001 -n 4  # no pasa
```

Toca incrementar el número de workers.

```
/sync_flask$ ./run.sh 5
./run_clients.py 8001 -n 4  # pasa
./run_clients.py 8001 -n 10  # no pasa
```

Con FastAPI no hay que especificar workers.

```
/async_fastapi$ ./run.sh
./run_clients.py 8002 -n 1  # pasa
./run_clients.py 8002 -n 4  # pasa
./run_clients.py 8002 -n 10  # pasa
```

Lo malo de `asyncio` es que toca saber que operaciones son síncronas y cuales
no.

```
# Hacer cambio en app.py
/async_fastapi$ ./run.sh
./run_clients.py 8002 -n 1  # pasa
./run_clients.py 8002 -n 2  # no pasa
```

`run_clients.py` está hecho con `asyncio`.
