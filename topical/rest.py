from django.http import HttpResponse
from rest_framework import routers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer

router = routers.DefaultRouter()

class UserViewSet(viewsets.ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	lookup_field = 'username'
	@action(detail = False, methods = ['GET'])
	def me(self, request):
		if not request.user.is_authenticated:
			return HttpResponse(status = 404)
		serializer = UserSerializer(
			request.user,
			many = False,
			context = { 'context': request }
		)
		return Response(serializer.data)
router.register('user', UserViewSet)