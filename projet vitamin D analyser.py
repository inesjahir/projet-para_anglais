# projet vitamin D analyser .
print ("bonjour , bienvenue dans ce 'vitamin analyser' veuillez introduire les donnees suivantes :  ")
quantitedesang =(float(input("quel est quantite de sang de cet echantillon?")))
quantitevitaminD=(float(input("quel quantite de vitamin D a ete trouve dans cet echantillon ?")))

concentration =(float(quantitevitaminD/quantitedesang))


print ("la concentration est de :" +str (concentration) + " ng/ml") 


if  concentration <=10 :
   print ("diagnostic ""=>"" ""en"" ""deficience")
   
if  concentration <=30 :
    print ("diagnostic ""=>"" ""en"" ""insuffisance")
    
if  concentration >30 :
    print ("diagnostic ""=>"" ""en"" ""suffisance")
    
elif concentration >100:
    print ("diagnostic ""=>"" ""en"" ""exces")
     
    
    
   
  
    
    
