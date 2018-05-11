class Orig(object):
    def __init__(self):
        self.type = "orig"

class Tim(object):
    def __init__(self, foundation, arg):
        if isinstance(foundation, Orig):
            print("it is an Orig object")
        else:
            print('problem')
            
        for thing in arg:
            print("Parm:" + str(thing))

            
def callclass(name, *args):
    origobj = Orig()
    
    parmlist = []
    
    
    #parmlist = []

    for element in args:
        parmlist.append(element)
        #parmlist += element + ","
        
        
    #parmlist = parmlist[:len(parmlist)-1]
    #print(parmlist)
        
    new_frame = name(origobj, parmlist)
    #print("final return is " + str(new_frame))
          

argys = ['arg1', 'arg2']
callclass(Tim, 'arg1', 'arg2')

