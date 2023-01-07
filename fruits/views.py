from django.shortcuts import render
from django.http import JsonResponse
from .models import Fruits, Shops, ShopFake, ShopFake2
import time
from django.db.models import Sum, Count, Avg, Min, Max, StdDev, Variance


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
    # for a,b,c, in zip(range(0,100000), range(100000,200000), range(200000,300000)):
    #     if not Fruits.objects.filter(name=a).exists():
    #         Fruits.objects.create(name=a, price=b, grade=c)
    #     else:
    #     #     fruit = Fruits.objects.get(name=a)
    #         print(a)
    #         # print(f'{fruit.name} - {fruit.price} - {fruit.grade}')
    print(len(Fruits.objects.all()))
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

    # fruits_group_values = Fruits.objects.filter(group=1).values('name')
    # for i in fruits_group_values:
        # print(i)
    # print(fruits_group_values)
    return JsonResponse({'status':'view2_success'})

def fruit_view3(request):
    fruits = Fruits.objects.all()
    for i in fruits:
        if int(i.name) < 50000:
            i.group = 1
        else:
            i.group = 2
        i.save()
        print(i)
    return JsonResponse({'status':'view3_success'})


def fruit_view4(request):
    # fruits_group_values_list = Fruits.objects.filter(group=1).values_list('name', flat=True)
    fruits_group_values = Fruits.objects.filter(group=1).values('name')

    # print(fruits_group_values_list)
    print(fruits_group_values)
    return JsonResponse({'status':'view4_success'})
