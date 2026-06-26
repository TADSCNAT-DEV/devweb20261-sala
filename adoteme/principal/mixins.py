from django.contrib.auth.mixins import UserPassesTestMixin
from principal.utils import Utils

class AdotanteMixin(UserPassesTestMixin):
    raise_exception=True
    def test_func(self):
        return Utils.check_adotante(self.request.user)
class AbrigoMixin(UserPassesTestMixin):
    raise_exception=True
    def test_func(self):
        return Utils.check_abrigo(self.request.user)