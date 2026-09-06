from django.shortcuts import redirect

# func = def get_all_categories(request):
def admin_only(func):
    def views_func(request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('homepage')
        else:
            return func(request, *args, **kwargs)
    return views_func


def user_only(func):
    def views_func(request, *args, **kwargs):
        if not request.user.is_staff:
            return func(request, *args, **kwargs)
        else:
            return redirect('all-products')
    return views_func
