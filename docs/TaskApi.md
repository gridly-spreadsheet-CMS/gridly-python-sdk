# gridly.TaskApi

All URIs are relative to *https://api.gridly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](TaskApi.md#get) | **GET** /v1/tasks/{taskId} | get


# **get**
> Task get(task_id)

get

get

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import task_api
from gridly.model.task import Task
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
configuration.api_key['ApiKey'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKey'] = 'Bearer'

# Enter a context with an instance of the API client
with gridly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = task_api.TaskApi(api_client)
    task_id = "taskId_example" # str | taskId

    # example passing only required values which don't have defaults set
    try:
        # get
        api_response = api_instance.get(task_id)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling TaskApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| taskId |

### Return type

[**Task**](Task.md)

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

