# xepmts.TpcPmtError1tApi

All URIs are relative to *https://api-dot-xenon-pmts.uc.r.appspot.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tpc_pmt_error1t_item**](TpcPmtError1tApi.md#delete_tpc_pmt_error1t_item) | **DELETE** /xenon1t/tpc/pmt_errors/{tpcpmterror1tId} | Deletes a TpcPmtError1t document
[**get_tpc_pmt_error1t_item**](TpcPmtError1tApi.md#get_tpc_pmt_error1t_item) | **GET** /xenon1t/tpc/pmt_errors/{tpcpmterror1tId} | Retrieves a TpcPmtError1t document
[**get_tpc_pmt_error1ts**](TpcPmtError1tApi.md#get_tpc_pmt_error1ts) | **GET** /xenon1t/tpc/pmt_errors | Retrieves one or more TpcPmtError1ts
[**patch_tpc_pmt_error1t_item**](TpcPmtError1tApi.md#patch_tpc_pmt_error1t_item) | **PATCH** /xenon1t/tpc/pmt_errors/{tpcpmterror1tId} | Updates a TpcPmtError1t document
[**post_tpc_pmt_error1ts**](TpcPmtError1tApi.md#post_tpc_pmt_error1ts) | **POST** /xenon1t/tpc/pmt_errors | Stores one or more TpcPmtError1ts.
[**put_tpc_pmt_error1t_item**](TpcPmtError1tApi.md#put_tpc_pmt_error1t_item) | **PUT** /xenon1t/tpc/pmt_errors/{tpcpmterror1tId} | Replaces a TpcPmtError1t document


# **delete_tpc_pmt_error1t_item**
> delete_tpc_pmt_error1t_item(tpcpmterror1t_id, if_match=if_match)

Deletes a TpcPmtError1t document

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
    api_instance = xepmts.TpcPmtError1tApi(api_client)
    tpcpmterror1t_id = 'tpcpmterror1t_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a TpcPmtError1t document
        api_instance.delete_tpc_pmt_error1t_item(tpcpmterror1t_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcPmtError1tApi->delete_tpc_pmt_error1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcpmterror1t_id** | **str**|  | 
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
**204** | TpcPmtError1t document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_pmt_error1t_item**
> TpcPmtError1t get_tpc_pmt_error1t_item(tpcpmterror1t_id)

Retrieves a TpcPmtError1t document

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
    api_instance = xepmts.TpcPmtError1tApi(api_client)
    tpcpmterror1t_id = 'tpcpmterror1t_id_example' # str | 

    try:
        # Retrieves a TpcPmtError1t document
        api_response = api_instance.get_tpc_pmt_error1t_item(tpcpmterror1t_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcPmtError1tApi->get_tpc_pmt_error1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcpmterror1t_id** | **str**|  | 

### Return type

[**TpcPmtError1t**](TpcPmtError1t.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcPmtError1t document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_pmt_error1ts**
> InlineResponse20045 get_tpc_pmt_error1ts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more TpcPmtError1ts

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
    api_instance = xepmts.TpcPmtError1tApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more TpcPmtError1ts
        api_response = api_instance.get_tpc_pmt_error1ts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcPmtError1tApi->get_tpc_pmt_error1ts: %s\n" % e)
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

[**InlineResponse20045**](InlineResponse20045.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of TpcPmtError1ts |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_tpc_pmt_error1t_item**
> patch_tpc_pmt_error1t_item(tpcpmterror1t_id, tpc_pmt_error1t, if_match=if_match)

Updates a TpcPmtError1t document

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
    api_instance = xepmts.TpcPmtError1tApi(api_client)
    tpcpmterror1t_id = 'tpcpmterror1t_id_example' # str | 
tpc_pmt_error1t = xepmts.TpcPmtError1t() # TpcPmtError1t | A TpcPmtError1t or list of TpcPmtError1t documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Updates a TpcPmtError1t document
        api_instance.patch_tpc_pmt_error1t_item(tpcpmterror1t_id, tpc_pmt_error1t, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcPmtError1tApi->patch_tpc_pmt_error1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcpmterror1t_id** | **str**|  | 
 **tpc_pmt_error1t** | [**TpcPmtError1t**](TpcPmtError1t.md)| A TpcPmtError1t or list of TpcPmtError1t documents | 
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
**200** | TpcPmtError1t document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tpc_pmt_error1ts**
> post_tpc_pmt_error1ts(tpc_pmt_error1t)

Stores one or more TpcPmtError1ts.

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
    api_instance = xepmts.TpcPmtError1tApi(api_client)
    tpc_pmt_error1t = xepmts.TpcPmtError1t() # TpcPmtError1t | A TpcPmtError1t or list of TpcPmtError1t documents

    try:
        # Stores one or more TpcPmtError1ts.
        api_instance.post_tpc_pmt_error1ts(tpc_pmt_error1t)
    except ApiException as e:
        print("Exception when calling TpcPmtError1tApi->post_tpc_pmt_error1ts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpc_pmt_error1t** | [**TpcPmtError1t**](TpcPmtError1t.md)| A TpcPmtError1t or list of TpcPmtError1t documents | 

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

# **put_tpc_pmt_error1t_item**
> put_tpc_pmt_error1t_item(tpcpmterror1t_id, tpc_pmt_error1t, if_match=if_match)

Replaces a TpcPmtError1t document

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
    api_instance = xepmts.TpcPmtError1tApi(api_client)
    tpcpmterror1t_id = 'tpcpmterror1t_id_example' # str | 
tpc_pmt_error1t = xepmts.TpcPmtError1t() # TpcPmtError1t | A TpcPmtError1t or list of TpcPmtError1t documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a TpcPmtError1t document
        api_instance.put_tpc_pmt_error1t_item(tpcpmterror1t_id, tpc_pmt_error1t, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcPmtError1tApi->put_tpc_pmt_error1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcpmterror1t_id** | **str**|  | 
 **tpc_pmt_error1t** | [**TpcPmtError1t**](TpcPmtError1t.md)| A TpcPmtError1t or list of TpcPmtError1t documents | 
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
**200** | TpcPmtError1t document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

