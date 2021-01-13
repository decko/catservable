from tapioca import JSONAdapterMixin, TapiocaAdapter, generate_wrapper_from_adapter

from .resource_maps import RESOURCE_MAPPING


class CatAPIAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = "https://api.thecatapi.com/v1"
    resource_mapping = RESOURCE_MAPPING


CatAPI = generate_wrapper_from_adapter(CatAPIAdapter)
