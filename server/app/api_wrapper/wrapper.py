import requests
from app.settings import Policy, assistance_for_policy

class Wrapper(object):


    @staticmethod
    def get_customer(customer_id):
        url = "https://api.insurhack.com/apis/gi/1/Account_Set(%27pc:" + str(customer_id) + "%27)"

        querystring = {"$expand": "AccountHolderContact"}

        headers = {
            'authorization': "Bearer 415aeaf7-58c7-3d4e-97e6-412d97f57161",
            'content-type': "application/json",
            'cache-control': "no-cache"
        }
        return requests.request("GET", url, headers=headers, params=querystring)


    @staticmethod
    def customer_exists(customer_id):
        return Wrapper.get_customer(customer_id).status_code == 200


    @staticmethod
    def get_assistance_for_customer(customer_id):

        # TODO FIX
        # respones = get_customer(customer_id)
        # get policys
            #get assistance for each policy
        return assistance_for_policy[Policy.Lebensversicherung] # MOCKED
