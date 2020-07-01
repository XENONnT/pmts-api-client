# xepmts.TpcCurrentChangeApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_tpc_current_change_item**](TpcCurrentChangeApi.md#delete_tpc_current_change_item) | **DELETE** /tpc/current_changes/{tpccurrentchangeId} | Deletes a TpcCurrentChange document
[**get_tpc_current_change_item**](TpcCurrentChangeApi.md#get_tpc_current_change_item) | **GET** /tpc/current_changes/{tpccurrentchangeId} | Retrieves a TpcCurrentChange document
[**get_tpc_current_changes**](TpcCurrentChangeApi.md#get_tpc_current_changes) | **GET** /tpc/current_changes | Retrieves one or more TpcCurrentChanges
[**post_tpc_current_changes**](TpcCurrentChangeApi.md#post_tpc_current_changes) | **POST** /tpc/current_changes | Stores one or more TpcCurrentChanges.
[**put_tpc_current_change_item**](TpcCurrentChangeApi.md#put_tpc_current_change_item) | **PUT** /tpc/current_changes/{tpccurrentchangeId} | Replaces a TpcCurrentChange document


# **delete_tpc_current_change_item**
> delete_tpc_current_change_item(tpccurrentchange_id, if_match=if_match)

Deletes a TpcCurrentChange document

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
    api_instance = xepmts.TpcCurrentChangeApi(api_client)
    tpccurrentchange_id = 'tpccurrentchange_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a TpcCurrentChange document
        api_instance.delete_tpc_current_change_item(tpccurrentchange_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcCurrentChangeApi->delete_tpc_current_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpccurrentchange_id** | **str**|  | 
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
**204** | TpcCurrentChange document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_current_change_item**
> TpcCurrentChange get_tpc_current_change_item(tpccurrentchange_id)

Retrieves a TpcCurrentChange document

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
    api_instance = xepmts.TpcCurrentChangeApi(api_client)
    tpccurrentchange_id = 'tpccurrentchange_id_example' # str | 

    try:
        # Retrieves a TpcCurrentChange document
        api_response = api_instance.get_tpc_current_change_item(tpccurrentchange_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcCurrentChangeApi->get_tpc_current_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpccurrentchange_id** | **str**|  | 

### Return type

[**TpcCurrentChange**](TpcCurrentChange.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TpcCurrentChange document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tpc_current_changes**
> InlineResponse2004 get_tpc_current_changes(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more TpcCurrentChanges

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
    api_instance = xepmts.TpcCurrentChangeApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more TpcCurrentChanges
        api_response = api_instance.get_tpc_current_changes(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling TpcCurrentChangeApi->get_tpc_current_changes: %s\n" % e)
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

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of TpcCurrentChanges |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_tpc_current_changes**
> post_tpc_current_changes(tpc_current_change)

Stores one or more TpcCurrentChanges.

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
    api_instance = xepmts.TpcCurrentChangeApi(api_client)
    tpc_current_change = xepmts.TpcCurrentChange() # TpcCurrentChange | A TpcCurrentChange or list of TpcCurrentChange documents

    try:
        # Stores one or more TpcCurrentChanges.
        api_instance.post_tpc_current_changes(tpc_current_change)
    except ApiException as e:
        print("Exception when calling TpcCurrentChangeApi->post_tpc_current_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpc_current_change** | [**TpcCurrentChange**](TpcCurrentChange.md)| A TpcCurrentChange or list of TpcCurrentChange documents | 

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

# **put_tpc_current_change_item**
> put_tpc_current_change_item(tpccurrentchange_id, tpc_current_change, if_match=if_match)

Replaces a TpcCurrentChange document

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
    api_instance = xepmts.TpcCurrentChangeApi(api_client)
    tpccurrentchange_id = 'tpccurrentchange_id_example' # str | 
tpc_current_change = xepmts.TpcCurrentChange() # TpcCurrentChange | A TpcCurrentChange or list of TpcCurrentChange documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a TpcCurrentChange document
        api_instance.put_tpc_current_change_item(tpccurrentchange_id, tpc_current_change, if_match=if_match)
    except ApiException as e:
        print("Exception when calling TpcCurrentChangeApi->put_tpc_current_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tpccurrentchange_id** | **str**|  | 
 **tpc_current_change** | [**TpcCurrentChange**](TpcCurrentChange.md)| A TpcCurrentChange or list of TpcCurrentChange documents | 
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
**200** | TpcCurrentChange document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

