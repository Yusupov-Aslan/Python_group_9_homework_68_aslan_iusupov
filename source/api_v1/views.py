from datetime import datetime
import json
from django.http import JsonResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt


def validate_nums(data):
    a = data.get("A")
    b = data.get("B")
    if a is not None and b is not None and isinstance(a, int) and isinstance(b, int):
        return True
    return False


@csrf_exempt
def add(request, *args, **kwargs):
    if request.method != "POST":
        return HttpResponseNotAllowed(permitted_methods=["POST"])
    if request.body:
        nums = json.loads(request.body)
        if not validate_nums(nums):
            print(validate_nums(nums))
            return HttpResponseBadRequest("Данные не являются числами!")
        response = {'answer': nums['A'] + nums['B']}
        return JsonResponse(response)


@csrf_exempt
def subtract(request, *args, **kwargs):
    if request.method != "POST":
        return HttpResponseNotAllowed(permitted_methods=["POST"])
    if request.body:
        nums = json.loads(request.body)
        if not validate_nums(nums):
            return HttpResponseBadRequest("Данные не являются числами!")
        response = {'answer': nums['A'] - nums['B']}
        return JsonResponse(response)


@csrf_exempt
def multiply(request, *args, **kwargs):
    if request.method != "POST":
        return HttpResponseNotAllowed(permitted_methods=["POST"])
    if request.body:
        nums = json.loads(request.body)
        if not validate_nums(nums):
            return HttpResponseBadRequest("Данные не являются числами!")
        response = {'answer': nums['A'] * nums['B']}
        return JsonResponse(response)


@csrf_exempt
def divide(request, *args, **kwargs):
    if request.method != "POST":
        return HttpResponseNotAllowed(permitted_methods=["POST"])
    if request.body:
        nums = json.loads(request.body)
        if not validate_nums(nums):
            response = {"error": "Данные не являются числами!"}
            return HttpResponseBadRequest(json.dumps(response))
        if nums.get("B") == 0:
            response = {"error": "Division by zero!"}
            return HttpResponseBadRequest(json.dumps(response))
        response = {'answer': nums['A'] / nums['B']}
        return JsonResponse(response)
