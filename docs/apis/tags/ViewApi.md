<a name="__pageTop"></a>
# gridly.apis.tags.view_api.ViewApi

All URIs are relative to *https://api.gridly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**call_list**](#call_list) | **get** /v1/views | list
[**create**](#create) | **post** /v1/views | create
[**export**](#export) | **get** /v1/views/{viewId}/export | export
[**get**](#get) | **get** /v1/views/{viewId} | get
[**get_statistic**](#get_statistic) | **get** /v1/views/{viewId}/statistic | getStatistic
[**import_view**](#import_view) | **post** /v1/views/{viewId}/import | importView
[**merge**](#merge) | **post** /v1/views/{viewId}/merge | merge

# **call_list**
<a name="call_list"></a>
> [View] call_list()

list

list

### Example

* Api Key Authentication (ApiKey):
```python
import gridly
from gridly.apis.tags import view_api
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

    # example passing only optional values
    query_params = {
        'branchId': "branchId_example",
        'gridId': "gridId_example",
        'type': "defaultView",
    }
    try:
        # list
        api_response = api_instance.call_list(
            query_params=query_params,
        )
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ViewApi->call_list: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
branchId | BranchIdSchema | | optional
gridId | GridIdSchema | | optional
type | TypeSchema | | optional


# BranchIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GridIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# TypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["defaultView", "accessView", "userView", "workflowView", "widgetView", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#call_list.ApiResponseFor200) | OK

#### call_list.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**View**]({{complexTypePrefix}}View.md) | [**View**]({{complexTypePrefix}}View.md) | [**View**]({{complexTypePrefix}}View.md) |  | 

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create**
<a name="create"></a>
> View create(create_view)

create

create

### Example

* Api Key Authentication (ApiKey):
```python
import gridly
from gridly.apis.tags import view_api
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

    # example passing only required values which don't have defaults set
    body = CreateView(
        name="name_example",
        grid_id="grid_id_example",
        columns=[
            AddViewColumn(
                id="id_example",
                editable=True,
                name="name_example",
                description="description_example",
                type="singleLine",
                language_code="enUS",
                localization_type="sourceLanguage",
                number_format=NumberFormat(
                    type="decimal",
                    decimal_places=1,
                    currency_symbol="currency_symbol_example",
                    use1000_separator=True,
                ),
                selection_options=[
                    "selection_options_example"
                ],
                reference=Reference(
                    grid_id="grid_id_example",
                    branch_id="branch_id_example",
                    column_id="column_id_example",
                    type="row",
                    selection_type="single",
                ),
                formula=Formula(
                    formula_text="formula_text_example",
                    always_format_result_value_as_list=True,
                    detect_result_value_type="list",
                ),
                date_time_format=DateTimeFormat(
                    date_format="date_format_example",
                    time_format="time_format_example",
                    zone_offset="zone_offset_example",
                    show_time_zone=True,
                ),
            )
        ],
    )
    try:
        # create
        api_response = api_instance.create(
            body=body,
        )
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ViewApi->create: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CreateView**](../../models/CreateView.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create.ApiResponseFor200) | OK

#### create.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**View**](../../models/View.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **export**
<a name="export"></a>
> file_type export(view_id)

export

export

### Example

* Api Key Authentication (ApiKey):
```python
import gridly
from gridly.apis.tags import view_api
from gridly.model.file_type import FileType
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

    # example passing only required values which don't have defaults set
    path_params = {
        'viewId': "viewId_example",
    }
    query_params = {
    }
    try:
        # export
        api_response = api_instance.export(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ViewApi->export: %s\n" % e)

    # example passing only optional values
    path_params = {
        'viewId': "viewId_example",
    }
    query_params = {
        'columnIds': [],
        'fileHeader': ExportFileHeader("none"),
        'query': "{}",
        'sort': "{}",
        'type': FileType("csv"),
    }
    try:
        # export
        api_response = api_instance.export(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ViewApi->export: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/octet-stream', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
columnIds | ColumnIdsSchema | | optional
fileHeader | FileHeaderSchema | | optional
query | QuerySchema | | optional
sort | SortSchema | | optional
type | TypeSchema | | optional


# ColumnIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# FileHeaderSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**ExportFileHeader**](../../models/ExportFileHeader.md) |  | 


# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  |  | if omitted the server will use the default value of "{}"

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  |  | if omitted the server will use the default value of "{}"

# TypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**FileType**](../../models/FileType.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
viewId | ViewIdSchema | | 

# ViewIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
default | [ApiResponseForDefault](#export.ApiResponseForDefault) | default response

#### export.ApiResponseForDefault
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor0ResponseBodyApplicationOctetStream, ] |  |
headers | Unset | headers were not defined |

# SchemaFor0ResponseBodyApplicationOctetStream

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  |  | 

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get**
<a name="get"></a>
> View get(view_id)

get

get

### Example

* Api Key Authentication (ApiKey):
```python
import gridly
from gridly.apis.tags import view_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'viewId': "viewId_example",
    }
    query_params = {
    }
    try:
        # get
        api_response = api_instance.get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ViewApi->get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'viewId': "viewId_example",
    }
    query_params = {
        'columnIds': [],
        'include': [],
        'page': "{}",
        'query': "{}",
        'sort': "{}",
    }
    try:
        # get
        api_response = api_instance.get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ViewApi->get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
columnIds | ColumnIdsSchema | | optional
include | IncludeSchema | | optional
page | PageSchema | | optional
query | QuerySchema | | optional
sort | SortSchema | | optional


# ColumnIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# IncludeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["records", ] 

# PageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  |  | if omitted the server will use the default value of "{}"

# QuerySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  |  | if omitted the server will use the default value of "{}"

# SortSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  |  | if omitted the server will use the default value of "{}"

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
viewId | ViewIdSchema | | 

# ViewIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get.ApiResponseFor200) | OK

#### get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**View**](../../models/View.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_statistic**
<a name="get_statistic"></a>
> ViewStatistic get_statistic(view_id)

getStatistic

getStatistic

### Example

* Api Key Authentication (ApiKey):
```python
import gridly
from gridly.apis.tags import view_api
from gridly.model.view_statistic import ViewStatistic
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

    # example passing only required values which don't have defaults set
    path_params = {
        'viewId': "viewId_example",
    }
    query_params = {
    }
    try:
        # getStatistic
        api_response = api_instance.get_statistic(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ViewApi->get_statistic: %s\n" % e)

    # example passing only optional values
    path_params = {
        'viewId': "viewId_example",
    }
    query_params = {
        'columnIds': [],
    }
    try:
        # getStatistic
        api_response = api_instance.get_statistic(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ViewApi->get_statistic: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
columnIds | ColumnIdsSchema | | optional


# ColumnIdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
viewId | ViewIdSchema | | 

# ViewIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_statistic.ApiResponseFor200) | OK

#### get_statistic.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ViewStatistic**](../../models/ViewStatistic.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **import_view**
<a name="import_view"></a>
> import_view(view_id)

importView

importView

### Example

* Api Key Authentication (ApiKey):
```python
import gridly
from gridly.apis.tags import view_api
from gridly.model.file_type import FileType
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

    # example passing only required values which don't have defaults set
    path_params = {
        'viewId': "viewId_example",
    }
    query_params = {
    }
    try:
        # importView
        api_response = api_instance.import_view(
            path_params=path_params,
            query_params=query_params,
        )
    except gridly.ApiException as e:
        print("Exception when calling ViewApi->import_view: %s\n" % e)

    # example passing only optional values
    path_params = {
        'viewId': "viewId_example",
    }
    query_params = {
        'importRequest': "{}",
        'type': FileType("csv"),
    }
    body = dict(
        file=open('/path/to/file', 'rb'),
    )
    try:
        # importView
        api_response = api_instance.import_view(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except gridly.ApiException as e:
        print("Exception when calling ViewApi->import_view: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyMultipartFormData, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'multipart/form-data' | Selects the schema and serialization of the request body
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyMultipartFormData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**file** | bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  | The following file types are supported: csv, tsv, xls, xlsx and json | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
importRequest | ImportRequestSchema | | optional
type | TypeSchema | | optional


# ImportRequestSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
None, str,  | NoneClass, str,  |  | if omitted the server will use the default value of "{}"

# TypeSchema
Type | Description  | Notes
------------- | ------------- | -------------
[**FileType**](../../models/FileType.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
viewId | ViewIdSchema | | 

# ViewIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#import_view.ApiResponseFor202) | Accepted

#### import_view.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **merge**
<a name="merge"></a>
> Task merge(destination_view_idview_idmerge_branch_request)

merge

merge

### Example

* Api Key Authentication (ApiKey):
```python
import gridly
from gridly.apis.tags import view_api
from gridly.model.merge_branch_request import MergeBranchRequest
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

    # example passing only required values which don't have defaults set
    path_params = {
        'viewId': "viewId_example",
    }
    query_params = {
        'destinationViewId': "destinationViewId_example",
    }
    body = MergeBranchRequest(
        merge_record_options=[
            "add"
        ],
        merge_record_conflicts=[
            MergeRecordConflict(
                cells=[
                    MergeCellConflict(
                        column_id="column_id_example",
                        option="child",
                    )
                ],
                path_tag="path_tag_example",
                record_id="record_id_example",
            )
        ],
        use_last_merge_resolve=True,
        check_mismatched_column_type=True,
        query=[
            FilterField(
                case_sensitive=True,
                column_id="column_id_example",
                dynamic_column="dynamic_column_example",
                operator="isNull",
                query_path_tag_via_id=True,
                sub_field="_dependencyStatus",
                values=[
                    dict()
                ],
            )
        ],
    )
    try:
        # merge
        api_response = api_instance.merge(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ViewApi->merge: %s\n" % e)

    # example passing only optional values
    path_params = {
        'viewId': "viewId_example",
    }
    query_params = {
        'destinationViewId': "destinationViewId_example",
        'mergeRecordOptions': [],
    }
    body = MergeBranchRequest(
        merge_record_options=[
            "add"
        ],
        merge_record_conflicts=[
            MergeRecordConflict(
                cells=[
                    MergeCellConflict(
                        column_id="column_id_example",
                        option="child",
                    )
                ],
                path_tag="path_tag_example",
                record_id="record_id_example",
            )
        ],
        use_last_merge_resolve=True,
        check_mismatched_column_type=True,
        query=[
            FilterField(
                case_sensitive=True,
                column_id="column_id_example",
                dynamic_column="dynamic_column_example",
                operator="isNull",
                query_path_tag_via_id=True,
                sub_field="_dependencyStatus",
                values=[
                    dict()
                ],
            )
        ],
    )
    try:
        # merge
        api_response = api_instance.merge(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ViewApi->merge: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MergeBranchRequest**](../../models/MergeBranchRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
destinationViewId | DestinationViewIdSchema | | 
mergeRecordOptions | MergeRecordOptionsSchema | | optional


# DestinationViewIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# MergeRecordOptionsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple, None,  | tuple, NoneClass,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["add", "update", "delete", "override", ] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
viewId | ViewIdSchema | | 

# ViewIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#merge.ApiResponseFor202) | Accepted

#### merge.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Task**](../../models/Task.md) |  | 


### Authorization

[ApiKey](../../../README.md#ApiKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

