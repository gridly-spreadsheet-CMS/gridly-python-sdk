# gridly.RecordApi

All URIs are relative to *https://api.gridly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](RecordApi.md#create) | **POST** /v1/views/{viewId}/records | create
[**delete**](RecordApi.md#delete) | **DELETE** /v1/views/{viewId}/records | delete
[**download_record_histories**](RecordApi.md#download_record_histories) | **GET** /v1/views/{viewId}/record-histories/export/{taskId} | downloadRecordHistories
[**export_record_histories**](RecordApi.md#export_record_histories) | **POST** /v1/views/{viewId}/record-histories/export | exportRecordHistories
[**fetch**](RecordApi.md#fetch) | **GET** /v1/views/{viewId}/records | fetch
[**fetch_histories**](RecordApi.md#fetch_histories) | **GET** /v1/views/{viewId}/records/{recordId}/histories | fetchHistories
[**update**](RecordApi.md#update) | **PATCH** /v1/views/{viewId}/records | update
[**update_record**](RecordApi.md#update_record) | **PATCH** /v1/views/{viewId}/records/{id} | updateRecord


# **create**
> List[Record] create(view_id, create_records)

create

create

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.record import Record
from gridly.models.set_record import SetRecord
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
    api_instance = gridly.RecordApi(api_client)
    view_id = 'view_id_example' # str | viewId
    create_records = [gridly.SetRecord()] # List[SetRecord] | createRecords

    try:
        # create
        api_response = api_instance.create(view_id, create_records)
        print("The response of RecordApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId | 
 **create_records** | [**List[SetRecord]**](SetRecord.md)| createRecords | 

### Return type

[**List[Record]**](Record.md)

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
import gridly
from gridly.models.delete_record import DeleteRecord
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
    api_instance = gridly.RecordApi(api_client)
    view_id = 'view_id_example' # str | viewId
    delete_record = gridly.DeleteRecord() # DeleteRecord | 

    try:
        # delete
        api_instance.delete(view_id, delete_record)
    except Exception as e:
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

# **download_record_histories**
> bytearray download_record_histories(view_id, task_id)

downloadRecordHistories

downloadRecordHistories

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
    api_instance = gridly.RecordApi(api_client)
    view_id = 'view_id_example' # str | viewId
    task_id = 'task_id_example' # str | taskId

    try:
        # downloadRecordHistories
        api_response = api_instance.download_record_histories(view_id, task_id)
        print("The response of RecordApi->download_record_histories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordApi->download_record_histories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId | 
 **task_id** | **str**| taskId | 

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

# **export_record_histories**
> Task export_record_histories(view_id, export_record_history)

exportRecordHistories

exportRecordHistories

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.export_record_history import ExportRecordHistory
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
    api_instance = gridly.RecordApi(api_client)
    view_id = 'view_id_example' # str | viewId
    export_record_history = gridly.ExportRecordHistory() # ExportRecordHistory | 

    try:
        # exportRecordHistories
        api_response = api_instance.export_record_histories(view_id, export_record_history)
        print("The response of RecordApi->export_record_histories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordApi->export_record_histories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId | 
 **export_record_history** | [**ExportRecordHistory**](ExportRecordHistory.md)|  | 

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
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **fetch**
> List[Record] fetch(view_id, column_ids=column_ids, page=page, query=query, sort=sort, fetch_file_option=fetch_file_option, after_record_id=after_record_id, before_record_id=before_record_id)

fetch

fetch

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.fetch_file_option import FetchFileOption
from gridly.models.record import Record
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
    api_instance = gridly.RecordApi(api_client)
    view_id = 'view_id_example' # str | viewId
    column_ids = [] # List[str] | columnIds (optional) (default to [])
    page = '{}' # str | page (optional) (default to '{}')
    query = '{}' # str | query (optional) (default to '{}')
    sort = '{}' # str | sort (optional) (default to '{}')
    fetch_file_option = gridly.FetchFileOption() # FetchFileOption | fetchFileOption (optional)
    after_record_id = 'after_record_id_example' # str | afterRecordId (optional)
    before_record_id = 'before_record_id_example' # str | beforeRecordId (optional)

    try:
        # fetch
        api_response = api_instance.fetch(view_id, column_ids=column_ids, page=page, query=query, sort=sort, fetch_file_option=fetch_file_option, after_record_id=after_record_id, before_record_id=before_record_id)
        print("The response of RecordApi->fetch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordApi->fetch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId | 
 **column_ids** | [**List[str]**](str.md)| columnIds | [optional] [default to []]
 **page** | **str**| page | [optional] [default to &#39;{}&#39;]
 **query** | **str**| query | [optional] [default to &#39;{}&#39;]
 **sort** | **str**| sort | [optional] [default to &#39;{}&#39;]
 **fetch_file_option** | [**FetchFileOption**](.md)| fetchFileOption | [optional] 
 **after_record_id** | **str**| afterRecordId | [optional] 
 **before_record_id** | **str**| beforeRecordId | [optional] 

### Return type

[**List[Record]**](Record.md)

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
> List[RecordHistory] fetch_histories(view_id, record_id, fetch_request)

fetchHistories

fetchHistories

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.fetch_record_history_request import FetchRecordHistoryRequest
from gridly.models.record_history import RecordHistory
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
    api_instance = gridly.RecordApi(api_client)
    view_id = 'view_id_example' # str | viewId
    record_id = 'record_id_example' # str | recordId
    fetch_request = gridly.FetchRecordHistoryRequest() # FetchRecordHistoryRequest | fetchRequest

    try:
        # fetchHistories
        api_response = api_instance.fetch_histories(view_id, record_id, fetch_request)
        print("The response of RecordApi->fetch_histories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordApi->fetch_histories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId | 
 **record_id** | **str**| recordId | 
 **fetch_request** | [**FetchRecordHistoryRequest**](.md)| fetchRequest | 

### Return type

[**List[RecordHistory]**](RecordHistory.md)

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
> List[Record] update(view_id, set_record)

update

update

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.record import Record
from gridly.models.set_record import SetRecord
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
    api_instance = gridly.RecordApi(api_client)
    view_id = 'view_id_example' # str | viewId
    set_record = [gridly.SetRecord()] # List[SetRecord] | 

    try:
        # update
        api_response = api_instance.update(view_id, set_record)
        print("The response of RecordApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RecordApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId | 
 **set_record** | [**List[SetRecord]**](SetRecord.md)|  | 

### Return type

[**List[Record]**](Record.md)

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
> Record update_record(id, view_id, set_record, path=path)

updateRecord

updateRecord

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.record import Record
from gridly.models.set_record import SetRecord
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
    api_instance = gridly.RecordApi(api_client)
    id = 'id_example' # str | id
    view_id = 'view_id_example' # str | viewId
    set_record = gridly.SetRecord() # SetRecord | 
    path = 'path_example' # str | path (optional)

    try:
        # updateRecord
        api_response = api_instance.update_record(id, view_id, set_record, path=path)
        print("The response of RecordApi->update_record:\n")
        pprint(api_response)
    except Exception as e:
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

