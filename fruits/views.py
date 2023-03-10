from django.shortcuts import render
from django.http import JsonResponse
from .models import Fruits, Shops, ShopFake, ShopFake2, CharTest
import time
from django.db.models import Sum, Count, Avg, Min, Max, StdDev, Variance
from django import forms
from django.views.generic import FormView

class TestForm(forms.Form):
    a = forms.CharField(
        label = "a",
        max_length = 20
    )

    b = forms.CharField(
        label = "b",
        max_length = 20,
        required=False
    )

class FormViewTest(FormView):
    template_name = 'form_test.html'
    form_class = TestForm
    success_url = '/'

    def form_valid(self, form):
        data = self.request.POST
        CharTest.objects.create(**data)
        return super().form_valid(form)

def not_null_test(request):
    if request.method == 'GET':
        return render(request, 'test.html')
    elif request.method == 'POST':
        data = request.POST
        data = {k:v for k,v in data.items() if k != 'csrfmiddlewaretoken'}
        print(data)
        print("a: ", data.get("a"))
        print("b: ", data.get("b"))
        CharTest.objects.create(**data)
        return JsonResponse(data)

def intersection_view(request):
    # 실습 안했음
    return JsonResponse({'status':'intersection'})


def shopw_view(request):
    # total_fruits = Fruits.objects.aggregate(Count('id'))
    # avg_fruits1 = Fruits.objects.aggregate(Avg('name'))
    # min_max_prices = Fruits.objects.aggregate(Min('price'), Max('price'))
    # price_stddev = Fruits.objects.aggregate(StdDev('price'))
    # price_Variance = Fruits.objects.aggregate(Variance('price'))

    # object_id_list = [1, 2, 3, 4, 5]
    # objects = Fruits.objects.in_bulk()
    # objects1 = Fruits.objects.in_bulk(object_id_list)
    # # .in_bulk(): {ID: object(ID)}형태로m 리턴해줌(dictionary 형태로 ID와 함께)

    fruits_all = Fruits.objects.all()
    fruits_only_price = Fruits.objects.all().only('price')
    fruits_defer_price = Fruits.objects.all().defer('price')
    # only의 경우 해당하는 field만 뽑아서 오브젝트를 불러온다. 
    # defer의 경우 해당하는 field만 제외하고 오브젝트를 불러온다.
    # 둘 다, Model이 큰 경우에 특정 필드만 불러오기 때문에 자원 효율적으로 사용하는데,
    # 제외되었던 필드에 대해서 조회를 하게 되면 에러가 나는게 아니라 작동이 된다. 이런 경우는 해당 필드에 대해서 다시 조회를 하는거기 때문에
    # 오히려 자원을 비효율적으로 두배 쓰게 될 수도 있다. 이를 주의하고 써야함
    
    shops1 = Shops.objects.filter(id=1)
    shops2 = Shops.objects.filter(id=2)
    shops_union = shops1.union(shops2)
    
    # shop1 = Shops.objects.get(id=1)
    # shop2 = Shops.objects.get(id=2)
    # shop_union = shops1.union(shop2)

    fruits1 = Fruits.objects.filter(id=1)

    # s_f_union = shops1.union(fruits1)
    shop_fakes = ShopFake.objects.all()
    shop_fakes2 = ShopFake2.objects.all()
    sf_union = shop_fakes.union(shop_fakes2)
    for i in sf_union:
        print(i.no_name, i.no_fruits)
        print("----")
    # https://django-orm-cookbook-ko.readthedocs.io/en/latest/union.html
    # 위에서는 field 같아야 한다고 하지만, union... field의 유형이 달라도 field수만 맞으면 union이 먹는다 (에러는 안나고 실행됐다는 말. 항상 그런지는 확인 안했으나 그런 경우 있음)
    # values_list로 합집합을 구해서 원하는 정보로 쓸수도 있을 듯
    # https://gardeny.tistory.com/13 여기서 좀 더 자세히 확인 가능 with annotate
    # https://brownbears.tistory.com/426    # chain에 대한 설명도 있음. chain 도 ORM. filter가 아닌 get으로 얻어온 것도 chain으로 합칠수 있다는 말처럼  들리는데. 확인해보기
    return JsonResponse({'status':'shop'})


def fruit_view(request):
    return JsonResponse({'status':'success'})


def fruit_view2(request):
    start1 = time.time()
    fruits_group = Fruits.objects.filter(group=1)
    fruits_group_list = []
    for i in fruits_group:
        fruits_group_list.append(i.name)
    print(len(fruits_group_list))
    finish1 = time.time()
    print(finish1-start1)
    
    start2 = time.time()
    fruits_group_re = Fruits.objects.filter(group=1)
    fruits_group_list_comprehension = [i.name for i in fruits_group_re]
    print(len(fruits_group_list_comprehension))
    finish2 = time.time()
    print(finish2-start2)

    start3 = time.time()
    fruits_group_values_list = Fruits.objects.filter(group=1).values_list('name', flat=True)
    print(len(fruits_group_values_list))
    finish3 = time.time()
    print(finish3-start3)

    return JsonResponse({'status':'view2_success'})

def fruit_view3(request):
    return JsonResponse({'status':'view3_success'})


def fruit_view4(request):
    # fruits_group_values_list = Fruits.objects.filter(group=1).values_list('name', flat=True)
    fruits_group_values = Fruits.objects.filter(group=1).values('name')
    return JsonResponse({'status':'view4_success'})
