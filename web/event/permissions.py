from EpicEvents import BasePermissions


class EventPermissions(BasePermissions):
    def has_permission(self, request, view):
        can_access = self.is_staff(request) or self.is_salesman(request) or self.is_support(request)
        return can_access or self.methods_are_safe(request)

    def has_object_permission(self, request, view, obj):
        if self.is_support(request) and not self.methods_are_safe(request):
            return getattr(obj.support, "id", None) == request.user.support.id

        if self.is_salesman(request) and not self.methods_are_safe(request):
            return getattr(obj.client.sales_contact, "id", None) == request.user.salesman.id

        return self.is_staff(request) or self.methods_are_safe(request)
