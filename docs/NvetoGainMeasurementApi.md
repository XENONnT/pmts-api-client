# xepmts.NvetoGainMeasurementApi

All URIs are relative to *https://xenon-pmts.uc.r.appspot.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_nveto_gain_measurement_item**](NvetoGainMeasurementApi.md#delete_nveto_gain_measurement_item) | **DELETE** /nveto/gain_measurements/{nvetogainmeasurementId} | Deletes a NvetoGainMeasurement document
[**get_nveto_gain_measurement_item**](NvetoGainMeasurementApi.md#get_nveto_gain_measurement_item) | **GET** /nveto/gain_measurements/{nvetogainmeasurementId} | Retrieves a NvetoGainMeasurement document
[**get_nveto_gain_measurements**](NvetoGainMeasurementApi.md#get_nveto_gain_measurements) | **GET** /nveto/gain_measurements | Retrieves one or more NvetoGainMeasurements
[**patch_nveto_gain_measurement_item**](NvetoGainMeasurementApi.md#patch_nveto_gain_measurement_item) | **PATCH** /nveto/gain_measurements/{nvetogainmeasurementId} | Updates a NvetoGainMeasurement document
[**post_nveto_gain_measurements**](NvetoGainMeasurementApi.md#post_nveto_gain_measurements) | **POST** /nveto/gain_measurements | Stores one or more NvetoGainMeasurements.
[**put_nveto_gain_measurement_item**](NvetoGainMeasurementApi.md#put_nveto_gain_measurement_item) | **PUT** /nveto/gain_measurements/{nvetogainmeasurementId} | Replaces a NvetoGainMeasurement document


# **delete_nveto_gain_measurement_item**
> delete_nveto_gain_measurement_item(nvetogainmeasurement_id, if_match=if_match)

Deletes a NvetoGainMeasurement document

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
    api_instance = xepmts.NvetoGainMeasurementApi(api_client)
    nvetogainmeasurement_id = 'nvetogainmeasurement_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a NvetoGainMeasurement document
        api_instance.delete_nveto_gain_measurement_item(nvetogainmeasurement_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoGainMeasurementApi->delete_nveto_gain_measurement_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetogainmeasurement_id** | **str**|  | 
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
**204** | NvetoGainMeasurement document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nveto_gain_measurement_item**
> NvetoGainMeasurement get_nveto_gain_measurement_item(nvetogainmeasurement_id)

Retrieves a NvetoGainMeasurement document

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
    api_instance = xepmts.NvetoGainMeasurementApi(api_client)
    nvetogainmeasurement_id = 'nvetogainmeasurement_id_example' # str | 

    try:
        # Retrieves a NvetoGainMeasurement document
        api_response = api_instance.get_nveto_gain_measurement_item(nvetogainmeasurement_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoGainMeasurementApi->get_nveto_gain_measurement_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetogainmeasurement_id** | **str**|  | 

### Return type

[**NvetoGainMeasurement**](NvetoGainMeasurement.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NvetoGainMeasurement document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nveto_gain_measurements**
> InlineResponse20016 get_nveto_gain_measurements(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more NvetoGainMeasurements

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
    api_instance = xepmts.NvetoGainMeasurementApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more NvetoGainMeasurements
        api_response = api_instance.get_nveto_gain_measurements(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NvetoGainMeasurementApi->get_nveto_gain_measurements: %s\n" % e)
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

[**InlineResponse20016**](InlineResponse20016.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of NvetoGainMeasurements |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_nveto_gain_measurement_item**
> patch_nveto_gain_measurement_item(nvetogainmeasurement_id, nveto_gain_measurement, if_match=if_match)

Updates a NvetoGainMeasurement document

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
    api_instance = xepmts.NvetoGainMeasurementApi(api_client)
    nvetogainmeasurement_id = 'nvetogainmeasurement_id_example' # str | 
nveto_gain_measurement = xepmts.NvetoGainMeasurement() # NvetoGainMeasurement | A NvetoGainMeasurement or list of NvetoGainMeasurement documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Updates a NvetoGainMeasurement document
        api_instance.patch_nveto_gain_measurement_item(nvetogainmeasurement_id, nveto_gain_measurement, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoGainMeasurementApi->patch_nveto_gain_measurement_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetogainmeasurement_id** | **str**|  | 
 **nveto_gain_measurement** | [**NvetoGainMeasurement**](NvetoGainMeasurement.md)| A NvetoGainMeasurement or list of NvetoGainMeasurement documents | 
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
**200** | NvetoGainMeasurement document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_nveto_gain_measurements**
> post_nveto_gain_measurements(nveto_gain_measurement)

Stores one or more NvetoGainMeasurements.

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
    api_instance = xepmts.NvetoGainMeasurementApi(api_client)
    nveto_gain_measurement = xepmts.NvetoGainMeasurement() # NvetoGainMeasurement | A NvetoGainMeasurement or list of NvetoGainMeasurement documents

    try:
        # Stores one or more NvetoGainMeasurements.
        api_instance.post_nveto_gain_measurements(nveto_gain_measurement)
    except ApiException as e:
        print("Exception when calling NvetoGainMeasurementApi->post_nveto_gain_measurements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nveto_gain_measurement** | [**NvetoGainMeasurement**](NvetoGainMeasurement.md)| A NvetoGainMeasurement or list of NvetoGainMeasurement documents | 

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

# **put_nveto_gain_measurement_item**
> put_nveto_gain_measurement_item(nvetogainmeasurement_id, nveto_gain_measurement, if_match=if_match)

Replaces a NvetoGainMeasurement document

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
    api_instance = xepmts.NvetoGainMeasurementApi(api_client)
    nvetogainmeasurement_id = 'nvetogainmeasurement_id_example' # str | 
nveto_gain_measurement = xepmts.NvetoGainMeasurement() # NvetoGainMeasurement | A NvetoGainMeasurement or list of NvetoGainMeasurement documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a NvetoGainMeasurement document
        api_instance.put_nveto_gain_measurement_item(nvetogainmeasurement_id, nveto_gain_measurement, if_match=if_match)
    except ApiException as e:
        print("Exception when calling NvetoGainMeasurementApi->put_nveto_gain_measurement_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nvetogainmeasurement_id** | **str**|  | 
 **nveto_gain_measurement** | [**NvetoGainMeasurement**](NvetoGainMeasurement.md)| A NvetoGainMeasurement or list of NvetoGainMeasurement documents | 
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
**200** | NvetoGainMeasurement document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

