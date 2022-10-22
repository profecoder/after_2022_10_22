from django.shortcuts import render

from my_app.models import Car

def cars(request):
    cars = Car.objects.all()

    context_dict = {"cars": cars}

    return render(
        request=request,
        context=context_dict,
        template_name="my_app/car_list.html",
    )
