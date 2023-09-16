from rest_framework import serializers
from .models import Profile, Project, CertifyingInstitution, Certificate


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = CertificateSerializer(
        many=True, required=False
    )  # Permitir que seja nulo

    class Meta:
        model = CertifyingInstitution
        fields = "__all__"

    def create(self, validated_data):
        certificates_data = validated_data.pop(
            "certificates", []
        )  # Tratar como uma lista vazia se não for fornecido
        certifying_institution = CertifyingInstitution.objects.create(
            **validated_data
        )
        for certificate_data in certificates_data:
            Certificate.objects.create(
                certifying_institution=certifying_institution,
                **certificate_data,
            )
        return certifying_institution
