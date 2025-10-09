# gridly.LqaModelApi

All URIs are relative to *https://api.gridly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lqa_model**](LqaModelApi.md#get_lqa_model) | **GET** /v1/lqa-models | Get default lqa model


# **get_lqa_model**
> LQAModelResponse get_lqa_model(project_id=project_id)

Get default lqa model

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.lqa_model_response import LQAModelResponse
from gridly.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.gridly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = gridly.Configuration(
    host = "https://api.gridly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKey
configuration.api_key['ApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with gridly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gridly.LqaModelApi(api_client)
    project_id = 56 # int |  (optional)

    try:
        # Get default lqa model
        api_response = api_instance.get_lqa_model(project_id=project_id)
        print("The response of LqaModelApi->get_lqa_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LqaModelApi->get_lqa_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **int**|  | [optional] 

### Return type

[**LQAModelResponse**](LQAModelResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

