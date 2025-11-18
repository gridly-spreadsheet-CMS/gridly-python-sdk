# gridly.PathApi

All URIs are relative to *https://api.gridly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](PathApi.md#create) | **POST** /v1/views/{viewId}/paths | create
[**delete**](PathApi.md#delete) | **DELETE** /v1/views/{viewId}/paths | delete
[**list**](PathApi.md#list) | **GET** /v1/views/{viewId}/paths/tree | list
[**move**](PathApi.md#move) | **POST** /v1/views/{viewId}/paths/move | move
[**update**](PathApi.md#update) | **PUT** /v1/views/{viewId}/paths/{path} | update
[**update_path_node**](PathApi.md#update_path_node) | **PUT** /v1/views/{viewId}/paths | updatePathNode


# **create**
> PathList create(view_id, create_path)

create

create

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.create_path import CreatePath
from gridly.models.path_list import PathList
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
    api_instance = gridly.PathApi(api_client)
    view_id = 'view_id_example' # str | viewId
    create_path = gridly.CreatePath() # CreatePath | 

    try:
        # create
        api_response = api_instance.create(view_id, create_path)
        print("The response of PathApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PathApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId | 
 **create_path** | [**CreatePath**](CreatePath.md)|  | 

### Return type

[**PathList**](PathList.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(view_id, delete_path)

delete

delete

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.delete_path import DeletePath
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
    api_instance = gridly.PathApi(api_client)
    view_id = 'view_id_example' # str | viewId
    delete_path = gridly.DeletePath() # DeletePath | 

    try:
        # delete
        api_instance.delete(view_id, delete_path)
    except Exception as e:
        print("Exception when calling PathApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId | 
 **delete_path** | [**DeletePath**](DeletePath.md)|  | 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> List[PathNode] list(view_id, root_path=root_path)

list

list

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.path_node import PathNode
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
    api_instance = gridly.PathApi(api_client)
    view_id = 'view_id_example' # str | viewId
    root_path = 'root_path_example' # str | rootPath (optional)

    try:
        # list
        api_response = api_instance.list(view_id, root_path=root_path)
        print("The response of PathApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PathApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId | 
 **root_path** | **str**| rootPath | [optional] 

### Return type

[**List[PathNode]**](PathNode.md)

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

# **move**
> PathList move(view_id, move_path)

move

move

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.move_path import MovePath
from gridly.models.path_list import PathList
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
    api_instance = gridly.PathApi(api_client)
    view_id = 'view_id_example' # str | viewId
    move_path = gridly.MovePath() # MovePath | 

    try:
        # move
        api_response = api_instance.move(view_id, move_path)
        print("The response of PathApi->move:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PathApi->move: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId | 
 **move_path** | [**MovePath**](MovePath.md)|  | 

### Return type

[**PathList**](PathList.md)

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

# **update**
> PathSingle update(view_id, path, update_path)

update

update

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.path_single import PathSingle
from gridly.models.update_path import UpdatePath
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
    api_instance = gridly.PathApi(api_client)
    view_id = 'view_id_example' # str | viewId
    path = 'path_example' # str | path
    update_path = gridly.UpdatePath() # UpdatePath | 

    try:
        # update
        api_response = api_instance.update(view_id, path, update_path)
        print("The response of PathApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PathApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId | 
 **path** | **str**| path | 
 **update_path** | [**UpdatePath**](UpdatePath.md)|  | 

### Return type

[**PathSingle**](PathSingle.md)

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

# **update_path_node**
> PathSingle update_path_node(view_id, update_path)

updatePathNode

updatePathNode

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.path_single import PathSingle
from gridly.models.update_path import UpdatePath
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
    api_instance = gridly.PathApi(api_client)
    view_id = 'view_id_example' # str | viewId
    update_path = gridly.UpdatePath() # UpdatePath | 

    try:
        # updatePathNode
        api_response = api_instance.update_path_node(view_id, update_path)
        print("The response of PathApi->update_path_node:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PathApi->update_path_node: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId | 
 **update_path** | [**UpdatePath**](UpdatePath.md)|  | 

### Return type

[**PathSingle**](PathSingle.md)

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

