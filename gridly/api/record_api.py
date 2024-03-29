"""
    Gridly API

    Gridly API documentation  # noqa: E501

    The version of the OpenAPI document: 4.29.1
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
from gridly.model.delete_record import DeleteRecord
from gridly.model.fetch_file_option import FetchFileOption
from gridly.model.fetch_record_history_request import FetchRecordHistoryRequest
from gridly.model.record import Record
from gridly.model.record_history import RecordHistory
from gridly.model.set_record import SetRecord


class RecordApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_endpoint = _Endpoint(
            settings={
                'response_type': ([Record],),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/v1/views/{viewId}/records',
                'operation_id': 'create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'view_id',
                    'create_records',
                ],
                'required': [
                    'view_id',
                    'create_records',
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
                    'create_records':
                        ([SetRecord],),
                },
                'attribute_map': {
                    'view_id': 'viewId',
                },
                'location_map': {
                    'view_id': 'path',
                    'create_records': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.delete_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/v1/views/{viewId}/records',
                'operation_id': 'delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'view_id',
                    'delete_record',
                ],
                'required': [
                    'view_id',
                    'delete_record',
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
                    'delete_record':
                        (DeleteRecord,),
                },
                'attribute_map': {
                    'view_id': 'viewId',
                },
                'location_map': {
                    'view_id': 'path',
                    'delete_record': 'body',
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
        self.fetch_endpoint = _Endpoint(
            settings={
                'response_type': ([Record],),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/v1/views/{viewId}/records',
                'operation_id': 'fetch',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'view_id',
                    'column_ids',
                    'page',
                    'query',
                    'sort',
                    'fetch_file_option',
                    'after_record_id',
                    'before_record_id',
                ],
                'required': [
                    'view_id',
                ],
                'nullable': [
                    'column_ids',
                    'page',
                    'query',
                    'sort',
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
                    'column_ids':
                        ([str], none_type,),
                    'page':
                        (str, none_type,),
                    'query':
                        (str, none_type,),
                    'sort':
                        (str, none_type,),
                    'fetch_file_option':
                        (FetchFileOption,),
                    'after_record_id':
                        (str,),
                    'before_record_id':
                        (str,),
                },
                'attribute_map': {
                    'view_id': 'viewId',
                    'column_ids': 'columnIds',
                    'page': 'page',
                    'query': 'query',
                    'sort': 'sort',
                    'fetch_file_option': 'fetchFileOption',
                    'after_record_id': 'afterRecordId',
                    'before_record_id': 'beforeRecordId',
                },
                'location_map': {
                    'view_id': 'path',
                    'column_ids': 'query',
                    'page': 'query',
                    'query': 'query',
                    'sort': 'query',
                    'fetch_file_option': 'query',
                    'after_record_id': 'query',
                    'before_record_id': 'query',
                },
                'collection_format_map': {
                    'column_ids': 'multi',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.fetch_histories_endpoint = _Endpoint(
            settings={
                'response_type': ([RecordHistory],),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/v1/views/{viewId}/records/{recordId}/histories',
                'operation_id': 'fetch_histories',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'view_id',
                    'record_id',
                    'fetch_request',
                ],
                'required': [
                    'view_id',
                    'record_id',
                    'fetch_request',
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
                    'record_id':
                        (str,),
                    'fetch_request':
                        (FetchRecordHistoryRequest,),
                },
                'attribute_map': {
                    'view_id': 'viewId',
                    'record_id': 'recordId',
                    'fetch_request': 'fetchRequest',
                },
                'location_map': {
                    'view_id': 'path',
                    'record_id': 'path',
                    'fetch_request': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.update_endpoint = _Endpoint(
            settings={
                'response_type': ([Record],),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/v1/views/{viewId}/records',
                'operation_id': 'update',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'view_id',
                    'set_record',
                ],
                'required': [
                    'view_id',
                    'set_record',
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
                    'set_record':
                        ([SetRecord],),
                },
                'attribute_map': {
                    'view_id': 'viewId',
                },
                'location_map': {
                    'view_id': 'path',
                    'set_record': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.update_record_endpoint = _Endpoint(
            settings={
                'response_type': (Record,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/v1/views/{viewId}/records/{id}',
                'operation_id': 'update_record',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'view_id',
                    'set_record',
                    'path',
                ],
                'required': [
                    'id',
                    'view_id',
                    'set_record',
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
                    'id':
                        (str,),
                    'view_id':
                        (str,),
                    'set_record':
                        (SetRecord,),
                    'path':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'view_id': 'viewId',
                    'path': 'path',
                },
                'location_map': {
                    'id': 'path',
                    'view_id': 'path',
                    'set_record': 'body',
                    'path': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def create(
        self,
        view_id,
        create_records,
        **kwargs
    ):
        """create  # noqa: E501

        create  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create(view_id, create_records, async_req=True)
        >>> result = thread.get()

        Args:
            view_id (str): viewId
            create_records ([SetRecord]): createRecords

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
        kwargs['create_records'] = \
            create_records
        return self.create_endpoint.call_with_http_info(**kwargs)

    def delete(
        self,
        view_id,
        delete_record,
        **kwargs
    ):
        """delete  # noqa: E501

        delete  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete(view_id, delete_record, async_req=True)
        >>> result = thread.get()

        Args:
            view_id (str): viewId
            delete_record (DeleteRecord):

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
        kwargs['view_id'] = \
            view_id
        kwargs['delete_record'] = \
            delete_record
        return self.delete_endpoint.call_with_http_info(**kwargs)

    def fetch(
        self,
        view_id,
        **kwargs
    ):
        """fetch  # noqa: E501

        fetch  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fetch(view_id, async_req=True)
        >>> result = thread.get()

        Args:
            view_id (str): viewId

        Keyword Args:
            column_ids ([str], none_type): columnIds. [optional] if omitted the server will use the default value of []
            page (str, none_type): page. [optional] if omitted the server will use the default value of "{}"
            query (str, none_type): query. [optional] if omitted the server will use the default value of "{}"
            sort (str, none_type): sort. [optional] if omitted the server will use the default value of "{}"
            fetch_file_option (FetchFileOption): fetchFileOption. [optional]
            after_record_id (str): afterRecordId. [optional]
            before_record_id (str): beforeRecordId. [optional]
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
        return self.fetch_endpoint.call_with_http_info(**kwargs)

    def fetch_histories(
        self,
        view_id,
        record_id,
        fetch_request,
        **kwargs
    ):
        """fetchHistories  # noqa: E501

        fetchHistories  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.fetch_histories(view_id, record_id, fetch_request, async_req=True)
        >>> result = thread.get()

        Args:
            view_id (str): viewId
            record_id (str): recordId
            fetch_request (FetchRecordHistoryRequest): fetchRequest

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
            [RecordHistory]
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
        kwargs['record_id'] = \
            record_id
        kwargs['fetch_request'] = \
            fetch_request
        return self.fetch_histories_endpoint.call_with_http_info(**kwargs)

    def update(
        self,
        view_id,
        set_record,
        **kwargs
    ):
        """update  # noqa: E501

        update  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update(view_id, set_record, async_req=True)
        >>> result = thread.get()

        Args:
            view_id (str): viewId
            set_record ([SetRecord]):

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
        kwargs['set_record'] = \
            set_record
        return self.update_endpoint.call_with_http_info(**kwargs)

    def update_record(
        self,
        id,
        view_id,
        set_record,
        **kwargs
    ):
        """updateRecord  # noqa: E501

        updateRecord  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_record(id, view_id, set_record, async_req=True)
        >>> result = thread.get()

        Args:
            id (str): id
            view_id (str): viewId
            set_record (SetRecord):

        Keyword Args:
            path (str): path. [optional]
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
            Record
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
        kwargs['id'] = \
            id
        kwargs['view_id'] = \
            view_id
        kwargs['set_record'] = \
            set_record
        return self.update_record_endpoint.call_with_http_info(**kwargs)

