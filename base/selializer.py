from rest_framework import serializers
from home.models import HomePage

class HomePageSerializers(serializers.ModelSerializer):
    class Meta:
        model = HomePage
        # fields = ('published_date', 'hero_text', 'hero_cta', 'body')
        fields = '__all__'
