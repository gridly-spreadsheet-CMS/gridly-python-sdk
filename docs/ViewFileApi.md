# gridly.ViewFileApi

All URIs are relative to *https://api.gridly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](ViewFileApi.md#delete) | **DELETE** /v1/views/{viewId}/files | delete
[**download**](ViewFileApi.md#download) | **GET** /v1/views/{viewId}/files/{fileId} | download
[**upload**](ViewFileApi.md#upload) | **POST** /v1/views/{viewId}/files | upload
[**upload_zip**](ViewFileApi.md#upload_zip) | **POST** /v1/views/{viewId}/files/zip | uploadZip


# **delete**
> delete(column_id, record_id, view_id, delete_file)

delete

delete

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import view_file_api
from gridly.model.delete_file import DeleteFile
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
    api_instance = view_file_api.ViewFileApi(api_client)
    column_id = "columnId_example" # str | columnId
    record_id = "recordId_example" # str | recordId
    view_id = "viewId_example" # str | viewId
    delete_file = DeleteFile(
        ids=[
            "ids_example",
        ],
    ) # DeleteFile | 

    # example passing only required values which don't have defaults set
    try:
        # delete
        api_instance.delete(column_id, record_id, view_id, delete_file)
    except gridly.ApiException as e:
        print("Exception when calling ViewFileApi->delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **column_id** | **str**| columnId |
 **record_id** | **str**| recordId |
 **view_id** | **str**| viewId |
 **delete_file** | [**DeleteFile**](DeleteFile.md)|  |

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

# **download**
> file_type download(file_id, view_id)

download

download

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import view_file_api
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
    api_instance = view_file_api.ViewFileApi(api_client)
    file_id = "fileId_example" # str | fileId
    view_id = "viewId_example" # str | viewId

    # example passing only required values which don't have defaults set
    try:
        # download
        api_response = api_instance.download(file_id, view_id)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ViewFileApi->download: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| fileId |
 **view_id** | **str**| viewId |

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

# **upload**
> UploadedFile upload(view_id, column_id, record_id, file)

upload

upload

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import view_file_api
from gridly.model.uploaded_file import UploadedFile
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
    api_instance = view_file_api.ViewFileApi(api_client)
    view_id = "viewId_example" # str | viewId
    column_id = "columnId_example" # str | columnId
    record_id = "recordId_example" # str | recordId
    file = open('/path/to/file', 'rb') # file_type | 

    # example passing only required values which don't have defaults set
    try:
        # upload
        api_response = api_instance.upload(view_id, column_id, record_id, file)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ViewFileApi->upload: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId |
 **column_id** | **str**| columnId |
 **record_id** | **str**| recordId |
 **file** | **file_type**|  |

### Return type

[**UploadedFile**](UploadedFile.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_zip**
> [Record] upload_zip(view_id, column_id, file_mappings, file)

uploadZip

uploadZip

### Example

* Api Key Authentication (ApiKey):

```python
import time
import gridly
from gridly.api import view_file_api
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
    api_instance = view_file_api.ViewFileApi(api_client)
    view_id = "viewId_example" # str | viewId
    column_id = "column_id_example" # str | 
    file_mappings = "file_mappings_example" # str | 
    file = open('/path/to/file', 'rb') # file_type | 

    # example passing only required values which don't have defaults set
    try:
        # uploadZip
        api_response = api_instance.upload_zip(view_id, column_id, file_mappings, file)
        pprint(api_response)
    except gridly.ApiException as e:
        print("Exception when calling ViewFileApi->upload_zip: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId |
 **column_id** | **str**|  |
 **file_mappings** | **str**|  |
 **file** | **file_type**|  |

### Return type

[**[Record]**](Record.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

