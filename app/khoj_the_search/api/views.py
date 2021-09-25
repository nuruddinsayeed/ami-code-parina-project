from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from core.models import UserInputValue
from khoj_the_search.api.serializers import InputValueSerializer


class InputValuesAPIView(APIView):
    """Returns Input Value API response"""
    # sample end point:
    # http://127.0.0.1:8000/api/input-values?format=api&user_id=1&start_datetime=2021-09-24T19:58:23.332624Z&end_datetime=2021-09-24T21:29:28.865268Z

    def get(self, request):
        """Manages api get request for input values"""

        # get search credientials form urls or riese Error
        try:
            start_datetime = request.GET["start_datetime"]
            end_datetime = request.GET["end_datetime"]
            # converting to int to validate user_id as int
            user_id = int(request.GET["user_id"])
        except Exception as e:
            return Response({"Error": "Please Provie user id, start date and end date"},
                            status=status.HTTP_404_NOT_FOUND)

        try:
            input_data = UserInputValue.objects.filter(
                user__id=user_id,
                timestamp__gte=start_datetime,
                timestamp__lte=end_datetime,
            )
        except Exception as e:
            return Response({"Error": e},
                            status=status.HTTP_404_NOT_FOUND)

        serializeed_data = InputValueSerializer(input_data, many=True)

        response_data = {
            "status": "success",
            "user_id": user_id,
            "payload": serializeed_data.data
        }
        return Response(response_data, status=status.HTTP_200_OK)
