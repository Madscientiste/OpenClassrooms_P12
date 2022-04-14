from EpicEvents import BasePermissions


# salesman can read
# salesman can write ONLY IF he is in relation with the client


class ContractPermissions(BasePermissions):
    def has_permission(self, request, view):
        return self.can_write(request, "salesman") or self.methods_are_safe(request)

    def has_object_permission(self, request, view, obj):
        # can only write if he has a contract with the client
        if self.can_write(request, "salesman"):
            return obj.salesmans.filter(pk=request.user.salesman.pk).count() > 0

        return self.methods_are_safe(request)
