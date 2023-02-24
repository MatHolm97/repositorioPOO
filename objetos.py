
from Personaje import * 

#1 solicitar datos

print("")
print("#### datos heroe #")
especieH= input("Escribe la especie ")
nombreH= input("Escribe el nombre") 
alturaH= float(input("Escribe la altura")) 
recargarH= int(input("Cunatas balas "))

print("")
print("##### datos #")
especieV= input("Escribe la especie ")
nombreV= input("Escribe el nombre")
alturaV= float(input("Escribe la altura"))
recargarV= int(input("Cunatas balas "))

#2 crear objeto de la clase Personaeje

heroe= Personaje(especieH,nombreH,alturaH)
villano= Personaje(especieV,nombreV,alturaV)

#3 usar atriutos jiji



print("")
print("El personaje se llama: "+ heroe.getNombre())
print("El personaje es: "+ heroe.getEspecie())
print("El personaje mide: "+ str(heroe.getAltura())) 

print("")
print("El personaje se llama: "+ villano.getNombre())
print("El personaje es: "+ villano.getEspecie())
print("El personaje mide: "+ str(villano.getAltura()))


#usar metodos

heroe.correr(True)
heroe.lanzarGranadas()
heroe.recargarArma(recargarH)

villano.correr(True)
villano.lanzarGranadas()
villano.recargarArma(recargarH)