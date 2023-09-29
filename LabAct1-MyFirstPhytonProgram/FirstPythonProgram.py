# Lumibao, Tom Peycee C.
# BSCS 1B
pound = float(input('Pounds = '))
print('Pounds (lbs) = ', pound)
Kilograms = float(pound * 0.45359237)
print('Converted to Kilograms (kg) = %.2f' % Kilograms)
print('================================================')
miles = float(input('Mile = '))
print('Miles (mi) = ', miles)
kilometers = float(miles * 1.609344)
print('Converted to kilometers (km) = %.2f' % kilometers)
print('================================================')
fahrenheit = float(input('Fahrenheit = '))
print('Fahrenheit (°F) = ', fahrenheit)
C = float(fahrenheit - 32)
celsius = float(C / 1.8)
print('Converted to Celsius (°C) = %.2f' % celsius)
print('================================================')
a, b, c, d, e, f, g, h, i, j = 18, 20, 21, 19, 17, 22, 16, 18, 23, 22
print('Age of student 1 : ', a)
print('Age of student 2 : ', b)
print('Age of student 3 : ', c)
print('Age of student 4 : ', d)
print('Age of student 5 : ', e)
print('Age of student 6 : ', f)
print('Age of student 7 : ', g)
print('Age of student 8 : ', h)
print('Age of student 9 : ', i)
print('Age of student 10 : ', j)
AgeSum = (a + b + c + d + e + f + g + h + i + j)
AverageAge = float(AgeSum / 10)
print('Average Age of the Students is : ', AverageAge)
print('================================================')
string = ("""{Mc} and his comrades. All having lost their place to belong in a broken world, these 
teenagers gradually realize that they are living in a dangerous society resembling a prison full of slavery,and 
injustice. They can't live with the system and can't live without it, and simply existing means they are at risk of 
being condemned to a life of slavery.In order to seek freedom, liberation and justice, they live dual lives as 
rebellious <{Band}>. Using a mysterious smartphone app, they undertake fantastical adventures by using otherworldly 
powers to enter the hearts of people in order to re-shape and transform them. they do it by giving a calling card to 
<{Ability}>.The Phantom Thieves realize that society forces people to wear masks to protect their inner vulnerabilities,
and by confronting their inner selves and by literally ripping off their protective mask do the heroes awaken their 
inner power, the <{Skill}>. using it to help those in need. Ultimately, the group of Phantom Thieves seeks <{Enemy}> the
master mind of all to change his heart and change their day-to-day world to match their perception, end slavery and see 
through the masks modern society wears.""".format(Mc='~Joker~', Band='Phantom Thieves of Heart',
                                                Ability='Steal their Hearts', Skill='Persona', Enemy='Masayoshi Shido'))
print(string)
