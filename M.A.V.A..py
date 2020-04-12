import datetime

str(entry)

bool(looptyloop)

def wishme():
    hr = int(datetime.datetime.now().hour)
    if 0 <= hr < 12:
        print("Good Morning")
    elif 12 <= hr < 17:
        print("Good Afternoon")
    elif 17 <= hr <= 24:
        print("Good Evening")
    else:
        print("lol")


wishme()

while looptyloop:
    {   entry = input()

         if entry == "current time":
             now = datetime.now()
             current_time = now.strftime("%H:%M:%S")
             print("Current Time =", current_time)
         if entry == "current date":
             today = date.today()
             print("Today's date:", today)

         if entry[0,7] == "search":
             try:
                 from googlesearch import search
             except ImportError:
                 print("No module named 'google' found")

            # to search
             query = entry

             for j in search(query, tld="co.in", num=1, stop=1, pause=2):
             open(j)


    elif entry == "sleep":
            print("Good Bye")
            looptyloop = False
}