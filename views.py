from django.shortcuts import render
from computing_app.forms import Nameform
# Write View Here
def lab_activity_1(request):
    return render(request, 'testapp/lab_active.html')

def lab_activity_2(request):
    form = Nameform()
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '')
        length = len(full_name)

        first_character = full_name[0]
        last_character = full_name[-1]

        return render(request, 'testapp/lab_activity_2_result.html', {
            'length': length,
            'first_character': first_character,
            'last_character': last_character,'form':form
        })
    else:
        return render(request, 'testapp/lab_activity_2_form.html')

def len_view(request):
    return render(request,'testapp/len_page.html')

def informatics(request):
    return render(request,'testapp/infor.html')

def difficult_view(request):
    return render(request,'testapp/difficult.html')

