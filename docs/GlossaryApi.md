# gridly.GlossaryApi

All URIs are relative to *https://api.gridly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](GlossaryApi.md#create) | **POST** /v1/glossaries | Create a new glossary
[**delete**](GlossaryApi.md#delete) | **DELETE** /v1/glossaries/{id} | Delete a glossary
[**export_file**](GlossaryApi.md#export_file) | **GET** /v1/glossaries/{id}/export | Export a glossary
[**get**](GlossaryApi.md#get) | **GET** /v1/glossaries/{id} | Get glossary info
[**get_all**](GlossaryApi.md#get_all) | **GET** /v1/glossaries | List all glossaries
[**import_file**](GlossaryApi.md#import_file) | **POST** /v1/glossaries/{id}/import | Import a glossary from file
[**update**](GlossaryApi.md#update) | **PUT** /v1/glossaries/{id} | Update glossary info


# **create**
> Glossary create(create_glossary)

Create a new glossary

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.create_glossary import CreateGlossary
from gridly.models.glossary import Glossary
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
    api_instance = gridly.GlossaryApi(api_client)
    create_glossary = gridly.CreateGlossary() # CreateGlossary | 

    try:
        # Create a new glossary
        api_response = api_instance.create(create_glossary)
        print("The response of GlossaryApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlossaryApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_glossary** | [**CreateGlossary**](CreateGlossary.md)|  | 

### Return type

[**Glossary**](Glossary.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(id)

Delete a glossary

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
    api_instance = gridly.GlossaryApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete a glossary
        api_instance.delete(id)
    except Exception as e:
        print("Exception when calling GlossaryApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **export_file**
> bytearray export_file(id, fields=fields, format=format, langs=langs)

Export a glossary

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
    api_instance = gridly.GlossaryApi(api_client)
    id = 'id_example' # str | 
    fields = ['fields_example'] # List[str] |  (optional)
    format = gridly.ExportGlossaryFormat() # ExportGlossaryFormat |  (optional)
    langs = ['langs_example'] # List[str] |  (optional)

    try:
        # Export a glossary
        api_response = api_instance.export_file(id, fields=fields, format=format, langs=langs)
        print("The response of GlossaryApi->export_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlossaryApi->export_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **fields** | [**List[str]**](str.md)|  | [optional] 
 **format** | [**ExportGlossaryFormat**](.md)|  | [optional] 
 **langs** | [**List[str]**](str.md)|  | [optional] 

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
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Glossary get(id)

Get glossary info

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.glossary import Glossary
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
    api_instance = gridly.GlossaryApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get glossary info
        api_response = api_instance.get(id)
        print("The response of GlossaryApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlossaryApi->get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Glossary**](Glossary.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all**
> List[Glossary] get_all()

List all glossaries

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.glossary import Glossary
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
    api_instance = gridly.GlossaryApi(api_client)

    try:
        # List all glossaries
        api_response = api_instance.get_all()
        print("The response of GlossaryApi->get_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlossaryApi->get_all: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Glossary]**](Glossary.md)

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

# **import_file**
> import_file(id, import_option=import_option, file=file)

Import a glossary from file

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
    api_instance = gridly.GlossaryApi(api_client)
    id = 'id_example' # str | 
    import_option = gridly.ImportGlossaryOption() # ImportGlossaryOption |  (optional)
    file = None # bytearray |  (optional)

    try:
        # Import a glossary from file
        api_instance.import_file(id, import_option=import_option, file=file)
    except Exception as e:
        print("Exception when calling GlossaryApi->import_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **import_option** | [**ImportGlossaryOption**](.md)|  | [optional] 
 **file** | **bytearray**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> Glossary update(id, update_glossary)

Update glossary info

### Example

* Api Key Authentication (ApiKey):

```python
import gridly
from gridly.models.glossary import Glossary
from gridly.models.update_glossary import UpdateGlossary
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
    api_instance = gridly.GlossaryApi(api_client)
    id = 'id_example' # str | 
    update_glossary = gridly.UpdateGlossary() # UpdateGlossary | 

    try:
        # Update glossary info
        api_response = api_instance.update(id, update_glossary)
        print("The response of GlossaryApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GlossaryApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **update_glossary** | [**UpdateGlossary**](UpdateGlossary.md)|  | 

### Return type

[**Glossary**](Glossary.md)

### Authorization

[ApiKey](../README.md#ApiKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

