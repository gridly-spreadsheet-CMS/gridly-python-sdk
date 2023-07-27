# gridly.ShareViewApi

All URIs are relative to *https://api.gridly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ShareViewApi.md#create) | **PUT** /v1/views/{viewId}/shares | create
[**delete**](ShareViewApi.md#delete) | **DELETE** /v1/views/{viewId}/shares | delete
[**get**](ShareViewApi.md#get) | **GET** /v1/views/{viewId}/shares | get


# **create**
> ShareView create(view_id, create_share_view)

create

create

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import share_view_api
from gridly.model.create_share_view import CreateShareView
from gridly.model.share_view import ShareView
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
    api_instance = share_view_api.ShareViewApi(api_client)
    view_id = "viewId_example" # str | viewId
    create_share_view = CreateShareView(
        include_grid_history=True,
    ) # CreateShareView | 

    # example passing only required values which don't have defaults set
    try:
        # create
        api_response = api_instance.create(view_id, create_share_view)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ShareViewApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId |
 **create_share_view** | [**CreateShareView**](CreateShareView.md)|  |

### Return type

[**ShareView**](ShareView.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(view_id)

delete

delete

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import share_view_api
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
    api_instance = share_view_api.ShareViewApi(api_client)
    view_id = "viewId_example" # str | viewId

    # example passing only required values which don't have defaults set
    try:
        # delete
        api_instance.delete(view_id)
    except gridly.ApiException as e:
        print("Exception when calling ShareViewApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId |

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> ShareView get(view_id)

get

get

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import share_view_api
from gridly.model.share_view import ShareView
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
    api_instance = share_view_api.ShareViewApi(api_client)
    view_id = "viewId_example" # str | viewId

    # example passing only required values which don't have defaults set
    try:
        # get
        api_response = api_instance.get(view_id)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ShareViewApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId |

### Return type

[**ShareView**](ShareView.md)

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

