# xepmts.MuvetoGain1tApi

All URIs are relative to *https://xenon-pmts.uc.r.appspot.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_muveto_gain1t_item**](MuvetoGain1tApi.md#delete_muveto_gain1t_item) | **DELETE** /xenon1t/muveto/gains/{muvetogain1tId} | Deletes a MuvetoGain1t document
[**get_muveto_gain1t_item**](MuvetoGain1tApi.md#get_muveto_gain1t_item) | **GET** /xenon1t/muveto/gains/{muvetogain1tId} | Retrieves a MuvetoGain1t document
[**get_muveto_gain1ts**](MuvetoGain1tApi.md#get_muveto_gain1ts) | **GET** /xenon1t/muveto/gains | Retrieves one or more MuvetoGain1ts
[**patch_muveto_gain1t_item**](MuvetoGain1tApi.md#patch_muveto_gain1t_item) | **PATCH** /xenon1t/muveto/gains/{muvetogain1tId} | Updates a MuvetoGain1t document
[**post_muveto_gain1ts**](MuvetoGain1tApi.md#post_muveto_gain1ts) | **POST** /xenon1t/muveto/gains | Stores one or more MuvetoGain1ts.
[**put_muveto_gain1t_item**](MuvetoGain1tApi.md#put_muveto_gain1t_item) | **PUT** /xenon1t/muveto/gains/{muvetogain1tId} | Replaces a MuvetoGain1t document


# **delete_muveto_gain1t_item**
> delete_muveto_gain1t_item(muvetogain1t_id, if_match=if_match)

Deletes a MuvetoGain1t document

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

# Defining host is optional and default to https://xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.MuvetoGain1tApi(api_client)
    muvetogain1t_id = 'muvetogain1t_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a MuvetoGain1t document
        api_instance.delete_muveto_gain1t_item(muvetogain1t_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoGain1tApi->delete_muveto_gain1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetogain1t_id** | **str**|  | 
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
**204** | MuvetoGain1t document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_gain1t_item**
> MuvetoGain1t get_muveto_gain1t_item(muvetogain1t_id)

Retrieves a MuvetoGain1t document

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

# Defining host is optional and default to https://xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.MuvetoGain1tApi(api_client)
    muvetogain1t_id = 'muvetogain1t_id_example' # str | 

    try:
        # Retrieves a MuvetoGain1t document
        api_response = api_instance.get_muveto_gain1t_item(muvetogain1t_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoGain1tApi->get_muveto_gain1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetogain1t_id** | **str**|  | 

### Return type

[**MuvetoGain1t**](MuvetoGain1t.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoGain1t document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_gain1ts**
> InlineResponse20051 get_muveto_gain1ts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more MuvetoGain1ts

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

# Defining host is optional and default to https://xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.MuvetoGain1tApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more MuvetoGain1ts
        api_response = api_instance.get_muveto_gain1ts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoGain1tApi->get_muveto_gain1ts: %s\n" % e)
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

[**InlineResponse20051**](InlineResponse20051.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of MuvetoGain1ts |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_muveto_gain1t_item**
> patch_muveto_gain1t_item(muvetogain1t_id, muveto_gain1t, if_match=if_match)

Updates a MuvetoGain1t document

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

# Defining host is optional and default to https://xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.MuvetoGain1tApi(api_client)
    muvetogain1t_id = 'muvetogain1t_id_example' # str | 
muveto_gain1t = xepmts.MuvetoGain1t() # MuvetoGain1t | A MuvetoGain1t or list of MuvetoGain1t documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Updates a MuvetoGain1t document
        api_instance.patch_muveto_gain1t_item(muvetogain1t_id, muveto_gain1t, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoGain1tApi->patch_muveto_gain1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetogain1t_id** | **str**|  | 
 **muveto_gain1t** | [**MuvetoGain1t**](MuvetoGain1t.md)| A MuvetoGain1t or list of MuvetoGain1t documents | 
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
**200** | MuvetoGain1t document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_muveto_gain1ts**
> post_muveto_gain1ts(muveto_gain1t)

Stores one or more MuvetoGain1ts.

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

# Defining host is optional and default to https://xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.MuvetoGain1tApi(api_client)
    muveto_gain1t = xepmts.MuvetoGain1t() # MuvetoGain1t | A MuvetoGain1t or list of MuvetoGain1t documents

    try:
        # Stores one or more MuvetoGain1ts.
        api_instance.post_muveto_gain1ts(muveto_gain1t)
    except ApiException as e:
        print("Exception when calling MuvetoGain1tApi->post_muveto_gain1ts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muveto_gain1t** | [**MuvetoGain1t**](MuvetoGain1t.md)| A MuvetoGain1t or list of MuvetoGain1t documents | 

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

# **put_muveto_gain1t_item**
> put_muveto_gain1t_item(muvetogain1t_id, muveto_gain1t, if_match=if_match)

Replaces a MuvetoGain1t document

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

# Defining host is optional and default to https://xenon-pmts.uc.r.appspot.com/v1
configuration.host = "https://xenon-pmts.uc.r.appspot.com/v1"

# Enter a context with an instance of the API client
with xepmts.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = xepmts.MuvetoGain1tApi(api_client)
    muvetogain1t_id = 'muvetogain1t_id_example' # str | 
muveto_gain1t = xepmts.MuvetoGain1t() # MuvetoGain1t | A MuvetoGain1t or list of MuvetoGain1t documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a MuvetoGain1t document
        api_instance.put_muveto_gain1t_item(muvetogain1t_id, muveto_gain1t, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoGain1tApi->put_muveto_gain1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetogain1t_id** | **str**|  | 
 **muveto_gain1t** | [**MuvetoGain1t**](MuvetoGain1t.md)| A MuvetoGain1t or list of MuvetoGain1t documents | 
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
**200** | MuvetoGain1t document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

