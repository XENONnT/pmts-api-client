# xepmts.MuvetoCurrentChangeApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_muveto_current_change_item**](MuvetoCurrentChangeApi.md#delete_muveto_current_change_item) | **DELETE** /muveto/current_changes/{muvetocurrentchangeId} | Deletes a MuvetoCurrentChange document
[**get_muveto_current_change_item**](MuvetoCurrentChangeApi.md#get_muveto_current_change_item) | **GET** /muveto/current_changes/{muvetocurrentchangeId} | Retrieves a MuvetoCurrentChange document
[**get_muveto_current_changes**](MuvetoCurrentChangeApi.md#get_muveto_current_changes) | **GET** /muveto/current_changes | Retrieves one or more MuvetoCurrentChanges
[**post_muveto_current_changes**](MuvetoCurrentChangeApi.md#post_muveto_current_changes) | **POST** /muveto/current_changes | Stores one or more MuvetoCurrentChanges.
[**put_muveto_current_change_item**](MuvetoCurrentChangeApi.md#put_muveto_current_change_item) | **PUT** /muveto/current_changes/{muvetocurrentchangeId} | Replaces a MuvetoCurrentChange document


# **delete_muveto_current_change_item**
> delete_muveto_current_change_item(muvetocurrentchange_id, if_match=if_match)

Deletes a MuvetoCurrentChange document

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
    api_instance = xepmts.MuvetoCurrentChangeApi(api_client)
    muvetocurrentchange_id = 'muvetocurrentchange_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a MuvetoCurrentChange document
        api_instance.delete_muveto_current_change_item(muvetocurrentchange_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoCurrentChangeApi->delete_muveto_current_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetocurrentchange_id** | **str**|  | 
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
**204** | MuvetoCurrentChange document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_current_change_item**
> MuvetoCurrentChange get_muveto_current_change_item(muvetocurrentchange_id)

Retrieves a MuvetoCurrentChange document

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
    api_instance = xepmts.MuvetoCurrentChangeApi(api_client)
    muvetocurrentchange_id = 'muvetocurrentchange_id_example' # str | 

    try:
        # Retrieves a MuvetoCurrentChange document
        api_response = api_instance.get_muveto_current_change_item(muvetocurrentchange_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoCurrentChangeApi->get_muveto_current_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetocurrentchange_id** | **str**|  | 

### Return type

[**MuvetoCurrentChange**](MuvetoCurrentChange.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoCurrentChange document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_current_changes**
> InlineResponse20031 get_muveto_current_changes(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more MuvetoCurrentChanges

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
    api_instance = xepmts.MuvetoCurrentChangeApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more MuvetoCurrentChanges
        api_response = api_instance.get_muveto_current_changes(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoCurrentChangeApi->get_muveto_current_changes: %s\n" % e)
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

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of MuvetoCurrentChanges |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_muveto_current_changes**
> post_muveto_current_changes(muveto_current_change)

Stores one or more MuvetoCurrentChanges.

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
    api_instance = xepmts.MuvetoCurrentChangeApi(api_client)
    muveto_current_change = xepmts.MuvetoCurrentChange() # MuvetoCurrentChange | A MuvetoCurrentChange or list of MuvetoCurrentChange documents

    try:
        # Stores one or more MuvetoCurrentChanges.
        api_instance.post_muveto_current_changes(muveto_current_change)
    except ApiException as e:
        print("Exception when calling MuvetoCurrentChangeApi->post_muveto_current_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muveto_current_change** | [**MuvetoCurrentChange**](MuvetoCurrentChange.md)| A MuvetoCurrentChange or list of MuvetoCurrentChange documents | 

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

# **put_muveto_current_change_item**
> put_muveto_current_change_item(muvetocurrentchange_id, muveto_current_change, if_match=if_match)

Replaces a MuvetoCurrentChange document

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
    api_instance = xepmts.MuvetoCurrentChangeApi(api_client)
    muvetocurrentchange_id = 'muvetocurrentchange_id_example' # str | 
muveto_current_change = xepmts.MuvetoCurrentChange() # MuvetoCurrentChange | A MuvetoCurrentChange or list of MuvetoCurrentChange documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a MuvetoCurrentChange document
        api_instance.put_muveto_current_change_item(muvetocurrentchange_id, muveto_current_change, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoCurrentChangeApi->put_muveto_current_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetocurrentchange_id** | **str**|  | 
 **muveto_current_change** | [**MuvetoCurrentChange**](MuvetoCurrentChange.md)| A MuvetoCurrentChange or list of MuvetoCurrentChange documents | 
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
**200** | MuvetoCurrentChange document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

