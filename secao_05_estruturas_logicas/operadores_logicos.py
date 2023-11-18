ativo = False
logado = False

if ativo and logado:
    print('Bem vindo usuário!')
elif not logado:
    print('Por favor registri-se!')
else:
    print('Você precisa ativar sua conta. Por favor, cheque seu e-mail.')