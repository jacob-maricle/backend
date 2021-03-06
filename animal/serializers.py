from rest_framework import serializers
from .models import Tracker, Point, TrackerStatus, LocationMethod


class TrackerSerializer(serializers.ModelSerializer):
    points = serializers.SerializerMethodField()

    class Meta:
        model = Tracker
        fields = (
            "id",
            "animal_id",
            "status",
            "max_error_radius",
            "location_method",
            "points",
        )
        read_only_fields = ("id",)

    def get_points(self, obj):
        point = Point.objects.filter(tracker=obj)
        return PointSerializer(point, many=True).data


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = (
            "id",
            "tracker",
            "timestamp",
            "geo_lat",
            "geo_long",
            "geo_error_radius",
            "geo_method",
        )
        read_only_fields = (
            "id",
            "tracker",
            "timestamp",
            "geo_lat",
            "geo_long",
            "geo_error_radius",
            "geo_method",
        )


class PointCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = (
            "id",
            "tracker",
            "timestamp",
            "geo_lat",
            "geo_long",
            "geo_error_radius",
            "geo_method",
        )
        read_only_fields = ("id",)
