# gridly.AutomationApi

All URIs are relative to *https://api.gridly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_trigger**](AutomationApi.md#bulk_trigger) | **POST** /v1/automations/trigger | 
[**get**](AutomationApi.md#get) | **GET** /v1/automations/{automationId} | 
[**get_execution**](AutomationApi.md#get_execution) | **GET** /v1/automations/{automationId}/executions/{executionId} | 
[**get_executions**](AutomationApi.md#get_executions) | **GET** /v1/automations/{automationId}/executions | 
[**list**](AutomationApi.md#list) | **GET** /v1/automations | 
[**trigger**](AutomationApi.md#trigger) | **POST** /v1/automations/{automationId}/trigger | 


# **bulk_trigger**
> List[ExecutionResponse] bulk_trigger(bulk_execution_trigger_request)

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.bulk_execution_trigger_request import BulkExecutionTriggerRequest
from gridly.models.execution_response import ExecutionResponse
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
    api_instance = gridly.AutomationApi(api_client)
    bulk_execution_trigger_request = gridly.BulkExecutionTriggerRequest() # BulkExecutionTriggerRequest | 

    try:
        api_response = api_instance.bulk_trigger(bulk_execution_trigger_request)
        print("The response of AutomationApi->bulk_trigger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationApi->bulk_trigger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_execution_trigger_request** | [**BulkExecutionTriggerRequest**](BulkExecutionTriggerRequest.md)|  | 

### Return type

[**List[ExecutionResponse]**](ExecutionResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Automation get(automation_id)

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.automation import Automation
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
    api_instance = gridly.AutomationApi(api_client)
    automation_id = 'automation_id_example' # str | 

    try:
        api_response = api_instance.get(automation_id)
        print("The response of AutomationApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationApi->get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **automation_id** | **str**|  | 

### Return type

[**Automation**](Automation.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_execution**
> ExecutionResponse get_execution(automation_id, execution_id)

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.execution_response import ExecutionResponse
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
    api_instance = gridly.AutomationApi(api_client)
    automation_id = 'automation_id_example' # str | 
    execution_id = 'execution_id_example' # str | 

    try:
        api_response = api_instance.get_execution(automation_id, execution_id)
        print("The response of AutomationApi->get_execution:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationApi->get_execution: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **automation_id** | **str**|  | 
 **execution_id** | **str**|  | 

### Return type

[**ExecutionResponse**](ExecutionResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_executions**
> List[ExecutionResponse] get_executions(automation_id, page=page, size=size)

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.execution_response import ExecutionResponse
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
    api_instance = gridly.AutomationApi(api_client)
    automation_id = 'automation_id_example' # str | 
    page = 0 # int |  (optional) (default to 0)
    size = 10 # int |  (optional) (default to 10)

    try:
        api_response = api_instance.get_executions(automation_id, page=page, size=size)
        print("The response of AutomationApi->get_executions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationApi->get_executions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **automation_id** | **str**|  | 
 **page** | **int**|  | [optional] [default to 0]
 **size** | **int**|  | [optional] [default to 10]

### Return type

[**List[ExecutionResponse]**](ExecutionResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> List[Automation] list(view_id)

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.automation import Automation
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
    api_instance = gridly.AutomationApi(api_client)
    view_id = 'view_id_example' # str | 

    try:
        api_response = api_instance.list(view_id)
        print("The response of AutomationApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**|  | 

### Return type

[**List[Automation]**](Automation.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger**
> ExecutionResponse trigger(automation_id, execution_trigger_request)

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.execution_response import ExecutionResponse
from gridly.models.execution_trigger_request import ExecutionTriggerRequest
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
    api_instance = gridly.AutomationApi(api_client)
    automation_id = 'automation_id_example' # str | 
    execution_trigger_request = gridly.ExecutionTriggerRequest() # ExecutionTriggerRequest | 

    try:
        api_response = api_instance.trigger(automation_id, execution_trigger_request)
        print("The response of AutomationApi->trigger:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AutomationApi->trigger: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **automation_id** | **str**|  | 
 **execution_trigger_request** | [**ExecutionTriggerRequest**](ExecutionTriggerRequest.md)|  | 

### Return type

[**ExecutionResponse**](ExecutionResponse.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

