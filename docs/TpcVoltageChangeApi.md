# xepmts.TpcVoltageChangeApi

All URIs are relative to *https://api-dot-xenon-pmts.uc.r.appspot.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tpc_voltage_change_item**](TpcVoltageChangeApi.md#delete_tpc_voltage_change_item) | **DELETE** /tpc/voltage_changes/{tpcvoltagechangeId} | Deletes a TpcVoltageChange document
[**get_tpc_voltage_change_item**](TpcVoltageChangeApi.md#get_tpc_voltage_change_item) | **GET** /tpc/voltage_changes/{tpcvoltagechangeId} | Retrieves a TpcVoltageChange document
[**get_tpc_voltage_changes**](TpcVoltageChangeApi.md#get_tpc_voltage_changes) | **GET** /tpc/voltage_changes | Retrieves one or more TpcVoltageChanges
[**patch_tpc_voltage_change_item**](TpcVoltageChangeApi.md#patch_tpc_voltage_change_item) | **PATCH** /tpc/voltage_changes/{tpcvoltagechangeId} | Updates a TpcVoltageChange document
[**post_tpc_voltage_changes**](TpcVoltageChangeApi.md#post_tpc_voltage_changes) | **POST** /tpc/voltage_changes | Stores one or more TpcVoltageChanges.
[**put_tpc_voltage_change_item**](TpcVoltageChangeApi.md#put_tpc_voltage_change_item) | **PUT** /tpc/voltage_changes/{tpcvoltagechangeId} | Replaces a TpcVoltageChange document


# **delete_tpc_voltage_change_item**
> delete_tpc_voltage_change_item(tpcvoltagechange_id, if_match=if_match)

Deletes a TpcVoltageChange document

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
    api_instance = xepmts.TpcVoltageChangeApi(api_client)
    tpcvoltagechange_id = 'tpcvoltagechange_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a TpcVoltageChange document
        api_instance.delete_tpc_voltage_change_item(tpcvoltagechange_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcVoltageChangeApi->delete_tpc_voltage_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcvoltagechange_id** | **str**|  | 
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
**204** | TpcVoltageChange document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_voltage_change_item**
> TpcVoltageChange get_tpc_voltage_change_item(tpcvoltagechange_id)

Retrieves a TpcVoltageChange document

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
    api_instance = xepmts.TpcVoltageChangeApi(api_client)
    tpcvoltagechange_id = 'tpcvoltagechange_id_example' # str | 

    try:
        # Retrieves a TpcVoltageChange document
        api_response = api_instance.get_tpc_voltage_change_item(tpcvoltagechange_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcVoltageChangeApi->get_tpc_voltage_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcvoltagechange_id** | **str**|  | 

### Return type

[**TpcVoltageChange**](TpcVoltageChange.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcVoltageChange document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_voltage_changes**
> InlineResponse20011 get_tpc_voltage_changes(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more TpcVoltageChanges

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
    api_instance = xepmts.TpcVoltageChangeApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more TpcVoltageChanges
        api_response = api_instance.get_tpc_voltage_changes(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcVoltageChangeApi->get_tpc_voltage_changes: %s\n" % e)
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

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of TpcVoltageChanges |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_tpc_voltage_change_item**
> patch_tpc_voltage_change_item(tpcvoltagechange_id, tpc_voltage_change, if_match=if_match)

Updates a TpcVoltageChange document

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
    api_instance = xepmts.TpcVoltageChangeApi(api_client)
    tpcvoltagechange_id = 'tpcvoltagechange_id_example' # str | 
tpc_voltage_change = xepmts.TpcVoltageChange() # TpcVoltageChange | A TpcVoltageChange or list of TpcVoltageChange documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Updates a TpcVoltageChange document
        api_instance.patch_tpc_voltage_change_item(tpcvoltagechange_id, tpc_voltage_change, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcVoltageChangeApi->patch_tpc_voltage_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcvoltagechange_id** | **str**|  | 
 **tpc_voltage_change** | [**TpcVoltageChange**](TpcVoltageChange.md)| A TpcVoltageChange or list of TpcVoltageChange documents | 
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
**200** | TpcVoltageChange document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tpc_voltage_changes**
> post_tpc_voltage_changes(tpc_voltage_change)

Stores one or more TpcVoltageChanges.

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
    api_instance = xepmts.TpcVoltageChangeApi(api_client)
    tpc_voltage_change = xepmts.TpcVoltageChange() # TpcVoltageChange | A TpcVoltageChange or list of TpcVoltageChange documents

    try:
        # Stores one or more TpcVoltageChanges.
        api_instance.post_tpc_voltage_changes(tpc_voltage_change)
    except ApiException as e:
        print("Exception when calling TpcVoltageChangeApi->post_tpc_voltage_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpc_voltage_change** | [**TpcVoltageChange**](TpcVoltageChange.md)| A TpcVoltageChange or list of TpcVoltageChange documents | 

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

# **put_tpc_voltage_change_item**
> put_tpc_voltage_change_item(tpcvoltagechange_id, tpc_voltage_change, if_match=if_match)

Replaces a TpcVoltageChange document

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
    api_instance = xepmts.TpcVoltageChangeApi(api_client)
    tpcvoltagechange_id = 'tpcvoltagechange_id_example' # str | 
tpc_voltage_change = xepmts.TpcVoltageChange() # TpcVoltageChange | A TpcVoltageChange or list of TpcVoltageChange documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a TpcVoltageChange document
        api_instance.put_tpc_voltage_change_item(tpcvoltagechange_id, tpc_voltage_change, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcVoltageChangeApi->put_tpc_voltage_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcvoltagechange_id** | **str**|  | 
 **tpc_voltage_change** | [**TpcVoltageChange**](TpcVoltageChange.md)| A TpcVoltageChange or list of TpcVoltageChange documents | 
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
**200** | TpcVoltageChange document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

