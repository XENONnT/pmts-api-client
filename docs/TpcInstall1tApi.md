# xepmts.TpcInstall1tApi

All URIs are relative to *https://api-dot-xenon-pmts.uc.r.appspot.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tpc_install1t_item**](TpcInstall1tApi.md#delete_tpc_install1t_item) | **DELETE** /xenon1t/tpc/installs/{tpcinstall1tId} | Deletes a TpcInstall1t document
[**get_tpc_install1t_item**](TpcInstall1tApi.md#get_tpc_install1t_item) | **GET** /xenon1t/tpc/installs/{tpcinstall1tId} | Retrieves a TpcInstall1t document
[**get_tpc_install1t_item_by_uid**](TpcInstall1tApi.md#get_tpc_install1t_item_by_uid) | **GET** /xenon1t/tpc/installs/{Uid} | Retrieves a TpcInstall1t document by uid
[**get_tpc_install1ts**](TpcInstall1tApi.md#get_tpc_install1ts) | **GET** /xenon1t/tpc/installs | Retrieves one or more TpcInstall1ts
[**patch_tpc_install1t_item**](TpcInstall1tApi.md#patch_tpc_install1t_item) | **PATCH** /xenon1t/tpc/installs/{tpcinstall1tId} | Updates a TpcInstall1t document
[**post_tpc_install1ts**](TpcInstall1tApi.md#post_tpc_install1ts) | **POST** /xenon1t/tpc/installs | Stores one or more TpcInstall1ts.
[**put_tpc_install1t_item**](TpcInstall1tApi.md#put_tpc_install1t_item) | **PUT** /xenon1t/tpc/installs/{tpcinstall1tId} | Replaces a TpcInstall1t document


# **delete_tpc_install1t_item**
> delete_tpc_install1t_item(tpcinstall1t_id, if_match=if_match)

Deletes a TpcInstall1t document

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
    api_instance = xepmts.TpcInstall1tApi(api_client)
    tpcinstall1t_id = 'tpcinstall1t_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a TpcInstall1t document
        api_instance.delete_tpc_install1t_item(tpcinstall1t_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcInstall1tApi->delete_tpc_install1t_item: %s\n" % e)
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
**204** | TpcInstall1t document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_install1t_item**
> TpcInstall1t get_tpc_install1t_item(tpcinstall1t_id)

Retrieves a TpcInstall1t document

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
    api_instance = xepmts.TpcInstall1tApi(api_client)
    tpcinstall1t_id = 'tpcinstall1t_id_example' # str | 

    try:
        # Retrieves a TpcInstall1t document
        api_response = api_instance.get_tpc_install1t_item(tpcinstall1t_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcInstall1tApi->get_tpc_install1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcinstall1t_id** | **str**|  | 

### Return type

[**TpcInstall1t**](TpcInstall1t.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcInstall1t document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_install1t_item_by_uid**
> TpcInstall1t get_tpc_install1t_item_by_uid(uid)

Retrieves a TpcInstall1t document by uid

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
    api_instance = xepmts.TpcInstall1tApi(api_client)
    uid = 'uid_example' # str | 

    try:
        # Retrieves a TpcInstall1t document by uid
        api_response = api_instance.get_tpc_install1t_item_by_uid(uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcInstall1tApi->get_tpc_install1t_item_by_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**TpcInstall1t**](TpcInstall1t.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcInstall1t document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_install1ts**
> InlineResponse20044 get_tpc_install1ts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more TpcInstall1ts

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
    api_instance = xepmts.TpcInstall1tApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more TpcInstall1ts
        api_response = api_instance.get_tpc_install1ts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcInstall1tApi->get_tpc_install1ts: %s\n" % e)
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

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of TpcInstall1ts |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_tpc_install1t_item**
> patch_tpc_install1t_item(tpcinstall1t_id, tpc_install1t, if_match=if_match)

Updates a TpcInstall1t document

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
    api_instance = xepmts.TpcInstall1tApi(api_client)
    tpcinstall1t_id = 'tpcinstall1t_id_example' # str | 
tpc_install1t = xepmts.TpcInstall1t() # TpcInstall1t | A TpcInstall1t or list of TpcInstall1t documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Updates a TpcInstall1t document
        api_instance.patch_tpc_install1t_item(tpcinstall1t_id, tpc_install1t, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcInstall1tApi->patch_tpc_install1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcinstall1t_id** | **str**|  | 
 **tpc_install1t** | [**TpcInstall1t**](TpcInstall1t.md)| A TpcInstall1t or list of TpcInstall1t documents | 
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
**200** | TpcInstall1t document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tpc_install1ts**
> post_tpc_install1ts(tpc_install1t)

Stores one or more TpcInstall1ts.

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
    api_instance = xepmts.TpcInstall1tApi(api_client)
    tpc_install1t = xepmts.TpcInstall1t() # TpcInstall1t | A TpcInstall1t or list of TpcInstall1t documents

    try:
        # Stores one or more TpcInstall1ts.
        api_instance.post_tpc_install1ts(tpc_install1t)
    except ApiException as e:
        print("Exception when calling TpcInstall1tApi->post_tpc_install1ts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpc_install1t** | [**TpcInstall1t**](TpcInstall1t.md)| A TpcInstall1t or list of TpcInstall1t documents | 

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

# **put_tpc_install1t_item**
> put_tpc_install1t_item(tpcinstall1t_id, tpc_install1t, if_match=if_match)

Replaces a TpcInstall1t document

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
    api_instance = xepmts.TpcInstall1tApi(api_client)
    tpcinstall1t_id = 'tpcinstall1t_id_example' # str | 
tpc_install1t = xepmts.TpcInstall1t() # TpcInstall1t | A TpcInstall1t or list of TpcInstall1t documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a TpcInstall1t document
        api_instance.put_tpc_install1t_item(tpcinstall1t_id, tpc_install1t, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcInstall1tApi->put_tpc_install1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcinstall1t_id** | **str**|  | 
 **tpc_install1t** | [**TpcInstall1t**](TpcInstall1t.md)| A TpcInstall1t or list of TpcInstall1t documents | 
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
**200** | TpcInstall1t document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

