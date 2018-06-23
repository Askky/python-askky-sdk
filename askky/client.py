import json
import requests

class callSurvey:
    def __init__(self,privateKey=None):
        self.base_url = "https://api.askky.co/"
        self.privateKey = privateKey

    def survey(self, survey_id, user_id, **kwargs):
        """"
        trigger specific survey for a user
        Args:
            survey_id : Id of the Survey that you want to call
            user_id : Id of the user to whom you want to show the Survey
        Returns:
            Success Response Dict
        """
        
        
        url = str(self.base_url) + str('trigger/form/')
        data = {}
        data["privateKey"] = self.privateKey
        data["campaignId"] = survey_id
        data["userId"] = user_id
        print ('data',json.dumps(data))
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url,data=str(json.dumps(data)),headers=headers)
        print ('response',response.json())

        return response


# def test():
#     obj = callSurvey(privateKey="3d3209966caf8b781db16005c320a29701776613247bb80118")
#     response = obj.survey(survey_id="aszx2f8b75de2c6",user_id="abc")


# test()
