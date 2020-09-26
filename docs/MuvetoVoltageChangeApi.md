# xepmts.MuvetoVoltageChangeApi

All URIs are relative to *https://xenon-pmts.uc.r.appspot.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_muveto_voltage_change_item**](MuvetoVoltageChangeApi.md#delete_muveto_voltage_change_item) | **DELETE** /muveto/voltage_changes/{muvetovoltagechangeId} | Deletes a MuvetoVoltageChange document
[**get_muveto_voltage_change_item**](MuvetoVoltageChangeApi.md#get_muveto_voltage_change_item) | **GET** /muveto/voltage_changes/{muvetovoltagechangeId} | Retrieves a MuvetoVoltageChange document
[**get_muveto_voltage_changes**](MuvetoVoltageChangeApi.md#get_muveto_voltage_changes) | **GET** /muveto/voltage_changes | Retrieves one or more MuvetoVoltageChanges
[**patch_muveto_voltage_change_item**](MuvetoVoltageChangeApi.md#patch_muveto_voltage_change_item) | **PATCH** /muveto/voltage_changes/{muvetovoltagechangeId} | Updates a MuvetoVoltageChange document
[**post_muveto_voltage_changes**](MuvetoVoltageChangeApi.md#post_muveto_voltage_changes) | **POST** /muveto/voltage_changes | Stores one or more MuvetoVoltageChanges.
[**put_muveto_voltage_change_item**](MuvetoVoltageChangeApi.md#put_muveto_voltage_change_item) | **PUT** /muveto/voltage_changes/{muvetovoltagechangeId} | Replaces a MuvetoVoltageChange document


# **delete_muveto_voltage_change_item**
> delete_muveto_voltage_change_item(muvetovoltagechange_id, if_match=if_match)

Deletes a MuvetoVoltageChange document

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
    api_instance = xepmts.MuvetoVoltageChangeApi(api_client)
    muvetovoltagechange_id = 'muvetovoltagechange_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a MuvetoVoltageChange document
        api_instance.delete_muveto_voltage_change_item(muvetovoltagechange_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoVoltageChangeApi->delete_muveto_voltage_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetovoltagechange_id** | **str**|  | 
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
**204** | MuvetoVoltageChange document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_voltage_change_item**
> MuvetoVoltageChange get_muveto_voltage_change_item(muvetovoltagechange_id)

Retrieves a MuvetoVoltageChange document

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
    api_instance = xepmts.MuvetoVoltageChangeApi(api_client)
    muvetovoltagechange_id = 'muvetovoltagechange_id_example' # str | 

    try:
        # Retrieves a MuvetoVoltageChange document
        api_response = api_instance.get_muveto_voltage_change_item(muvetovoltagechange_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoVoltageChangeApi->get_muveto_voltage_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetovoltagechange_id** | **str**|  | 

### Return type

[**MuvetoVoltageChange**](MuvetoVoltageChange.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoVoltageChange document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_voltage_changes**
> InlineResponse20033 get_muveto_voltage_changes(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more MuvetoVoltageChanges

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
    api_instance = xepmts.MuvetoVoltageChangeApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more MuvetoVoltageChanges
        api_response = api_instance.get_muveto_voltage_changes(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoVoltageChangeApi->get_muveto_voltage_changes: %s\n" % e)
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

[**InlineResponse20033**](InlineResponse20033.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of MuvetoVoltageChanges |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_muveto_voltage_change_item**
> patch_muveto_voltage_change_item(muvetovoltagechange_id, muveto_voltage_change, if_match=if_match)

Updates a MuvetoVoltageChange document

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
    api_instance = xepmts.MuvetoVoltageChangeApi(api_client)
    muvetovoltagechange_id = 'muvetovoltagechange_id_example' # str | 
muveto_voltage_change = xepmts.MuvetoVoltageChange() # MuvetoVoltageChange | A MuvetoVoltageChange or list of MuvetoVoltageChange documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Updates a MuvetoVoltageChange document
        api_instance.patch_muveto_voltage_change_item(muvetovoltagechange_id, muveto_voltage_change, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoVoltageChangeApi->patch_muveto_voltage_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetovoltagechange_id** | **str**|  | 
 **muveto_voltage_change** | [**MuvetoVoltageChange**](MuvetoVoltageChange.md)| A MuvetoVoltageChange or list of MuvetoVoltageChange documents | 
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
**200** | MuvetoVoltageChange document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_muveto_voltage_changes**
> post_muveto_voltage_changes(muveto_voltage_change)

Stores one or more MuvetoVoltageChanges.

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
    api_instance = xepmts.MuvetoVoltageChangeApi(api_client)
    muveto_voltage_change = xepmts.MuvetoVoltageChange() # MuvetoVoltageChange | A MuvetoVoltageChange or list of MuvetoVoltageChange documents

    try:
        # Stores one or more MuvetoVoltageChanges.
        api_instance.post_muveto_voltage_changes(muveto_voltage_change)
    except ApiException as e:
        print("Exception when calling MuvetoVoltageChangeApi->post_muveto_voltage_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muveto_voltage_change** | [**MuvetoVoltageChange**](MuvetoVoltageChange.md)| A MuvetoVoltageChange or list of MuvetoVoltageChange documents | 

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

# **put_muveto_voltage_change_item**
> put_muveto_voltage_change_item(muvetovoltagechange_id, muveto_voltage_change, if_match=if_match)

Replaces a MuvetoVoltageChange document

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
    api_instance = xepmts.MuvetoVoltageChangeApi(api_client)
    muvetovoltagechange_id = 'muvetovoltagechange_id_example' # str | 
muveto_voltage_change = xepmts.MuvetoVoltageChange() # MuvetoVoltageChange | A MuvetoVoltageChange or list of MuvetoVoltageChange documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a MuvetoVoltageChange document
        api_instance.put_muveto_voltage_change_item(muvetovoltagechange_id, muveto_voltage_change, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoVoltageChangeApi->put_muveto_voltage_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetovoltagechange_id** | **str**|  | 
 **muveto_voltage_change** | [**MuvetoVoltageChange**](MuvetoVoltageChange.md)| A MuvetoVoltageChange or list of MuvetoVoltageChange documents | 
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
**200** | MuvetoVoltageChange document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

