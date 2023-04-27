from . import models
from .models import company



class CompanyResource(resources.ModelResource):

    class Meta:
        model = company