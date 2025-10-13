# gridly.CdnApi

All URIs are relative to *https://api.gridly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list**](CdnApi.md#list) | **GET** /v1/cdns | list
[**publish**](CdnApi.md#publish) | **PUT** /v1/cdns/{cdnId}/publish | publish
[**un_publish**](CdnApi.md#un_publish) | **PUT** /v1/cdns/{cdnId}/unpublish | unPublish


# **list**
> List[CDN] list(grid_id, offset=offset, limit=limit, ids=ids, published=published)

list

list

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.cdn import CDN
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
    api_instance = gridly.CdnApi(api_client)
    grid_id = 'grid_id_example' # str | gridId
    offset = 0 # int | offset (optional) (default to 0)
    limit = 128 # int | limit (optional) (default to 128)
    ids = ['ids_example'] # List[str] | ids (optional)
    published = True # bool | published (optional)

    try:
        # list
        api_response = api_instance.list(grid_id, offset=offset, limit=limit, ids=ids, published=published)
        print("The response of CdnApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CdnApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grid_id** | **str**| gridId | 
 **offset** | **int**| offset | [optional] [default to 0]
 **limit** | **int**| limit | [optional] [default to 128]
 **ids** | [**List[str]**](str.md)| ids | [optional] 
 **published** | **bool**| published | [optional] 

### Return type

[**List[CDN]**](CDN.md)

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

# **publish**
> CDN publish(cdn_id)

publish

publish

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.cdn import CDN
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
    api_instance = gridly.CdnApi(api_client)
    cdn_id = 'cdn_id_example' # str | cdnId

    try:
        # publish
        api_response = api_instance.publish(cdn_id)
        print("The response of CdnApi->publish:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CdnApi->publish: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cdn_id** | **str**| cdnId | 

### Return type

[**CDN**](CDN.md)

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

# **un_publish**
> CDN un_publish(cdn_id)

unPublish

unPublish

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.cdn import CDN
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
    api_instance = gridly.CdnApi(api_client)
    cdn_id = 'cdn_id_example' # str | cdnId

    try:
        # unPublish
        api_response = api_instance.un_publish(cdn_id)
        print("The response of CdnApi->un_publish:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CdnApi->un_publish: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cdn_id** | **str**| cdnId | 

### Return type

[**CDN**](CDN.md)

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

