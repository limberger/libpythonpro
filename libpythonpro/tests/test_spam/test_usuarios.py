from libpythonpro.spam.models import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome='Joao', email='jlimberger@gmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Joao', email='jlimberger@gmail.com'),
        Usuario(nome='Paulo L', email='jlimberger@gmail.com')
            ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
