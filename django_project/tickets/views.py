from django.http import JsonResponse
from .ml_model import predict_category
from .models import Ticket

from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def classify_ticket(request):

    data = json.loads(request.body)

    text = data["text"]

    category = predict_category(text)

    Ticket.objects.create(
        text=text,
        predicted_category=category
    )

    return JsonResponse({"category": category})