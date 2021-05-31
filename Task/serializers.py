from rest_framework import serializers
from Task.models import *
from lib.Log import RecodeLog
from django.contrib.contenttypes.models import ContentType
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

    def validate(self, validated_data):
        """
        :param validated_data:
        :return:
        """
        exec_list = validated_data.pop('exec_list')
        format_list = []
        for data in exec_list:
            object_id = data.get('object_id')
            tmp_model = data.get('content_type').model_class()
            data['content_type'] = data.get('content_type').id
            data['content_object'] = tmp_model.objects.get(id=object_id)
            format_list.append(data)

        data = ExecListSerializers(data=format_list, many=True)
        if not data.is_valid():
            raise serializers.ValidationError('exec_list 字段校验失败！')
        validated_data['exec_list'] = data.save()
        return validated_data

    def update(self, instance, validated_data):
        """
        :param instance:
        :param validated_data:
        :return:
        """
        print(instance)
        print(validated_data)

    def create(self, validated_data):
        """
        :param validated_data:
        :return:
        """
        print("11111111111111111")
        print(validated_data)
        exec_list = validated_data.pop('exec_list')
        obj = SubTask.objects.create(**validated_data)
        obj.save()
        for exe in exec_list:
            obj.exec_list.add(exe)
        return obj


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
