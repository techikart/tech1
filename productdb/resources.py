from import_export import resources
from .models import product_details

class productResource(resources.ModelResource):
    class meta:
        model = product_details