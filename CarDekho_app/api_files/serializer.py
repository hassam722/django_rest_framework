from ..models import CarList,ShowRoomList,Reviews
from rest_framework import serializers

class CarListSerializer(serializers.ModelSerializer):
    Car_Review = serializers.StringRelatedField(many =True,read_only = True)
    discounted_price = serializers.SerializerMethodField()
    class Meta:
        model = CarList
        fields = '__all__'
    
    def get_discounted_price(self, obj):
        return obj.price - 5000


class ShowRoomListSerializer(serializers.ModelSerializer):
    # Showrooms = CarListSerializer(many = True)
    # Showrooms = serializers.StringRelatedField(many = True)
    # Showrooms = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    Showrooms =serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='car_detail_view'
    )
    class Meta:
        model = ShowRoomList
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    apiuser = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Reviews
        fields = '__all__'

        