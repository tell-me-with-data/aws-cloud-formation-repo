# INITIAL COMMIT 2021-11-13 11:55:36

## Branch: learning 2021-11-13 11:57:12

- dev-first-stack-cli-1
```
aws cloudformation create-stack --stack-namedev-first-stack-cli-1 --template-body file:///home/bryanprojects/aws/aws-cloud-formation-repo/mydynamo.yml--parameters ParameterKey=DynamoAtributoParameterValue=nombre ParameterKey=NombreDynamoParameterValue=Clientes --profile bryanuser
```