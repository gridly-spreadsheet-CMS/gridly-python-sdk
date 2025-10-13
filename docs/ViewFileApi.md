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
import gridly
from gridly.models.delete_file import DeleteFile
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
    api_instance = gridly.ViewFileApi(api_client)
    column_id = 'column_id_example' # str | columnId
    record_id = 'record_id_example' # str | recordId
    view_id = 'view_id_example' # str | viewId
    delete_file = gridly.DeleteFile() # DeleteFile | 

    try:
        # delete
        api_instance.delete(column_id, record_id, view_id, delete_file)
    except Exception as e:
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
> bytearray download(file_id, view_id)

download

download

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
    api_instance = gridly.ViewFileApi(api_client)
    file_id = 'file_id_example' # str | fileId
    view_id = 'view_id_example' # str | viewId

    try:
        # download
        api_response = api_instance.download(file_id, view_id)
        print("The response of ViewFileApi->download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewFileApi->download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| fileId | 
 **view_id** | **str**| viewId | 

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

# **upload**
> UploadedFile upload(view_id, column_id, record_id, file)

upload

upload

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.uploaded_file import UploadedFile
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
    api_instance = gridly.ViewFileApi(api_client)
    view_id = 'view_id_example' # str | viewId
    column_id = 'column_id_example' # str | columnId
    record_id = 'record_id_example' # str | recordId
    file = None # bytearray | 

    try:
        # upload
        api_response = api_instance.upload(view_id, column_id, record_id, file)
        print("The response of ViewFileApi->upload:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewFileApi->upload: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId | 
 **column_id** | **str**| columnId | 
 **record_id** | **str**| recordId | 
 **file** | **bytearray**|  | 

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
> List[Record] upload_zip(view_id, column_id, file_mappings, file)

uploadZip

uploadZip

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
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
    api_instance = gridly.ViewFileApi(api_client)
    view_id = 'view_id_example' # str | viewId
    column_id = 'column_id_example' # str | 
    file_mappings = 'file_mappings_example' # str | 
    file = None # bytearray | 

    try:
        # uploadZip
        api_response = api_instance.upload_zip(view_id, column_id, file_mappings, file)
        print("The response of ViewFileApi->upload_zip:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewFileApi->upload_zip: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | **str**| viewId | 
 **column_id** | **str**|  | 
 **file_mappings** | **str**|  | 
 **file** | **bytearray**|  | 

### Return type

[**List[Record]**](Record.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

