import django
import sys

import os

# sys.path.insert(0, '/Users/zhikuncheng/PycharmProjects/cfda_orm')
os.environ["DJANGO_SETTINGS_MODULE"] = "cfda_orm.settings"
django.setup()

from orm import models


def get_source():
    set_inf = models.Source.objects.all()
    return set_inf


def save_source(item):
    try:
        source_info = models.Source(id=item['id'],
                                    ik=item['ik'],
                                    code=item['code'])

    except Exception as e:
        print(e)
        return False
    try:
        source_info.save()
    except:
        return True
