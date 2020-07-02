# xepmts.TpcInstall1TApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tpc_install1_t_item**](TpcInstall1TApi.md#delete_tpc_install1_t_item) | **DELETE** /xenon1t/tpc/installs/{tpcinstall1tId} | Deletes a TpcInstall1T document
[**get_tpc_install1_t_item**](TpcInstall1TApi.md#get_tpc_install1_t_item) | **GET** /xenon1t/tpc/installs/{tpcinstall1tId} | Retrieves a TpcInstall1T document
[**get_tpc_install1_t_item_by_uid**](TpcInstall1TApi.md#get_tpc_install1_t_item_by_uid) | **GET** /xenon1t/tpc/installs/{Uid} | Retrieves a TpcInstall1T document by uid
[**get_tpc_installs1_t**](TpcInstall1TApi.md#get_tpc_installs1_t) | **GET** /xenon1t/tpc/installs | Retrieves one or more TpcInstalls1T
[**post_tpc_installs1_t**](TpcInstall1TApi.md#post_tpc_installs1_t) | **POST** /xenon1t/tpc/installs | Stores one or more TpcInstalls1T.
[**put_tpc_install1_t_item**](TpcInstall1TApi.md#put_tpc_install1_t_item) | **PUT** /xenon1t/tpc/installs/{tpcinstall1tId} | Replaces a TpcInstall1T document


# **delete_tpc_install1_t_item**
> delete_tpc_install1_t_item(tpcinstall1t_id, if_match=if_match)

Deletes a TpcInstall1T document

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

# Defining host is optional and default to https://api.pmts.xenonnt.org/v1
configuration.host = "https://api.pmts.xenonnt.org/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcInstall1TApi(api_client)
    tpcinstall1t_id = 'tpcinstall1t_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a TpcInstall1T document
        api_instance.delete_tpc_install1_t_item(tpcinstall1t_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcInstall1TApi->delete_tpc_install1_t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcinstall1t_id** | **str**|  | 
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
**204** | TpcInstall1T document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_install1_t_item**
> TpcInstall1T get_tpc_install1_t_item(tpcinstall1t_id)

Retrieves a TpcInstall1T document

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

# Defining host is optional and default to https://api.pmts.xenonnt.org/v1
configuration.host = "https://api.pmts.xenonnt.org/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcInstall1TApi(api_client)
    tpcinstall1t_id = 'tpcinstall1t_id_example' # str | 

    try:
        # Retrieves a TpcInstall1T document
        api_response = api_instance.get_tpc_install1_t_item(tpcinstall1t_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcInstall1TApi->get_tpc_install1_t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcinstall1t_id** | **str**|  | 

### Return type

[**TpcInstall1T**](TpcInstall1T.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcInstall1T document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_install1_t_item_by_uid**
> TpcInstall1T get_tpc_install1_t_item_by_uid(uid)

Retrieves a TpcInstall1T document by uid

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

# Defining host is optional and default to https://api.pmts.xenonnt.org/v1
configuration.host = "https://api.pmts.xenonnt.org/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcInstall1TApi(api_client)
    uid = 'uid_example' # str | 

    try:
        # Retrieves a TpcInstall1T document by uid
        api_response = api_instance.get_tpc_install1_t_item_by_uid(uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcInstall1TApi->get_tpc_install1_t_item_by_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**TpcInstall1T**](TpcInstall1T.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcInstall1T document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_installs1_t**
> InlineResponse20046 get_tpc_installs1_t(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more TpcInstalls1T

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

# Defining host is optional and default to https://api.pmts.xenonnt.org/v1
configuration.host = "https://api.pmts.xenonnt.org/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcInstall1TApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more TpcInstalls1T
        api_response = api_instance.get_tpc_installs1_t(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcInstall1TApi->get_tpc_installs1_t: %s\n" % e)
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

[**InlineResponse20046**](InlineResponse20046.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of TpcInstalls1T |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tpc_installs1_t**
> post_tpc_installs1_t(tpc_install1_t)

Stores one or more TpcInstalls1T.

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

# Defining host is optional and default to https://api.pmts.xenonnt.org/v1
configuration.host = "https://api.pmts.xenonnt.org/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcInstall1TApi(api_client)
    tpc_install1_t = xepmts.TpcInstall1T() # TpcInstall1T | A TpcInstall1T or list of TpcInstall1T documents

    try:
        # Stores one or more TpcInstalls1T.
        api_instance.post_tpc_installs1_t(tpc_install1_t)
    except ApiException as e:
        print("Exception when calling TpcInstall1TApi->post_tpc_installs1_t: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpc_install1_t** | [**TpcInstall1T**](TpcInstall1T.md)| A TpcInstall1T or list of TpcInstall1T documents | 

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

# **put_tpc_install1_t_item**
> put_tpc_install1_t_item(tpcinstall1t_id, tpc_install1_t, if_match=if_match)

Replaces a TpcInstall1T document

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

# Defining host is optional and default to https://api.pmts.xenonnt.org/v1
configuration.host = "https://api.pmts.xenonnt.org/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.TpcInstall1TApi(api_client)
    tpcinstall1t_id = 'tpcinstall1t_id_example' # str | 
tpc_install1_t = xepmts.TpcInstall1T() # TpcInstall1T | A TpcInstall1T or list of TpcInstall1T documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a TpcInstall1T document
        api_instance.put_tpc_install1_t_item(tpcinstall1t_id, tpc_install1_t, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcInstall1TApi->put_tpc_install1_t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcinstall1t_id** | **str**|  | 
 **tpc_install1_t** | [**TpcInstall1T**](TpcInstall1T.md)| A TpcInstall1T or list of TpcInstall1T documents | 
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
**200** | TpcInstall1T document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

