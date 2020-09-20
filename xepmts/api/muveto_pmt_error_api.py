# coding: utf-8

"""
    XENON PMT API

    API for the XENON PMT database  # noqa: E501

    The version of the OpenAPI document: 0.2
    Contact: joe.mosbacher@gmail.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from xepmts.api_client import ApiClient
from xepmts.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class MuvetoPmtErrorApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_muveto_pmt_error_item(self, muvetopmterror_id, **kwargs):  # noqa: E501
        """Deletes a MuvetoPmtError document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_muveto_pmt_error_item(muvetopmterror_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str muvetopmterror_id: (required)
        :param str if_match: Current value of the _etag field
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.delete_muveto_pmt_error_item_with_http_info(muvetopmterror_id, **kwargs)  # noqa: E501

    def delete_muveto_pmt_error_item_with_http_info(self, muvetopmterror_id, **kwargs):  # noqa: E501
        """Deletes a MuvetoPmtError document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_muveto_pmt_error_item_with_http_info(muvetopmterror_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str muvetopmterror_id: (required)
        :param str if_match: Current value of the _etag field
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'muvetopmterror_id',
            'if_match'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_muveto_pmt_error_item" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'muvetopmterror_id' is set
        if self.api_client.client_side_validation and ('muvetopmterror_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['muvetopmterror_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `muvetopmterror_id` when calling `delete_muveto_pmt_error_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'muvetopmterror_id' in local_var_params:
            path_params['muvetopmterrorId'] = local_var_params['muvetopmterror_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_match' in local_var_params:
            header_params['If-Match'] = local_var_params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/muveto/pmt_errors/{muvetopmterrorId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_muveto_pmt_error_item(self, muvetopmterror_id, **kwargs):  # noqa: E501
        """Retrieves a MuvetoPmtError document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_muveto_pmt_error_item(muvetopmterror_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str muvetopmterror_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: MuvetoPmtError
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_muveto_pmt_error_item_with_http_info(muvetopmterror_id, **kwargs)  # noqa: E501

    def get_muveto_pmt_error_item_with_http_info(self, muvetopmterror_id, **kwargs):  # noqa: E501
        """Retrieves a MuvetoPmtError document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_muveto_pmt_error_item_with_http_info(muvetopmterror_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str muvetopmterror_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(MuvetoPmtError, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'muvetopmterror_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_muveto_pmt_error_item" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'muvetopmterror_id' is set
        if self.api_client.client_side_validation and ('muvetopmterror_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['muvetopmterror_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `muvetopmterror_id` when calling `get_muveto_pmt_error_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'muvetopmterror_id' in local_var_params:
            path_params['muvetopmterrorId'] = local_var_params['muvetopmterror_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/muveto/pmt_errors/{muvetopmterrorId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MuvetoPmtError',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_muveto_pmt_errors(self, **kwargs):  # noqa: E501
        """Retrieves one or more MuvetoPmtErrors  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_muveto_pmt_errors(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str where: the filters query parameter (ex.: {\"number\": 10})
        :param str projection: the projections query parameter (ex.: {\"name\": 1})
        :param str sort: the sort query parameter (ex.: \"city,-lastname\")
        :param int page: the pages query parameter
        :param int max_results: the max results query parameter
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: InlineResponse20028
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_muveto_pmt_errors_with_http_info(**kwargs)  # noqa: E501

    def get_muveto_pmt_errors_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves one or more MuvetoPmtErrors  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_muveto_pmt_errors_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str where: the filters query parameter (ex.: {\"number\": 10})
        :param str projection: the projections query parameter (ex.: {\"name\": 1})
        :param str sort: the sort query parameter (ex.: \"city,-lastname\")
        :param int page: the pages query parameter
        :param int max_results: the max results query parameter
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(InlineResponse20028, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'where',
            'projection',
            'sort',
            'page',
            'max_results'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_muveto_pmt_errors" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'where' in local_var_params and local_var_params['where'] is not None:  # noqa: E501
            query_params.append(('where', local_var_params['where']))  # noqa: E501
        if 'projection' in local_var_params and local_var_params['projection'] is not None:  # noqa: E501
            query_params.append(('projection', local_var_params['projection']))  # noqa: E501
        if 'sort' in local_var_params and local_var_params['sort'] is not None:  # noqa: E501
            query_params.append(('sort', local_var_params['sort']))  # noqa: E501
        if 'page' in local_var_params and local_var_params['page'] is not None:  # noqa: E501
            query_params.append(('page', local_var_params['page']))  # noqa: E501
        if 'max_results' in local_var_params and local_var_params['max_results'] is not None:  # noqa: E501
            query_params.append(('max_results', local_var_params['max_results']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/muveto/pmt_errors', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20028',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_muveto_pmt_errors(self, muveto_pmt_error, **kwargs):  # noqa: E501
        """Stores one or more MuvetoPmtErrors.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_muveto_pmt_errors(muveto_pmt_error, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param MuvetoPmtError muveto_pmt_error: A MuvetoPmtError or list of MuvetoPmtError documents (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.post_muveto_pmt_errors_with_http_info(muveto_pmt_error, **kwargs)  # noqa: E501

    def post_muveto_pmt_errors_with_http_info(self, muveto_pmt_error, **kwargs):  # noqa: E501
        """Stores one or more MuvetoPmtErrors.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_muveto_pmt_errors_with_http_info(muveto_pmt_error, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param MuvetoPmtError muveto_pmt_error: A MuvetoPmtError or list of MuvetoPmtError documents (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'muveto_pmt_error'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_muveto_pmt_errors" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'muveto_pmt_error' is set
        if self.api_client.client_side_validation and ('muveto_pmt_error' not in local_var_params or  # noqa: E501
                                                        local_var_params['muveto_pmt_error'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `muveto_pmt_error` when calling `post_muveto_pmt_errors`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'muveto_pmt_error' in local_var_params:
            body_params = local_var_params['muveto_pmt_error']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/muveto/pmt_errors', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def put_muveto_pmt_error_item(self, muvetopmterror_id, muveto_pmt_error, **kwargs):  # noqa: E501
        """Replaces a MuvetoPmtError document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_muveto_pmt_error_item(muvetopmterror_id, muveto_pmt_error, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str muvetopmterror_id: (required)
        :param MuvetoPmtError muveto_pmt_error: A MuvetoPmtError or list of MuvetoPmtError documents (required)
        :param str if_match: Current value of the _etag field
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.put_muveto_pmt_error_item_with_http_info(muvetopmterror_id, muveto_pmt_error, **kwargs)  # noqa: E501

    def put_muveto_pmt_error_item_with_http_info(self, muvetopmterror_id, muveto_pmt_error, **kwargs):  # noqa: E501
        """Replaces a MuvetoPmtError document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_muveto_pmt_error_item_with_http_info(muvetopmterror_id, muveto_pmt_error, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str muvetopmterror_id: (required)
        :param MuvetoPmtError muveto_pmt_error: A MuvetoPmtError or list of MuvetoPmtError documents (required)
        :param str if_match: Current value of the _etag field
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'muvetopmterror_id',
            'muveto_pmt_error',
            'if_match'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method put_muveto_pmt_error_item" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'muvetopmterror_id' is set
        if self.api_client.client_side_validation and ('muvetopmterror_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['muvetopmterror_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `muvetopmterror_id` when calling `put_muveto_pmt_error_item`")  # noqa: E501
        # verify the required parameter 'muveto_pmt_error' is set
        if self.api_client.client_side_validation and ('muveto_pmt_error' not in local_var_params or  # noqa: E501
                                                        local_var_params['muveto_pmt_error'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `muveto_pmt_error` when calling `put_muveto_pmt_error_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'muvetopmterror_id' in local_var_params:
            path_params['muvetopmterrorId'] = local_var_params['muvetopmterror_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_match' in local_var_params:
            header_params['If-Match'] = local_var_params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'muveto_pmt_error' in local_var_params:
            body_params = local_var_params['muveto_pmt_error']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/muveto/pmt_errors/{muvetopmterrorId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
