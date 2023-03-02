# Deploy backend

1. aws cloudformation package --template .\template.yaml --s3-bucket deploy-frontend --output-template-file packaged-template.yaml
2. aws cloudformation deploy --template-file C:\Users\dines\OneDrive\Desktop\infuse\git\Restaurent_management_system\packaged-template.yaml --stack-name fastapi-server-deploy --capabilities CAPABILITY_NAMED_IAM

# Deploy frontend

1. Changed the url for all the request endpoints
2. Build the static site
3. Uplaod static site to S3 bucket
4. Get the Url of the static site
 