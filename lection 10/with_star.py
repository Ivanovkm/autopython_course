# Есть маркер @pytest.mark.id_check(1, 2, 3), нужно вывести на печать, то что в него передано
#
# >>> 1, 2, 3
import keyword

import pytest


@pytest.mark.id_check(1, 2, 3)
def test(request):
    print(*(request.keywords._markers['id_check'].args))
    pass
