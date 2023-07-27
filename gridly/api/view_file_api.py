"""
    Gridly API

    Gridly API documentation  # noqa: E501

    The version of the OpenAPI document: 4.15.1
    Contact: support@gridly.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from gridly.api_client import ApiClient, Endpoint as _Endpoint
from gridly.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from gridly.model.delete_file import DeleteFile
from gridly.model.record import Record
from gridly.model.uploaded_file import UploadedFile


class ViewFileApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.delete_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/v1/views/{viewId}/files',
                'operation_id': 'delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'column_id',
                    'record_id',
                    'view_id',
                    'delete_file',
                ],
                'required': [
                    'column_id',
                    'record_id',
                    'view_id',
                    'delete_file',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'column_id':
                        (str,),
                    'record_id':
                        (str,),
                    'view_id':
                        (str,),
                    'delete_file':
                        (DeleteFile,),
                },
                'attribute_map': {
                    'column_id': 'columnId',
                    'record_id': 'recordId',
                    'view_id': 'viewId',
                },
                'location_map': {
                    'column_id': 'query',
                    'record_id': 'query',
                    'view_id': 'path',
                    'delete_file': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.download_endpoint = _Endpoint(
            settings={
                'response_type': (file_type,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/v1/views/{viewId}/files/{fileId}',
                'operation_id': 'download',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_id',
                    'view_id',
                ],
                'required': [
                    'file_id',
                    'view_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'file_id':
                        (str,),
                    'view_id':
                        (str,),
                },
                'attribute_map': {
                    'file_id': 'fileId',
                    'view_id': 'viewId',
                },
                'location_map': {
                    'file_id': 'path',
                    'view_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/octet-stream'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.upload_endpoint = _Endpoint(
            settings={
                'response_type': (UploadedFile,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/v1/views/{viewId}/files',
                'operation_id': 'upload',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'view_id',
                    'column_id',
                    'record_id',
                    'file',
                ],
                'required': [
                    'view_id',
                    'column_id',
                    'record_id',
                    'file',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'view_id':
                        (str,),
                    'column_id':
                        (str,),
                    'record_id':
                        (str,),
                    'file':
                        (file_type,),
                },
                'attribute_map': {
                    'view_id': 'viewId',
                    'column_id': 'columnId',
                    'record_id': 'recordId',
                    'file': 'file',
                },
                'location_map': {
                    'view_id': 'path',
                    'column_id': 'query',
                    'record_id': 'query',
                    'file': 'form',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'multipart/form-data'
                ]
            },
            api_client=api_client
        )
        self.upload_zip_endpoint = _Endpoint(
            settings={
                'response_type': ([Record],),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/v1/views/{viewId}/files/zip',
                'operation_id': 'upload_zip',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'view_id',
                    'column_id',
                    'file_mappings',
                    'file',
                ],
                'required': [
                    'view_id',
                    'column_id',
                    'file_mappings',
                    'file',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'view_id':
                        (str,),
                    'column_id':
                        (str,),
                    'file_mappings':
                        (str,),
                    'file':
                        (file_type,),
                },
                'attribute_map': {
                    'view_id': 'viewId',
                    'column_id': 'columnId',
                    'file_mappings': 'fileMappings',
                    'file': 'file',
                },
                'location_map': {
                    'view_id': 'path',
                    'column_id': 'form',
                    'file_mappings': 'form',
                    'file': 'form',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'multipart/form-data',
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def delete(
        self,
        column_id,
        record_id,
        view_id,
        delete_file,
        **kwargs
    ):
        """delete  # noqa: E501

        delete  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete(column_id, record_id, view_id, delete_file, async_req=True)
        >>> result = thread.get()

        Args:
            column_id (str): columnId
            record_id (str): recordId
            view_id (str): viewId
            delete_file (DeleteFile):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            None
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['column_id'] = \
            column_id
        kwargs['record_id'] = \
            record_id
        kwargs['view_id'] = \
            view_id
        kwargs['delete_file'] = \
            delete_file
        return self.delete_endpoint.call_with_http_info(**kwargs)

    def download(
        self,
        file_id,
        view_id,
        **kwargs
    ):
        """download  # noqa: E501

        download  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.download(file_id, view_id, async_req=True)
        >>> result = thread.get()

        Args:
            file_id (str): fileId
            view_id (str): viewId

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            file_type
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['file_id'] = \
            file_id
        kwargs['view_id'] = \
            view_id
        return self.download_endpoint.call_with_http_info(**kwargs)

    def upload(
        self,
        view_id,
        column_id,
        record_id,
        file,
        **kwargs
    ):
        """upload  # noqa: E501

        upload  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload(view_id, column_id, record_id, file, async_req=True)
        >>> result = thread.get()

        Args:
            view_id (str): viewId
            column_id (str): columnId
            record_id (str): recordId
            file (file_type):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            UploadedFile
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['view_id'] = \
            view_id
        kwargs['column_id'] = \
            column_id
        kwargs['record_id'] = \
            record_id
        kwargs['file'] = \
            file
        return self.upload_endpoint.call_with_http_info(**kwargs)

    def upload_zip(
        self,
        view_id,
        column_id,
        file_mappings,
        file,
        **kwargs
    ):
        """uploadZip  # noqa: E501

        uploadZip  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_zip(view_id, column_id, file_mappings, file, async_req=True)
        >>> result = thread.get()

        Args:
            view_id (str): viewId
            column_id (str):
            file_mappings (str):
            file (file_type):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [Record]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['view_id'] = \
            view_id
        kwargs['column_id'] = \
            column_id
        kwargs['file_mappings'] = \
            file_mappings
        kwargs['file'] = \
            file
        return self.upload_zip_endpoint.call_with_http_info(**kwargs)
