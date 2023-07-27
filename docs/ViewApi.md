# gridly.ViewApi

All URIs are relative to *https://api.gridly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ViewApi.md#create) | **POST** /v1/views | create
[**export**](ViewApi.md#export) | **GET** /v1/views/{viewId}/export | export
[**get**](ViewApi.md#get) | **GET** /v1/views/{viewId} | get
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
import time
import gridly
from gridly.api import view_api
from gridly.model.create_view import CreateView
from gridly.model.view import View
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
    api_instance = view_api.ViewApi(api_client)
    create_view = CreateView(
        name="name_example",
        columns=[
            AddViewColumn(
                editable=True,
                id="id_example",
            ),
        ],
        grid_id="grid_id_example",
    ) # CreateView | 

    # example passing only required values which don't have defaults set
    try:
        # create
        api_response = api_instance.create(create_view)
        pprint(api_response)
    except gridly.ApiException as e:
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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export**
> file_type export(view_id)

export

export

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import view_api
from gridly.model.export_file_header import ExportFileHeader
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
    api_instance = view_api.ViewApi(api_client)
    view_id = "viewId_example" # str | viewId
    column_ids = [] # [str], none_type | columnIds (optional) if omitted the server will use the default value of []
    file_header = ExportFileHeader("none") # ExportFileHeader | fileHeader (optional)
    query = "{}" # str, none_type | query (optional) if omitted the server will use the default value of "{}"
    sort = "{}" # str, none_type | sort (optional) if omitted the server will use the default value of "{}"
    type = "csv" # str, none_type | type (optional) if omitted the server will use the default value of "csv"

    # example passing only required values which don't have defaults set
    try:
        # export
        api_response = api_instance.export(view_id)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ViewApi->export: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # export
        api_response = api_instance.export(view_id, column_ids=column_ids, file_header=file_header, query=query, sort=sort, type=type)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ViewApi->export: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId |
 **column_ids** | **[str], none_type**| columnIds | [optional] if omitted the server will use the default value of []
 **file_header** | **ExportFileHeader**| fileHeader | [optional]
 **query** | **str, none_type**| query | [optional] if omitted the server will use the default value of "{}"
 **sort** | **str, none_type**| sort | [optional] if omitted the server will use the default value of "{}"
 **type** | **str, none_type**| type | [optional] if omitted the server will use the default value of "csv"

### Return type

**file_type**

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
> View get(view_id)

get

get

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import view_api
from gridly.model.view import View
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
    api_instance = view_api.ViewApi(api_client)
    view_id = "viewId_example" # str | viewId
    column_ids = [] # [str], none_type | columnIds (optional) if omitted the server will use the default value of []
    include = [] # [str], none_type | include (optional) if omitted the server will use the default value of []
    page = "{}" # str, none_type | page (optional) if omitted the server will use the default value of "{}"
    query = "{}" # str, none_type | query (optional) if omitted the server will use the default value of "{}"
    sort = "{}" # str, none_type | sort (optional) if omitted the server will use the default value of "{}"

    # example passing only required values which don't have defaults set
    try:
        # get
        api_response = api_instance.get(view_id)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ViewApi->get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # get
        api_response = api_instance.get(view_id, column_ids=column_ids, include=include, page=page, query=query, sort=sort)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ViewApi->get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId |
 **column_ids** | **[str], none_type**| columnIds | [optional] if omitted the server will use the default value of []
 **include** | **[str], none_type**| include | [optional] if omitted the server will use the default value of []
 **page** | **str, none_type**| page | [optional] if omitted the server will use the default value of "{}"
 **query** | **str, none_type**| query | [optional] if omitted the server will use the default value of "{}"
 **sort** | **str, none_type**| sort | [optional] if omitted the server will use the default value of "{}"

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

# **import_view**
> import_view(view_id, file)

importView

importView

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import view_api
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
    api_instance = view_api.ViewApi(api_client)
    view_id = "viewId_example" # str | viewId
    file = open('/path/to/file', 'rb') # file_type | The following file types are supported: csv, tsv, xls, xlsx and json
    import_request = "{}" # str, none_type | importRequest (optional) if omitted the server will use the default value of "{}"
    type = "csv" # str, none_type | type (optional) if omitted the server will use the default value of "csv"

    # example passing only required values which don't have defaults set
    try:
        # importView
        api_instance.import_view(view_id, file)
    except gridly.ApiException as e:
        print("Exception when calling ViewApi->import_view: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # importView
        api_instance.import_view(view_id, file, import_request=import_request, type=type)
    except gridly.ApiException as e:
        print("Exception when calling ViewApi->import_view: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId |
 **file** | **file_type**| The following file types are supported: csv, tsv, xls, xlsx and json |
 **import_request** | **str, none_type**| importRequest | [optional] if omitted the server will use the default value of "{}"
 **type** | **str, none_type**| type | [optional] if omitted the server will use the default value of "csv"

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
> [View] list()

list

list

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import view_api
from gridly.model.view import View
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
    api_instance = view_api.ViewApi(api_client)
    branch_id = "branchId_example" # str | branchId (optional)
    grid_id = "gridId_example" # str | gridId (optional)
    type = "defaultView" # str | type (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # list
        api_response = api_instance.list(branch_id=branch_id, grid_id=grid_id, type=type)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ViewApi->list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **branch_id** | **str**| branchId | [optional]
 **grid_id** | **str**| gridId | [optional]
 **type** | **str**| type | [optional]

### Return type

[**[View]**](View.md)

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
> Task merge(destination_view_id, view_id)

merge

merge

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import view_api
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
    api_instance = view_api.ViewApi(api_client)
    destination_view_id = "destinationViewId_example" # str | destinationViewId
    view_id = "viewId_example" # str | viewId
    merge_record_options = [] # [str], none_type | mergeRecordOptions (optional) if omitted the server will use the default value of []

    # example passing only required values which don't have defaults set
    try:
        # merge
        api_response = api_instance.merge(destination_view_id, view_id)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ViewApi->merge: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # merge
        api_response = api_instance.merge(destination_view_id, view_id, merge_record_options=merge_record_options)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ViewApi->merge: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **destination_view_id** | **str**| destinationViewId |
 **view_id** | **str**| viewId |
 **merge_record_options** | **[str], none_type**| mergeRecordOptions | [optional] if omitted the server will use the default value of []

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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

