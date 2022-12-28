# AutomateDownloadsFolder

Order all your files in any folder, saving them in sub directories like: word, powerpoint, rar.

# Download

---

## Installation of dependencies 
`pip install -r requeriments.txt`

---

## Features / config file
`json/informacion.json`

### Parameters
- **limiteDias:** Number of days that the files will be in the folder until being ordered

- **enviarAPapelera:** Determine if the files will be sent to the trash or will be permanently deleted

- **limiteTamanio:** Max weight of files that the script will order

- **rutas/rutaOrigen:** Determines what is the origin folder to order

- **rutas/rutaDestino:** Determines what is the destinarion

- **extensiones:** The extensions folders what will be created and destinarion of the ordered files 

---
## Program operation

The program will read all your files in the origin path and will register their name and the date they were read. 

The script will read the logs and determines which files have passed the allowed number of days selected in order to delete them / send to trash them
