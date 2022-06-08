from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from clientes.models import Clientes
from clientes.api.serializers import ClientesSerializer

class ClientesView(APIView):

#----------OBTENER TODOS LOS REGISTROS DE LA BASE DE DATOS------------------------
    def get(self, request):
        clientes =  Clientes.objects.all()
        serializer = ClientesSerializer(clientes, many=True)
        return Response(serializer.data)

#----------AGREGAR UN NUEVO REGISTRO A LA BASE DE DATOS------------------------
    def post(self, request):
        serializer = ClientesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.data)



class ClientesDetalle(APIView):

#----------OBTENER UN REGISTRO EN ESPECÍFICO DE LA BASE DE DATOS------------------------
    def get(self, request, id):
        try:
            clientes = Clientes.objects.get(pk=id)
        except Clientes.DoesNotExist:
            # SI PONEMOS UN "id" QUE NO EXISTE
            return Response({'Error': 'El Cliente no existe'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ClientesSerializer(clientes)
        return Response(serializer.data)


#----------EDITAR UN REGISTRO EN LA BASE DE DATOS------------------------
    def put(self, request, id):
        try:
            clientes = Clientes.objects.get(pk=id)
        except Clientes.DoesNotExist:
            # SI PONEMOS UN "id" QUE NO EXISTE
            return Response({'Error': 'El Cliente no existe'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ClientesSerializer(clientes, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            # SI ENVÍAMOS DATOS QUE NO SON VÁLIDOS
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#----------ELIMINAR UN REGISTRO DE LA BASE DE DATOS------------------------
    def delete(self, request, id):
            try:
                clientes = Clientes.objects.get(pk=id)
            except Clientes.DoesNotExist:
                # SI PONEMOS UN "id" QUE NO EXISTE
                return Response({'Error': 'El cliente no existe'}, status=status.HTTP_404_NOT_FOUND)
            clientes.delete()
            # CONFIRMAMOS QUE LA OPERACIÓN SE REALIZÓ, PERO NO HAY NADA QUE MOSTRAR
            return Response(status=status.HTTP_204_NO_CONTENT)