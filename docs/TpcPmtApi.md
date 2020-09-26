# xepmts.TpcPmtApi

All URIs are relative to *https://xenon-pmts.uc.r.appspot.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tpc_pmt_item**](TpcPmtApi.md#delete_tpc_pmt_item) | **DELETE** /tpc/pmts/{tpcpmtId} | Deletes a TpcPmt document
[**get_tpc_pmt_item**](TpcPmtApi.md#get_tpc_pmt_item) | **GET** /tpc/pmts/{tpcpmtId} | Retrieves a TpcPmt document
[**get_tpc_pmt_item_by_serial_number**](TpcPmtApi.md#get_tpc_pmt_item_by_serial_number) | **GET** /tpc/pmts/{Serial_Number} | Retrieves a TpcPmt document by serial_number
[**get_tpc_pmts**](TpcPmtApi.md#get_tpc_pmts) | **GET** /tpc/pmts | Retrieves one or more TpcPmts
[**patch_tpc_pmt_item**](TpcPmtApi.md#patch_tpc_pmt_item) | **PATCH** /tpc/pmts/{tpcpmtId} | Updates a TpcPmt document
[**post_tpc_pmts**](TpcPmtApi.md#post_tpc_pmts) | **POST** /tpc/pmts | Stores one or more TpcPmts.
[**put_tpc_pmt_item**](TpcPmtApi.md#put_tpc_pmt_item) | **PUT** /tpc/pmts/{tpcpmtId} | Replaces a TpcPmt document


# **delete_tpc_pmt_item**
> delete_tpc_pmt_item(tpcpmt_id, if_match=if_match)

Deletes a TpcPmt document

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
    api_instance = xepmts.TpcPmtApi(api_client)
    tpcpmt_id = 'tpcpmt_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a TpcPmt document
        api_instance.delete_tpc_pmt_item(tpcpmt_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcPmtApi->delete_tpc_pmt_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcpmt_id** | **str**|  | 
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
**204** | TpcPmt document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_pmt_item**
> TpcPmt get_tpc_pmt_item(tpcpmt_id)

Retrieves a TpcPmt document

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
    api_instance = xepmts.TpcPmtApi(api_client)
    tpcpmt_id = 'tpcpmt_id_example' # str | 

    try:
        # Retrieves a TpcPmt document
        api_response = api_instance.get_tpc_pmt_item(tpcpmt_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcPmtApi->get_tpc_pmt_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcpmt_id** | **str**|  | 

### Return type

[**TpcPmt**](TpcPmt.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcPmt document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_pmt_item_by_serial_number**
> TpcPmt get_tpc_pmt_item_by_serial_number(serial_number)

Retrieves a TpcPmt document by serial_number

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
    api_instance = xepmts.TpcPmtApi(api_client)
    serial_number = 'serial_number_example' # str | 

    try:
        # Retrieves a TpcPmt document by serial_number
        api_response = api_instance.get_tpc_pmt_item_by_serial_number(serial_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcPmtApi->get_tpc_pmt_item_by_serial_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial_number** | **str**|  | 

### Return type

[**TpcPmt**](TpcPmt.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcPmt document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_pmts**
> InlineResponse20010 get_tpc_pmts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more TpcPmts

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
    api_instance = xepmts.TpcPmtApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more TpcPmts
        api_response = api_instance.get_tpc_pmts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcPmtApi->get_tpc_pmts: %s\n" % e)
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

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of TpcPmts |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_tpc_pmt_item**
> patch_tpc_pmt_item(tpcpmt_id, tpc_pmt, if_match=if_match)

Updates a TpcPmt document

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
    api_instance = xepmts.TpcPmtApi(api_client)
    tpcpmt_id = 'tpcpmt_id_example' # str | 
tpc_pmt = xepmts.TpcPmt() # TpcPmt | A TpcPmt or list of TpcPmt documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Updates a TpcPmt document
        api_instance.patch_tpc_pmt_item(tpcpmt_id, tpc_pmt, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcPmtApi->patch_tpc_pmt_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcpmt_id** | **str**|  | 
 **tpc_pmt** | [**TpcPmt**](TpcPmt.md)| A TpcPmt or list of TpcPmt documents | 
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
**200** | TpcPmt document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tpc_pmts**
> post_tpc_pmts(tpc_pmt)

Stores one or more TpcPmts.

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
    api_instance = xepmts.TpcPmtApi(api_client)
    tpc_pmt = xepmts.TpcPmt() # TpcPmt | A TpcPmt or list of TpcPmt documents

    try:
        # Stores one or more TpcPmts.
        api_instance.post_tpc_pmts(tpc_pmt)
    except ApiException as e:
        print("Exception when calling TpcPmtApi->post_tpc_pmts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpc_pmt** | [**TpcPmt**](TpcPmt.md)| A TpcPmt or list of TpcPmt documents | 

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

# **put_tpc_pmt_item**
> put_tpc_pmt_item(tpcpmt_id, tpc_pmt, if_match=if_match)

Replaces a TpcPmt document

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
    api_instance = xepmts.TpcPmtApi(api_client)
    tpcpmt_id = 'tpcpmt_id_example' # str | 
tpc_pmt = xepmts.TpcPmt() # TpcPmt | A TpcPmt or list of TpcPmt documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a TpcPmt document
        api_instance.put_tpc_pmt_item(tpcpmt_id, tpc_pmt, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcPmtApi->put_tpc_pmt_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpcpmt_id** | **str**|  | 
 **tpc_pmt** | [**TpcPmt**](TpcPmt.md)| A TpcPmt or list of TpcPmt documents | 
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
**200** | TpcPmt document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

