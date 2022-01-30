# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from pyowm import OWM
import requests
import requests
from bs4 import BeautifulSoup
#
key="8e32146026cf47574839aa9599d2302b"
#
class ActionHelloWorld(Action):
#
     def name(self) -> Text:
         return "action_weather"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
             api_key="8e32146026cf47574839aa9599d2302b"
             city=tracker.get_slot('city')
             if (city is not None):
                 city=city.capitalize()
             url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
             response=requests.get(url).json()
             temp=(response['main']['temp']-273)
             if city is not None:
                 text_res=f"Temperature of {city} is {temp} celisus"
             else:
                 text_res=f"Unable to fetch temperature at this moment (or) Try to captilize first letter, eg: shimla --> Shimla"


             dispatcher.utter_message(text=text_res)


class ActionCases(Action):
         
#
     def name(self) -> Text:
         return "action_cases"

     def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         url="https://www.worldometers.info/coronavirus/country/india/"
        #url='https://covid-india-api.herokuapp.com/v1/api'
         def Corona_cases(url):

             page = requests.get(url)
             print(page)

             soup = BeautifulSoup(page.text, "html.parser")
             pew = soup.findAll(['span'])

             data=[]
             for subs in pew:
                 if subs.get_text()!='[source]':
                     if subs.get_text()!='':
                         if '\n'not in subs.get_text():
                             if not any([i in subs.get_text() for i in [i for i in 'aeiou']]):
                                 data.append(subs.get_text())
             return data

         lis=Corona_cases(url)
         lis=lis[:3]
         val=["Total Coronavirus Cases","Deaths","Recovered"]
         data={}
         for i in range(len(lis)):
             data[str(val[i])]=lis[i]

         text_rest=f"Total Number of Cases in India: {data['Total Coronavirus Cases']} \n Number of People Recovered are: {data['Recovered']} \n Deaths recorded are: {data['Deaths']}"   

         dispatcher.utter_message(text=text_rest)

#         return []
