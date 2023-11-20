from my_app.models import MainDetails

def data_sender(request):
    main_detail = MainDetails.objects.first()
    return {"main_detail": main_detail,}
    