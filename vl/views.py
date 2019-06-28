from django.shortcuts import render
from .forms import LeaveForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import LeaveTable
from django.contrib.auth.models import User

def req_list(request):
    my_leaves = LeaveTable.objects.filter(user_id=request.user.id).order_by('date')
    all_leaves = LeaveTable.objects.order_by('date')
    return render(request, 'vl/req_list.html', {'my_leaves': my_leaves, 'all_leaves': all_leaves})

@login_required
def req_post(request):
    if request.method == "POST":
        form = LeaveForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            # post.published_date = timezone.now()
            post.save()
            return redirect('req_list')
    else:
        form = LeaveForm()
    return render(request, 'vl/req_post.html', {'form': form})

@login_required
def approve(request, pk):
    leave = get_object_or_404(LeaveTable, pk=pk)
    leave.sw_approval()
    return redirect('req_list')
