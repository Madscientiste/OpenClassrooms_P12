from EpicEvents import BasePermissions

# Only sales & staff can Create/Delete
# The others are read only


class SalesPermissions(BasePermissions):
    def has_permission(self, request, view):
        return self.can_write(request, "salesman") or self.methods_are_safe(request)

    def has_object_permission(self, request, view, obj):
        if self.methods_are_safe(request):
            return True

        if self.can_write(request, "salesman"):
            contract = request.user.salesman.contract_set
            return contract.filter(client=obj).exists()

        return False
