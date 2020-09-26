# xepmts.MuvetoPmtError1tApi

All URIs are relative to *https://xenon-pmts.uc.r.appspot.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_muveto_pmt_error1t_item**](MuvetoPmtError1tApi.md#delete_muveto_pmt_error1t_item) | **DELETE** /xenon1t/muveto/pmt_errors/{muvetopmterror1tId} | Deletes a MuvetoPmtError1t document
[**get_muveto_pmt_error1t_item**](MuvetoPmtError1tApi.md#get_muveto_pmt_error1t_item) | **GET** /xenon1t/muveto/pmt_errors/{muvetopmterror1tId} | Retrieves a MuvetoPmtError1t document
[**get_muveto_pmt_error1ts**](MuvetoPmtError1tApi.md#get_muveto_pmt_error1ts) | **GET** /xenon1t/muveto/pmt_errors | Retrieves one or more MuvetoPmtError1ts
[**patch_muveto_pmt_error1t_item**](MuvetoPmtError1tApi.md#patch_muveto_pmt_error1t_item) | **PATCH** /xenon1t/muveto/pmt_errors/{muvetopmterror1tId} | Updates a MuvetoPmtError1t document
[**post_muveto_pmt_error1ts**](MuvetoPmtError1tApi.md#post_muveto_pmt_error1ts) | **POST** /xenon1t/muveto/pmt_errors | Stores one or more MuvetoPmtError1ts.
[**put_muveto_pmt_error1t_item**](MuvetoPmtError1tApi.md#put_muveto_pmt_error1t_item) | **PUT** /xenon1t/muveto/pmt_errors/{muvetopmterror1tId} | Replaces a MuvetoPmtError1t document


# **delete_muveto_pmt_error1t_item**
> delete_muveto_pmt_error1t_item(muvetopmterror1t_id, if_match=if_match)

Deletes a MuvetoPmtError1t document

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
    api_instance = xepmts.MuvetoPmtError1tApi(api_client)
    muvetopmterror1t_id = 'muvetopmterror1t_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a MuvetoPmtError1t document
        api_instance.delete_muveto_pmt_error1t_item(muvetopmterror1t_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoPmtError1tApi->delete_muveto_pmt_error1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetopmterror1t_id** | **str**|  | 
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
**204** | MuvetoPmtError1t document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_pmt_error1t_item**
> MuvetoPmtError1t get_muveto_pmt_error1t_item(muvetopmterror1t_id)

Retrieves a MuvetoPmtError1t document

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
    api_instance = xepmts.MuvetoPmtError1tApi(api_client)
    muvetopmterror1t_id = 'muvetopmterror1t_id_example' # str | 

    try:
        # Retrieves a MuvetoPmtError1t document
        api_response = api_instance.get_muveto_pmt_error1t_item(muvetopmterror1t_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoPmtError1tApi->get_muveto_pmt_error1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetopmterror1t_id** | **str**|  | 

### Return type

[**MuvetoPmtError1t**](MuvetoPmtError1t.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoPmtError1t document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_pmt_error1ts**
> InlineResponse20053 get_muveto_pmt_error1ts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more MuvetoPmtError1ts

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
    api_instance = xepmts.MuvetoPmtError1tApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more MuvetoPmtError1ts
        api_response = api_instance.get_muveto_pmt_error1ts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoPmtError1tApi->get_muveto_pmt_error1ts: %s\n" % e)
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

[**InlineResponse20053**](InlineResponse20053.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of MuvetoPmtError1ts |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_muveto_pmt_error1t_item**
> patch_muveto_pmt_error1t_item(muvetopmterror1t_id, muveto_pmt_error1t, if_match=if_match)

Updates a MuvetoPmtError1t document

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
    api_instance = xepmts.MuvetoPmtError1tApi(api_client)
    muvetopmterror1t_id = 'muvetopmterror1t_id_example' # str | 
muveto_pmt_error1t = xepmts.MuvetoPmtError1t() # MuvetoPmtError1t | A MuvetoPmtError1t or list of MuvetoPmtError1t documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Updates a MuvetoPmtError1t document
        api_instance.patch_muveto_pmt_error1t_item(muvetopmterror1t_id, muveto_pmt_error1t, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoPmtError1tApi->patch_muveto_pmt_error1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetopmterror1t_id** | **str**|  | 
 **muveto_pmt_error1t** | [**MuvetoPmtError1t**](MuvetoPmtError1t.md)| A MuvetoPmtError1t or list of MuvetoPmtError1t documents | 
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
**200** | MuvetoPmtError1t document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_muveto_pmt_error1ts**
> post_muveto_pmt_error1ts(muveto_pmt_error1t)

Stores one or more MuvetoPmtError1ts.

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
    api_instance = xepmts.MuvetoPmtError1tApi(api_client)
    muveto_pmt_error1t = xepmts.MuvetoPmtError1t() # MuvetoPmtError1t | A MuvetoPmtError1t or list of MuvetoPmtError1t documents

    try:
        # Stores one or more MuvetoPmtError1ts.
        api_instance.post_muveto_pmt_error1ts(muveto_pmt_error1t)
    except ApiException as e:
        print("Exception when calling MuvetoPmtError1tApi->post_muveto_pmt_error1ts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muveto_pmt_error1t** | [**MuvetoPmtError1t**](MuvetoPmtError1t.md)| A MuvetoPmtError1t or list of MuvetoPmtError1t documents | 

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

# **put_muveto_pmt_error1t_item**
> put_muveto_pmt_error1t_item(muvetopmterror1t_id, muveto_pmt_error1t, if_match=if_match)

Replaces a MuvetoPmtError1t document

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
    api_instance = xepmts.MuvetoPmtError1tApi(api_client)
    muvetopmterror1t_id = 'muvetopmterror1t_id_example' # str | 
muveto_pmt_error1t = xepmts.MuvetoPmtError1t() # MuvetoPmtError1t | A MuvetoPmtError1t or list of MuvetoPmtError1t documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a MuvetoPmtError1t document
        api_instance.put_muveto_pmt_error1t_item(muvetopmterror1t_id, muveto_pmt_error1t, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoPmtError1tApi->put_muveto_pmt_error1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetopmterror1t_id** | **str**|  | 
 **muveto_pmt_error1t** | [**MuvetoPmtError1t**](MuvetoPmtError1t.md)| A MuvetoPmtError1t or list of MuvetoPmtError1t documents | 
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
**200** | MuvetoPmtError1t document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

