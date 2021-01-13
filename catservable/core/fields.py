from rest_framework import fields


class StringArrayField(fields.ListField):
    def to_representation(self, obj):
        obj = super().to_representation(obj)
        return ",".join([str(element) for element in obj])

    def to_internal_value(self, data):
        data = data.split(",")  # convert string to list
        return super().to_internal_value(data)
