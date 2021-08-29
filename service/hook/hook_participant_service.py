from service.loonflow_call.loonflow_call_service import LoonflowCallService


class HookParticipantService(object):
    @staticmethod
    def response_hook_sync(request_data_dict):
        """
        本示例是同步响应，即收到hook请求后，完成所有任务后，直接response。
        当任务执行耗时较长时，需要使用异步任务。
        :param ticket_id:
        :return:
        """
        # 执行hook任务, 如调用某个其他接口完成授权、如登录到服务器执行某个命令等
        print("执行hook任务")
        ticket_id = request_data_dict.get("ticket_id")

        # 更新工单字段， 某些情况下任务执行后，需要更新工单中的一些信息，如完成授权后， 将授权的用户名信息更新到工单中
        flag, msg = LoonflowCallService().update_ticket_filed(ticket_id, "username", "zhangsan")
        return True, "任务执行成功"

    @staticmethod
    def response_hook_asyn(ticket_id):
        """
        本实例是异步响应，即收到hook请求后，触发一个异步任务后，立即response。
        等异步任务执行完成后，再回调loonflow告知执行结果
        :param ticket_id:
        :return:
        """
        print("该示例等待完善中")


class HookNoticeService(object):
    def response_notice(self, request_data):
        """
        通知hook
        :param request_data:
        :return:
        """
        """
        这是loonflow 通知hook的数据内容
        params = {'title_result': title_result, 'content_result': content_result,
               'participant': ticket_obj.participant, 'participant_type_id': ticket_obj.participant_type_id,
               'multi_all_person': ticket_obj.multi_all_person, 'ticket_value_info': ticket_value_info,
               'last_flow_log': last_flow_log, 'participant_info_list': participant_info_list}
        """
        participant_info_list = request_data.get('participant_info_list')
        phone_list = []
        email_list = []
        for participant_info in participant_info_list:
            phone_list.append(participant_info.get('phone'))
            email_list.append(participant_info.get('email_list'))
        title_result = request_data.get('title_result')  # 这是根据工作流标题模板生成的标题
        content_result = request_data.get('content_result')  # 这是根据工作流通知内容模板生成的通知内容

        # 发送短信: 找个短信服务，调用该服务
        self.send_sms(phone_list, content_result)
        self.send_email(phone_list, title_result, content_result)

    @staticmethod
    def send_sms(phone_list, content):
        """
        发送短信的demo，未实际实现
        :param phone_list:
        :param content:
        :return:
        """
        print("发送短信通知成功")   # 未实际实现，你需要根据你的短信服务商的接口文档来实现

    @staticmethod
    def send_email(email_list, title, content):
        """
        发送短信的demo，未实际实现
        :param email_list:
        :param title:
        :param content:
        :return:
        """
        print("发送邮件通知成功")   # 未实际实现，你需要根据你的邮箱服务商的接口文档来实现

