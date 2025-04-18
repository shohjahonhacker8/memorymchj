from django.shortcuts import render
from django.contrib import messages
from django.http import JsonResponse
from .forms import ContactForm


def index(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()  # Ma'lumotlarni bazaga saqlash
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'message': 'Xabaringiz muvaffaqiyatli yuborildi!', 'status': 'success'})
                else:
                    messages.success(request, 'Xabaringiz muvaffaqiyatli yuborildi!')
                    form = ContactForm()  # Yangi, bo‘sh forma
            except Exception as e:
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'message': f'Bazada xatolik: {str(e)}', 'status': 'error'})
                else:
                    messages.error(request, f'Bazada xatolik: {str(e)}')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse(
                    {'message': 'Xatolik yuz berdi. Iltimos, ma\'lumotlarni qayta tekshiring.', 'status': 'error'})
            else:
                messages.error(request, 'Xatolik yuz berdi. Iltimos, ma\'lumotlarni qayta tekshiring.')

    return render(request, 'index.html', {'form': form})


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                form.save()  # Ma'lumotlarni bazaga saqlash
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'message': 'Xabaringiz muvaffaqiyatli yuborildi!', 'status': 'success'})
                else:
                    messages.success(request, 'Xabaringiz muvaffaqiyatli yuborildi!')
                    form = ContactForm()
            except Exception as e:
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'message': f'Bazada xatolik: {str(e)}', 'status': 'error'})
                else:
                    messages.error(request, f'Bazada xatolik: {str(e)}')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse(
                    {'message': 'Xatolik yuz berdi. Iltimos, ma\'lumotlarni qayta tekshiring.', 'status': 'error'})
            else:
                messages.error(request, 'Xatolik yuz berdi. Iltimos, ma\'lumotlarni qayta tekshiring.')

    return render(request, 'contact.html', {'form': form})