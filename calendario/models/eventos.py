from django.db import models

# Create your models here.

from django.core import validators
from django.core.mail import send_mail
from django.utils.translation import ugettext_lazy as _
from calendario.models import clientes, fornecedores


class t_evento(models.Model):
    tipo_evento = (
        ('Aniversario', 'Aniversário'),
        ('Casamento', 'Casamento'),
        ('Confrat', 'Confraternização'),
        ('Debutante', 'Debutante'),
        ('Locacao', 'Locação do Espaço'),
        ('Outros', 'Outros'),
    )

    opcao_servico = [
        ('Escolha o(s) serviço(s) a ser(em) incluídos: ', (
            ('Som / Ilum / Telao', 'Som / Iluminação / Telão'),
            ('Decoracao', 'Decoração'),
            ('Buffet', 'Buffet'),
            ('Outros', 'Outros'),
            )
        ),
    ]

    id_evento = models.AutoField(primary_key=True)
    evento = models.CharField(max_length=40, choices=tipo_evento, default='',
        verbose_name='Tipo de Evento')
    servicos = models.CharField(max_length=40, choices=opcao_servico, default='',
        verbose_name='Opções de Serviço')
    descricao = models.TextField(blank=True, verbose_name='Descrições Extra')
    valor = models.DecimalField(max_digits=8, decimal_places=2, blank=False,
        verbose_name='Valor Total do Evento')
    # USE_TZ=True, a verificação será realizada no fuso horário atual no momento
    # em que o objeto for salvo. A validação do modelo não é no nível do BD
    data = models.DateTimeField()
    data_hora = models.SlugField(unique_for_date='data')
    fk_Cliente = models.ForeignKey(clientes.t_cliente, on_delete=models.PROTECT, default='',
        verbose_name='Cliente')
    fk_Fornecedor = models.ManyToManyField(fornecedores.t_fornecedor, blank=False,
        verbose_name="Fornecedor(es)")

    class Meta:
        verbose_name = _('Evento')
        verbose_name_plural = _('Eventos')

    # def email_user(self, subject, message, from_email=None):
    #    send_mail(subject, message, from_email, [self.email])
    
    def __str__(self):
        return self.evento
