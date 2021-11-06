from rest_framework import serializers
from .models import Student, Path

# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     number = serializers.IntegerField(required=False)

class PathSerializer(serializers.Serializer):
    class Meta:
        model = Path
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    path = serializers.StringRelatedField()
    path_id = serializers.IntegerField()
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'number', 'id', 'path', 'path_id')
        # fields = '__all__'
        # exclude = ('number') bu hariç hepsi demek