from rest_framework.serializers import ModelSerializer, Serializer, ValidationError
from .models import District, DistrictStaff, Subcounty, SubcountyStaff

class DistrictListSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = ("id", "district_name", "district_region", "district_size_hectares")

class DistrictCreateSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = ("district_name", "district_region", "district_size_hectares")

    def validate_district_name(self, value):
        if not isinstance(value, str):
            raise ValidationError('District nameshould be of type string')
        return value

class DistrictStaffListSerializer(ModelSerializer):
    district_related = DistrictListSerializer(read_only=True)

    class Meta:
        model = DistrictStaff
        fields = ("id", "user_related", "district_related", "staff_role", "staff_contact", "active", "date_created")

class DistrictStaffCreateSerializer(ModelSerializer):
    class Meta:
        model = DistrictStaff
        fields = ("user_related", "district_related", "staff_role", "staff_contact")


