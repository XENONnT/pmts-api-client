# coding: utf-8

"""
    XENON PMT API

    API for the XENON PMT database  # noqa: E501

    The version of the OpenAPI document: 1.0
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


class NvetoVoltageChangeApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_nveto_voltage_change_item(self, nvetovoltagechange_id, **kwargs):  # noqa: E501
        """Deletes a NvetoVoltageChange document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_nveto_voltage_change_item(nvetovoltagechange_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str nvetovoltagechange_id: (required)
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
        return self.delete_nveto_voltage_change_item_with_http_info(nvetovoltagechange_id, **kwargs)  # noqa: E501

    def delete_nveto_voltage_change_item_with_http_info(self, nvetovoltagechange_id, **kwargs):  # noqa: E501
        """Deletes a NvetoVoltageChange document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_nveto_voltage_change_item_with_http_info(nvetovoltagechange_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str nvetovoltagechange_id: (required)
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
            'nvetovoltagechange_id',
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
                    " to method delete_nveto_voltage_change_item" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'nvetovoltagechange_id' is set
        if self.api_client.client_side_validation and ('nvetovoltagechange_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nvetovoltagechange_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nvetovoltagechange_id` when calling `delete_nveto_voltage_change_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'nvetovoltagechange_id' in local_var_params:
            path_params['nvetovoltagechangeId'] = local_var_params['nvetovoltagechange_id']  # noqa: E501

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
            '/nveto/voltage_changes/{nvetovoltagechangeId}', 'DELETE',
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

    def get_nveto_voltage_change_item(self, nvetovoltagechange_id, **kwargs):  # noqa: E501
        """Retrieves a NvetoVoltageChange document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_nveto_voltage_change_item(nvetovoltagechange_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str nvetovoltagechange_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: NvetoVoltageChange
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_nveto_voltage_change_item_with_http_info(nvetovoltagechange_id, **kwargs)  # noqa: E501

    def get_nveto_voltage_change_item_with_http_info(self, nvetovoltagechange_id, **kwargs):  # noqa: E501
        """Retrieves a NvetoVoltageChange document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_nveto_voltage_change_item_with_http_info(nvetovoltagechange_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str nvetovoltagechange_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(NvetoVoltageChange, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'nvetovoltagechange_id'
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
                    " to method get_nveto_voltage_change_item" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'nvetovoltagechange_id' is set
        if self.api_client.client_side_validation and ('nvetovoltagechange_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nvetovoltagechange_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nvetovoltagechange_id` when calling `get_nveto_voltage_change_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'nvetovoltagechange_id' in local_var_params:
            path_params['nvetovoltagechangeId'] = local_var_params['nvetovoltagechange_id']  # noqa: E501

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
            '/nveto/voltage_changes/{nvetovoltagechangeId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NvetoVoltageChange',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_nveto_voltage_changes(self, **kwargs):  # noqa: E501
        """Retrieves one or more NvetoVoltageChanges  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_nveto_voltage_changes(async_req=True)
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
        :return: InlineResponse20023
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_nveto_voltage_changes_with_http_info(**kwargs)  # noqa: E501

    def get_nveto_voltage_changes_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves one or more NvetoVoltageChanges  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_nveto_voltage_changes_with_http_info(async_req=True)
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
        :return: tuple(InlineResponse20023, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_nveto_voltage_changes" % key
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
            '/nveto/voltage_changes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse20023',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_nveto_voltage_change_item(self, nvetovoltagechange_id, nveto_voltage_change, **kwargs):  # noqa: E501
        """Updates a NvetoVoltageChange document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_nveto_voltage_change_item(nvetovoltagechange_id, nveto_voltage_change, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str nvetovoltagechange_id: (required)
        :param NvetoVoltageChange nveto_voltage_change: A NvetoVoltageChange or list of NvetoVoltageChange documents (required)
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
        return self.patch_nveto_voltage_change_item_with_http_info(nvetovoltagechange_id, nveto_voltage_change, **kwargs)  # noqa: E501

    def patch_nveto_voltage_change_item_with_http_info(self, nvetovoltagechange_id, nveto_voltage_change, **kwargs):  # noqa: E501
        """Updates a NvetoVoltageChange document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_nveto_voltage_change_item_with_http_info(nvetovoltagechange_id, nveto_voltage_change, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str nvetovoltagechange_id: (required)
        :param NvetoVoltageChange nveto_voltage_change: A NvetoVoltageChange or list of NvetoVoltageChange documents (required)
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
            'nvetovoltagechange_id',
            'nveto_voltage_change',
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
                    " to method patch_nveto_voltage_change_item" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'nvetovoltagechange_id' is set
        if self.api_client.client_side_validation and ('nvetovoltagechange_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nvetovoltagechange_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nvetovoltagechange_id` when calling `patch_nveto_voltage_change_item`")  # noqa: E501
        # verify the required parameter 'nveto_voltage_change' is set
        if self.api_client.client_side_validation and ('nveto_voltage_change' not in local_var_params or  # noqa: E501
                                                        local_var_params['nveto_voltage_change'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nveto_voltage_change` when calling `patch_nveto_voltage_change_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'nvetovoltagechange_id' in local_var_params:
            path_params['nvetovoltagechangeId'] = local_var_params['nvetovoltagechange_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_match' in local_var_params:
            header_params['If-Match'] = local_var_params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'nveto_voltage_change' in local_var_params:
            body_params = local_var_params['nveto_voltage_change']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/nveto/voltage_changes/{nvetovoltagechangeId}', 'PATCH',
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

    def post_nveto_voltage_changes(self, nveto_voltage_change, **kwargs):  # noqa: E501
        """Stores one or more NvetoVoltageChanges.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_nveto_voltage_changes(nveto_voltage_change, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param NvetoVoltageChange nveto_voltage_change: A NvetoVoltageChange or list of NvetoVoltageChange documents (required)
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
        return self.post_nveto_voltage_changes_with_http_info(nveto_voltage_change, **kwargs)  # noqa: E501

    def post_nveto_voltage_changes_with_http_info(self, nveto_voltage_change, **kwargs):  # noqa: E501
        """Stores one or more NvetoVoltageChanges.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_nveto_voltage_changes_with_http_info(nveto_voltage_change, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param NvetoVoltageChange nveto_voltage_change: A NvetoVoltageChange or list of NvetoVoltageChange documents (required)
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
            'nveto_voltage_change'
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
                    " to method post_nveto_voltage_changes" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'nveto_voltage_change' is set
        if self.api_client.client_side_validation and ('nveto_voltage_change' not in local_var_params or  # noqa: E501
                                                        local_var_params['nveto_voltage_change'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nveto_voltage_change` when calling `post_nveto_voltage_changes`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'nveto_voltage_change' in local_var_params:
            body_params = local_var_params['nveto_voltage_change']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/nveto/voltage_changes', 'POST',
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

    def put_nveto_voltage_change_item(self, nvetovoltagechange_id, nveto_voltage_change, **kwargs):  # noqa: E501
        """Replaces a NvetoVoltageChange document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_nveto_voltage_change_item(nvetovoltagechange_id, nveto_voltage_change, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str nvetovoltagechange_id: (required)
        :param NvetoVoltageChange nveto_voltage_change: A NvetoVoltageChange or list of NvetoVoltageChange documents (required)
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
        return self.put_nveto_voltage_change_item_with_http_info(nvetovoltagechange_id, nveto_voltage_change, **kwargs)  # noqa: E501

    def put_nveto_voltage_change_item_with_http_info(self, nvetovoltagechange_id, nveto_voltage_change, **kwargs):  # noqa: E501
        """Replaces a NvetoVoltageChange document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_nveto_voltage_change_item_with_http_info(nvetovoltagechange_id, nveto_voltage_change, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str nvetovoltagechange_id: (required)
        :param NvetoVoltageChange nveto_voltage_change: A NvetoVoltageChange or list of NvetoVoltageChange documents (required)
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
            'nvetovoltagechange_id',
            'nveto_voltage_change',
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
                    " to method put_nveto_voltage_change_item" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'nvetovoltagechange_id' is set
        if self.api_client.client_side_validation and ('nvetovoltagechange_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['nvetovoltagechange_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nvetovoltagechange_id` when calling `put_nveto_voltage_change_item`")  # noqa: E501
        # verify the required parameter 'nveto_voltage_change' is set
        if self.api_client.client_side_validation and ('nveto_voltage_change' not in local_var_params or  # noqa: E501
                                                        local_var_params['nveto_voltage_change'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `nveto_voltage_change` when calling `put_nveto_voltage_change_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'nvetovoltagechange_id' in local_var_params:
            path_params['nvetovoltagechangeId'] = local_var_params['nvetovoltagechange_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_match' in local_var_params:
            header_params['If-Match'] = local_var_params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'nveto_voltage_change' in local_var_params:
            body_params = local_var_params['nveto_voltage_change']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/nveto/voltage_changes/{nvetovoltagechangeId}', 'PUT',
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
