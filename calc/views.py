from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse

from .models import Activity

def index(request):
    activity_list = Activity.objects.order_by('-pub_date')
    contact_time = Activity.objects.filter(activity_type__startswith='Contact')
    independent_time = Activity.objects.filter(activity_type__startswith='Independent Learning')
    if request.method == 'POST':
        credits = int(request.POST['credits'])
        credits_double = credits * 2
        credits_quadrupled = credits * 4
        weeks = int(request.POST['weeks'])
        hoursContactTotal = 0
        hoursIndependentTotal = 0
        for h in contact_time:
            if request.POST['hoursContact' + str(h.id)]:
                int_h = int(request.POST['hoursContact' + str(h.id)])
                hoursContactTotal += int_h
        for h in independent_time:
            if request.POST['hoursIndependent' + str(h.id)]:
                int_h2 = int(request.POST['hoursIndependent' + str(h.id)])
                hoursIndependentTotal += int_h2
        context = {'activity_list': activity_list, 'credits': credits, 'credits_double': credits_double, 'credits_quadrupled': credits_quadrupled, 'weeks': weeks, 'hoursContactTotal': hoursContactTotal, 'hoursIndependentTotal': hoursIndependentTotal}
        return render(request, 'calc/index.html', context)
    else:
        context = {'activity_list': activity_list}
        return render(request, 'calc/index.html', context)

def activity(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    return render(request, 'calc/activity.html', {'activity': activity})
