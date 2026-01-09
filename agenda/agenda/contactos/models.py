from django.db import models

class categorias(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class contactos(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    categoria = models.ForeignKey(
        categorias,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class enderecos(models.Model):
    contacto = models.OneToOneField(contactos, on_delete=models.CASCADE)
    rua = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)


class nota(models.Model):
    contacto = models.ForeignKey(contactos, on_delete=models.CASCADE)
    texto = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
