import requests


class API:
    def __init__(self):
        self.session_id = None

    def login(self, username, password):
        requests.post("https://prelive.idram.am/api/SignUp/PreSignUp", verify=False, data={"u": username})
        response = requests.post("https://prelive.idram.am/api/Signin/Login", verify=False,
                                 data={"u": username, "p": password})
        if response.status_code == 200 and response.json()['OpCode'] == 0:
            sid, token = response.json()['SessionId'], response.json()['Token']
            self.session_id = sid
            return sid
        else:
            print("Login failed")
            print(response.json())

    def get(self, api_url, data=None):
        response = requests.get(api_url, headers={'_SessionId_': self.session_id}, verify=False)
        return response.json()

    def post(self, api_url, data=None):
        response = requests.post(api_url, headers={'_SessionId_': self.session_id}, data=data, verify=False)
        return response.json()


s1 = API()
s1.login("+37455010890", "Test123!")
# print(s1.get("https://prelive.idram.am/api/Group/Run"))
print(s1.post("https://prelive.idram.am/api/MyInfo/getClientAccountsInfo"))
