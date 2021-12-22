from rest_framework import serializers

from . import models


class companySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.company
        fields = [
            "created",
            "company_address",
            "last_updated",
            "company_name",
            "company_phone",
        ]

class projectsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.projects
        fields = [
            "created",
            "project_name",
            "last_updated",
        ]

class reportsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.reports
        fields = [
            "created",
            "last_updated",
        ]

class laborratesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.laborrates
        fields = [
            "last_updated",
            "labor_cost",
            "labor_affiliation",
            "labor_name",
            "created",
        ]

class materialratesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.materialrates
        fields = [
            "created",
            "material_name",
            "last_updated",
            "material_cost",
        ]

class equipmentratesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.equipmentrates
        fields = [
            "last_updated",
            "created",
            "equipment_cost",
            "equipment_name",
        ]

class divisionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.divisions
        fields = [
            "division_code",
            "created",
            "last_updated",
            "division_name",
        ]
