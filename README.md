# Simple Serverless Project

Este repositorio te ayuda a inicializar un proyecto en Python utilizando Serverless Application Model (SAM) + AWS Lambda + DynamoDB + Poetry y Github Actions.

## ¿Cómo usar la plantilla?

Una vez inicializado tu repositorio, necesitas definir las siguientes variables de entorno en Github Actions:

- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_REGION
- AWS_ACCOUNT_ID
- AWS_SAM_STACK_NAME
- AWS_SAM_S3_BUCKET

## ¿Cómo probar localmente con SAM?

Para probar localmente, necesitas tener instalado Docker y SAM CLI. Una vez instalado, ejecuta el siguiente comando:

```bash
sam local start-api
```

## ¿Cómo desplegar en AWS?

Dentro de la plantilla se agregó un archivo de Github Actions que te permite desplegar automáticamente en AWS. Para ello, necesitas definir las variables de entorno mencionadas anteriormente.

Si eliges desplegar desde tu computadora, puedes utilizar directamente el comando de SAM CLI:

```bash
sam deploy --guided
```

## ¿Cómo agregar dependencias?

Para agregar dependencias, necesitas utilizar Poetry. Para ello, ejecuta el siguiente comando:

```bash
poetry add <nombre-de-la-dependencia>
```

## ¿Cómo ejecutar los tests?

Esta plantilla utiliza Pytest para ejecutar las pruebas, para ello, ejecuta el siguiente comando:

```bash
poetry run pytest
```
