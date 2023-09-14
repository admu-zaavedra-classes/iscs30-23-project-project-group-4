from django.shortcuts import render, redirect
from django.views.generic import DetailView, CreateView, UpdateView
from .models import Assignment
from .forms import AddAssignmentForm


# assignment view for FBV implementation.
def assignments_view(request):
    assignments = Assignment.objects.all().order_by('id')
    return render(request, 'assignments.html', {'assignments': assignments})

# assignement Detail view for CBV implementation. 
class AssignmentDetailView(DetailView):
    model = Assignment
    template_name = 'assignment-details.html'
    context_object_name = 'assignment'

# assignment for adding CBV implementation.
class AssignmentAddListView(CreateView):
    model = Assignment
    form_class = AddAssignmentForm
    template_name = "assignment-add.html"

    def post(self, request):
        form = AddAssignmentForm(request.POST)
        if form.is_valid():
            # onSave is called, the form will have essential data and this includes pk as well. 
            new_assignment = form.save()
            # pass the pk and redirect. 
            return redirect('assignment_details', pk = new_assignment.pk)
        else:
            return render(request, 'assignment_details.html', {'form': form})
        
# assignment for edditing CBV implementation. 
class AssignmentEditView(UpdateView):
    model = Assignment
    form_class = AddAssignmentForm
    template_name = 'assignment-edit.html'


    # This will get the object, and this object is used to tell Django
    # that we are updating. 
    def get_object(self, queryset = None):
        pk = self.kwargs.get('pk')
        return Assignment.objects.get(pk=pk)

    def post(self, request, pk):
        assignment = self.get_object()
        form = AddAssignmentForm(request.POST, instance = assignment)
        if form.is_valid():
            # onSave is called, the form will have essential data and this includes pk as well. 
            update_assignment = form.save()
            # pass the pk and redirect. 
            return redirect('assignment_details', pk = update_assignment.pk)
        else:
            return render(request, 'assignment_details.html', {'form': form})