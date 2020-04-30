from django.db import models
class alternatif(models.Model):
    kodealternatif = models.CharField(max_length=3, primary_key=True)
    namaalternatif = models.CharField(max_length=25)
    c1 = models.FloatField()
    c2 = models.FloatField()
    angka= (
        (1, 'KURANG MENDUKUNG'),
        (2, 'CUKUP MENDUKUNG'),
        (3, 'SANGAT MENDUKUNG'),
    )
    c3 = models.FloatField(choices=angka, default=1)
    prio = (
        (1, 'SANGAT PRIORITAS'),
        (2, 'PRIORITAS'),
        (3, 'KURANG PRIORITAS'),
    )
    c4 = models.FloatField(choices=prio, default=1)
    oleh = (
        (1, 'SULIT DIPEROLEH'),
        (2, 'SEDIKIT MUDAH DIPEROLEH'),
        (3, 'SANGAT MUDAH DIPEROLEH'),
    )
    c5 = models.FloatField(choices=oleh, default=1)

    def __str__(self):
        return "{}". format(self.kodealternatif)
class normalisasi(models.Model):
    kodealternatif = models.CharField(max_length=3)
    c1norm = models.IntegerField()
    c2norm = models.IntegerField()
    c3norm = models.IntegerField()
    c4norm = models.IntegerField()
    c5norm = models.IntegerField()
    def __str__(self):
        return "{}". format(self.kodealternatif)