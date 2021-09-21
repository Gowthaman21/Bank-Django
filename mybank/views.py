from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    acc = Account.objects.all()
    txn = Transfer.objects.all()
    return render(request, 'index.html', {'acc': acc, 'txn': txn})


def account(request, ano):
    acc = Account.objects.get(pk=ano)
    toacc = Account.objects.all()
    return render(request, 'transfer.html', {'acc': acc, 'toacc': toacc})


def transfermoney(request):
    if request.method == 'POST':
        fromAccNo = request.POST['fromAccNo']
        toAccNo = request.POST['toAccNo']
        date = request.POST['date']
        amount = request.POST['amount']
        f = Account.objects.get(ano=fromAccNo)
        t = Account.objects.get(ano=toAccNo)
        if f.ano != t.ano:
            if int(f.balance) > int(amount):
                ttot = int(t.balance) + int(amount)
                ftot = int(f.balance) - int(amount)
                Account.objects.filter(ano=toAccNo).update(balance=ttot)
                Account.objects.filter(ano=fromAccNo).update(balance=ftot)
                Transfer.objects.create(fromAccNo=f, toAccNo=t, date=date, amount=amount)
                return render(request, 'msg.html', {'msg': 'Transaction Successful'})
            else:
                return render(request, 'msg.html', {'msg': 'Insufficient Balance'})
        else:
            return render(request, 'msg.html', {'msg': 'Both accounts cannot be same'})


def about(request):
    return render(request, 'about.html')
