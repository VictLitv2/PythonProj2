import os

from proj2.tools.service.MainAppLogic import MainAppLogic


def start_use_site_search():
   user_decision_to_continue = None
   while (user_decision_to_continue != "No"):
      MainAppLogic().process_logic()
      user_decision_to_continue = input("Please enter `No` If you want to exit\n")
   print("Thank for your patience!\n")
if __name__ == '__main__':

   start_use_site_search()
   #exit(0)