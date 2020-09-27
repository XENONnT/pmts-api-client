# xepmts.NvetoCurrentChangeApi

All URIs are relative to *https://api-dot-xenon-pmts.uc.r.appspot.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_nveto_current_change_item**](NvetoCurrentChangeApi.md#delete_nveto_current_change_item) | **DELETE** /nveto/current_changes/{nvetocurrentchangeId} | Deletes a NvetoCurrentChange document
[**get_nveto_current_change_item**](NvetoCurrentChangeApi.md#get_nveto_current_change_item) | **GET** /nveto/current_changes/{nvetocurrentchangeId} | Retrieves a NvetoCurrentChange document
[**get_nveto_current_changes**](NvetoCurrentChangeApi.md#get_nveto_current_changes) | **GET** /nveto/current_changes | Retrieves one or more NvetoCurrentChanges
[**patch_nveto_current_change_item**](NvetoCurrentChangeApi.md#patch_nveto_current_change_item) | **PATCH** /nveto/current_changes/{nvetocurrentchangeId} | Updates a NvetoCurrentChange document
[**post_nveto_current_changes**](NvetoCurrentChangeApi.md#post_nveto_current_changes) | **POST** /nveto/current_changes | Stores one or more NvetoCurrentChanges.
[**put_nveto_current_change_item**](NvetoCurrentChangeApi.md#put_nveto_current_change_item) | **PUT** /nveto/current_changes/{nvetocurrentchangeId} | Replaces a NvetoCurrentChange document


# **delete_nveto_current_change_item**
> delete_nveto_current_change_item(nvetocurrentchange_id, if_match=if_match)

Deletes a NvetoCurrentChange document

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
    api_instance = xepmts.NvetoCurrentChangeApi(api_client)
    nvetocurrentchange_id = 'nvetocurrentchange_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a NvetoCurrentChange document
        api_instance.delete_nveto_current_change_item(nvetocurrentchange_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoCurrentChangeApi->delete_nveto_current_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetocurrentchange_id** | **str**|  | 
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
**204** | NvetoCurrentChange document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nveto_current_change_item**
> NvetoCurrentChange get_nveto_current_change_item(nvetocurrentchange_id)

Retrieves a NvetoCurrentChange document

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
    api_instance = xepmts.NvetoCurrentChangeApi(api_client)
    nvetocurrentchange_id = 'nvetocurrentchange_id_example' # str | 

    try:
        # Retrieves a NvetoCurrentChange document
        api_response = api_instance.get_nveto_current_change_item(nvetocurrentchange_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoCurrentChangeApi->get_nveto_current_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetocurrentchange_id** | **str**|  | 

### Return type

[**NvetoCurrentChange**](NvetoCurrentChange.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NvetoCurrentChange document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nveto_current_changes**
> InlineResponse20015 get_nveto_current_changes(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more NvetoCurrentChanges

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
    api_instance = xepmts.NvetoCurrentChangeApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more NvetoCurrentChanges
        api_response = api_instance.get_nveto_current_changes(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoCurrentChangeApi->get_nveto_current_changes: %s\n" % e)
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

[**InlineResponse20015**](InlineResponse20015.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of NvetoCurrentChanges |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_nveto_current_change_item**
> patch_nveto_current_change_item(nvetocurrentchange_id, nveto_current_change, if_match=if_match)

Updates a NvetoCurrentChange document

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
    api_instance = xepmts.NvetoCurrentChangeApi(api_client)
    nvetocurrentchange_id = 'nvetocurrentchange_id_example' # str | 
nveto_current_change = xepmts.NvetoCurrentChange() # NvetoCurrentChange | A NvetoCurrentChange or list of NvetoCurrentChange documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Updates a NvetoCurrentChange document
        api_instance.patch_nveto_current_change_item(nvetocurrentchange_id, nveto_current_change, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoCurrentChangeApi->patch_nveto_current_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetocurrentchange_id** | **str**|  | 
 **nveto_current_change** | [**NvetoCurrentChange**](NvetoCurrentChange.md)| A NvetoCurrentChange or list of NvetoCurrentChange documents | 
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
**200** | NvetoCurrentChange document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_nveto_current_changes**
> post_nveto_current_changes(nveto_current_change)

Stores one or more NvetoCurrentChanges.

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
    api_instance = xepmts.NvetoCurrentChangeApi(api_client)
    nveto_current_change = xepmts.NvetoCurrentChange() # NvetoCurrentChange | A NvetoCurrentChange or list of NvetoCurrentChange documents

    try:
        # Stores one or more NvetoCurrentChanges.
        api_instance.post_nveto_current_changes(nveto_current_change)
    except ApiException as e:
        print("Exception when calling NvetoCurrentChangeApi->post_nveto_current_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nveto_current_change** | [**NvetoCurrentChange**](NvetoCurrentChange.md)| A NvetoCurrentChange or list of NvetoCurrentChange documents | 

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

# **put_nveto_current_change_item**
> put_nveto_current_change_item(nvetocurrentchange_id, nveto_current_change, if_match=if_match)

Replaces a NvetoCurrentChange document

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
    api_instance = xepmts.NvetoCurrentChangeApi(api_client)
    nvetocurrentchange_id = 'nvetocurrentchange_id_example' # str | 
nveto_current_change = xepmts.NvetoCurrentChange() # NvetoCurrentChange | A NvetoCurrentChange or list of NvetoCurrentChange documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a NvetoCurrentChange document
        api_instance.put_nveto_current_change_item(nvetocurrentchange_id, nveto_current_change, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoCurrentChangeApi->put_nveto_current_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetocurrentchange_id** | **str**|  | 
 **nveto_current_change** | [**NvetoCurrentChange**](NvetoCurrentChange.md)| A NvetoCurrentChange or list of NvetoCurrentChange documents | 
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
**200** | NvetoCurrentChange document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

