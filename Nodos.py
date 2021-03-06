class Nodos:
    def __init__( self ) :
        self.datos=[]
        
    def agregar(self,dato):
        self.datos.append(dato)

    def agregarDcl(self,dato,dato1):
        tmp={'type':dato.get('type'),'val':dato1.get('val')}
        self.datos.append(tmp)

    def agregarPrint(self,dato,dato1):
        tmp={'type':dato.get('type'),'val':dato1.get('val')}
        self.datos.append(tmp)

    def agregarAssign(self,dato,dato1,dato2):
        tmp={'type':dato1.get('type'),'val':dato.get('val'),'val1':dato2.get('val')}
        self.datos.append(tmp)

    def agregarSumYRes(self,dato,dato1):
        tmp={'type':dato.get('type'),'val':dato1.get('val')}
        self.datos.append(tmp)  

    def imprimir(self):
        print('Datos en nodos')
        contadorTabs=0
        for i in range(len(self.datos)):
            if self.datos[i].get('type')=='plus' or self.datos[i].get('type')=='minus':
                contadorTabs=contadorTabs+1
            else:
                contadorTabs=0
            tabs=""
            for j in range(contadorTabs):
                tabs+='\t'
            print(f'{tabs} {self.datos[i]}')
        #print(self.datos)

   

    def codigo3(self):
        valido = True
        codigo3Dir=''
        print()
        print("Codigo 3 direcciónes")
        floats=[]
        ints=[]
        arreglo=[]
        string=""
        for i in range(len(self.datos)-1,-1,-1):
            if(self.datos[i].get('type')=='assign' or self.datos[i].get('type')=='plus' or self.datos[i].get('type')=='minus'):
                if(self.datos[i].get('type')=='plus'):
                    string=string+" + "+self.datos[i].get('val')
                elif(self.datos[i].get('type')=='minus'):
                    string=string+" + "+self.datos[i].get('val')
                elif(self.datos[i].get('type')=='assign'):
                    string=self.datos[i].get('val')+" = "+ self.datos[i].get('val1')+string
                    arreglo.append(string)
                    string=""
                else:
                    exit()
            elif self.datos[i].get('type')=='floatdcl':
                floats.append(self.datos[i].get('val'))
            elif self.datos[i].get('type')=='intdcl':
                ints.append(self.datos[i].get('val'))
    
        
        r=0
        for i in range(1,len(arreglo)+1):
            dividido=arreglo[-i].split(' ')
            if len(dividido)>3:
                
                sonFloats=False
                for j in range(2,len(dividido),2):
                    if dividido[j] in floats:
                        sonFloats=True
                    elif dividido[j] in ints:
                        1
                    else:
                        try:
                            int(dividido[j])
                        except:
                            sonFloats=True
                
                if(sonFloats): 
                    for j in range(2,len(dividido),2):
                        if not (dividido[j] in floats or dividido[j] in ints):
                            try:
                                dividido[j]=str(float(dividido[j]))
                            except:
                                1
                
                stack=[]
                for j in dividido:
                    stack.append(j)
                a1=stack.pop()
                signo=stack.pop()
                
                try:
                    int(a1)
                except:
                    try:
                        float(a1)
                    except:
                        if not (a1 in ints or a1 in floats):
                            valido=False                    
                
                codigo3Dir+=f'r{r}={stack.pop()}{signo}{a1}\n'
                r+=1
                while(not (stack[len(stack)-1] == '=')):                    
                    signo=stack.pop()
                    a1=stack.pop()

                    try:
                        int(a1)
                    except:
                        try:
                            float(a1)
                        except:
                            if not (a1 in ints or a1 in floats):
                                valido=False                    

                    codigo3Dir+=(f'r{r}=r{r-1}{signo}{a1}\n')
                    r+=1
                stack.pop()
                codigo3Dir+=(f'{stack.pop()}=r{r}\n')
            else:
                if not (dividido[0] in ints or dividido[0] in floats):
                    valido=False
                try: 
                    int(dividido[2])
                except:
                    try:
                        float(dividido[2])
                    except:
                        if not (dividido[2] in ints or dividido[2] in floats):
                            valido=False                    
                codigo3Dir+=(f'{dividido[0]} {dividido[1]} {dividido[2]}\n')
        if valido:
            print(codigo3Dir)
        else:
            print('Error semantico')
        return 1       

    

def main():
    prueba=Nodos()
    a={'type':'float'}
    b={'type':'id', 'val':'a'}
    prueba.agregarDcl(a,b)
    prueba.agregarDcl(a,b)
    prueba.imprimir()




    
