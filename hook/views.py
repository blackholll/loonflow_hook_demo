import json

from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from service.common.common_service import CommonService
from service.hook.hook_participant_service import HookParticipantService, HookNoticeService


@method_decorator(csrf_exempt, name='dispatch')
class HookParticipantView(View):
    def post(self, request, *args, **kwargs):
        json_str = request.body.decode('utf-8')
        signature = request.META.get('HTTP_SIGNATURE', '')
        timestamp = request.META.get('HTTP_TIMESTAMP', '')
        request_data_dict = json.loads(json_str)

        # 校验请求是否合法
        flag, msg = CommonService.check_signature(timestamp, signature)
        if flag:
            flag, msg = HookParticipantService.response_hook_sync(request_data_dict)
            if flag:
                return JsonResponse(dict(code=-1, msg=msg, data=""))
        return JsonResponse(dict(code=0, msg="任务执行成功", data=""))

@method_decorator(csrf_exempt, name='dispatch')
class HookNoticeView(View):
    def post(self, request, *args, **kwargs):
        json_str = request.body.decode('utf-8')
        signature = request.META.get('HTTP_SIGNATURE', '')
        timestamp = request.META.get('HTTP_TIMESTAMP', '')
        request_data_dict = json.loads(json_str)
        # 校验请求是否合法
        flag, msg = CommonService.check_signature(timestamp, signature)
        if flag:
            flag, msg = HookNoticeService.response_notice(request_data_dict)