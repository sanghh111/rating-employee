from rest_framework import serializers


#nang cap thang hieu len
class BasicSerializer(serializers.Serializer):
    def create(self,object, validated_data):
        pass


    def update(self, object, instance, validated_data):
        pass