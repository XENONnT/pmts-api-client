# xepmts.MuvetoPmtApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_muveto_pmt_item**](MuvetoPmtApi.md#delete_muveto_pmt_item) | **DELETE** /muveto/pmts/{muvetopmtId} | Deletes a MuvetoPmt document
[**get_muveto_pmt_item**](MuvetoPmtApi.md#get_muveto_pmt_item) | **GET** /muveto/pmts/{muvetopmtId} | Retrieves a MuvetoPmt document
[**get_muveto_pmt_item_by_serial_number**](MuvetoPmtApi.md#get_muveto_pmt_item_by_serial_number) | **GET** /muveto/pmts/{Serial_Number} | Retrieves a MuvetoPmt document by serial_number
[**get_muveto_pmts**](MuvetoPmtApi.md#get_muveto_pmts) | **GET** /muveto/pmts | Retrieves one or more MuvetoPmts
[**post_muveto_pmts**](MuvetoPmtApi.md#post_muveto_pmts) | **POST** /muveto/pmts | Stores one or more MuvetoPmts.
[**put_muveto_pmt_item**](MuvetoPmtApi.md#put_muveto_pmt_item) | **PUT** /muveto/pmts/{muvetopmtId} | Replaces a MuvetoPmt document


# **delete_muveto_pmt_item**
> delete_muveto_pmt_item(muvetopmt_id, if_match=if_match)

Deletes a MuvetoPmt document

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
    api_instance = xepmts.MuvetoPmtApi(api_client)
    muvetopmt_id = 'muvetopmt_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a MuvetoPmt document
        api_instance.delete_muveto_pmt_item(muvetopmt_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoPmtApi->delete_muveto_pmt_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetopmt_id** | **str**|  | 
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
**204** | MuvetoPmt document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_pmt_item**
> MuvetoPmt get_muveto_pmt_item(muvetopmt_id)

Retrieves a MuvetoPmt document

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
    api_instance = xepmts.MuvetoPmtApi(api_client)
    muvetopmt_id = 'muvetopmt_id_example' # str | 

    try:
        # Retrieves a MuvetoPmt document
        api_response = api_instance.get_muveto_pmt_item(muvetopmt_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoPmtApi->get_muveto_pmt_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetopmt_id** | **str**|  | 

### Return type

[**MuvetoPmt**](MuvetoPmt.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoPmt document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_pmt_item_by_serial_number**
> MuvetoPmt get_muveto_pmt_item_by_serial_number(serial_number)

Retrieves a MuvetoPmt document by serial_number

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
    api_instance = xepmts.MuvetoPmtApi(api_client)
    serial_number = 'serial_number_example' # str | 

    try:
        # Retrieves a MuvetoPmt document by serial_number
        api_response = api_instance.get_muveto_pmt_item_by_serial_number(serial_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoPmtApi->get_muveto_pmt_item_by_serial_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial_number** | **str**|  | 

### Return type

[**MuvetoPmt**](MuvetoPmt.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoPmt document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_pmts**
> InlineResponse20025 get_muveto_pmts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more MuvetoPmts

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
    api_instance = xepmts.MuvetoPmtApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more MuvetoPmts
        api_response = api_instance.get_muveto_pmts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoPmtApi->get_muveto_pmts: %s\n" % e)
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

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of MuvetoPmts |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_muveto_pmts**
> post_muveto_pmts(muveto_pmt)

Stores one or more MuvetoPmts.

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
    api_instance = xepmts.MuvetoPmtApi(api_client)
    muveto_pmt = xepmts.MuvetoPmt() # MuvetoPmt | A MuvetoPmt or list of MuvetoPmt documents

    try:
        # Stores one or more MuvetoPmts.
        api_instance.post_muveto_pmts(muveto_pmt)
    except ApiException as e:
        print("Exception when calling MuvetoPmtApi->post_muveto_pmts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muveto_pmt** | [**MuvetoPmt**](MuvetoPmt.md)| A MuvetoPmt or list of MuvetoPmt documents | 

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

# **put_muveto_pmt_item**
> put_muveto_pmt_item(muvetopmt_id, muveto_pmt, if_match=if_match)

Replaces a MuvetoPmt document

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
    api_instance = xepmts.MuvetoPmtApi(api_client)
    muvetopmt_id = 'muvetopmt_id_example' # str | 
muveto_pmt = xepmts.MuvetoPmt() # MuvetoPmt | A MuvetoPmt or list of MuvetoPmt documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a MuvetoPmt document
        api_instance.put_muveto_pmt_item(muvetopmt_id, muveto_pmt, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoPmtApi->put_muveto_pmt_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetopmt_id** | **str**|  | 
 **muveto_pmt** | [**MuvetoPmt**](MuvetoPmt.md)| A MuvetoPmt or list of MuvetoPmt documents | 
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
**200** | MuvetoPmt document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

