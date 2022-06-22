class Funcionario:

    #criando inicializador para usar classe Programador
    def __init__(self, nome):
        self.nome =  nome

    def registra_horas(self, horas):
        print('Horas registradas...')
    

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    #def mostrar_tarefas(self):
        #print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')

class Programador:
    def __str__(self):
        return f'Programador, {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

class Estagiário(Alura, Caelum, Programador):
    pass
    
#problema: Todos funcionários só estáo atribuidos a Alura
#criando junior
'''joao = Junior()
joao.busca_perguntas_sem_resposta()
joao.mostrar_tarefas()

#criando funcionário pleno
brendom = Pleno()
brendom.busca_perguntas_sem_resposta()
brendom.busca_cursos_do_mes()
brendom.mostrar_tarefas()
'''

#método exibe objeto na memória, sem herdar o Estágiario na classe
marcus = Estagiário('Marcus')
print(f'{marcus} \n')

#herdando Programador
marcus = Estagiário('Marcus')
print(marcus)
