import pytest

from libpythonpro.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('destinatario',
                         ['jlimberger@gmail.com', 'foo@bar.com.br'])
def test_remetente(destinatario):
    enviador = Enviador()
    origem = 'jlimberger@gmail.com'
    resultado = enviador.enviar(destinatario,
                                origem,
                                'Cursos Python Pro',
                                'Primeira turma ')
    assert destinatario in resultado


@pytest.mark.parametrize('remetente',
                         ['', 'foo'])
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(remetente,
                        'jlimberger@gmail.com',
                        'Cursos Python Pro',
                        'Primeira turma ')
