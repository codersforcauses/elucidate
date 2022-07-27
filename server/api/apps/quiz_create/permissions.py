from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission
from api.apps.shared_models.quiz_models import Question
import re 
class IsOwner(BasePermission): 
    def has_permission(self, request): 
        path = request.path
        q_str = re.search("\/question\/[0-9]+\/", path)[0]
        q_num = re.findall("[0-9]+", q_str)
        q_creator = quiz_models.Question.objects.get(id=q_num[0]).creator
        return q_creator == request.user




