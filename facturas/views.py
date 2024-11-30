import datetime
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from . models import Facturas

# Create your views here.

def obtener_facturas(request):
    facturas = Facturas.objects.all()
    datos = [
        {
            'id': factura.id,
            'estudiante': factura.estudiante,
            'institucion_asociada': factura.institucion_asociada,
            'responsable_economico': factura.responsable_economico,
            'fecha_limite_pago': factura.fecha_limite_pago,
            'fecha_inicial': factura.fecha_inicial,
            'valor': factura.valor,
        }
        for factura in facturas
    ]
    return JsonResponse({'facturas': datos})

def facturas_por_fecha(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    try:
        if not fecha_inicio or not fecha_fin:
            return JsonResponse({'error': 'Debe proporcionar fecha_inicio y fecha_fin'}, status=400)

        fecha_inicio = datetime.datetime.strptime(fecha_inicio, '%Y-%m-%d').date()
        fecha_fin = datetime.datetime.strptime(fecha_fin, '%Y-%m-%d').date()

        facturas = Facturas.objects.filter(
                fecha_inicial__range=(fecha_inicio, fecha_fin)
            )


        datos = [
            {
                'id': factura.id,
                'estudiante': factura.estudiante,
                'institucion_asociada': factura.institucion_asociada,
                'responsable_economico': factura.responsable_economico,
                'fecha_limite_pago': factura.fecha_limite_pago,
                'fecha_inicial': factura.fecha_inicial,
                'valor': factura.valor,
            }
            for factura in facturas
        ]

        return JsonResponse({'facturas': datos}, status=200)

    except ValueError:
        return JsonResponse({'error': 'Formato de fecha inválido. Use YYYY-MM-DD'}, status=400)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)