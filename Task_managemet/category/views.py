from django.shortcuts import render,redirect
from .forms import categoryForm

def add_category(req):
    if req.method == 'POST':
        form = categoryForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('task')
    else:
        form = categoryForm()
    return render(req, 'category/category.html',{'form':form})

