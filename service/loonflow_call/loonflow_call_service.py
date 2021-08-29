import requests
from django.conf import settings

from service.common.common_service import CommonService


class LoonflowCallService(object):
    def __init__(self):
        self.token = settings.LOONFLOW_TOKEN

    def update_ticket_filed(self, ticket_id, field_key, field_value):
        """
        更新工单字段的值
        :param ticket_id:
        :param field_key:
        :param field_value:
        :return:
        """
        url = settings.LOONFLOW_HOST + "/api/v1.0/tickets/{ticket_id}/fields"
        app_name = settings.LOONFLOW_APP

        common_service_ins = CommonService()
        timestamp, signature = common_service_ins.gen_signature(self.token)
        headers = dict(timestamp=timestamp, signature=timestamp, appname=app_name, username="robot")
        data = dict(ticket_id=ticket_id, field_key=field_key, field_value=field_value)
        r = requests.post(url, json=data, headers=headers)
        result = r.json()
        if result.get("code") == 0:
            return True, ""
        else:
            return False, result.get('msg')







