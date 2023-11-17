from my_app.models import MainDetails


def data_sender(request):
    main_details = MainDetails.objects.first()
    return {"main_details": main_details, }
