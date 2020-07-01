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


class TpcInstallApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_tpc_install_item(self, tpcinstall_id, **kwargs):  # noqa: E501
        """Deletes a TpcInstall document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_tpc_install_item(tpcinstall_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str tpcinstall_id: (required)
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
        return self.delete_tpc_install_item_with_http_info(tpcinstall_id, **kwargs)  # noqa: E501

    def delete_tpc_install_item_with_http_info(self, tpcinstall_id, **kwargs):  # noqa: E501
        """Deletes a TpcInstall document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_tpc_install_item_with_http_info(tpcinstall_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str tpcinstall_id: (required)
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
            'tpcinstall_id',
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
                    " to method delete_tpc_install_item" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tpcinstall_id' is set
        if self.api_client.client_side_validation and ('tpcinstall_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['tpcinstall_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `tpcinstall_id` when calling `delete_tpc_install_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tpcinstall_id' in local_var_params:
            path_params['tpcinstallId'] = local_var_params['tpcinstall_id']  # noqa: E501

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
            '/tpc/installs/{tpcinstallId}', 'DELETE',
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

    def get_tpc_install_item(self, tpcinstall_id, **kwargs):  # noqa: E501
        """Retrieves a TpcInstall document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tpc_install_item(tpcinstall_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str tpcinstall_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TpcInstall
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_tpc_install_item_with_http_info(tpcinstall_id, **kwargs)  # noqa: E501

    def get_tpc_install_item_with_http_info(self, tpcinstall_id, **kwargs):  # noqa: E501
        """Retrieves a TpcInstall document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tpc_install_item_with_http_info(tpcinstall_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str tpcinstall_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TpcInstall, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'tpcinstall_id'
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
                    " to method get_tpc_install_item" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tpcinstall_id' is set
        if self.api_client.client_side_validation and ('tpcinstall_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['tpcinstall_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `tpcinstall_id` when calling `get_tpc_install_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tpcinstall_id' in local_var_params:
            path_params['tpcinstallId'] = local_var_params['tpcinstall_id']  # noqa: E501

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
            '/tpc/installs/{tpcinstallId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TpcInstall',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tpc_install_item_by_uid(self, uid, **kwargs):  # noqa: E501
        """Retrieves a TpcInstall document by uid  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tpc_install_item_by_uid(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str uid: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: TpcInstall
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_tpc_install_item_by_uid_with_http_info(uid, **kwargs)  # noqa: E501

    def get_tpc_install_item_by_uid_with_http_info(self, uid, **kwargs):  # noqa: E501
        """Retrieves a TpcInstall document by uid  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tpc_install_item_by_uid_with_http_info(uid, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str uid: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(TpcInstall, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'uid'
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
                    " to method get_tpc_install_item_by_uid" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'uid' is set
        if self.api_client.client_side_validation and ('uid' not in local_var_params or  # noqa: E501
                                                        local_var_params['uid'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `uid` when calling `get_tpc_install_item_by_uid`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uid' in local_var_params:
            path_params['Uid'] = local_var_params['uid']  # noqa: E501

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
            '/tpc/installs/{Uid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TpcInstall',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_tpc_installs(self, **kwargs):  # noqa: E501
        """Retrieves one or more TpcInstalls  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tpc_installs(async_req=True)
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
        :return: InlineResponse2009
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_tpc_installs_with_http_info(**kwargs)  # noqa: E501

    def get_tpc_installs_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves one or more TpcInstalls  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tpc_installs_with_http_info(async_req=True)
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
        :return: tuple(InlineResponse2009, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_tpc_installs" % key
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
            '/tpc/installs', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2009',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_tpc_installs(self, tpc_install, **kwargs):  # noqa: E501
        """Stores one or more TpcInstalls.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_tpc_installs(tpc_install, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param TpcInstall tpc_install: A TpcInstall or list of TpcInstall documents (required)
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
        return self.post_tpc_installs_with_http_info(tpc_install, **kwargs)  # noqa: E501

    def post_tpc_installs_with_http_info(self, tpc_install, **kwargs):  # noqa: E501
        """Stores one or more TpcInstalls.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_tpc_installs_with_http_info(tpc_install, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param TpcInstall tpc_install: A TpcInstall or list of TpcInstall documents (required)
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
            'tpc_install'
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
                    " to method post_tpc_installs" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tpc_install' is set
        if self.api_client.client_side_validation and ('tpc_install' not in local_var_params or  # noqa: E501
                                                        local_var_params['tpc_install'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `tpc_install` when calling `post_tpc_installs`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tpc_install' in local_var_params:
            body_params = local_var_params['tpc_install']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tpc/installs', 'POST',
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

    def put_tpc_install_item(self, tpcinstall_id, tpc_install, **kwargs):  # noqa: E501
        """Replaces a TpcInstall document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_tpc_install_item(tpcinstall_id, tpc_install, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str tpcinstall_id: (required)
        :param TpcInstall tpc_install: A TpcInstall or list of TpcInstall documents (required)
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
        return self.put_tpc_install_item_with_http_info(tpcinstall_id, tpc_install, **kwargs)  # noqa: E501

    def put_tpc_install_item_with_http_info(self, tpcinstall_id, tpc_install, **kwargs):  # noqa: E501
        """Replaces a TpcInstall document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.put_tpc_install_item_with_http_info(tpcinstall_id, tpc_install, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str tpcinstall_id: (required)
        :param TpcInstall tpc_install: A TpcInstall or list of TpcInstall documents (required)
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
            'tpcinstall_id',
            'tpc_install',
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
                    " to method put_tpc_install_item" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'tpcinstall_id' is set
        if self.api_client.client_side_validation and ('tpcinstall_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['tpcinstall_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `tpcinstall_id` when calling `put_tpc_install_item`")  # noqa: E501
        # verify the required parameter 'tpc_install' is set
        if self.api_client.client_side_validation and ('tpc_install' not in local_var_params or  # noqa: E501
                                                        local_var_params['tpc_install'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `tpc_install` when calling `put_tpc_install_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'tpcinstall_id' in local_var_params:
            path_params['tpcinstallId'] = local_var_params['tpcinstall_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_match' in local_var_params:
            header_params['If-Match'] = local_var_params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tpc_install' in local_var_params:
            body_params = local_var_params['tpc_install']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BearerAuth']  # noqa: E501

        return self.api_client.call_api(
            '/tpc/installs/{tpcinstallId}', 'PUT',
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
