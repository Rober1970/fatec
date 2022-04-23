from hashlib import sha256

usuario_padrao = "14514307be9ef4287877636f9a3397b7bb9dddfded42ee0449e8c83ac2f2a78a"
senha_padrao = "b7e94be513e96e8c45cd23d162275e5a12ebde9100a425c4ebcdd7fa4dcd897c"

usuario_digitado = input("Digite seu usuario: ").encode("ascii")
senha_digitada = input("Digite sua senha: ").encode("ascii")
usuario_digitado = sha256(usuario_digitado).hexdigest()
senha_digitada = sha256(senha_digitada).hexdigest()

if senha_digitada == senha_padrao and usuario_digitado == usuario_padrao:
    print("Bem vindo ao curso Fatec")
else:
    print("Ou senha ou usuário incorreto")
    
#fatec = usuario
#senha = senha