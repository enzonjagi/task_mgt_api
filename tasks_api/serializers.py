from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.ModelSerializer):
    """Enables the API to read data easily"""

    class Meta:
        model = Data
        fields = ('task_name', 'task_description', "timestamp", "updated", "completed")