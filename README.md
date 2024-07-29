# Simple Serverless Project

Esta "Github Template" te permitirá generar un proyecto serverless sencillo utilizando Python, AWS SAM y Github Actions (CI/CD).
Por default, está diseñada utilizando la estructura de un proyecto python con Poetry, y toma ventaja de las herramientas como AWS Lambda Layers para reducir la cantidad de código inicial necesario para conectarlo con la plataforma.


## Cómo usar esta plantilla?

Los siguientes comandos te permitirán generar el directorio `dist` que será utilizado para desplegar el proyecto en AWS.

```bash
mkdir -p dist/python/
poetry export -o requirements.txt
pip install . -t dist/python/
```

### Ejecutar la API localmente

Una vez que has instalado las dependencias, puedes ejecutar la API localmente utilizando el siguiente comando:

```bash
sam local start-api
```

Automaticamente, SAM se encargará de levantar un servidor local en el puerto 3000, y podrás acceder a la API en `http://localhost:3000/`. Además intentará utilizar el Layer definido dentro del archivo `template.yaml`.

## Cómo usarla en AWS?

> Esta sección está en construcción.

```bash
sam deploy --guided
```

O una vez que hayas configurado el archivo `samconfig.toml`:

```bash
sam deploy
```
