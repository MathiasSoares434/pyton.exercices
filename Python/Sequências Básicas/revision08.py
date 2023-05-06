distance= float(input('Digite o número da distância em metros: '))
kilometers= distance/1000
hectometers= distance/100
dekameters= distance/10
decimeters= distance*10
centimeters= distance*100
milimeters= distance*1000

print(f'{distance}m vale: {kilometers}km, {hectometers}hm, {dekameters}dm, {decimeters}dcm, {centimeters}cm e {milimeters}mm')