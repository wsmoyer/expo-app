from asgiref.sync import async_to_sync
from .models import Question,Response,Answer
from channels.db import database_sync_to_async


class SocketsDatabaseMixin:
    @database_sync_to_async
    def get_responses(self):
        return Response.objects.all()


    @database_sync_to_async
    def save_response(self,response,question_id):
        question = Question.objects.get(id=question_id)
        answer = Answer.objects.get(id=response)
        res = Response.objects.create(answer=answer,question=question)
        res.save()
        return res


    @database_sync_to_async
    def get_answer_list(self):
        arr = []
        for question in questions:
            answers = question.answer.all()
            for a in answers:
                res = Response.objects.filter(answer=a)
                res_dict = {'count':res.count,'answer':a}
                arr.append(res_dict)
        print(arr)