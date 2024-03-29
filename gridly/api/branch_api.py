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
from gridly.model.branch import Branch
from gridly.model.branch_diff_record import BranchDiffRecord
from gridly.model.create_branch import CreateBranch
from gridly.model.merge_branch_request import MergeBranchRequest
from gridly.model.task import Task


class BranchApi(object):
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
                'response_type': (Branch,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/v1/branches',
                'operation_id': 'create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'create_branch',
                    'grid_id',
                    'branch_id',
                ],
                'required': [
                    'create_branch',
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
                    'create_branch':
                        (CreateBranch,),
                    'grid_id':
                        (str,),
                    'branch_id':
                        (str,),
                },
                'attribute_map': {
                    'grid_id': 'gridId',
                    'branch_id': 'branchId',
                },
                'location_map': {
                    'create_branch': 'body',
                    'grid_id': 'query',
                    'branch_id': 'query',
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
        self.create_diff_check_endpoint = _Endpoint(
            settings={
                'response_type': (Task,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/v1/branches/diffcheck',
                'operation_id': 'create_diff_check',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'source_view_id',
                    'destination_view_id',
                ],
                'required': [
                    'source_view_id',
                    'destination_view_id',
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
                    'source_view_id':
                        (str,),
                    'destination_view_id':
                        (str,),
                },
                'attribute_map': {
                    'source_view_id': 'sourceViewId',
                    'destination_view_id': 'destinationViewId',
                },
                'location_map': {
                    'source_view_id': 'query',
                    'destination_view_id': 'query',
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
        self.delete_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/v1/branches/{branchId}',
                'operation_id': 'delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'branch_id',
                ],
                'required': [
                    'branch_id',
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
                    'branch_id':
                        (str,),
                },
                'attribute_map': {
                    'branch_id': 'branchId',
                },
                'location_map': {
                    'branch_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_endpoint = _Endpoint(
            settings={
                'response_type': (Branch,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/v1/branches/{branchId}',
                'operation_id': 'get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'branch_id',
                ],
                'required': [
                    'branch_id',
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
                    'branch_id':
                        (str,),
                },
                'attribute_map': {
                    'branch_id': 'branchId',
                },
                'location_map': {
                    'branch_id': 'path',
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
        self.get_diff_check_endpoint = _Endpoint(
            settings={
                'response_type': ([BranchDiffRecord],),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/v1/branches/diffcheck/{taskId}',
                'operation_id': 'get_diff_check',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'task_id',
                    'merge_record_options',
                    'query',
                    'page',
                ],
                'required': [
                    'task_id',
                ],
                'nullable': [
                    'merge_record_options',
                    'query',
                    'page',
                ],
                'enum': [
                    'merge_record_options',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('merge_record_options',): {
                        'None': None,
                        "ADD": "add",
                        "UPDATE": "update",
                        "DELETE": "delete",
                        "OVERRIDE": "override"
                    },
                },
                'openapi_types': {
                    'task_id':
                        (str,),
                    'merge_record_options':
                        ([str], none_type,),
                    'query':
                        (str, none_type,),
                    'page':
                        (str, none_type,),
                },
                'attribute_map': {
                    'task_id': 'taskId',
                    'merge_record_options': 'mergeRecordOptions',
                    'query': 'query',
                    'page': 'page',
                },
                'location_map': {
                    'task_id': 'path',
                    'merge_record_options': 'query',
                    'query': 'query',
                    'page': 'query',
                },
                'collection_format_map': {
                    'merge_record_options': 'multi',
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
        self.list_endpoint = _Endpoint(
            settings={
                'response_type': ([Branch],),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/v1/branches',
                'operation_id': 'list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'grid_id',
                ],
                'required': [
                    'grid_id',
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
                    'grid_id':
                        (str,),
                },
                'attribute_map': {
                    'grid_id': 'gridId',
                },
                'location_map': {
                    'grid_id': 'query',
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
        self.merge_endpoint = _Endpoint(
            settings={
                'response_type': (Task,),
                'auth': [
                    'ApiKey'
                ],
                'endpoint_path': '/v1/branches/{branchId}/merge',
                'operation_id': 'merge',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'branch_id',
                    'destination_branch_id',
                    'merge_branch_request',
                    'merge_record_options',
                ],
                'required': [
                    'branch_id',
                    'destination_branch_id',
                    'merge_branch_request',
                ],
                'nullable': [
                    'merge_record_options',
                ],
                'enum': [
                    'merge_record_options',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('merge_record_options',): {
                        'None': None,
                        "ADD": "add",
                        "UPDATE": "update",
                        "DELETE": "delete",
                        "OVERRIDE": "override"
                    },
                },
                'openapi_types': {
                    'branch_id':
                        (str,),
                    'destination_branch_id':
                        (str,),
                    'merge_branch_request':
                        (MergeBranchRequest,),
                    'merge_record_options':
                        ([str], none_type,),
                },
                'attribute_map': {
                    'branch_id': 'branchId',
                    'destination_branch_id': 'destinationBranchId',
                    'merge_record_options': 'mergeRecordOptions',
                },
                'location_map': {
                    'branch_id': 'path',
                    'destination_branch_id': 'query',
                    'merge_branch_request': 'body',
                    'merge_record_options': 'query',
                },
                'collection_format_map': {
                    'merge_record_options': 'multi',
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
        create_branch,
        **kwargs
    ):
        """create  # noqa: E501

        create  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create(create_branch, async_req=True)
        >>> result = thread.get()

        Args:
            create_branch (CreateBranch):

        Keyword Args:
            grid_id (str): gridId. [optional]
            branch_id (str): branchId. [optional]
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
            Branch
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
        kwargs['create_branch'] = \
            create_branch
        return self.create_endpoint.call_with_http_info(**kwargs)

    def create_diff_check(
        self,
        source_view_id,
        destination_view_id,
        **kwargs
    ):
        """createDiffCheck  # noqa: E501

        createDiffCheck  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_diff_check(source_view_id, destination_view_id, async_req=True)
        >>> result = thread.get()

        Args:
            source_view_id (str): sourceViewId
            destination_view_id (str): destinationViewId

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
            Task
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
        kwargs['source_view_id'] = \
            source_view_id
        kwargs['destination_view_id'] = \
            destination_view_id
        return self.create_diff_check_endpoint.call_with_http_info(**kwargs)

    def delete(
        self,
        branch_id,
        **kwargs
    ):
        """delete  # noqa: E501

        delete  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete(branch_id, async_req=True)
        >>> result = thread.get()

        Args:
            branch_id (str): branchId

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
        kwargs['branch_id'] = \
            branch_id
        return self.delete_endpoint.call_with_http_info(**kwargs)

    def get(
        self,
        branch_id,
        **kwargs
    ):
        """get  # noqa: E501

        get  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get(branch_id, async_req=True)
        >>> result = thread.get()

        Args:
            branch_id (str): branchId

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
            Branch
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
        kwargs['branch_id'] = \
            branch_id
        return self.get_endpoint.call_with_http_info(**kwargs)

    def get_diff_check(
        self,
        task_id,
        **kwargs
    ):
        """getDiffCheck  # noqa: E501

        getDiffCheck  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_diff_check(task_id, async_req=True)
        >>> result = thread.get()

        Args:
            task_id (str): taskId

        Keyword Args:
            merge_record_options ([str], none_type): mergeRecordOptions. [optional]
            query (str, none_type): query. [optional] if omitted the server will use the default value of "{}"
            page (str, none_type): page. [optional] if omitted the server will use the default value of "{}"
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
            [BranchDiffRecord]
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
        kwargs['task_id'] = \
            task_id
        return self.get_diff_check_endpoint.call_with_http_info(**kwargs)

    def list(
        self,
        grid_id,
        **kwargs
    ):
        """list  # noqa: E501

        list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list(grid_id, async_req=True)
        >>> result = thread.get()

        Args:
            grid_id (str): gridId

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
            [Branch]
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
        kwargs['grid_id'] = \
            grid_id
        return self.list_endpoint.call_with_http_info(**kwargs)

    def merge(
        self,
        branch_id,
        destination_branch_id,
        merge_branch_request,
        **kwargs
    ):
        """merge  # noqa: E501

        merge  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.merge(branch_id, destination_branch_id, merge_branch_request, async_req=True)
        >>> result = thread.get()

        Args:
            branch_id (str): branchId
            destination_branch_id (str): destinationBranchId
            merge_branch_request (MergeBranchRequest):

        Keyword Args:
            merge_record_options ([str], none_type): mergeRecordOptions. [optional] if omitted the server will use the default value of []
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
            Task
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
        kwargs['branch_id'] = \
            branch_id
        kwargs['destination_branch_id'] = \
            destination_branch_id
        kwargs['merge_branch_request'] = \
            merge_branch_request
        return self.merge_endpoint.call_with_http_info(**kwargs)

