from rest_framework import serializers, viewsets
from .models import contactos, categorias, enderecos, nota

# ------------------- Serializers -------------------

class enderecosSerializer(serializers.ModelSerializer):
    contacto = serializers.PrimaryKeyRelatedField(queryset=contactos.objects.all())

    class Meta:
        model = enderecos
        fields = ['id', 'rua', 'cidade', 'pais', 'contacto']


class contactosSerializer(serializers.ModelSerializer):
    categoria_nome = serializers.CharField(
        source='categoria.nome',
        read_only=True
    )
    endereco = enderecosSerializer(source='enderecos', read_only=True)  

    class Meta:
        model = contactos
        fields = '__all__'  


class categoriasSerializer(serializers.ModelSerializer):
    class Meta:
        model = categorias
        fields = '__all__'


class notaSerializer(serializers.ModelSerializer):
    class Meta:
        model = nota
        fields = '__all__'


# ------------------- ViewSets -------------------

class contactosViewSet(viewsets.ModelViewSet):
    queryset = contactos.objects.all().order_by('-criado_em')
    serializer_class = contactosSerializer


class categoriasViewSet(viewsets.ModelViewSet):
    queryset = categorias.objects.all()
    serializer_class = categoriasSerializer


class enderecosViewSet(viewsets.ModelViewSet):
    queryset = enderecos.objects.all()
    serializer_class = enderecosSerializer


class notaViewSet(viewsets.ModelViewSet):
    queryset = nota.objects.all().order_by('-criado_em')
    serializer_class = notaSerializer



