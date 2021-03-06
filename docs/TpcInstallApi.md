# xepmts.TpcInstallApi

All URIs are relative to *https://api-dot-xenon-pmts.uc.r.appspot.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tpc_install_item**](TpcInstallApi.md#delete_tpc_install_item) | **DELETE** /tpc/installs/{tpcinstallId} | Deletes a TpcInstall document
[**get_tpc_install_item**](TpcInstallApi.md#get_tpc_install_item) | **GET** /tpc/installs/{tpcinstallId} | Retrieves a TpcInstall document
[**get_tpc_install_item_by_uid**](TpcInstallApi.md#get_tpc_install_item_by_uid) | **GET** /tpc/installs/{Uid} | Retrieves a TpcInstall document by uid
[**get_tpc_installs**](TpcInstallApi.md#get_tpc_installs) | **GET** /tpc/installs | Retrieves one or more TpcInstalls
[**patch_tpc_install_item**](TpcInstallApi.md#patch_tpc_install_item) | **PATCH** /tpc/installs/{tpcinstallId} | Updates a TpcInstall document
[**post_tpc_installs**](TpcInstallApi.md#post_tpc_installs) | **POST** /tpc/installs | Stores one or more TpcInstalls.
[**put_tpc_install_item**](TpcInstallApi.md#put_tpc_install_item) | **PUT** /tpc/installs/{tpcinstallId} | Replaces a TpcInstall document


# **delete_tpc_install_item**
> delete_tpc_install_item(tpcinstall_id, if_match=if_match)

Deletes a TpcInstall document

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
configuration = xepmts.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api-dot-xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://api-dot-xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcInstallApi(api_client)
    tpcinstall_id = 'tpcinstall_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a TpcInstall document
        api_instance.delete_tpc_install_item(tpcinstall_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcInstallApi->delete_tpc_install_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcinstall_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | TpcInstall document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_install_item**
> TpcInstall get_tpc_install_item(tpcinstall_id)

Retrieves a TpcInstall document

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
configuration = xepmts.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api-dot-xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://api-dot-xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcInstallApi(api_client)
    tpcinstall_id = 'tpcinstall_id_example' # str | 

    try:
        # Retrieves a TpcInstall document
        api_response = api_instance.get_tpc_install_item(tpcinstall_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcInstallApi->get_tpc_install_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcinstall_id** | **str**|  | 

### Return type

[**TpcInstall**](TpcInstall.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcInstall document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_install_item_by_uid**
> TpcInstall get_tpc_install_item_by_uid(uid)

Retrieves a TpcInstall document by uid

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
configuration = xepmts.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api-dot-xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://api-dot-xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcInstallApi(api_client)
    uid = 'uid_example' # str | 

    try:
        # Retrieves a TpcInstall document by uid
        api_response = api_instance.get_tpc_install_item_by_uid(uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcInstallApi->get_tpc_install_item_by_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**TpcInstall**](TpcInstall.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcInstall document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_installs**
> InlineResponse2008 get_tpc_installs(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more TpcInstalls

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
configuration = xepmts.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api-dot-xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://api-dot-xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcInstallApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more TpcInstalls
        api_response = api_instance.get_tpc_installs(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcInstallApi->get_tpc_installs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **projection** | **str**| the projections query parameter (ex.: {\&quot;name\&quot;: 1}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of TpcInstalls |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_tpc_install_item**
> patch_tpc_install_item(tpcinstall_id, tpc_install, if_match=if_match)

Updates a TpcInstall document

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
configuration = xepmts.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api-dot-xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://api-dot-xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcInstallApi(api_client)
    tpcinstall_id = 'tpcinstall_id_example' # str | 
tpc_install = xepmts.TpcInstall() # TpcInstall | A TpcInstall or list of TpcInstall documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Updates a TpcInstall document
        api_instance.patch_tpc_install_item(tpcinstall_id, tpc_install, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcInstallApi->patch_tpc_install_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcinstall_id** | **str**|  | 
 **tpc_install** | [**TpcInstall**](TpcInstall.md)| A TpcInstall or list of TpcInstall documents | 
 **if_match** | **str**| Current value of the _etag field | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcInstall document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tpc_installs**
> post_tpc_installs(tpc_install)

Stores one or more TpcInstalls.

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
configuration = xepmts.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api-dot-xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://api-dot-xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcInstallApi(api_client)
    tpc_install = xepmts.TpcInstall() # TpcInstall | A TpcInstall or list of TpcInstall documents

    try:
        # Stores one or more TpcInstalls.
        api_instance.post_tpc_installs(tpc_install)
    except ApiException as e:
        print("Exception when calling TpcInstallApi->post_tpc_installs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpc_install** | [**TpcInstall**](TpcInstall.md)| A TpcInstall or list of TpcInstall documents | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | operation has been successful |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_tpc_install_item**
> put_tpc_install_item(tpcinstall_id, tpc_install, if_match=if_match)

Replaces a TpcInstall document

### Example

* Bearer Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
configuration = xepmts.Configuration()
# Configure Bearer authorization: BearerAuth
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to https://api-dot-xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://api-dot-xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcInstallApi(api_client)
    tpcinstall_id = 'tpcinstall_id_example' # str | 
tpc_install = xepmts.TpcInstall() # TpcInstall | A TpcInstall or list of TpcInstall documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a TpcInstall document
        api_instance.put_tpc_install_item(tpcinstall_id, tpc_install, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcInstallApi->put_tpc_install_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcinstall_id** | **str**|  | 
 **tpc_install** | [**TpcInstall**](TpcInstall.md)| A TpcInstall or list of TpcInstall documents | 
 **if_match** | **str**| Current value of the _etag field | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcInstall document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

