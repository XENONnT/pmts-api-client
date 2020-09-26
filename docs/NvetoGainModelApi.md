# xepmts.NvetoGainModelApi

All URIs are relative to *https://xenon-pmts.uc.r.appspot.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_nveto_gain_model_item**](NvetoGainModelApi.md#delete_nveto_gain_model_item) | **DELETE** /nveto/gain_models/{nvetogainmodelId} | Deletes a NvetoGainModel document
[**delete_nveto_gain_models**](NvetoGainModelApi.md#delete_nveto_gain_models) | **DELETE** /nveto/gain_models | Deletes all NvetoGainModels
[**get_nveto_gain_model_item**](NvetoGainModelApi.md#get_nveto_gain_model_item) | **GET** /nveto/gain_models/{nvetogainmodelId} | Retrieves a NvetoGainModel document
[**get_nveto_gain_models**](NvetoGainModelApi.md#get_nveto_gain_models) | **GET** /nveto/gain_models | Retrieves one or more NvetoGainModels
[**patch_nveto_gain_model_item**](NvetoGainModelApi.md#patch_nveto_gain_model_item) | **PATCH** /nveto/gain_models/{nvetogainmodelId} | Updates a NvetoGainModel document
[**post_nveto_gain_models**](NvetoGainModelApi.md#post_nveto_gain_models) | **POST** /nveto/gain_models | Stores one or more NvetoGainModels.
[**put_nveto_gain_model_item**](NvetoGainModelApi.md#put_nveto_gain_model_item) | **PUT** /nveto/gain_models/{nvetogainmodelId} | Replaces a NvetoGainModel document


# **delete_nveto_gain_model_item**
> delete_nveto_gain_model_item(nvetogainmodel_id, if_match=if_match)

Deletes a NvetoGainModel document

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
    api_instance = xepmts.NvetoGainModelApi(api_client)
    nvetogainmodel_id = 'nvetogainmodel_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a NvetoGainModel document
        api_instance.delete_nveto_gain_model_item(nvetogainmodel_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoGainModelApi->delete_nveto_gain_model_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetogainmodel_id** | **str**|  | 
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
**204** | NvetoGainModel document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nveto_gain_models**
> delete_nveto_gain_models()

Deletes all NvetoGainModels

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
    api_instance = xepmts.NvetoGainModelApi(api_client)
    
    try:
        # Deletes all NvetoGainModels
        api_instance.delete_nveto_gain_models()
    except ApiException as e:
        print("Exception when calling NvetoGainModelApi->delete_nveto_gain_models: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

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
**204** | operation has been successful |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nveto_gain_model_item**
> NvetoGainModel get_nveto_gain_model_item(nvetogainmodel_id)

Retrieves a NvetoGainModel document

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
    api_instance = xepmts.NvetoGainModelApi(api_client)
    nvetogainmodel_id = 'nvetogainmodel_id_example' # str | 

    try:
        # Retrieves a NvetoGainModel document
        api_response = api_instance.get_nveto_gain_model_item(nvetogainmodel_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoGainModelApi->get_nveto_gain_model_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetogainmodel_id** | **str**|  | 

### Return type

[**NvetoGainModel**](NvetoGainModel.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NvetoGainModel document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nveto_gain_models**
> InlineResponse20017 get_nveto_gain_models(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more NvetoGainModels

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
    api_instance = xepmts.NvetoGainModelApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more NvetoGainModels
        api_response = api_instance.get_nveto_gain_models(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoGainModelApi->get_nveto_gain_models: %s\n" % e)
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

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of NvetoGainModels |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_nveto_gain_model_item**
> patch_nveto_gain_model_item(nvetogainmodel_id, nveto_gain_model, if_match=if_match)

Updates a NvetoGainModel document

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
    api_instance = xepmts.NvetoGainModelApi(api_client)
    nvetogainmodel_id = 'nvetogainmodel_id_example' # str | 
nveto_gain_model = xepmts.NvetoGainModel() # NvetoGainModel | A NvetoGainModel or list of NvetoGainModel documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Updates a NvetoGainModel document
        api_instance.patch_nveto_gain_model_item(nvetogainmodel_id, nveto_gain_model, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoGainModelApi->patch_nveto_gain_model_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetogainmodel_id** | **str**|  | 
 **nveto_gain_model** | [**NvetoGainModel**](NvetoGainModel.md)| A NvetoGainModel or list of NvetoGainModel documents | 
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
**200** | NvetoGainModel document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_nveto_gain_models**
> post_nveto_gain_models(nveto_gain_model)

Stores one or more NvetoGainModels.

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
    api_instance = xepmts.NvetoGainModelApi(api_client)
    nveto_gain_model = xepmts.NvetoGainModel() # NvetoGainModel | A NvetoGainModel or list of NvetoGainModel documents

    try:
        # Stores one or more NvetoGainModels.
        api_instance.post_nveto_gain_models(nveto_gain_model)
    except ApiException as e:
        print("Exception when calling NvetoGainModelApi->post_nveto_gain_models: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nveto_gain_model** | [**NvetoGainModel**](NvetoGainModel.md)| A NvetoGainModel or list of NvetoGainModel documents | 

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

# **put_nveto_gain_model_item**
> put_nveto_gain_model_item(nvetogainmodel_id, nveto_gain_model, if_match=if_match)

Replaces a NvetoGainModel document

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
    api_instance = xepmts.NvetoGainModelApi(api_client)
    nvetogainmodel_id = 'nvetogainmodel_id_example' # str | 
nveto_gain_model = xepmts.NvetoGainModel() # NvetoGainModel | A NvetoGainModel or list of NvetoGainModel documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a NvetoGainModel document
        api_instance.put_nveto_gain_model_item(nvetogainmodel_id, nveto_gain_model, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoGainModelApi->put_nveto_gain_model_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetogainmodel_id** | **str**|  | 
 **nveto_gain_model** | [**NvetoGainModel**](NvetoGainModel.md)| A NvetoGainModel or list of NvetoGainModel documents | 
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
**200** | NvetoGainModel document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

