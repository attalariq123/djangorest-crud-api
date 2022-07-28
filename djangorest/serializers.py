from rest_framework import serializers

from djangorest.models import Mahasiswa

class MahasiswaSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mahasiswa
        fields = ['id', 'nama', 'nim', 'jurusan', 'umur']