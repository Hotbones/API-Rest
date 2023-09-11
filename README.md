# API REST con Python y Django

![video API Rest](https://github.com/Hotbones/API-Rest/assets/105388226/b5079c09-db0a-4738-9601-3a9f66bbe140)


Esta es una API REST desarrollada con Python y el framework Django, que permite a los desarrolladores crear y consumir servicios web de manera eficiente y escalable. Las API REST son ideales para la comunicación entre aplicaciones y se basan en los principios del estilo arquitectónico REST (Representational State Transfer).

## Características de la API

- **Endpoints:** La API proporciona una serie de endpoints (URLs) que representan diferentes recursos o funcionalidades. Por ejemplo, `/api/usuarios` podría ser un endpoint para obtener información sobre usuarios.

- **Métodos HTTP:** Se utilizan métodos HTTP estándar como GET, POST, PUT y DELETE para interactuar con los recursos. Por ejemplo, GET se utiliza para recuperar datos, POST para crear nuevos registros y PUT para actualizar registros existentes.

- **Autenticación:** La API puede incluir autenticación para garantizar que solo usuarios autorizados puedan acceder a ciertos recursos. Esto puede hacerse mediante tokens de acceso, autenticación basada en sesiones o incluso autenticación de terceros como OAuth.

- **Serialización de Datos:** La API utiliza la serialización de datos para convertir objetos de Python en formatos de datos estándar como JSON o XML, y viceversa.

- **Validación de Datos:** Los datos enviados a través de la API se validan para garantizar que cumplan con los requisitos y restricciones necesarios antes de procesarlos.

## Uso de la API

Para utilizar la API, los desarrolladores pueden realizar solicitudes HTTP a los endpoints proporcionados, siguiendo las convenciones y restricciones definidas en la documentación de la API. Por ejemplo, para obtener una lista de usuarios, se podría realizar una solicitud GET a `/api/usuarios`.

## Ejemplo de Código

A continuación se muestra un ejemplo simplificado de cómo podría definirse un endpoint de usuarios en una API Django:

```python
from rest_framework import serializers, viewsets, routers

# Definición del modelo de Usuario
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

# Serializador para el modelo Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

# Vista de conjunto para los usuarios
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Configuración de rutas de la API
router = routers.DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)

# URL de la API
urlpatterns = [
    path('api/', include(router.urls)),
]



