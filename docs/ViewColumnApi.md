# gridly.ViewColumnApi

All URIs are relative to *https://api.gridly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add**](ViewColumnApi.md#add) | **POST** /v1/views/{viewId}/columns/{columnId}/add | add
[**bulk_create**](ViewColumnApi.md#bulk_create) | **POST** /v1/views/{viewId}/columns/bulk | bulkCreate
[**create**](ViewColumnApi.md#create) | **POST** /v1/views/{viewId}/columns | create
[**delete**](ViewColumnApi.md#delete) | **DELETE** /v1/views/{viewId}/columns/{columnId} | delete
[**get**](ViewColumnApi.md#get) | **GET** /v1/views/{viewId}/columns/{columnId} | get
[**remove**](ViewColumnApi.md#remove) | **POST** /v1/views/{viewId}/columns/{columnId}/remove | remove
[**update**](ViewColumnApi.md#update) | **PATCH** /v1/views/{viewId}/columns/{columnId} | update


# **add**
> ViewColumn add(column_id, view_id)

add

add

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.view_column import ViewColumn
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
    api_instance = gridly.ViewColumnApi(api_client)
    column_id = 'column_id_example' # str | columnId
    view_id = 'view_id_example' # str | viewId

    try:
        # add
        api_response = api_instance.add(column_id, view_id)
        print("The response of ViewColumnApi->add:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewColumnApi->add: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **column_id** | **str**| columnId | 
 **view_id** | **str**| viewId | 

### Return type

[**ViewColumn**](ViewColumn.md)

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

# **bulk_create**
> List[ViewColumn] bulk_create(view_id, create_column)

bulkCreate

bulkCreate

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.create_column import CreateColumn
from gridly.models.view_column import ViewColumn
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
    api_instance = gridly.ViewColumnApi(api_client)
    view_id = 'view_id_example' # str | viewId
    create_column = [gridly.CreateColumn()] # List[CreateColumn] | 

    try:
        # bulkCreate
        api_response = api_instance.bulk_create(view_id, create_column)
        print("The response of ViewColumnApi->bulk_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewColumnApi->bulk_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId | 
 **create_column** | [**List[CreateColumn]**](CreateColumn.md)|  | 

### Return type

[**List[ViewColumn]**](ViewColumn.md)

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

# **create**
> ViewColumn create(view_id, create_column)

create

Create a Column

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.create_column import CreateColumn
from gridly.models.view_column import ViewColumn
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
    api_instance = gridly.ViewColumnApi(api_client)
    view_id = 'view_id_example' # str | viewId
    create_column = gridly.CreateColumn() # CreateColumn | 

    try:
        # create
        api_response = api_instance.create(view_id, create_column)
        print("The response of ViewColumnApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewColumnApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId | 
 **create_column** | [**CreateColumn**](CreateColumn.md)|  | 

### Return type

[**ViewColumn**](ViewColumn.md)

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
> delete(column_id, view_id)

delete

delete

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
    api_instance = gridly.ViewColumnApi(api_client)
    column_id = 'column_id_example' # str | columnId
    view_id = 'view_id_example' # str | viewId

    try:
        # delete
        api_instance.delete(column_id, view_id)
    except Exception as e:
        print("Exception when calling ViewColumnApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **column_id** | **str**| columnId | 
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
> ViewColumn get(column_id, view_id)

get

get

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.view_column import ViewColumn
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
    api_instance = gridly.ViewColumnApi(api_client)
    column_id = 'column_id_example' # str | columnId
    view_id = 'view_id_example' # str | viewId

    try:
        # get
        api_response = api_instance.get(column_id, view_id)
        print("The response of ViewColumnApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewColumnApi->get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **column_id** | **str**| columnId | 
 **view_id** | **str**| viewId | 

### Return type

[**ViewColumn**](ViewColumn.md)

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

# **remove**
> remove(column_id, view_id)

remove

remove

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
    api_instance = gridly.ViewColumnApi(api_client)
    column_id = 'column_id_example' # str | columnId
    view_id = 'view_id_example' # str | viewId

    try:
        # remove
        api_instance.remove(column_id, view_id)
    except Exception as e:
        print("Exception when calling ViewColumnApi->remove: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **column_id** | **str**| columnId | 
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> ViewColumn update(column_id, view_id, update_column)

update

update

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.update_column import UpdateColumn
from gridly.models.view_column import ViewColumn
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
    api_instance = gridly.ViewColumnApi(api_client)
    column_id = 'column_id_example' # str | columnId
    view_id = 'view_id_example' # str | viewId
    update_column = gridly.UpdateColumn() # UpdateColumn | 

    try:
        # update
        api_response = api_instance.update(column_id, view_id, update_column)
        print("The response of ViewColumnApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewColumnApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **column_id** | **str**| columnId | 
 **view_id** | **str**| viewId | 
 **update_column** | [**UpdateColumn**](UpdateColumn.md)|  | 

### Return type

[**ViewColumn**](ViewColumn.md)

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

