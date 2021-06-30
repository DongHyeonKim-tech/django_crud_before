from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .models import BidCrawling
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponseRedirect
from .forms import BookCreateForm, BookUpdateForm, bookForm
# Create your views here.


class Index(generic.ListView):
    model = BidCrawling
    paginate_by = 100
    context_object_name = 'books'
    template_name = 'index.html'

    # def get_context_data(self, **kwargs):
    #     context = super(Index, self).get_context_data(**kwargs)
    #     context['writer_infos'] = WriterInfo.objects.all()
    #     context['tasks'] = Task.objects.all()

    #     return context


# def tasks(request):
#     data = dict()
#     if request.method == 'GET':
#         tasks = Task.objects.all()
#         data['table'] = render_to_string(
#             'book/task.html',
#             {'tasks': tasks},
#             request=request
#         )
#         return JsonResponse(data)


class BookDetailView(generic.DetailView):
    model = BidCrawling
    template_name = 'book/read_book.html'
    context_object_name = 'book_detail'

    # def get_context_data(self, **kwargs):
    #     context = super(BookDetailView, self).get_context_data(**kwargs)
    #     pk = self.kwargs['pk']
    #     book_detail = BidCrawling.objects.get(pk=pk)
    #     context["writer"] = WriterInfo.objects.all().filter(
    #         bid=book_detail.bid)
    #     writer = WriterInfo.objects.all().filter(bid=book_detail.bid)
    #     context["writer_book"] = WriterInfo.objects.all().filter(
    #         name__icontains=book_detail.writer)
    #     context["book_another"] = BidCrawling.objects.all().filter(
    #         bid=writer.bid)
    #     context["book"] = BidCrawling.objects.all()

    # context["writer_info"] = WriterInfo.objects.filter(
    #    isbn=str(BidCrawling.isbn))
    # return context


class BookCreateView(generic.CreateView):
    model = BidCrawling
    form_class = BookCreateForm
    success_url = reverse_lazy('index')
    template_name = 'book/create_book.html'


class BookUpdateView(generic.UpdateView):
    model = BidCrawling
    form_class = BookUpdateForm
    context_object_name = 'update_book'
    success_url = reverse_lazy('index')
    template_name = 'book/update_book.html'


class BookDeleteView(generic.DeleteView):
    model = BidCrawling
    context_object_name = 'delete_book'
    success_url = reverse_lazy('index')
    template_name = 'book/delete_book.html'


# class TaskView(generic.ListView):
#     model = Task
#     context_object_name = 'tasks'
#     template_name = 'book/task.html'


# class WriterUpdateView(generic.UpdateView):
#     model = WriterInfo
#     context_object_name = 'update_writer'
#     form_class = WriterUpdateForm
#     success_url = reverse_lazy('index')
#     template_name = 'book/update_book.html'
