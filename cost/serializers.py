from rest_framework import serializers

from . import models


class changeorderSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.changeorder
        fields = [
            "backup",
            "total_labor",
            "last_updated",
            "created",
            "status",
            "exclusion_assumption",
            "total_material",
            "total_equipment",
            "change_amt",
            "work_scope",
        ]

class ticketSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ticket
        fields = [
            "total_cost",
            "work_start",
            "status",
            "work_shifts",
            "created",
            "total_material",
            "work_end",
            "co_type",
            "last_updated",
            "total_labor",
            "co_reason",
        ]

class contractsSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.contracts
        fields = [
            "contract_description",
            "attachment",
            "contract_file",
            "created",
            "last_updated",
            "scheduleofvalues",
            "contract_type",
            "exclusion_assumption",
        ]

class requisitionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.requisition
        fields = [
            "created",
            "last_updated",
            "req_number",
            "req_amount",
            "coi",
            "stored_materials",
            "prev_amount",
            "lienwaiver",
        ]

class budgetSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.budget
        fields = [
            "line_code",
            "line_amount",
            "last_updated",
            "created",
            "line_description",
        ]
