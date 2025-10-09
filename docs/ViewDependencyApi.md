# gridly.ViewDependencyApi

All URIs are relative to *https://api.gridly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ViewDependencyApi.md#create) | **POST** /v1/views/{viewId}/dependencies | create
[**delete**](ViewDependencyApi.md#delete) | **DELETE** /v1/views/{viewId}/dependencies | delete
[**delete_by_id**](ViewDependencyApi.md#delete_by_id) | **DELETE** /v1/views/{viewId}/dependencies/{dependencyId} | deleteById
[**get**](ViewDependencyApi.md#get) | **GET** /v1/views/{viewId}/dependencies/{dependencyId} | get
[**list**](ViewDependencyApi.md#list) | **GET** /v1/views/{viewId}/dependencies | list
[**update**](ViewDependencyApi.md#update) | **PUT** /v1/views/{viewId}/dependencies/{dependencyId} | update


# **create**
> Dependency create(view_id, create_dependency)

create

create

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.create_dependency import CreateDependency
from gridly.models.dependency import Dependency
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
    api_instance = gridly.ViewDependencyApi(api_client)
    view_id = 'view_id_example' # str | viewId
    create_dependency = gridly.CreateDependency() # CreateDependency | 

    try:
        # create
        api_response = api_instance.create(view_id, create_dependency)
        print("The response of ViewDependencyApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewDependencyApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId | 
 **create_dependency** | [**CreateDependency**](CreateDependency.md)|  | 

### Return type

[**Dependency**](Dependency.md)

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
> delete(view_id, delete_dependency)

delete

delete

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.delete_dependency import DeleteDependency
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
    api_instance = gridly.ViewDependencyApi(api_client)
    view_id = 'view_id_example' # str | viewId
    delete_dependency = gridly.DeleteDependency() # DeleteDependency | 

    try:
        # delete
        api_instance.delete(view_id, delete_dependency)
    except Exception as e:
        print("Exception when calling ViewDependencyApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId | 
 **delete_dependency** | [**DeleteDependency**](DeleteDependency.md)|  | 

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

# **delete_by_id**
> delete_by_id(view_id, dependency_id)

deleteById

deleteById

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
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
    api_instance = gridly.ViewDependencyApi(api_client)
    view_id = 'view_id_example' # str | viewId
    dependency_id = 'dependency_id_example' # str | dependencyId

    try:
        # deleteById
        api_instance.delete_by_id(view_id, dependency_id)
    except Exception as e:
        print("Exception when calling ViewDependencyApi->delete_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId | 
 **dependency_id** | **str**| dependencyId | 

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
> Dependency get(dependency_id, view_id)

get

get

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.dependency import Dependency
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
    api_instance = gridly.ViewDependencyApi(api_client)
    dependency_id = 'dependency_id_example' # str | dependencyId
    view_id = 'view_id_example' # str | viewId

    try:
        # get
        api_response = api_instance.get(dependency_id, view_id)
        print("The response of ViewDependencyApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewDependencyApi->get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dependency_id** | **str**| dependencyId | 
 **view_id** | **str**| viewId | 

### Return type

[**Dependency**](Dependency.md)

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

# **list**
> List[Dependency] list(view_id)

list

list

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.dependency import Dependency
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
    api_instance = gridly.ViewDependencyApi(api_client)
    view_id = 'view_id_example' # str | viewId

    try:
        # list
        api_response = api_instance.list(view_id)
        print("The response of ViewDependencyApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewDependencyApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId | 

### Return type

[**List[Dependency]**](Dependency.md)

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

# **update**
> Dependency update(dependency_id, view_id, update_dependency)

update

update

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.dependency import Dependency
from gridly.models.update_dependency import UpdateDependency
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
    api_instance = gridly.ViewDependencyApi(api_client)
    dependency_id = 'dependency_id_example' # str | dependencyId
    view_id = 'view_id_example' # str | viewId
    update_dependency = gridly.UpdateDependency() # UpdateDependency | 

    try:
        # update
        api_response = api_instance.update(dependency_id, view_id, update_dependency)
        print("The response of ViewDependencyApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewDependencyApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dependency_id** | **str**| dependencyId | 
 **view_id** | **str**| viewId | 
 **update_dependency** | [**UpdateDependency**](UpdateDependency.md)|  | 

### Return type

[**Dependency**](Dependency.md)

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

