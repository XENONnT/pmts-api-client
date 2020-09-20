# xepmts.MuvetoGainModelApi

All URIs are relative to *https://api.pmts.xenonnt.org/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_muveto_gain_model_item**](MuvetoGainModelApi.md#delete_muveto_gain_model_item) | **DELETE** /muveto/gain_models/{muvetogainmodelId} | Deletes a MuvetoGainModel document
[**get_muveto_gain_model_item**](MuvetoGainModelApi.md#get_muveto_gain_model_item) | **GET** /muveto/gain_models/{muvetogainmodelId} | Retrieves a MuvetoGainModel document
[**get_muveto_gain_models**](MuvetoGainModelApi.md#get_muveto_gain_models) | **GET** /muveto/gain_models | Retrieves one or more MuvetoGainModels
[**post_muveto_gain_models**](MuvetoGainModelApi.md#post_muveto_gain_models) | **POST** /muveto/gain_models | Stores one or more MuvetoGainModels.
[**put_muveto_gain_model_item**](MuvetoGainModelApi.md#put_muveto_gain_model_item) | **PUT** /muveto/gain_models/{muvetogainmodelId} | Replaces a MuvetoGainModel document


# **delete_muveto_gain_model_item**
> delete_muveto_gain_model_item(muvetogainmodel_id, if_match=if_match)

Deletes a MuvetoGainModel document

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
    api_instance = xepmts.MuvetoGainModelApi(api_client)
    muvetogainmodel_id = 'muvetogainmodel_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a MuvetoGainModel document
        api_instance.delete_muveto_gain_model_item(muvetogainmodel_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoGainModelApi->delete_muveto_gain_model_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetogainmodel_id** | **str**|  | 
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
**204** | MuvetoGainModel document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_gain_model_item**
> MuvetoGainModel get_muveto_gain_model_item(muvetogainmodel_id)

Retrieves a MuvetoGainModel document

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
    api_instance = xepmts.MuvetoGainModelApi(api_client)
    muvetogainmodel_id = 'muvetogainmodel_id_example' # str | 

    try:
        # Retrieves a MuvetoGainModel document
        api_response = api_instance.get_muveto_gain_model_item(muvetogainmodel_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoGainModelApi->get_muveto_gain_model_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetogainmodel_id** | **str**|  | 

### Return type

[**MuvetoGainModel**](MuvetoGainModel.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoGainModel document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_gain_models**
> InlineResponse20027 get_muveto_gain_models(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more MuvetoGainModels

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
    api_instance = xepmts.MuvetoGainModelApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more MuvetoGainModels
        api_response = api_instance.get_muveto_gain_models(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoGainModelApi->get_muveto_gain_models: %s\n" % e)
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

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of MuvetoGainModels |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_muveto_gain_models**
> post_muveto_gain_models(muveto_gain_model)

Stores one or more MuvetoGainModels.

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
    api_instance = xepmts.MuvetoGainModelApi(api_client)
    muveto_gain_model = xepmts.MuvetoGainModel() # MuvetoGainModel | A MuvetoGainModel or list of MuvetoGainModel documents

    try:
        # Stores one or more MuvetoGainModels.
        api_instance.post_muveto_gain_models(muveto_gain_model)
    except ApiException as e:
        print("Exception when calling MuvetoGainModelApi->post_muveto_gain_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muveto_gain_model** | [**MuvetoGainModel**](MuvetoGainModel.md)| A MuvetoGainModel or list of MuvetoGainModel documents | 

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

# **put_muveto_gain_model_item**
> put_muveto_gain_model_item(muvetogainmodel_id, muveto_gain_model, if_match=if_match)

Replaces a MuvetoGainModel document

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
    api_instance = xepmts.MuvetoGainModelApi(api_client)
    muvetogainmodel_id = 'muvetogainmodel_id_example' # str | 
muveto_gain_model = xepmts.MuvetoGainModel() # MuvetoGainModel | A MuvetoGainModel or list of MuvetoGainModel documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a MuvetoGainModel document
        api_instance.put_muveto_gain_model_item(muvetogainmodel_id, muveto_gain_model, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoGainModelApi->put_muveto_gain_model_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetogainmodel_id** | **str**|  | 
 **muveto_gain_model** | [**MuvetoGainModel**](MuvetoGainModel.md)| A MuvetoGainModel or list of MuvetoGainModel documents | 
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
**200** | MuvetoGainModel document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

