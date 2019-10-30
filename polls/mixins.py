from asgiref.sync import async_to_sync
from .models import Question,Response,Answer
from channels.db import database_sync_to_async


class SocketsDatabaseMixin:
    @database_sync_to_async
    def get_responses(self):
        q = Question.objects.get(id=2)
        print(q.answer.all())           
        return Response.objects.all()[:10]


    @database_sync_to_async
    def save_response(self,response,question_id):
        question = Question.objects.get(id=question_id)
        res = Response.objects.create(response=response,question=question)
        res.save()
        return res


    @database_sync_to_async
    def count_questions(self):
        arr = []
        for obj in Response.objects.distinct('response'):
            arr.append(obj.response_count())
        return arr
