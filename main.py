import json, requests
def main():
  message = ("Welcome to the View the Weather Program!")
  print(message)
  
#use loop to continue with a city or zip until user hits QUIT
  while True:
    city = input("Enter a city or zip code you would like to view the weather for, or enter QUIT to stop viewing the weather:")
    if(city.upper() == "QUIT"):
      print("Thanks for viewing the weather, have a great day!")
      break
 #use try catch block to inform user of invalid input
    else:
      try:
        display_weather(city)
      except:
        print("You entered an invalid city or zip code please try again!")


#display the weather when we put in a city
def display_weather(city):
  base_url = "https://api.openweathermap.org/data/2.5/weather"
  appid = "e427edb2e19ce433131b6148304d6bc9"
  url = f"{base_url}?q={city}&units=imperial&APPID={appid}"
  try:
    response = requests.get(url)
    response.raise_for_status()
    unformated_data = response.json()
    temp = unformated_data["main"]["temp"]
    print(f"The current temp is: {temp}")
    temp_max = unformated_data["main"]["temp_max"]
    print(f"The max temp is: {temp_max}")
    #check for status code
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
      print("Your connection was successful!")

  except requests.exceptions.HTTPError as err:
    if response.status_code == 404:
      raise Exception(err)
    print(err)
  
if __name__ == "__main__":
  main()

#Source for try catch block starting on line 30 (the link in the email you provided):
# John SmithJohn Smith                    10.8k1717 gold badges4545 silver badges5151 bronze badges, Jonathon ReinhartJonathon Reinhart                    126k3232 gold badges245245 silver badges315315 bronze badges, jouelljouell                    2, tshtsh                    75777 silver badges1212 bronze badges, &amp; mike rodentmike rodent                    12.5k1111 gold badges9090 silver badges125125 bronze badges. (1960, November 1). Correct way to try/except using python requests module? Stack Overflow. Retrieved July 30, 2022, from https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module 