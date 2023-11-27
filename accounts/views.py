# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login as auth_login
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse


        
# @csrf_exempt
# def register_user(request):
#     if request.method == 'POST':
#         # 프론트엔드에서 전달한 사용자 정보를 받아옴
#         user_data = request.POST
#         form = UserCreationForm(user_data)

#         if form.is_valid():
#             # 사용자 생성
#             user = form.save()

#             # 생성된 사용자로 로그인
#             auth_login(request, user)

#             # 회원가입 성공 후의 처리를 여기에 추가할 수 있음
#             return JsonResponse({'success': True, 'message': '회원가입이 완료되었습니다.'})
#         else:
#             # 폼이 유효하지 않을 때의 처리
#             errors = form.errors.as_json()
#             return JsonResponse({'success': False, 'errors': errors})

#     # GET 요청에 대한 처리
#     return render(request, 'Register/index.html')  # registration 폴더에 register.html 템플릿을 만들어야 함
