from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
# from django.views.generic import TemplateView
# from .forms import HelloForm
from .forms import FriendForm
# from django.db.models import QuerySet

# class HelloView(TemplateView):
#
#     def __init__(self):
#         self.params = {
#                 'title': 'Hello',
#                 'message': 'your data:',
#                 'form': HelloForm(),
#                 'result': None,
#             }
#
#     def get(self, request):
#         return render(request, 'hello/index.html', self.params)
#
#     def post(self, request):
#         msg = 'あなたは、<b>' + request.POST['name'] + \
#                 '（' + request.POST['age'] + \
#                 '）</b>さんです。<br>メールアドレスは<b>' + request.POST['mail'] + \
#                 '</b>ですね。'
#         self.params['message'] = msg
#         self.params['result'] = 'you selected: "' + request.POST['check'] + '".'
#         self.params['form'] = HelloForm(request.POST)
#         return render(request, 'hello/index.html', self.params)

# def index(request):
    # if 'msg' in request.GET:
    #     msg = request.GET['msg']
    #     result = 'you typed: "' + msg + '".'
    # else:
    #     result = 'please send msg paramater!'
    # result = 'your id: ' + str(id) + ', name: "' \
    #         + nickname + '".'
    # return HttpResponse(result)
    # params = {
    #         'title': 'Hello',
    #         'message': 'your data:',
    #         'form': HelloForm(),
    #         # 'goto': 'next',
    #     }
    # if (request.method == 'POST'):
    #     params['message'] = '名前:' + request.POST['name'] + \
    #             '<br>メール:' + request.POST['mail'] + \
    #             '<br>年齢:' + request.POST['age']
    #     params['form'] = HelloForm(request.POST)
    # return render(request, 'hello/index.html', params)

# def next(request):
#     params = {
#             'title': 'Hello/Next',
#             'msg': 'これは、もう一つのページです。',
#             'goto': 'index',
#         }
#     return render(request, 'hello/index.html', params)

# def form(request):
#     msg = request.POST['msg']
#     params = {
#             'title':'Hello/Form',
#             'msg':'こんにちは、' + msg + 'さん。',
#         }
#     return render(request, 'hello/index.html', params)

# def __new_str__(self):
#     result = ''
#     for item in self:
#         result += '<tr>'
#         for k in item:
#             result += '<td>' + str(k) + '=' + str(item[k]) + '</td>'
#         result += '</tr>'
#     return result
#
# QuerySet.__str__ = __new_str__

def index(request):
    data = Friend.objects.all()
    params = {
            'title': 'Hello',
            # 'message': 'all friends.',
            # 'form': HelloForm(),
            'data': data,
        }
    return render(request, 'hello/index.html', params)

# create model
def create(request):
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
            'title': 'Hello',
            'form': FriendForm(),
        }
    return render(request, 'hello/create.html', params)

def edit(request, num):
    obj = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
            'title': 'Hello',
            'id': num,
            'form': FriendForm(instance=obj),
        }
    return render(request, 'hello/edit.html', params)
