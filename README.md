# INITIAL COMMIT 2021-11-13 11:55:36

## Branch: learning 2021-11-13 11:57:12

- dev-first-stack-cli-1

    aws cloudformation create-stack --stack-name dev-first-stack-cli-1 --template-body file:///home/bryan/projects/aws/aws-cloud-formation-repo/mydynamo.yml --parameters ParameterKey=DynamoAtributo,ParameterValue=nombre ParameterKey=NombreDynamo,ParameterValue=Clientes --profile bryanuser