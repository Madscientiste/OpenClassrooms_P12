from EpicEvents import BasePermissions


class EventPermissions(BasePermissions):
    def has_permission(self, request, view):
        is_staff = request.user.is_staff
        is_sales = self.can_write(request, "salesman")
        is_support = self.can_write(request, "support")
        can_access = is_staff or is_sales or is_support

        return can_access or self.methods_are_safe(request)

    def has_object_permission(self, request, view, obj):
        is_staff = request.user.is_staff
        is_sales = self.can_write(request, "salesman")
        is_support = self.can_write(request, "support")
        can_access = is_staff or is_sales or is_support

        if is_support and not self.methods_are_safe(request):
            return False

        return can_access or self.methods_are_safe(request)
