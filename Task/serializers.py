from rest_framework import serializers
from Task.models import *
from lib.Log import RecodeLog
from Task import models


class AuthKEYSerializers(serializers.ModelSerializer):
    class Meta:
        model = AuthKEY
        fields = ("__all__")


class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ("__all__")


class TemplateDBSerializers(serializers.ModelSerializer):
    class Meta:
        model = TemplateDB
        fields = ("__all__")


class TemplateNacosSerializers(serializers.ModelSerializer):
    class Meta:
        model = TemplateNacos
        fields = ("__all__")


class TemplateTencentServiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = TemplateTencentService
        fields = ("__all__")


class TemplateKubernetesSerializers(serializers.ModelSerializer):
    class Meta:
        model = TemplateKubernetes
        fields = ("__all__")


class ExecListSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExecList
        fields = ("__all__")


class SubTaskserializers(serializers.ModelSerializer):
    exec_list = ExecListSerializers(many=True)

    class Meta:
        model = SubTask
        fields = ("__all__")

    def validation(self, validated_data):
        """
        :param validated_data:
        :return:
        """
        print(11111111111111111)
        print(validated_data)

    def validate(self, validated_data):
        """
        :param validated_data:
        :return:
        """
        exec_list = validated_data.pop('exec_list')
        format_list = []
        for data in exec_list:
            print(data)
            content_type = data.pop('content_type')
            object_id = data.pop('object_id')
            tmp_model = getattr(models, content_type)
            data['content_object'] = tmp_model.object.get(id=object_id)
            format_list.append(data)

        data = ExecListSerializers(data=format_list, many=True)
        if not data.is_valid():
            print(data.errors)
            raise serializers.ValidationError('exec_list 字段校验失败！')
        data.save()
        validated_data['exec_list'] = data
        return validated_data


class ExecListLogSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExecList
        fields = ("__all__")


class ProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("__all__")


__all__ = [
    'TaskSerializers',
    'SubTaskserializers',
    'AuthKEYSerializers',
    'TemplateDBSerializers',
    'TemplateKubernetesSerializers',
    'ExecListLogSerializers',
    'ExecListSerializers',
    'ProjectSerializers',
    'TemplateNacosSerializers',
    'TemplateTencentServiceSerializers'
]
