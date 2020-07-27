import json
from datetime import datetime as dt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.http import require_http_methods
from ..models import Parts
from django.utils import timezone

# Create your views here.





def allow_all(self):
    return True

@user_passes_test(allow_all)
@csrf_exempt
@require_http_methods(["POST","GET"])
def estimate_cycle_cost(request):
    response = {}
    final_price = 0.0
    try:
        if request.method == 'GET':
            record = Parts.objects.all()
            record_list = []
            for each_record in record:
                data_json = {
                    "name":each_record.Parts_name,
                    "price": each_record.Parts_price,
                    "description":each_record.Parts_description,
                    "stardata":str(each_record.start_date),
                    "enddate":str(each_record.end_date)
                }
                record_list.append(data_json)
            return JsonResponse(record_list,safe=False)
        if request.method == 'POST':
            received_json_data = json.loads(request.body)
            for item in received_json_data:
                product = item.get('product', None)
                count = item.get('count', 1)
                if product:
                    record = Parts.objects.filter(Parts_name=product).filter(end_date__gte=dt.now(tz=timezone.utc),
                                                                    start_date__lte=dt.now(tz=timezone.utc)).first()
                    if record:
                        price = record.price
                        final_price += (float(price) * count)
                    else:
                        response['error']='product [{}] not found'.format(product)
                        response['status']= 400

                        return JsonResponse(response)
            response['final_price'] = final_price
            response['status'] = 200
            return JsonResponse(response)
    except Exception as e:
        response['error'] = "Exception [{}] occurred".format(e)
        response['status'] = 500
        return JsonResponse(response)
