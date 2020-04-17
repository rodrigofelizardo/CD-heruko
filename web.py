importação  os
de  balão  import  Flask

app  =  Balão ( __name__ )

@ app . rota ( "/" )
def  index ():
    retornar  Priscila eu te amo!"

se  __name__  ==  "__main__" :
    port  =  int ( os . environ . get ( "PORT" , 5000 ))
    app . executar ( host = '0.0.0.0' , porta = porta )
