from django.shortcuts import render
import requests
from django.http import JsonResponse

FACTURAS_SERVICE_URL = "http://<IP_DE_TU_OTRO_MICROSERVICIO>:<PUERTO>/facturas_por_fecha/"

def generar_reporte(request):
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')

    if not fecha_inicio or not fecha_fin:
        return JsonResponse({'error': 'Debe proporcionar fecha_inicio y fecha_fin'}, status=400)

    try:
        # Consumir el microservicio de facturas
        response = requests.get(FACTURAS_SERVICE_URL, params={
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin
        })

        if response.status_code != 200:
            return JsonResponse({'error': 'Error al obtener facturas desde el servicio de facturación'}, status=response.status_code)

        facturas = response.json().get('facturas', [])

        # Generar el reporte
        reporte = {
            'reporte_generado': True,
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin,
            'total_facturas': len(facturas),
            'facturas': facturas
        }

        return JsonResponse(reporte, status=200)

    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': f'Error al conectar con el servicio de facturación: {str(e)}'}, status=500)

    except Exception as e:
        return JsonResponse({'error': f'Error interno: {str(e)}'}, status=500)

