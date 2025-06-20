from .models import ChildProfile

def child_profile_context(request):
    if request.user.is_authenticated:
        try:
            child_profile = ChildProfile.objects.get(user=request.user)
            return {'child_profile': child_profile}
        except ChildProfile.DoesNotExist:
            return {}
    return {}
