import math, datetime

"""
1
Det är ca 470 km mellan Stockholm och Göteborg. 
Skriv ett program som räknar ut hur lång tid det tar att köra från Stockholm till Göteborg. 
Du behöver fråga användaren hur fort man ska köra, i km/h.
"""
distance = 470

try: 
    speed = int(input("What speed, in km/h, do you want to travel between Goteborg and Stockholm? >> "))
    
    print(f"Resan kommer att ta {(distance / speed):.1f} timmar.")
    print(f"Resan kommer att ta {((distance / speed)*60*60):.0f} sekunder.")
    print(f"Resan kommer att ta {((distance / speed)*60):.0f} minuter.")
    
    train_seconds = (distance / speed) *60 *60
    train_hours = train_seconds // (60*60)
    train_min = (train_seconds % (60*60)) / 60
    
    print(f"Resan kommer att ta {train_hours:.0f} timmar och {train_min:.0f} minuter.")
except:
    print("Sorry the train got stuck")
    
    
"""
2
Skriv ett program som räknar ut längden på hypotenusan i en rätvinklig triangel. 
Användaren behöver skriva in längden på de två kortare sidorna.
"""
print("""
              +
              | \\  Side X
       Side A |  \\
              +---+
              Side B
      """)

try:
    side_a = int(input("What is the length of side A? >> "))
    side_b = int(input("What is the length of side B? >> "))
    
    side_x = math.sqrt(side_a * side_a + side_b * side_b)
    
    print(f"Side X is of lenght: {side_x:.1f}.")
    
except:
    print("Sorry that is an square")
    
    
"""
3A
Skriv ett program som talar om dagens datum.
"""

date_today = datetime.datetime.today().strftime('%Y%b%d')
date_next_week = (datetime.datetime.strptime(date_today , "%Y%b%d") + datetime.timedelta(days=7)).strftime('%Y%b%d')

print(f"\nTodays is: {date_today}")
print(f"In 7 days it will be: {date_next_week}.")

