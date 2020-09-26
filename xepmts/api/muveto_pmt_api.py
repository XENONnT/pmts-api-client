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


class MuvetoPmtApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_muveto_pmt_item(self, muvetopmt_id, **kwargs):  # noqa: E501
        """Deletes a MuvetoPmt document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_muveto_pmt_item(muvetopmt_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str muvetopmt_id: (required)
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
        return self.delete_muveto_pmt_item_with_http_info(muvetopmt_id, **kwargs)  # noqa: E501

    def delete_muveto_pmt_item_with_http_info(self, muvetopmt_id, **kwargs):  # noqa: E501
        """Deletes a MuvetoPmt document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_muveto_pmt_item_with_http_info(muvetopmt_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str muvetopmt_id: (required)
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
            'muvetopmt_id',
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
                    " to method delete_muveto_pmt_item" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'muvetopmt_id' is set
        if self.api_client.client_side_validation and ('muvetopmt_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['muvetopmt_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `muvetopmt_id` when calling `delete_muveto_pmt_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'muvetopmt_id' in local_var_params:
            path_params['muvetopmtId'] = local_var_params['muvetopmt_id']  # noqa: E501

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
            '/muveto/pmts/{muvetopmtId}', 'DELETE',
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

    def get_muveto_pmt_item(self, muvetopmt_id, **kwargs):  # noqa: E501
        """Retrieves a MuvetoPmt document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_muveto_pmt_item(muvetopmt_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str muvetopmt_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: MuvetoPmt
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_muveto_pmt_item_with_http_info(muvetopmt_id, **kwargs)  # noqa: E501

    def get_muveto_pmt_item_with_http_info(self, muvetopmt_id, **kwargs):  # noqa: E501
        """Retrieves a MuvetoPmt document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_muveto_pmt_item_with_http_info(muvetopmt_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str muvetopmt_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(MuvetoPmt, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'muvetopmt_id'
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
                    " to method get_muveto_pmt_item" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'muvetopmt_id' is set
        if self.api_client.client_side_validation and ('muvetopmt_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['muvetopmt_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `muvetopmt_id` when calling `get_muveto_pmt_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'muvetopmt_id' in local_var_params:
            path_params['muvetopmtId'] = local_var_params['muvetopmt_id']  # noqa: E501

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
            '/muveto/pmts/{muvetopmtId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MuvetoPmt',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_muveto_pmt_item_by_serial_number(self, serial_number, **kwargs):  # noqa: E501
        """Retrieves a MuvetoPmt document by serial_number  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_muveto_pmt_item_by_serial_number(serial_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str serial_number: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: MuvetoPmt
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_muveto_pmt_item_by_serial_number_with_http_info(serial_number, **kwargs)  # noqa: E501

    def get_muveto_pmt_item_by_serial_number_with_http_info(self, serial_number, **kwargs):  # noqa: E501
        """Retrieves a MuvetoPmt document by serial_number  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_muveto_pmt_item_by_serial_number_with_http_info(serial_number, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str serial_number: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(MuvetoPmt, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'serial_number'
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
                    " to method get_muveto_pmt_item_by_serial_number" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'serial_number' is set
        if self.api_client.client_side_validation and ('serial_number' not in local_var_params or  # noqa: E501
                                                        local_var_params['serial_number'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `serial_number` when calling `get_muveto_pmt_item_by_serial_number`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'serial_number' in local_var_params:
            path_params['Serial_Number'] = local_var_params['serial_number']  # noqa: E501

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
            '/muveto/pmts/{Serial_Number}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MuvetoPmt',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_muveto_pmts(self, **kwargs):  # noqa: E501
        """Retrieves one or more MuvetoPmts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_muveto_pmts(async_req=True)
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
        :return: InlineResponse20032
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_muveto_pmts_with_http_info(**kwargs)  # noqa: E501

    def get_muveto_pmts_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves one or more MuvetoPmts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_muveto_pmts_with_http_info(async_req=True)
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
        :return: tuple(InlineResponse20032, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_muveto_pmts" % key
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
            '/muveto/pmts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20032',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_muveto_pmt_item(self, muvetopmt_id, muveto_pmt, **kwargs):  # noqa: E501
        """Updates a MuvetoPmt document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_muveto_pmt_item(muvetopmt_id, muveto_pmt, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str muvetopmt_id: (required)
        :param MuvetoPmt muveto_pmt: A MuvetoPmt or list of MuvetoPmt documents (required)
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
        return self.patch_muveto_pmt_item_with_http_info(muvetopmt_id, muveto_pmt, **kwargs)  # noqa: E501

    def patch_muveto_pmt_item_with_http_info(self, muvetopmt_id, muveto_pmt, **kwargs):  # noqa: E501
        """Updates a MuvetoPmt document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_muveto_pmt_item_with_http_info(muvetopmt_id, muveto_pmt, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str muvetopmt_id: (required)
        :param MuvetoPmt muveto_pmt: A MuvetoPmt or list of MuvetoPmt documents (required)
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
            'muvetopmt_id',
            'muveto_pmt',
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
                    " to method patch_muveto_pmt_item" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'muvetopmt_id' is set
        if self.api_client.client_side_validation and ('muvetopmt_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['muvetopmt_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `muvetopmt_id` when calling `patch_muveto_pmt_item`")  # noqa: E501
        # verify the required parameter 'muveto_pmt' is set
        if self.api_client.client_side_validation and ('muveto_pmt' not in local_var_params or  # noqa: E501
                                                        local_var_params['muveto_pmt'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `muveto_pmt` when calling `patch_muveto_pmt_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'muvetopmt_id' in local_var_params:
            path_params['muvetopmtId'] = local_var_params['muvetopmt_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_match' in local_var_params:
            header_params['If-Match'] = local_var_params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'muveto_pmt' in local_var_params:
            body_params = local_var_params['muveto_pmt']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/muveto/pmts/{muvetopmtId}', 'PATCH',
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

    def post_muveto_pmts(self, muveto_pmt, **kwargs):  # noqa: E501
        """Stores one or more MuvetoPmts.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_muveto_pmts(muveto_pmt, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param MuvetoPmt muveto_pmt: A MuvetoPmt or list of MuvetoPmt documents (required)
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
        return self.post_muveto_pmts_with_http_info(muveto_pmt, **kwargs)  # noqa: E501

    def post_muveto_pmts_with_http_info(self, muveto_pmt, **kwargs):  # noqa: E501
        """Stores one or more MuvetoPmts.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_muveto_pmts_with_http_info(muveto_pmt, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param MuvetoPmt muveto_pmt: A MuvetoPmt or list of MuvetoPmt documents (required)
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
            'muveto_pmt'
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
                    " to method post_muveto_pmts" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'muveto_pmt' is set
        if self.api_client.client_side_validation and ('muveto_pmt' not in local_var_params or  # noqa: E501
                                                        local_var_params['muveto_pmt'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `muveto_pmt` when calling `post_muveto_pmts`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'muveto_pmt' in local_var_params:
            body_params = local_var_params['muveto_pmt']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/muveto/pmts', 'POST',
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

    def put_muveto_pmt_item(self, muvetopmt_id, muveto_pmt, **kwargs):  # noqa: E501
        """Replaces a MuvetoPmt document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_muveto_pmt_item(muvetopmt_id, muveto_pmt, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str muvetopmt_id: (required)
        :param MuvetoPmt muveto_pmt: A MuvetoPmt or list of MuvetoPmt documents (required)
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
        return self.put_muveto_pmt_item_with_http_info(muvetopmt_id, muveto_pmt, **kwargs)  # noqa: E501

    def put_muveto_pmt_item_with_http_info(self, muvetopmt_id, muveto_pmt, **kwargs):  # noqa: E501
        """Replaces a MuvetoPmt document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_muveto_pmt_item_with_http_info(muvetopmt_id, muveto_pmt, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str muvetopmt_id: (required)
        :param MuvetoPmt muveto_pmt: A MuvetoPmt or list of MuvetoPmt documents (required)
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
            'muvetopmt_id',
            'muveto_pmt',
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
                    " to method put_muveto_pmt_item" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'muvetopmt_id' is set
        if self.api_client.client_side_validation and ('muvetopmt_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['muvetopmt_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `muvetopmt_id` when calling `put_muveto_pmt_item`")  # noqa: E501
        # verify the required parameter 'muveto_pmt' is set
        if self.api_client.client_side_validation and ('muveto_pmt' not in local_var_params or  # noqa: E501
                                                        local_var_params['muveto_pmt'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `muveto_pmt` when calling `put_muveto_pmt_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'muvetopmt_id' in local_var_params:
            path_params['muvetopmtId'] = local_var_params['muvetopmt_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_match' in local_var_params:
            header_params['If-Match'] = local_var_params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'muveto_pmt' in local_var_params:
            body_params = local_var_params['muveto_pmt']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/muveto/pmts/{muvetopmtId}', 'PUT',
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
