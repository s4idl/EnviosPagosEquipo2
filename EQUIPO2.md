# Nuestro equipo

- **Nuestro servicio:** Envíos · puerto 50055 · contrato `envios.proto`
- **Servicio que consumimos (vecino):** Pagos · puerto 50056 · contrato `pagos.proto`
- **Repositorio del equipo vecino:** https://github.com/TheEdu28/reto-tienda

| Integrante | Matrícula | Rol |
| --- | --- | --- |
| Said Lopez Jr. | 20205276 | Servidor |
| Romina Fajardo | 20206423 | Cliente |
| Said Lopez Jr. y Romina Fajardo | 20205276 y 20206423 | Integración (README, issues y prueba cruzada) |

## Prueba cruzada

Corrimos `python cliente_vecino.py` contra el servidor **real** del equipo vecino (el que clonamos en `../vecino`) y esto fue lo que imprimió:

```
=== Parte 1 · ConsultarPago con un dato válido ===
Pedido: PED-100
Pagado: True
Monto: $13,298.00
=== Parte 2 · ConsultarPago con un dato que provoca error ===
Error: NOT_FOUND - Pedido no encontrado
=== Parte 3 · SeguirCobro (streaming) ===
Error: UNIMPLEMENTED - Method not implemented!
```

Las Partes 1 y 2 funcionaron. La Parte 3 falló por un error del servidor del vecino: en su `servidor.py`, la función `SeguirCobro` (línea 35) quedó sin indentación, fuera de la clase `PagosServicio`, y por eso el servidor responde `UNIMPLEMENTED`. Nuestro cliente recibe y atrapa el error con `try/except`, y el programa no truena. Lo reportamos en el issue enlazado abajo.

## Issues

Enlaces a los issues que abrimos en el repositorio del vecino o que nos abrieron a nosotros:

- (PEGAR AQUÍ EL ENLACE DEL ISSUE: https://github.com/TheEdu28/reto-tienda/issues/NÚMERO)

## Uso de IA (Acuerdo No. 23/2024 UdeC)

Sí usamos IA.

- **Herramienta:** Gemini AI.
- **Quién:** Said Lopez Jr.
- **Verificación:** revisamos el código línea por línea y lo probamos con los datos del README antes de subirlo. Cualquiera de los dos puede explicar cualquier parte.