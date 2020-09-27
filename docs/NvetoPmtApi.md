# xepmts.NvetoPmtApi

All URIs are relative to *https://api-dot-xenon-pmts.uc.r.appspot.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_nveto_pmt_item**](NvetoPmtApi.md#delete_nveto_pmt_item) | **DELETE** /nveto/pmts/{nvetopmtId} | Deletes a NvetoPmt document
[**get_nveto_pmt_item**](NvetoPmtApi.md#get_nveto_pmt_item) | **GET** /nveto/pmts/{nvetopmtId} | Retrieves a NvetoPmt document
[**get_nveto_pmt_item_by_serial_number**](NvetoPmtApi.md#get_nveto_pmt_item_by_serial_number) | **GET** /nveto/pmts/{Serial_Number} | Retrieves a NvetoPmt document by serial_number
[**get_nveto_pmts**](NvetoPmtApi.md#get_nveto_pmts) | **GET** /nveto/pmts | Retrieves one or more NvetoPmts
[**patch_nveto_pmt_item**](NvetoPmtApi.md#patch_nveto_pmt_item) | **PATCH** /nveto/pmts/{nvetopmtId} | Updates a NvetoPmt document
[**post_nveto_pmts**](NvetoPmtApi.md#post_nveto_pmts) | **POST** /nveto/pmts | Stores one or more NvetoPmts.
[**put_nveto_pmt_item**](NvetoPmtApi.md#put_nveto_pmt_item) | **PUT** /nveto/pmts/{nvetopmtId} | Replaces a NvetoPmt document


# **delete_nveto_pmt_item**
> delete_nveto_pmt_item(nvetopmt_id, if_match=if_match)

Deletes a NvetoPmt document

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
    api_instance = xepmts.NvetoPmtApi(api_client)
    nvetopmt_id = 'nvetopmt_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a NvetoPmt document
        api_instance.delete_nveto_pmt_item(nvetopmt_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoPmtApi->delete_nveto_pmt_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetopmt_id** | **str**|  | 
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
**204** | NvetoPmt document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nveto_pmt_item**
> NvetoPmt get_nveto_pmt_item(nvetopmt_id)

Retrieves a NvetoPmt document

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
    api_instance = xepmts.NvetoPmtApi(api_client)
    nvetopmt_id = 'nvetopmt_id_example' # str | 

    try:
        # Retrieves a NvetoPmt document
        api_response = api_instance.get_nveto_pmt_item(nvetopmt_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoPmtApi->get_nveto_pmt_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetopmt_id** | **str**|  | 

### Return type

[**NvetoPmt**](NvetoPmt.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NvetoPmt document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nveto_pmt_item_by_serial_number**
> NvetoPmt get_nveto_pmt_item_by_serial_number(serial_number)

Retrieves a NvetoPmt document by serial_number

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
    api_instance = xepmts.NvetoPmtApi(api_client)
    serial_number = 'serial_number_example' # str | 

    try:
        # Retrieves a NvetoPmt document by serial_number
        api_response = api_instance.get_nveto_pmt_item_by_serial_number(serial_number)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoPmtApi->get_nveto_pmt_item_by_serial_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial_number** | **str**|  | 

### Return type

[**NvetoPmt**](NvetoPmt.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NvetoPmt document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nveto_pmts**
> InlineResponse20022 get_nveto_pmts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more NvetoPmts

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
    api_instance = xepmts.NvetoPmtApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more NvetoPmts
        api_response = api_instance.get_nveto_pmts(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoPmtApi->get_nveto_pmts: %s\n" % e)
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

[**InlineResponse20022**](InlineResponse20022.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of NvetoPmts |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_nveto_pmt_item**
> patch_nveto_pmt_item(nvetopmt_id, nveto_pmt, if_match=if_match)

Updates a NvetoPmt document

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
    api_instance = xepmts.NvetoPmtApi(api_client)
    nvetopmt_id = 'nvetopmt_id_example' # str | 
nveto_pmt = xepmts.NvetoPmt() # NvetoPmt | A NvetoPmt or list of NvetoPmt documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Updates a NvetoPmt document
        api_instance.patch_nveto_pmt_item(nvetopmt_id, nveto_pmt, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoPmtApi->patch_nveto_pmt_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetopmt_id** | **str**|  | 
 **nveto_pmt** | [**NvetoPmt**](NvetoPmt.md)| A NvetoPmt or list of NvetoPmt documents | 
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
**200** | NvetoPmt document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_nveto_pmts**
> post_nveto_pmts(nveto_pmt)

Stores one or more NvetoPmts.

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
    api_instance = xepmts.NvetoPmtApi(api_client)
    nveto_pmt = xepmts.NvetoPmt() # NvetoPmt | A NvetoPmt or list of NvetoPmt documents

    try:
        # Stores one or more NvetoPmts.
        api_instance.post_nveto_pmts(nveto_pmt)
    except ApiException as e:
        print("Exception when calling NvetoPmtApi->post_nveto_pmts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nveto_pmt** | [**NvetoPmt**](NvetoPmt.md)| A NvetoPmt or list of NvetoPmt documents | 

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

# **put_nveto_pmt_item**
> put_nveto_pmt_item(nvetopmt_id, nveto_pmt, if_match=if_match)

Replaces a NvetoPmt document

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
    api_instance = xepmts.NvetoPmtApi(api_client)
    nvetopmt_id = 'nvetopmt_id_example' # str | 
nveto_pmt = xepmts.NvetoPmt() # NvetoPmt | A NvetoPmt or list of NvetoPmt documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a NvetoPmt document
        api_instance.put_nveto_pmt_item(nvetopmt_id, nveto_pmt, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoPmtApi->put_nveto_pmt_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetopmt_id** | **str**|  | 
 **nveto_pmt** | [**NvetoPmt**](NvetoPmt.md)| A NvetoPmt or list of NvetoPmt documents | 
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
**200** | NvetoPmt document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

