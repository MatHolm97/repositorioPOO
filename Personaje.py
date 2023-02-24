class Personaje:
    
    #constructor
    def __init__(self,esp,nom,alt):
        self.__especie= esp
        self.__nombre= nom
        self.__altura= alt
    
    #atriutos
    especie= "Humano"
    nombre= "Master chief"
    altura= "2.70"
    
    #metodos
    def correr(self,status):
        if(status):
            print("EL personaje "+ self.__nombre+ "esta corriendo")
        else:
            print("EL personaje "+ self.__nombre+ "no esta corriendo")
            
    def lanzarGranadas(self):
        print("El personaje "+ self.__nombre +"lanzo una granada")
        
    def recargarArma(self, municiones):
        cargador=10
        cargador= cargador + municiones
        print("El arma tiene " + str(cargador) + "balas")
        
        #declarar get y set
        
    def getNombre(self):
            return self.__nombre
    def setNombre(self,nom):
            self.__nombre= nom
            
    def getEspecie(self):
            return self.__especie
    def setEspecie(self,esp):
            self.__especie= esp
            
    def getAltura(self):
            return self.__altura
    def setAltura(self,alt):
            self.__altura= alt
        