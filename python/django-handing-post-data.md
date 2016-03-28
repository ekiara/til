Django, handline POST data
----------------------------------------

if request.method == "POST":
    value_0 = request.POST.get('value_0')
    value_1 = request.POST.get('value_1')
else:
    period_provided = False
