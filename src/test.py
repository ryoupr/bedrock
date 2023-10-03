from libs.bedrock import bedrock
import json 
import boto3

bedrock_runtime = boto3.client(
    service_name='bedrock-runtime', 
    region_name='us-west-2'
)

modelId = 'ai21.j2-ultra-v1' 
accept = 'application/json'
contentType = 'application/json'

body = json.dumps(
    {"prompt": "こんにちわ", 
     "maxTokens": 200,
     "temperature": 0.7,
     "topP": 1,
    }
)

response = bedrock_runtime.invoke_model(
    body=body, 
	modelId=modelId, 
	accept=accept, 
	contentType=contentType
)

response_body = json.loads(response.get('body').read())
outputText = response_body.get('completions')[0].get('data').get('text')
print(outputText)