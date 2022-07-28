from django.db import models

class Mahasiswa(models.Model):
    nama = models.CharField(max_length=64)
    nim = models.IntegerField()
    jurusan = models.CharField(max_length=64)
    umur = models.IntegerField()

    def __str__(self):
        return self.nama + ' ' + str(self.nim)