from django.shortcuts import render,redirect

class Dash_datas:
    def ret(self, request, Balete, usuario):
        Receitas = []
        Despesas = []
        RContext = []
        DContext = []
        Saldo = []
        if not Balete:
            return render(request, 'Financeiro/Dashboard.html',{'usuario':usuario})
        for bal in Balete:
            if bal is not None:
                if bal.receita_set.count() != 0:
                    for entrada in bal.receita_set.all():
                        Receitas.append(entrada.valor)
                        RContext.append(entrada)
                    
                    for saida in bal.despesa_set.all():
                        Despesas.append(saida.valor)
                        DContext.append(saida)
                           
                Saldo.append(sum(Receitas) - sum(Despesas))  
            else:
                Balete = []
        return render(request, 'Financeiro/Dashboard.html', {
            'usuario': usuario,
            'balanco': Balete,
            'saldo': Saldo,
            'receitas': RContext,
            'DContext': DContext
        })