from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
from .models import PredResults

def predict(request):
    return render(request, 'predict.html')
    
def predict_chances(request):

    if request.POST.get('action') == 'post':

        # Receive data from client
        Hat_Kodu = int(request.POST.get('Hat_Kodu'))
        Gun = int(request.POST.get('Gun'))
        Saat = int(request.POST.get('Saat'))
        Arac_Kimligi = int(request.POST.get('Arac_Kimligi'))
        Konum_Bilgisi = int(request.POST.get('Konum_Bilgisi'))
        Personel_Sicili = int(request.POST.get('Personel_Sicili'))
        Surucu_Performans_Puani = float(request.POST.get('Surucu_Performans_Puani'))

    
        # Unpickle model
        mlpc_model = pd.read_pickle("mlpc_model.pickle")
        # Make prediction
        result = mlpc_model.predict([[Hat_Kodu, Gun, Saat, Arac_Kimligi, Konum_Bilgisi, Personel_Sicili, Surucu_Performans_Puani]])

        Target = result[0]

        PredResults.objects.create(Hat_Kodu=Hat_Kodu, Gun=Gun, Saat=Saat, Arac_Kimligi=Arac_Kimligi, 
                                    Konum_Bilgisi=Konum_Bilgisi, Personel_Sicili=Personel_Sicili, 
                                    Surucu_Performans_Puani=Surucu_Performans_Puani, Target=Target)

        return JsonResponse({'result': Target, 'Hat_Kodu': Hat_Kodu, 'Gun': Gun, 'Saat': Saat, 'Arac_Kimligi': Arac_Kimligi,
                             'Konum_Bilgisi': Konum_Bilgisi, 'Personel_Sicili': Personel_Sicili, 'Surucu_Performans_Puani': Surucu_Performans_Puani},
                            safe=False)


def view_results(request):
    # Submit prediction and show all
    data = {"dataset": PredResults.objects.all()}
    return render(request, "results.html", data)