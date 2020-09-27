# xepmts.MuvetoAfterpulse1tApi

All URIs are relative to *https://api-dot-xenon-pmts.uc.r.appspot.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_muveto_afterpulse1t_item**](MuvetoAfterpulse1tApi.md#delete_muveto_afterpulse1t_item) | **DELETE** /xenon1t/muveto/afterpules/{muvetoafterpulse1tId} | Deletes a MuvetoAfterpulse1t document
[**get_muveto_afterpulse1t_item**](MuvetoAfterpulse1tApi.md#get_muveto_afterpulse1t_item) | **GET** /xenon1t/muveto/afterpules/{muvetoafterpulse1tId} | Retrieves a MuvetoAfterpulse1t document
[**get_muveto_afterpulse1ts**](MuvetoAfterpulse1tApi.md#get_muveto_afterpulse1ts) | **GET** /xenon1t/muveto/afterpules | Retrieves one or more MuvetoAfterpulse1ts
[**patch_muveto_afterpulse1t_item**](MuvetoAfterpulse1tApi.md#patch_muveto_afterpulse1t_item) | **PATCH** /xenon1t/muveto/afterpules/{muvetoafterpulse1tId} | Updates a MuvetoAfterpulse1t document
[**post_muveto_afterpulse1ts**](MuvetoAfterpulse1tApi.md#post_muveto_afterpulse1ts) | **POST** /xenon1t/muveto/afterpules | Stores one or more MuvetoAfterpulse1ts.
[**put_muveto_afterpulse1t_item**](MuvetoAfterpulse1tApi.md#put_muveto_afterpulse1t_item) | **PUT** /xenon1t/muveto/afterpules/{muvetoafterpulse1tId} | Replaces a MuvetoAfterpulse1t document


# **delete_muveto_afterpulse1t_item**
> delete_muveto_afterpulse1t_item(muvetoafterpulse1t_id, if_match=if_match)

Deletes a MuvetoAfterpulse1t document

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
    api_instance = xepmts.MuvetoAfterpulse1tApi(api_client)
    muvetoafterpulse1t_id = 'muvetoafterpulse1t_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a MuvetoAfterpulse1t document
        api_instance.delete_muveto_afterpulse1t_item(muvetoafterpulse1t_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoAfterpulse1tApi->delete_muveto_afterpulse1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetoafterpulse1t_id** | **str**|  | 
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
**204** | MuvetoAfterpulse1t document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_afterpulse1t_item**
> MuvetoAfterpulse1t get_muveto_afterpulse1t_item(muvetoafterpulse1t_id)

Retrieves a MuvetoAfterpulse1t document

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
    api_instance = xepmts.MuvetoAfterpulse1tApi(api_client)
    muvetoafterpulse1t_id = 'muvetoafterpulse1t_id_example' # str | 

    try:
        # Retrieves a MuvetoAfterpulse1t document
        api_response = api_instance.get_muveto_afterpulse1t_item(muvetoafterpulse1t_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoAfterpulse1tApi->get_muveto_afterpulse1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetoafterpulse1t_id** | **str**|  | 

### Return type

[**MuvetoAfterpulse1t**](MuvetoAfterpulse1t.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoAfterpulse1t document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_afterpulse1ts**
> InlineResponse20050 get_muveto_afterpulse1ts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more MuvetoAfterpulse1ts

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
    api_instance = xepmts.MuvetoAfterpulse1tApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more MuvetoAfterpulse1ts
        api_response = api_instance.get_muveto_afterpulse1ts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoAfterpulse1tApi->get_muveto_afterpulse1ts: %s\n" % e)
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

[**InlineResponse20050**](InlineResponse20050.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of MuvetoAfterpulse1ts |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_muveto_afterpulse1t_item**
> patch_muveto_afterpulse1t_item(muvetoafterpulse1t_id, muveto_afterpulse1t, if_match=if_match)

Updates a MuvetoAfterpulse1t document

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
    api_instance = xepmts.MuvetoAfterpulse1tApi(api_client)
    muvetoafterpulse1t_id = 'muvetoafterpulse1t_id_example' # str | 
muveto_afterpulse1t = xepmts.MuvetoAfterpulse1t() # MuvetoAfterpulse1t | A MuvetoAfterpulse1t or list of MuvetoAfterpulse1t documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Updates a MuvetoAfterpulse1t document
        api_instance.patch_muveto_afterpulse1t_item(muvetoafterpulse1t_id, muveto_afterpulse1t, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoAfterpulse1tApi->patch_muveto_afterpulse1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetoafterpulse1t_id** | **str**|  | 
 **muveto_afterpulse1t** | [**MuvetoAfterpulse1t**](MuvetoAfterpulse1t.md)| A MuvetoAfterpulse1t or list of MuvetoAfterpulse1t documents | 
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
**200** | MuvetoAfterpulse1t document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_muveto_afterpulse1ts**
> post_muveto_afterpulse1ts(muveto_afterpulse1t)

Stores one or more MuvetoAfterpulse1ts.

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
    api_instance = xepmts.MuvetoAfterpulse1tApi(api_client)
    muveto_afterpulse1t = xepmts.MuvetoAfterpulse1t() # MuvetoAfterpulse1t | A MuvetoAfterpulse1t or list of MuvetoAfterpulse1t documents

    try:
        # Stores one or more MuvetoAfterpulse1ts.
        api_instance.post_muveto_afterpulse1ts(muveto_afterpulse1t)
    except ApiException as e:
        print("Exception when calling MuvetoAfterpulse1tApi->post_muveto_afterpulse1ts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muveto_afterpulse1t** | [**MuvetoAfterpulse1t**](MuvetoAfterpulse1t.md)| A MuvetoAfterpulse1t or list of MuvetoAfterpulse1t documents | 

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

# **put_muveto_afterpulse1t_item**
> put_muveto_afterpulse1t_item(muvetoafterpulse1t_id, muveto_afterpulse1t, if_match=if_match)

Replaces a MuvetoAfterpulse1t document

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
    api_instance = xepmts.MuvetoAfterpulse1tApi(api_client)
    muvetoafterpulse1t_id = 'muvetoafterpulse1t_id_example' # str | 
muveto_afterpulse1t = xepmts.MuvetoAfterpulse1t() # MuvetoAfterpulse1t | A MuvetoAfterpulse1t or list of MuvetoAfterpulse1t documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a MuvetoAfterpulse1t document
        api_instance.put_muveto_afterpulse1t_item(muvetoafterpulse1t_id, muveto_afterpulse1t, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoAfterpulse1tApi->put_muveto_afterpulse1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetoafterpulse1t_id** | **str**|  | 
 **muveto_afterpulse1t** | [**MuvetoAfterpulse1t**](MuvetoAfterpulse1t.md)| A MuvetoAfterpulse1t or list of MuvetoAfterpulse1t documents | 
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
**200** | MuvetoAfterpulse1t document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

