from django.contrib.auth.mixins import UserPassesTestMixin
from principal.utils import Utils

class BaseMixin(UserPassesTestMixin):
    raise_exception=True
class AdotanteMixin(BaseMixin):
    def test_func(self):
        return Utils.check_adotante(self.request.user)
class AbrigoMixin(BaseMixin):
    def test_func(self):
        return Utils.check_abrigo(self.request.user)