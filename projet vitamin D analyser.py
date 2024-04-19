 # projet vitamin D analyser .
print ("bonjour , bienvenue dans ce 'vitamin analyser' veuillez introduire les donnees suivantes :  ")
quantitedesang =(float(input("quel est quantite de sang de cet echantillon?")))
quantitevitaminD=(float(input("quel quantite de vitamin D a ete trouve danscet echantillon ?")))

concentration =(float(quantitevitaminD/quantitedesang))


print ("la concentration est de :" +str (concentration) + " ng/ml") 


if  concentration <=10 :
   print ("diagnostic ""=>"" ""en"" ""deficience")
   
if  concentration <=30 or concentration >10 :
    print ("diagnostic ""=>"" ""en"" ""insuffisance")
    
if concentration <100 or concentration >30 :
    print ("diagnostic ""=>"" ""en"" ""suffisance")
    
else:
    print ("diagnostic ""=>"" ""en"" ""exces")
    
    
    
   
  
    
    
