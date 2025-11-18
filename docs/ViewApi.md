# gridly.ViewApi

All URIs are relative to *https://api.gridly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ViewApi.md#create) | **POST** /v1/views | create
[**delete**](ViewApi.md#delete) | **DELETE** /v1/views/{viewId} | delete
[**export**](ViewApi.md#export) | **GET** /v1/views/{viewId}/export | export
[**get**](ViewApi.md#get) | **GET** /v1/views/{viewId} | get
[**get_statistic**](ViewApi.md#get_statistic) | **GET** /v1/views/{viewId}/statistic | getStatistic
[**import_view**](ViewApi.md#import_view) | **POST** /v1/views/{viewId}/import | importView
[**list**](ViewApi.md#list) | **GET** /v1/views | list
[**merge**](ViewApi.md#merge) | **POST** /v1/views/{viewId}/merge | merge


# **create**
> View create(create_view)

create

create

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.create_view import CreateView
from gridly.models.view import View
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
    api_instance = gridly.ViewApi(api_client)
    create_view = gridly.CreateView() # CreateView | 

    try:
        # create
        api_response = api_instance.create(create_view)
        print("The response of ViewApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_view** | [**CreateView**](CreateView.md)|  | 

### Return type

[**View**](View.md)

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
> delete(view_id)

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
    api_instance = gridly.ViewApi(api_client)
    view_id = 'view_id_example' # str | viewId

    try:
        # delete
        api_instance.delete(view_id)
    except Exception as e:
        print("Exception when calling ViewApi->delete: %s\n" % e)
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

# **export**
> bytearray export(view_id, column_ids=column_ids, file_header=file_header, query=query, sort=sort, type=type)

export

export

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.export_file_header import ExportFileHeader
from gridly.models.file_type import FileType
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
    api_instance = gridly.ViewApi(api_client)
    view_id = 'view_id_example' # str | viewId
    column_ids = [] # List[str] | columnIds (optional) (default to [])
    file_header = gridly.ExportFileHeader() # ExportFileHeader | fileHeader (optional)
    query = '{}' # str | query (optional) (default to '{}')
    sort = '{}' # str | sort (optional) (default to '{}')
    type = gridly.FileType() # FileType | type (optional)

    try:
        # export
        api_response = api_instance.export(view_id, column_ids=column_ids, file_header=file_header, query=query, sort=sort, type=type)
        print("The response of ViewApi->export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId | 
 **column_ids** | [**List[str]**](str.md)| columnIds | [optional] [default to []]
 **file_header** | [**ExportFileHeader**](.md)| fileHeader | [optional] 
 **query** | **str**| query | [optional] [default to &#39;{}&#39;]
 **sort** | **str**| sort | [optional] [default to &#39;{}&#39;]
 **type** | [**FileType**](.md)| type | [optional] 

### Return type

**bytearray**

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> View get(view_id, column_ids=column_ids, include=include, page=page, query=query, sort=sort)

get

get

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.view import View
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
    api_instance = gridly.ViewApi(api_client)
    view_id = 'view_id_example' # str | viewId
    column_ids = [] # List[str] | columnIds (optional) (default to [])
    include = [] # List[str] | include (optional) (default to [])
    page = '{}' # str | page (optional) (default to '{}')
    query = '{}' # str | query (optional) (default to '{}')
    sort = '{}' # str | sort (optional) (default to '{}')

    try:
        # get
        api_response = api_instance.get(view_id, column_ids=column_ids, include=include, page=page, query=query, sort=sort)
        print("The response of ViewApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId | 
 **column_ids** | [**List[str]**](str.md)| columnIds | [optional] [default to []]
 **include** | [**List[str]**](str.md)| include | [optional] [default to []]
 **page** | **str**| page | [optional] [default to &#39;{}&#39;]
 **query** | **str**| query | [optional] [default to &#39;{}&#39;]
 **sort** | **str**| sort | [optional] [default to &#39;{}&#39;]

### Return type

[**View**](View.md)

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

# **get_statistic**
> ViewStatistic get_statistic(view_id, column_ids=column_ids)

getStatistic

getStatistic

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.view_statistic import ViewStatistic
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
    api_instance = gridly.ViewApi(api_client)
    view_id = 'view_id_example' # str | viewId
    column_ids = [] # List[str] | columnIds (optional) (default to [])

    try:
        # getStatistic
        api_response = api_instance.get_statistic(view_id, column_ids=column_ids)
        print("The response of ViewApi->get_statistic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->get_statistic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId | 
 **column_ids** | [**List[str]**](str.md)| columnIds | [optional] [default to []]

### Return type

[**ViewStatistic**](ViewStatistic.md)

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

# **import_view**
> import_view(view_id, file, import_request=import_request, type=type)

importView

importView

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.file_type import FileType
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
    api_instance = gridly.ViewApi(api_client)
    view_id = 'view_id_example' # str | viewId
    file = None # bytearray | The following file types are supported: csv, tsv, xls, xlsx and json
    import_request = '{}' # str | importRequest (optional) (default to '{}')
    type = gridly.FileType() # FileType | type (optional)

    try:
        # importView
        api_instance.import_view(view_id, file, import_request=import_request, type=type)
    except Exception as e:
        print("Exception when calling ViewApi->import_view: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId | 
 **file** | **bytearray**| The following file types are supported: csv, tsv, xls, xlsx and json | 
 **import_request** | **str**| importRequest | [optional] [default to &#39;{}&#39;]
 **type** | [**FileType**](.md)| type | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> List[View] list(branch_id=branch_id, grid_id=grid_id, type=type)

list

list

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.view import View
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
    api_instance = gridly.ViewApi(api_client)
    branch_id = 'branch_id_example' # str | branchId (optional)
    grid_id = 'grid_id_example' # str | gridId (optional)
    type = 'type_example' # str | type (optional)

    try:
        # list
        api_response = api_instance.list(branch_id=branch_id, grid_id=grid_id, type=type)
        print("The response of ViewApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch_id** | **str**| branchId | [optional] 
 **grid_id** | **str**| gridId | [optional] 
 **type** | **str**| type | [optional] 

### Return type

[**List[View]**](View.md)

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

# **merge**
> Task merge(destination_view_id, view_id, merge_branch_request, merge_record_options=merge_record_options)

merge

merge

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.merge_branch_request import MergeBranchRequest
from gridly.models.merge_record_option import MergeRecordOption
from gridly.models.task import Task
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
    api_instance = gridly.ViewApi(api_client)
    destination_view_id = 'destination_view_id_example' # str | destinationViewId
    view_id = 'view_id_example' # str | viewId
    merge_branch_request = gridly.MergeBranchRequest() # MergeBranchRequest | 
    merge_record_options = [] # List[MergeRecordOption] | mergeRecordOptions (optional) (default to [])

    try:
        # merge
        api_response = api_instance.merge(destination_view_id, view_id, merge_branch_request, merge_record_options=merge_record_options)
        print("The response of ViewApi->merge:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewApi->merge: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_view_id** | **str**| destinationViewId | 
 **view_id** | **str**| viewId | 
 **merge_branch_request** | [**MergeBranchRequest**](MergeBranchRequest.md)|  | 
 **merge_record_options** | [**List[MergeRecordOption]**](MergeRecordOption.md)| mergeRecordOptions | [optional] [default to []]

### Return type

[**Task**](Task.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

