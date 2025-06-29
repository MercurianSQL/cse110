"""
Author: Marinda Keller
Purpose: Compute the wind chill at multiple velocities for a user-input temperature.
"""

def wind_chill_factor(temperature, windspeed):
    windchill = (35.74 + (0.6215 * temperature)) - (35.75 * (windspeed ** 0.16)) + (0.4275 * (temperature * (windspeed ** 0.16)))
    windchill = round(windchill, 2)
    #print(windchill) # for testing
    return windchill


#temperature = float(8) # for testing
temperature = float(input("What is the temperature? "))
#print(temperature) # for testing
scale = (input("Fahrenheit or Celsius (F/C)? ").upper())
if scale == "C":
    temperature_c = temperature
    temperature_f = round(((temperature_c * 1.8) + 32), 2)
    print(f"{temperature_f} degreed F is equavalent to {temperature} degrees C")
    temperature = temperature_f
    scale = "F"
else:
    print()
#print(scale) #for testing
#windspeed = int(10) # for testing
windspeed = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
for speed in windspeed:
    #print(temperature, speed) # for testing
    windchill = wind_chill_factor(temperature, speed) 
    print(f"At {temperature} degrees {scale}, and wind at {speed} mph, the windchill makes it feel like {windchill} degrees {scale}.")

    

# Requirements
# [x] 1 Write a function to calculate and return the wind chill based on a given temperature and wind speed.
# [x] 2 Write a function to convert from Celsius to Fahrenheit and return the converted temperature. 
# The formula for this conversion is to multiply the Celsius temperature by (9/5) and then add 32.
# [x] 3 Allow the user to enter the temperature in Celsius or Fahrenheit. 
# If they provide it in Celsius, first convert it to Fahrenheit 
# (using the conversion function created above) before using the formula above.
# [x] 4 Loop through wind speeds from 5 to 60 miles per hour, incrementing by 5, and 
# [x] 4b calculate and display the wind chill (using the windchill function created above) for each of these wind speeds.
# [x] 5 Display the wind chill value to 2 decimals of precision.

"""
°F = (°C * 9/5) + 32.
°C = (°F - 32) * 5/9.

Wind Chill (ºF) = 35.74 + 0.6215T - 35.75(V0.16) + 0.4275T(V0.16)
Where,T= Air Temperature (ºF) V= Wind Speed (mph)

When done correctly:
What is the temperature? 8
Fahrenheit or Celsius (F/C)? F
At temperature 8.0F, and wind speed 5 mph, the windchill is: -1.11F
At temperature 8.0F, and wind speed 10 mph, the windchill is: -6.02F
At temperature 8.0F, and wind speed 15 mph, the windchill is: -9.15F
At temperature 8.0F, and wind speed 20 mph, the windchill is: -11.50F
At temperature 8.0F, and wind speed 25 mph, the windchill is: -13.40F
At temperature 8.0F, and wind speed 30 mph, the windchill is: -15.00F
At temperature 8.0F, and wind speed 35 mph, the windchill is: -16.39F
At temperature 8.0F, and wind speed 40 mph, the windchill is: -17.62F
At temperature 8.0F, and wind speed 45 mph, the windchill is: -18.73F
At temperature 8.0F, and wind speed 50 mph, the windchill is: -19.74F
At temperature 8.0F, and wind speed 55 mph, the windchill is: -20.67F
At temperature 8.0F, and wind speed 60 mph, the windchill is: -21.53F

What is the temperature? -10
Fahrenheit or Celsius (F/C)? C
At temperature 14.0F, and wind speed 5 mph, the windchill is: 5.93F
At temperature 14.0F, and wind speed 10 mph, the windchill is: 1.42F
At temperature 14.0F, and wind speed 15 mph, the windchill is: -1.47F
At temperature 14.0F, and wind speed 20 mph, the windchill is: -3.63F
At temperature 14.0F, and wind speed 25 mph, the windchill is: -5.38F
At temperature 14.0F, and wind speed 30 mph, the windchill is: -6.85F
At temperature 14.0F, and wind speed 35 mph, the windchill is: -8.13F
At temperature 14.0F, and wind speed 40 mph, the windchill is: -9.27F
At temperature 14.0F, and wind speed 45 mph, the windchill is: -10.29F
At temperature 14.0F, and wind speed 50 mph, the windchill is: -11.22F
At temperature 14.0F, and wind speed 55 mph, the windchill is: -12.07F
At temperature 14.0F, and wind speed 60 mph, the windchill is: -12.87F
"""