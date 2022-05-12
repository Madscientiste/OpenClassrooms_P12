from EpicEvents import BasePermissions


# salesman can read
# salesman can write ONLY IF he is in relation with the client


class ContractPermissions(BasePermissions):
    def has_permission(self, request, view):
        can_access = self.is_staff(request) or self.is_salesman(request) or self.is_support(request)
        return can_access or self.methods_are_safe(request)

    def has_object_permission(self, request, view, obj):
        if self.is_salesman(request) and not self.methods_are_safe(request):
            return obj.salesmans.filter(id=request.user.salesman.id).exists()

        return self.is_staff(request) or self.methods_are_safe(request)
