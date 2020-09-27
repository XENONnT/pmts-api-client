# xepmts.MuvetoInstall1tApi

All URIs are relative to *https://api-dot-xenon-pmts.uc.r.appspot.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_muveto_install1t_item**](MuvetoInstall1tApi.md#delete_muveto_install1t_item) | **DELETE** /xenon1t/muveto/installs/{muvetoinstall1tId} | Deletes a MuvetoInstall1t document
[**get_muveto_install1t_item**](MuvetoInstall1tApi.md#get_muveto_install1t_item) | **GET** /xenon1t/muveto/installs/{muvetoinstall1tId} | Retrieves a MuvetoInstall1t document
[**get_muveto_install1t_item_by_uid**](MuvetoInstall1tApi.md#get_muveto_install1t_item_by_uid) | **GET** /xenon1t/muveto/installs/{Uid} | Retrieves a MuvetoInstall1t document by uid
[**get_muveto_install1ts**](MuvetoInstall1tApi.md#get_muveto_install1ts) | **GET** /xenon1t/muveto/installs | Retrieves one or more MuvetoInstall1ts
[**patch_muveto_install1t_item**](MuvetoInstall1tApi.md#patch_muveto_install1t_item) | **PATCH** /xenon1t/muveto/installs/{muvetoinstall1tId} | Updates a MuvetoInstall1t document
[**post_muveto_install1ts**](MuvetoInstall1tApi.md#post_muveto_install1ts) | **POST** /xenon1t/muveto/installs | Stores one or more MuvetoInstall1ts.
[**put_muveto_install1t_item**](MuvetoInstall1tApi.md#put_muveto_install1t_item) | **PUT** /xenon1t/muveto/installs/{muvetoinstall1tId} | Replaces a MuvetoInstall1t document


# **delete_muveto_install1t_item**
> delete_muveto_install1t_item(muvetoinstall1t_id, if_match=if_match)

Deletes a MuvetoInstall1t document

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
    api_instance = xepmts.MuvetoInstall1tApi(api_client)
    muvetoinstall1t_id = 'muvetoinstall1t_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a MuvetoInstall1t document
        api_instance.delete_muveto_install1t_item(muvetoinstall1t_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoInstall1tApi->delete_muveto_install1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetoinstall1t_id** | **str**|  | 
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
**204** | MuvetoInstall1t document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_install1t_item**
> MuvetoInstall1t get_muveto_install1t_item(muvetoinstall1t_id)

Retrieves a MuvetoInstall1t document

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
    api_instance = xepmts.MuvetoInstall1tApi(api_client)
    muvetoinstall1t_id = 'muvetoinstall1t_id_example' # str | 

    try:
        # Retrieves a MuvetoInstall1t document
        api_response = api_instance.get_muveto_install1t_item(muvetoinstall1t_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoInstall1tApi->get_muveto_install1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetoinstall1t_id** | **str**|  | 

### Return type

[**MuvetoInstall1t**](MuvetoInstall1t.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoInstall1t document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_install1t_item_by_uid**
> MuvetoInstall1t get_muveto_install1t_item_by_uid(uid)

Retrieves a MuvetoInstall1t document by uid

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
    api_instance = xepmts.MuvetoInstall1tApi(api_client)
    uid = 'uid_example' # str | 

    try:
        # Retrieves a MuvetoInstall1t document by uid
        api_response = api_instance.get_muveto_install1t_item_by_uid(uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoInstall1tApi->get_muveto_install1t_item_by_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**MuvetoInstall1t**](MuvetoInstall1t.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoInstall1t document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_install1ts**
> InlineResponse20056 get_muveto_install1ts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more MuvetoInstall1ts

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
    api_instance = xepmts.MuvetoInstall1tApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more MuvetoInstall1ts
        api_response = api_instance.get_muveto_install1ts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoInstall1tApi->get_muveto_install1ts: %s\n" % e)
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

[**InlineResponse20056**](InlineResponse20056.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of MuvetoInstall1ts |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_muveto_install1t_item**
> patch_muveto_install1t_item(muvetoinstall1t_id, muveto_install1t, if_match=if_match)

Updates a MuvetoInstall1t document

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
    api_instance = xepmts.MuvetoInstall1tApi(api_client)
    muvetoinstall1t_id = 'muvetoinstall1t_id_example' # str | 
muveto_install1t = xepmts.MuvetoInstall1t() # MuvetoInstall1t | A MuvetoInstall1t or list of MuvetoInstall1t documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Updates a MuvetoInstall1t document
        api_instance.patch_muveto_install1t_item(muvetoinstall1t_id, muveto_install1t, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoInstall1tApi->patch_muveto_install1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetoinstall1t_id** | **str**|  | 
 **muveto_install1t** | [**MuvetoInstall1t**](MuvetoInstall1t.md)| A MuvetoInstall1t or list of MuvetoInstall1t documents | 
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
**200** | MuvetoInstall1t document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_muveto_install1ts**
> post_muveto_install1ts(muveto_install1t)

Stores one or more MuvetoInstall1ts.

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
    api_instance = xepmts.MuvetoInstall1tApi(api_client)
    muveto_install1t = xepmts.MuvetoInstall1t() # MuvetoInstall1t | A MuvetoInstall1t or list of MuvetoInstall1t documents

    try:
        # Stores one or more MuvetoInstall1ts.
        api_instance.post_muveto_install1ts(muveto_install1t)
    except ApiException as e:
        print("Exception when calling MuvetoInstall1tApi->post_muveto_install1ts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muveto_install1t** | [**MuvetoInstall1t**](MuvetoInstall1t.md)| A MuvetoInstall1t or list of MuvetoInstall1t documents | 

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

# **put_muveto_install1t_item**
> put_muveto_install1t_item(muvetoinstall1t_id, muveto_install1t, if_match=if_match)

Replaces a MuvetoInstall1t document

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
    api_instance = xepmts.MuvetoInstall1tApi(api_client)
    muvetoinstall1t_id = 'muvetoinstall1t_id_example' # str | 
muveto_install1t = xepmts.MuvetoInstall1t() # MuvetoInstall1t | A MuvetoInstall1t or list of MuvetoInstall1t documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a MuvetoInstall1t document
        api_instance.put_muveto_install1t_item(muvetoinstall1t_id, muveto_install1t, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoInstall1tApi->put_muveto_install1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetoinstall1t_id** | **str**|  | 
 **muveto_install1t** | [**MuvetoInstall1t**](MuvetoInstall1t.md)| A MuvetoInstall1t or list of MuvetoInstall1t documents | 
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
**200** | MuvetoInstall1t document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

