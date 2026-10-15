# Servidor del servicio Pagos · Reto de integración · Unidad II
# Contrato: pagos.proto · Puerto: 50056
# Antes de correrlo: bash compilar.sh
import time
import grpc
from concurrent import futures
import pagos_pb2
import pagos_pb2_grpc

PEDIDOS = {
    "PED-100": (True, 1329800),
    "PED-101": (False, 89900),
}
PASOS = ["Validando datos", "Autorizando con el banco", "Cobro aprobado"]


class PagosServicio(pagos_pb2_grpc.PagosServicer):

    def ConsultarPago(self, request, context):
        if request.pedido not in PEDIDOS:
            context.abort(grpc.StatusCode.NOT_FOUND, f"El pedido {request.pedido} no existe")
        pagado, monto = PEDIDOS[request.pedido]
        return pagos_pb2.EstadoPago(pedido=request.pedido, pagado=pagado, monto_centavos=monto)

    def SeguirCobro(self, request, context):
        if request.monto_centavos <= 0:
            context.abort(grpc.StatusCode.INVALID_ARGUMENT, "El monto debe ser mayor a 0")
        for numero, paso in enumerate(PASOS, start=1):
            time.sleep(1)
            yield pagos_pb2.PasoCobro(numero=numero, paso=paso)


servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
pagos_pb2_grpc.add_PagosServicer_to_server(PagosServicio(), servidor)
servidor.add_insecure_port("[::]:50056")
servidor.start()
print("Servidor de Pagos escuchando en el puerto 50056...")
servidor.wait_for_termination()