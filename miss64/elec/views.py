from django.shortcuts import render, redirect
from .models import Brand, Home, Middle, Product, Manual
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# 메인 페이지
def index(request):
    return render(request, 'elec/index.html')

# 브랜드 선택
def brand_select(request):
    brand_list = Brand.objects.all()

    # Pagination
    paginator = Paginator(brand_list, 5)
    page = request.GET.get('page')
    brands = paginator.get_page(page)

    context = {
        'brands': brands,
    }
    return render(request, 'elec/brand.html', context)

# 가전제품 선택
def home_select(request, brand_id):
    home_list = Home.objects.all()

    # Pagination
    paginator = Paginator(home_list, 10)
    page = request.GET.get('page')
    homes = paginator.get_page(page)

    context = {
        'homes': homes,
        'brand_id': brand_id,
    }

    return render(request, 'elec/select_h.html', context)

# 중분류 선택
def mid_select(request, brand_id, home_id):
    product_list = Product.objects.filter(brand_id = brand_id, home_id = home_id)

    middles = []
    for product in product_list:
        if not product.middle in middles:
            middles.append(product.middle)

    context = {
        'middles': middles,
        'brand_id': brand_id,
        'home_id': home_id,
    }

    return render(request, 'elec/select_m.html', context)

# 모델 선택
def model(request, brand_id, home_id, middle_id):
    product_list = Product.objects.filter(brand_id = brand_id, home_id = home_id, middle_id = middle_id)
  
    # Pagination
    paginator = Paginator(product_list, 9)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    context = {
        'products': products,
        'brand_id': brand_id,
        'home_id': home_id,
        'middle_id':middle_id,
    }

    return render(request, 'elec/model_select.html', context)

# 모델명으로 검색
def search(request):
    return render(request, 'elec/search.html')
# 검색 결과
def result(request):
    query = request.GET.get('query')
    # home에서 검색어가 model_name에 있는지 찾기
    products = Product.objects.filter(model_name__contains=query)
    
    context = {
        'products': products,
    }
    
    return render(request, 'elec/result.html', context)

# POST 요청만 받음
@login_required
def like(request, brand_id, home_id, middle_id, pk):
    # 1. pk번 Product 가져오기
    product = Product.objects.get(pk=pk)

    if request.user in product.like_users.all():       # 좋아요 취소
        product.like_users.remove(request.user)
    else:                                           # 좋아요
        product.like_users.add(request.user)

    return redirect('elec:model', brand_id, home_id, middle_id)

# user가 좋아요 누른 모델만 따로 모아보기
@login_required
def like_page(request):
    products = request.user.like_products.all()
    context = {
        'products': products,
    }
    return render(request, 'elec/like.html', context)