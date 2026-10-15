# Cliente del servicio Pagos (equipo vecino) · Reto de integración
import grpc
import pagos_pb2
import pagos_pb2_grpc

canal = grpc.insecure_channel("localhost:50056")
stub = pagos_pb2_grpc.PagosStub(canal)

print("=== Parte 1 · ConsultarPago con un dato válido ===")
respuesta = stub.ConsultarPago(pagos_pb2.PedidoRequest(pedido="PED-100"))
print("Pedido:", respuesta.pedido)
print("Pagado:", respuesta.pagado)
print(f"Monto: ${respuesta.monto_centavos / 100:,.2f}")

print("=== Parte 2 · ConsultarPago con un dato que provoca error ===")
try:
    stub.ConsultarPago(pagos_pb2.PedidoRequest(pedido="PED-999"))
except grpc.RpcError as e:
    print("Error:", e.code().name, "-", e.details())

print("=== Parte 3 · SeguirCobro (streaming) ===")
try:
    for paso in stub.SeguirCobro(pagos_pb2.CobroRequest(pedido="PED-101", monto_centavos=89900)):
        print(f"Paso {paso.numero}: {paso.paso}")
except grpc.RpcError as e:
    print("Error:", e.code().name, "-", e.details())