# Cliente del servicio Pagos (equipo vecino) · Reto de integración
# Contrato del vecino: pagos.proto · Qué hace y con qué datos probar: servicios/pagos/README.md
# Antes de correrlo, el servidor del vecino debe estar corriendo (README.md, paso 5).
import grpc

import pagos_pb2
import pagos_pb2_grpc

canal = grpc.insecure_channel("localhost:50056")
stub = pagos_pb2_grpc.PagosStub(canal)

print("=== Parte 1 · ConsultarPago con un dato válido ===")
# TODO: arma la petición con un dato que funcione (tabla "Datos para probar" del README del vecino),
#       llama a stub.ConsultarPago(...) e imprime los campos de la respuesta.

print("=== Parte 2 · ConsultarPago con un dato que provoca error ===")
# TODO: llama con un dato que provoque error, dentro de try/except grpc.RpcError,
#       e imprime e.code() y e.details(). El programa NO debe tronar.

print("=== Parte 3 · SeguirCobro (streaming) ===")
# TODO: recorre stub.SeguirCobro(...) con for e imprime cada caja en cuanto llegue.
#       Ponlo también dentro de try/except por si el servidor regresa un error.
