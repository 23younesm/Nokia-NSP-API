import requests
import json
import urllib3
import os
from datetime import datetime

try:
    serverip = "<SERVER_IP>"
    token = "<TOKEN>"
    urllib3.disable_warnings()

    def save_response_to_file(response_text):
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d-%H-%M-%S")
        folder_path = "data"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file_path = os.path.join(folder_path, f"{timestamp}.txt")
        dataform = str(response_text).strip("'<>() ").replace("'", '"')
        parsed = json.loads(dataform)
        response_text_pp = json.dumps(parsed, indent=4)
        with open(file_path, "w") as file:
            file.write(response_text_pp)

    def save_response_to_file_no_pp(response_text):
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d-%H-%M-%S")
        folder_path = "data"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        file_path = os.path.join(folder_path, f"{timestamp}.txt")
        with open(file_path, "w") as file:
            file.write(response_text)

    def optionNo():
        print("\n")
        url = "https://" + serverip + "/rest-gateway/rest/api/v1/auth/token"

        payload = json.dumps(
            {"grant_type": "client_credentials"},
            skipkeys=True,
            allow_nan=True,
            indent=6,
            separators=(",", ":"),
        )
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic <TOKEN>",
        }

        response = requests.request(
            "POST", url, headers=headers, data=payload, verify=False
        )

        try:
            save_response_to_file(response.text)
        except:
            save_response_to_file_no_pp(response.text)
        finally:
            print(response.text)
            global token
            token = input("Please enter the new token: ")

    def optionYes():
        global token
        token = input("Please enter the new token: ")

    def option2():

        print("\n")
        url = (
            "https://"
            + serverip
            + "/nsp-keycloak-api/v2/user-management/realm/Nokia/users"
        )

        payload = ""
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
        }
        response = requests.request(
            "GET", url, headers=headers, data=payload, verify=False
        )
        try:
            save_response_to_file(response.text)
        except:
            save_response_to_file_no_pp(response.text)
        finally:
            print(response.text)

    def option3():
        print("\n")
        url = (
            "https://"
            + serverip
            + "/restconf/data/nsp-equipment:network/network-element"
        )

        payload = {}
        headers = {"Authorization": f"Bearer {token}"}

        response = requests.request(
            "GET", url, headers=headers, data=payload, verify=False
        )
        try:
            save_response_to_file(response.text)
        except:
            save_response_to_file_no_pp(response.text)
        finally:
            print(response.text)

    def option4():

        print("\n")
        url = (
            "https://"
            + serverip
            + ":8545/restconf/data/nsp-fault:alarms/alarm-list/alarm?fields=alarm-fdn"
        )

        payload = {}
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

        response = requests.request(
            "GET", url, headers=headers, data=payload, verify=False
        )
        try:
            save_response_to_file(response.text)
        except:
            save_response_to_file_no_pp(response.text)
        finally:
            print(response.text)

    menu_options = {
        1: "Initial Authentication",
        2: "Get All Users",
        3: "Get All NE Info",
        4: "Get All Active Alarms",
    }

    while True:
        print("Menu:")
        for key, value in menu_options.items():
            print(f"{key}: {value}")

        user_input = input(
            "Enter the number of the option you'd like to choose or type exit: "
        )

        if user_input.isdigit():
            option_number = int(user_input)
            if option_number in menu_options:
                if option_number == 1:
                    menu_options_has_token = {
                        1: "Yes, I Need A New Token",
                        2: "No, I Already Have A Token",
                    }
                    print("Menu:")
                    for key, value in menu_options_has_token.items():
                        print(f"{key}: {value}")

                    has_token = input("Do you need a token? Please enter number: ")
                    if has_token.isdigit():
                        option_number1 = int(has_token)
                        if option_number1 in menu_options:
                            if option_number1 == 1:
                                optionNo()
                            elif option_number1 == 2:
                                optionYes()
                        else:
                            print("Invalid option. Please try again.")
                elif option_number == 2:
                    option2()
                elif option_number == 3:
                    option3()
                elif option_number == 4:
                    option4()
            else:
                print("Invalid option. Please try again.")
        elif user_input.lower() == "exit" or user_input.lower() == "quit":
            print("\n")
            print("Exiting program.")
            print("\n")

            url = "https://" + serverip + "/rest-gateway/rest/api/v1/auth/revocation"

            payload = "token=" + f"{token}" + "&token_type_hint=token"
            headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": "Basic <TOKEN>",
            }

            response = requests.request(
                "POST", url, headers=headers, data=payload, verify=False
            )

            print(response.text)
            print("Token has been disabled")
            break
        else:
            print("Invalid input. Please try again.")
except KeyboardInterrupt:
    print("\n")
    print("Exiting program.")
    print("\n")

    url = "https://" + serverip + "/rest-gateway/rest/api/v1/auth/revocation"

    payload = "token=" + f"{token}" + "&token_type_hint=token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": "Basic <TOKEN>",
    }

    response = requests.request(
        "POST", url, headers=headers, data=payload, verify=False
    )

    print(response.text)
    print("Token has been disabled")

