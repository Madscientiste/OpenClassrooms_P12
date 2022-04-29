from EpicEvents import BasePermissions

# Only sales & staff can Create/Delete
# The others are read only


class ClientPermissions(BasePermissions):
    def has_permission(self, request, view):
        can_access = self.is_staff(request) or self.is_salesman(request) or self.is_support(request)
        return can_access or self.methods_are_safe(request)

    def has_object_permission(self, request, view, obj):
        # if self.is_salesman(request) and not self.methods_are_safe(request):
        #     contract = request.user.salesman.contract_set
        #     return obj in contract

        # if self.can_write(request, "salesman"):
        # return contract.filter(client=obj).exists()

        can_access = self.is_staff(request) or self.is_salesman(request)
        return can_access or self.methods_are_safe(request)
