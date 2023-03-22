from rest_framework.serializers import ModelSerializer
from main.models import Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ('date_created', 'date_updated')


    def save(self, *args, **kwargs):
        if self.validated_data.get('status') == '1':
            self.validated_data['status'] = 'Active'
        else:
            self.validated_data['status'] = 'InActive'
        return super(ProductSerializer, self).save(*args, **kwargs)
