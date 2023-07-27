# gridly.PathApi

All URIs are relative to *https://api.gridly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](PathApi.md#create) | **POST** /v1/views/{viewId}/paths | create
[**delete**](PathApi.md#delete) | **DELETE** /v1/views/{viewId}/paths | delete
[**list**](PathApi.md#list) | **GET** /v1/views/{viewId}/paths/tree | list
[**move**](PathApi.md#move) | **POST** /v1/views/{viewId}/paths/move | move
[**update**](PathApi.md#update) | **PUT** /v1/views/{viewId}/paths/{path} | update


# **create**
> PathList create(view_id, create_path)

create

create

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import path_api
from gridly.model.create_path import CreatePath
from gridly.model.path_list import PathList
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
    api_instance = path_api.PathApi(api_client)
    view_id = "viewId_example" # str | viewId
    create_path = CreatePath(
        parent_path="parent_path_example",
        paths=[
            "paths_example",
        ],
    ) # CreatePath | 

    # example passing only required values which don't have defaults set
    try:
        # create
        api_response = api_instance.create(view_id, create_path)
        pprint(api_response)
    except gridly.ApiException as e:
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(view_id, delete_path)

delete

delete

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import path_api
from gridly.model.delete_path import DeletePath
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
    api_instance = path_api.PathApi(api_client)
    view_id = "viewId_example" # str | viewId
    delete_path = DeletePath(
        paths=[
            "paths_example",
        ],
    ) # DeletePath | 

    # example passing only required values which don't have defaults set
    try:
        # delete
        api_instance.delete(view_id, delete_path)
    except gridly.ApiException as e:
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
> [PathNode] list(view_id)

list

list

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import path_api
from gridly.model.path_node import PathNode
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
    api_instance = path_api.PathApi(api_client)
    view_id = "viewId_example" # str | viewId
    root_path = "rootPath_example" # str | rootPath (optional)

    # example passing only required values which don't have defaults set
    try:
        # list
        api_response = api_instance.list(view_id)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling PathApi->list: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # list
        api_response = api_instance.list(view_id, root_path=root_path)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling PathApi->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId |
 **root_path** | **str**| rootPath | [optional]

### Return type

[**[PathNode]**](PathNode.md)

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
import time
import gridly
from gridly.api import path_api
from gridly.model.move_path import MovePath
from gridly.model.path_list import PathList
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
    api_instance = path_api.PathApi(api_client)
    view_id = "viewId_example" # str | viewId
    move_path = MovePath(
        from_parent_path="from_parent_path_example",
        move_after="move_after_example",
        move_before="move_before_example",
        names=[
            "names_example",
        ],
        to_parent_path="to_parent_path_example",
    ) # MovePath | 

    # example passing only required values which don't have defaults set
    try:
        # move
        api_response = api_instance.move(view_id, move_path)
        pprint(api_response)
    except gridly.ApiException as e:
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
import time
import gridly
from gridly.api import path_api
from gridly.model.path_single import PathSingle
from gridly.model.update_path import UpdatePath
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
    api_instance = path_api.PathApi(api_client)
    view_id = "viewId_example" # str | viewId
    path = "path_example" # str | path
    update_path = UpdatePath(
        new_name="l",
    ) # UpdatePath | 

    # example passing only required values which don't have defaults set
    try:
        # update
        api_response = api_instance.update(view_id, path, update_path)
        pprint(api_response)
    except gridly.ApiException as e:
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

