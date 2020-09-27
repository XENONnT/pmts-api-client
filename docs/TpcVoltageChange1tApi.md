# xepmts.TpcVoltageChange1tApi

All URIs are relative to *https://api-dot-xenon-pmts.uc.r.appspot.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tpc_voltage_change1t_item**](TpcVoltageChange1tApi.md#delete_tpc_voltage_change1t_item) | **DELETE** /xenon1t/tpc/voltage_changes/{tpcvoltagechange1tId} | Deletes a TpcVoltageChange1t document
[**get_tpc_voltage_change1t_item**](TpcVoltageChange1tApi.md#get_tpc_voltage_change1t_item) | **GET** /xenon1t/tpc/voltage_changes/{tpcvoltagechange1tId} | Retrieves a TpcVoltageChange1t document
[**get_tpc_voltage_change1ts**](TpcVoltageChange1tApi.md#get_tpc_voltage_change1ts) | **GET** /xenon1t/tpc/voltage_changes | Retrieves one or more TpcVoltageChange1ts
[**patch_tpc_voltage_change1t_item**](TpcVoltageChange1tApi.md#patch_tpc_voltage_change1t_item) | **PATCH** /xenon1t/tpc/voltage_changes/{tpcvoltagechange1tId} | Updates a TpcVoltageChange1t document
[**post_tpc_voltage_change1ts**](TpcVoltageChange1tApi.md#post_tpc_voltage_change1ts) | **POST** /xenon1t/tpc/voltage_changes | Stores one or more TpcVoltageChange1ts.
[**put_tpc_voltage_change1t_item**](TpcVoltageChange1tApi.md#put_tpc_voltage_change1t_item) | **PUT** /xenon1t/tpc/voltage_changes/{tpcvoltagechange1tId} | Replaces a TpcVoltageChange1t document


# **delete_tpc_voltage_change1t_item**
> delete_tpc_voltage_change1t_item(tpcvoltagechange1t_id, if_match=if_match)

Deletes a TpcVoltageChange1t document

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
    api_instance = xepmts.TpcVoltageChange1tApi(api_client)
    tpcvoltagechange1t_id = 'tpcvoltagechange1t_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a TpcVoltageChange1t document
        api_instance.delete_tpc_voltage_change1t_item(tpcvoltagechange1t_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcVoltageChange1tApi->delete_tpc_voltage_change1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcvoltagechange1t_id** | **str**|  | 
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
**204** | TpcVoltageChange1t document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_voltage_change1t_item**
> TpcVoltageChange1t get_tpc_voltage_change1t_item(tpcvoltagechange1t_id)

Retrieves a TpcVoltageChange1t document

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
    api_instance = xepmts.TpcVoltageChange1tApi(api_client)
    tpcvoltagechange1t_id = 'tpcvoltagechange1t_id_example' # str | 

    try:
        # Retrieves a TpcVoltageChange1t document
        api_response = api_instance.get_tpc_voltage_change1t_item(tpcvoltagechange1t_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcVoltageChange1tApi->get_tpc_voltage_change1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcvoltagechange1t_id** | **str**|  | 

### Return type

[**TpcVoltageChange1t**](TpcVoltageChange1t.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcVoltageChange1t document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_voltage_change1ts**
> InlineResponse20047 get_tpc_voltage_change1ts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more TpcVoltageChange1ts

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
    api_instance = xepmts.TpcVoltageChange1tApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more TpcVoltageChange1ts
        api_response = api_instance.get_tpc_voltage_change1ts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcVoltageChange1tApi->get_tpc_voltage_change1ts: %s\n" % e)
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

[**InlineResponse20047**](InlineResponse20047.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of TpcVoltageChange1ts |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_tpc_voltage_change1t_item**
> patch_tpc_voltage_change1t_item(tpcvoltagechange1t_id, tpc_voltage_change1t, if_match=if_match)

Updates a TpcVoltageChange1t document

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
    api_instance = xepmts.TpcVoltageChange1tApi(api_client)
    tpcvoltagechange1t_id = 'tpcvoltagechange1t_id_example' # str | 
tpc_voltage_change1t = xepmts.TpcVoltageChange1t() # TpcVoltageChange1t | A TpcVoltageChange1t or list of TpcVoltageChange1t documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Updates a TpcVoltageChange1t document
        api_instance.patch_tpc_voltage_change1t_item(tpcvoltagechange1t_id, tpc_voltage_change1t, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcVoltageChange1tApi->patch_tpc_voltage_change1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcvoltagechange1t_id** | **str**|  | 
 **tpc_voltage_change1t** | [**TpcVoltageChange1t**](TpcVoltageChange1t.md)| A TpcVoltageChange1t or list of TpcVoltageChange1t documents | 
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
**200** | TpcVoltageChange1t document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tpc_voltage_change1ts**
> post_tpc_voltage_change1ts(tpc_voltage_change1t)

Stores one or more TpcVoltageChange1ts.

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
    api_instance = xepmts.TpcVoltageChange1tApi(api_client)
    tpc_voltage_change1t = xepmts.TpcVoltageChange1t() # TpcVoltageChange1t | A TpcVoltageChange1t or list of TpcVoltageChange1t documents

    try:
        # Stores one or more TpcVoltageChange1ts.
        api_instance.post_tpc_voltage_change1ts(tpc_voltage_change1t)
    except ApiException as e:
        print("Exception when calling TpcVoltageChange1tApi->post_tpc_voltage_change1ts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpc_voltage_change1t** | [**TpcVoltageChange1t**](TpcVoltageChange1t.md)| A TpcVoltageChange1t or list of TpcVoltageChange1t documents | 

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

# **put_tpc_voltage_change1t_item**
> put_tpc_voltage_change1t_item(tpcvoltagechange1t_id, tpc_voltage_change1t, if_match=if_match)

Replaces a TpcVoltageChange1t document

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
    api_instance = xepmts.TpcVoltageChange1tApi(api_client)
    tpcvoltagechange1t_id = 'tpcvoltagechange1t_id_example' # str | 
tpc_voltage_change1t = xepmts.TpcVoltageChange1t() # TpcVoltageChange1t | A TpcVoltageChange1t or list of TpcVoltageChange1t documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a TpcVoltageChange1t document
        api_instance.put_tpc_voltage_change1t_item(tpcvoltagechange1t_id, tpc_voltage_change1t, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcVoltageChange1tApi->put_tpc_voltage_change1t_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcvoltagechange1t_id** | **str**|  | 
 **tpc_voltage_change1t** | [**TpcVoltageChange1t**](TpcVoltageChange1t.md)| A TpcVoltageChange1t or list of TpcVoltageChange1t documents | 
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
**200** | TpcVoltageChange1t document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

