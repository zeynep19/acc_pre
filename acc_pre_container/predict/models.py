from django.db import models


class PredResults(models.Model):

    Hat_Kodu = models.FloatField()
    Gun = models.FloatField()
    Saat = models.FloatField()
    Konum_Bilgisi = models.FloatField()
    Personel_Sicili = models.FloatField()
    Surucu_Performans_Puani = models.FloatField()
    Target = models.CharField(max_length=30)

    def __str__(self):
        return self.Target