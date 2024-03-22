# gridly.RecordApi

All URIs are relative to *https://api.gridly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](RecordApi.md#create) | **POST** /v1/views/{viewId}/records | create
[**delete**](RecordApi.md#delete) | **DELETE** /v1/views/{viewId}/records | delete
[**fetch**](RecordApi.md#fetch) | **GET** /v1/views/{viewId}/records | fetch
[**fetch_histories**](RecordApi.md#fetch_histories) | **GET** /v1/views/{viewId}/records/{recordId}/histories | fetchHistories
[**update**](RecordApi.md#update) | **PATCH** /v1/views/{viewId}/records | update
[**update_record**](RecordApi.md#update_record) | **PATCH** /v1/views/{viewId}/records/{id} | updateRecord


# **create**
> [Record] create(view_id, create_records)

create

create

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import record_api
from gridly.model.set_record import SetRecord
from gridly.model.record import Record
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
    api_instance = record_api.RecordApi(api_client)
    view_id = "viewId_example" # str | viewId
    create_records = [
        SetRecord(
            id="id_example",
            cells=[
                SetCell(
                    column_id="column_id_example",
                    dependency_status="upToDate",
                    length_limit=1,
                    referenced_ids=[
                        "referenced_ids_example",
                    ],
                    source_status="unset",
null,
                ),
            ],
            path="path_example",
        ),
    ] # [SetRecord] | createRecords

    # example passing only required values which don't have defaults set
    try:
        # create
        api_response = api_instance.create(view_id, create_records)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling RecordApi->create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId |
 **create_records** | [**[SetRecord]**](SetRecord.md)| createRecords |

### Return type

[**[Record]**](Record.md)

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
> delete(view_id, delete_record)

delete

delete

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import record_api
from gridly.model.delete_record import DeleteRecord
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
    api_instance = record_api.RecordApi(api_client)
    view_id = "viewId_example" # str | viewId
    delete_record = DeleteRecord(
        ids=[
            "ids_example",
        ],
        identifiers=[
            RecordIdentifierWrapper(
                id="id_example",
                path="path_example",
            ),
        ],
    ) # DeleteRecord | 

    # example passing only required values which don't have defaults set
    try:
        # delete
        api_instance.delete(view_id, delete_record)
    except gridly.ApiException as e:
        print("Exception when calling RecordApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId |
 **delete_record** | [**DeleteRecord**](DeleteRecord.md)|  |

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

# **fetch**
> [Record] fetch(view_id)

fetch

fetch

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import record_api
from gridly.model.record import Record
from gridly.model.fetch_file_option import FetchFileOption
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
    api_instance = record_api.RecordApi(api_client)
    view_id = "viewId_example" # str | viewId
    column_ids = [] # [str], none_type | columnIds (optional) if omitted the server will use the default value of []
    page = "{}" # str, none_type | page (optional) if omitted the server will use the default value of "{}"
    query = "{}" # str, none_type | query (optional) if omitted the server will use the default value of "{}"
    sort = "{}" # str, none_type | sort (optional) if omitted the server will use the default value of "{}"
    fetch_file_option = FetchFileOption("id") # FetchFileOption | fetchFileOption (optional)
    after_record_id = "afterRecordId_example" # str | afterRecordId (optional)
    before_record_id = "beforeRecordId_example" # str | beforeRecordId (optional)

    # example passing only required values which don't have defaults set
    try:
        # fetch
        api_response = api_instance.fetch(view_id)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling RecordApi->fetch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # fetch
        api_response = api_instance.fetch(view_id, column_ids=column_ids, page=page, query=query, sort=sort, fetch_file_option=fetch_file_option, after_record_id=after_record_id, before_record_id=before_record_id)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling RecordApi->fetch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId |
 **column_ids** | **[str], none_type**| columnIds | [optional] if omitted the server will use the default value of []
 **page** | **str, none_type**| page | [optional] if omitted the server will use the default value of "{}"
 **query** | **str, none_type**| query | [optional] if omitted the server will use the default value of "{}"
 **sort** | **str, none_type**| sort | [optional] if omitted the server will use the default value of "{}"
 **fetch_file_option** | **FetchFileOption**| fetchFileOption | [optional]
 **after_record_id** | **str**| afterRecordId | [optional]
 **before_record_id** | **str**| beforeRecordId | [optional]

### Return type

[**[Record]**](Record.md)

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

# **fetch_histories**
> [RecordHistory] fetch_histories(view_id, record_id, fetch_request)

fetchHistories

fetchHistories

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import record_api
from gridly.model.record_history import RecordHistory
from gridly.model.fetch_record_history_request import FetchRecordHistoryRequest
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
    api_instance = record_api.RecordApi(api_client)
    view_id = "viewId_example" # str | viewId
    record_id = "recordId_example" # str | recordId
    fetch_request = FetchRecordHistoryRequest(
        column_ids=[
            "column_ids_example",
        ],
        query="query_example",
        sort="sort_example",
        group_by=[
            "group_by_example",
        ],
        page="page_example",
        fetch_options="fetch_options_example",
        include_system_user=True,
    ) # FetchRecordHistoryRequest | fetchRequest

    # example passing only required values which don't have defaults set
    try:
        # fetchHistories
        api_response = api_instance.fetch_histories(view_id, record_id, fetch_request)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling RecordApi->fetch_histories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId |
 **record_id** | **str**| recordId |
 **fetch_request** | **FetchRecordHistoryRequest**| fetchRequest |

### Return type

[**[RecordHistory]**](RecordHistory.md)

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
> [Record] update(view_id, set_record)

update

update

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import record_api
from gridly.model.set_record import SetRecord
from gridly.model.record import Record
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
    api_instance = record_api.RecordApi(api_client)
    view_id = "viewId_example" # str | viewId
    set_record = [
        SetRecord(
            id="id_example",
            cells=[
                SetCell(
                    column_id="column_id_example",
                    dependency_status="upToDate",
                    length_limit=1,
                    referenced_ids=[
                        "referenced_ids_example",
                    ],
                    source_status="unset",
null,
                ),
            ],
            path="path_example",
        ),
    ] # [SetRecord] | 

    # example passing only required values which don't have defaults set
    try:
        # update
        api_response = api_instance.update(view_id, set_record)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling RecordApi->update: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId |
 **set_record** | [**[SetRecord]**](SetRecord.md)|  |

### Return type

[**[Record]**](Record.md)

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

# **update_record**
> Record update_record(id, view_id, set_record)

updateRecord

updateRecord

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import record_api
from gridly.model.set_record import SetRecord
from gridly.model.record import Record
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
    api_instance = record_api.RecordApi(api_client)
    id = "id_example" # str | id
    view_id = "viewId_example" # str | viewId
    set_record = SetRecord(
        id="id_example",
        cells=[
            SetCell(
                column_id="column_id_example",
                dependency_status="upToDate",
                length_limit=1,
                referenced_ids=[
                    "referenced_ids_example",
                ],
                source_status="unset",
null,
            ),
        ],
        path="path_example",
    ) # SetRecord | 
    path = "path_example" # str | path (optional)

    # example passing only required values which don't have defaults set
    try:
        # updateRecord
        api_response = api_instance.update_record(id, view_id, set_record)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling RecordApi->update_record: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # updateRecord
        api_response = api_instance.update_record(id, view_id, set_record, path=path)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling RecordApi->update_record: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| id |
 **view_id** | **str**| viewId |
 **set_record** | [**SetRecord**](SetRecord.md)|  |
 **path** | **str**| path | [optional]

### Return type

[**Record**](Record.md)

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

