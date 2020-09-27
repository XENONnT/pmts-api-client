# xepmts.MuvetoInstallApi

All URIs are relative to *https://api-dot-xenon-pmts.uc.r.appspot.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_muveto_install_item**](MuvetoInstallApi.md#delete_muveto_install_item) | **DELETE** /muveto/installs/{muvetoinstallId} | Deletes a MuvetoInstall document
[**get_muveto_install_item**](MuvetoInstallApi.md#get_muveto_install_item) | **GET** /muveto/installs/{muvetoinstallId} | Retrieves a MuvetoInstall document
[**get_muveto_install_item_by_uid**](MuvetoInstallApi.md#get_muveto_install_item_by_uid) | **GET** /muveto/installs/{Uid} | Retrieves a MuvetoInstall document by uid
[**get_muveto_installs**](MuvetoInstallApi.md#get_muveto_installs) | **GET** /muveto/installs | Retrieves one or more MuvetoInstalls
[**patch_muveto_install_item**](MuvetoInstallApi.md#patch_muveto_install_item) | **PATCH** /muveto/installs/{muvetoinstallId} | Updates a MuvetoInstall document
[**post_muveto_installs**](MuvetoInstallApi.md#post_muveto_installs) | **POST** /muveto/installs | Stores one or more MuvetoInstalls.
[**put_muveto_install_item**](MuvetoInstallApi.md#put_muveto_install_item) | **PUT** /muveto/installs/{muvetoinstallId} | Replaces a MuvetoInstall document


# **delete_muveto_install_item**
> delete_muveto_install_item(muvetoinstall_id, if_match=if_match)

Deletes a MuvetoInstall document

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
    api_instance = xepmts.MuvetoInstallApi(api_client)
    muvetoinstall_id = 'muvetoinstall_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Deletes a MuvetoInstall document
        api_instance.delete_muveto_install_item(muvetoinstall_id, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoInstallApi->delete_muveto_install_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetoinstall_id** | **str**|  | 
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
**204** | MuvetoInstall document deleted successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_install_item**
> MuvetoInstall get_muveto_install_item(muvetoinstall_id)

Retrieves a MuvetoInstall document

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
    api_instance = xepmts.MuvetoInstallApi(api_client)
    muvetoinstall_id = 'muvetoinstall_id_example' # str | 

    try:
        # Retrieves a MuvetoInstall document
        api_response = api_instance.get_muveto_install_item(muvetoinstall_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoInstallApi->get_muveto_install_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetoinstall_id** | **str**|  | 

### Return type

[**MuvetoInstall**](MuvetoInstall.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoInstall document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_install_item_by_uid**
> MuvetoInstall get_muveto_install_item_by_uid(uid)

Retrieves a MuvetoInstall document by uid

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
    api_instance = xepmts.MuvetoInstallApi(api_client)
    uid = 'uid_example' # str | 

    try:
        # Retrieves a MuvetoInstall document by uid
        api_response = api_instance.get_muveto_install_item_by_uid(uid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoInstallApi->get_muveto_install_item_by_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**MuvetoInstall**](MuvetoInstall.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MuvetoInstall document fetched successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_muveto_installs**
> InlineResponse20032 get_muveto_installs(where=where, projection=projection, sort=sort, page=page, max_results=max_results)

Retrieves one or more MuvetoInstalls

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
    api_instance = xepmts.MuvetoInstallApi(api_client)
    where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
projection = 'projection_example' # str | the projections query parameter (ex.: {\"name\": 1}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 1 # int | the pages query parameter (optional)
max_results = 25 # int | the max results query parameter (optional)

    try:
        # Retrieves one or more MuvetoInstalls
        api_response = api_instance.get_muveto_installs(where=where, projection=projection, sort=sort, page=page, max_results=max_results)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MuvetoInstallApi->get_muveto_installs: %s\n" % e)
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

[**InlineResponse20032**](InlineResponse20032.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | An array of MuvetoInstalls |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_muveto_install_item**
> patch_muveto_install_item(muvetoinstall_id, muveto_install, if_match=if_match)

Updates a MuvetoInstall document

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
    api_instance = xepmts.MuvetoInstallApi(api_client)
    muvetoinstall_id = 'muvetoinstall_id_example' # str | 
muveto_install = xepmts.MuvetoInstall() # MuvetoInstall | A MuvetoInstall or list of MuvetoInstall documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Updates a MuvetoInstall document
        api_instance.patch_muveto_install_item(muvetoinstall_id, muveto_install, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoInstallApi->patch_muveto_install_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetoinstall_id** | **str**|  | 
 **muveto_install** | [**MuvetoInstall**](MuvetoInstall.md)| A MuvetoInstall or list of MuvetoInstall documents | 
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
**200** | MuvetoInstall document updated successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_muveto_installs**
> post_muveto_installs(muveto_install)

Stores one or more MuvetoInstalls.

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
    api_instance = xepmts.MuvetoInstallApi(api_client)
    muveto_install = xepmts.MuvetoInstall() # MuvetoInstall | A MuvetoInstall or list of MuvetoInstall documents

    try:
        # Stores one or more MuvetoInstalls.
        api_instance.post_muveto_installs(muveto_install)
    except ApiException as e:
        print("Exception when calling MuvetoInstallApi->post_muveto_installs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muveto_install** | [**MuvetoInstall**](MuvetoInstall.md)| A MuvetoInstall or list of MuvetoInstall documents | 

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

# **put_muveto_install_item**
> put_muveto_install_item(muvetoinstall_id, muveto_install, if_match=if_match)

Replaces a MuvetoInstall document

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
    api_instance = xepmts.MuvetoInstallApi(api_client)
    muvetoinstall_id = 'muvetoinstall_id_example' # str | 
muveto_install = xepmts.MuvetoInstall() # MuvetoInstall | A MuvetoInstall or list of MuvetoInstall documents
if_match = 'if_match_example' # str | Current value of the _etag field (optional)

    try:
        # Replaces a MuvetoInstall document
        api_instance.put_muveto_install_item(muvetoinstall_id, muveto_install, if_match=if_match)
    except ApiException as e:
        print("Exception when calling MuvetoInstallApi->put_muveto_install_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **muvetoinstall_id** | **str**|  | 
 **muveto_install** | [**MuvetoInstall**](MuvetoInstall.md)| A MuvetoInstall or list of MuvetoInstall documents | 
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
**200** | MuvetoInstall document replaced successfully |  -  |
**0** | An error message |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

