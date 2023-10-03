import requests
import json
import boto3

class bedrock():
    def get_model_list_json(self):
      bedrock = boto3.client(
          service_name = "bedrock",
          region_name= "us-west-2"
      )

      api_response = bedrock.list_foundation_models()
      model_list_json = json.dumps(api_response , indent = 2)
      print(model_list_json)
      model_list_json = json.loads(model_list_json)

      return model_list_json
    
    def invoke_model(prompt)):
      bedrock_runtime = boto3.client(
          service_name='bedrock-runtime', 
          region_name='us-west-2'
      )

      modelId = 'ai21.j2-ultra-v1' 
      accept = 'application/json'
      contentType = 'application/json'

      body = json.dumps(
          {"prompt": f"{prompt}", 
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