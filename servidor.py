# Servidor del servicio Envíos · Reto de integración · Unidad II
# Contrato: envios.proto · Puerto: 50055
# Antes de correrlo: bash compilar.sh
import time
import grpc
from concurrent import futures
import envios_pb2
import envios_pb2_grpc

# Datos de ejemplo (no hace falta base de datos)
GUIAS = {
    "GUIA-500": [("Recibido", "Colima"), ("En bodega", "Colima"), ("En camino", "Manzanillo"), ("Entregado", "Manzanillo")],
    "GUIA-501": [("Recibido", "Colima"), ("En camino", "Guadalajara")],
}


class EnviosServicio(envios_pb2_grpc.EnviosServicer):

    def CotizarEnvio(self, request, context):
        cp = request.codigo_postal
        if len(cp) != 5 or not cp.isdigit() or request.peso_gramos <= 0:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT,
                          "Código postal de 5 dígitos y peso mayor a 0")
        costo = 9900 + (request.peso_gramos // 1000) * 2000
        dias = 1 if cp.startswith("28") else 3
        return envios_pb2.Cotizacion(costo_centavos=costo, dias=dias)

    def Rastrear(self, request, context):
        if request.guia not in GUIAS:
            context.abort(grpc.StatusCode.NOT_FOUND, f"La guía {request.guia} no existe")
        for estado, lugar in GUIAS[request.guia]:
            time.sleep(1)
            yield envios_pb2.EstadoEnvio(guia=request.guia, estado=estado, lugar=lugar)


servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
envios_pb2_grpc.add_EnviosServicer_to_server(EnviosServicio(), servidor)
servidor.add_insecure_port("[::]:50055")
servidor.start()
print("Servidor de Envíos escuchando en el puerto 50055...")
servidor.wait_for_termination()