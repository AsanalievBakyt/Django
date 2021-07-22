from .models import Promo

def use_promo(promo,price):
    try:
        p = Promo.objects.get(code=promo)
        if p.status == 'active':
            total = price - (price * p.sale) / 100
            p.status = 'dead'
            p.save()
            return total
        else:
            raise ValueError('Код уже активирован')
    except Promo.DoesNotExist:
        raise ValueError('промокода не существует')