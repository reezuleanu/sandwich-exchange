# LINK: http://34.155.116.22/



# Salut!

### TL;DR :
sunt mult chestii pe care le-am facut prost la inceput si nu am mai avut timp sa le refac, dar aplicatia este functionala si sunt satisfacut de ce am putut sa fac intr-o saptamana cu ce am invatat si de la academie. dati docker-compose up pentru cea mai putina bataie de cap

### Instructiuni de utilizare:
sincer, doar folositi docker-compose, e cel mai usor. L-am testat si functioneaza, singura problema ar fi ca o sa fie accesibile si de pe alte calculatoare (o sa fie o problema doar daca nu vreti asta)

Deoarece probabil nu la asta v-ati asteptat cand mi-ati dat exercitiu de facut aplicatie in dash, cred ca ar fi ok sa explic
cum am interpretat eu cerinta, si mai bine, cum am indeplinit-o

### Cum am indeplinit cerintele minime:

#### API: aici nu cred ca trebuie explicat, are cate o functie pentru CRUD si inca cateva functii mai specifice

#### Web Application:
• displaying all objects in a list or table format - click pe stocks sau mers la /stonks/, acolo apar toate sendvisurile de pe platforma, si poti da click pe ele
pentru a merge la pagina lor

• searching for a specific object in this list or table - functia de search

• deleting an object from this list or table - click pe butonul de delete din /stonks/

• creating a new object and viewing it in the list/table - click pe create, sau pe butonul de create din /stonks/


### Probleme:

- importurile sunt varza, foloseam path.append pana m-au ajuns pacatele din urma si nu mai mergeau chestii

- pe langa import uri, si organizarea e varza, daca ma puneam sa repar totul ramaneam fara timp

- incercasem sa lucrez cu un .env, dar am renuntat, programul ia link uri si port uri direct din environment, si sunt setate in dockerfile si docker-compose

- in pagina de index (path /), cele 5 grafice sunt o aplicatie dash intreaga, aia a fost prima incercare de a integra dash intr-un server flask, si nu am mai apucat
sa fac sa fie fiecare grafic o aplicatie separata

- aplicatia dash de top 5 se actualizeaza doar la pornirea serverului, deci daca apare un sendvis si mai tare, nu o sa apara pe prima pagina decat la restartarea serverului,
will fix in the future

- am am incercat sa folosesc bootstrap, dar nu am reusit in totalitate. Pe scurt, SITE UL NU ESTE UTILIZABIL PE ECRANE MAI MICI. 

- tot css ul este inline

- imaginile de docker copiaza tot repo ul pentru ca nu am pus toate fisierele comune separat, trebuie optimizat

- erau multe locuri unde era mult mai usor sa folosesc javascript, dar am folosit python prin jinja2 pentru ca nu mai tin minte nimic despre javascript



### Ce nu am apucat sa fac (si s-ar putea sa fac in viitor):

- testele necesita sa fie pornit api ul si o baza de date, asa ca ar fi dificil sa implementez CI si CD in conditia lor actuala, dar e ceva ce o sa fac probabil dupa ce mai organizez codul si structura repo ului

- api ul este expus lumii, si am o clasa de token. Voiam sa folosesc o functie in folder ul dependencies care sa verifice token ul din fiecare api call,
scopul era sa aibe aplicatie web un token, dar sa pot faci si alte token uri pentru api ca sa poata fi folosit si inafara aplicatiei web, asa cum sunt
majoritatea api urilor vazute de mine facute (ca cele de vreme). Nu am mai apucat, acum doar accepta orice call

- voiam sa fac si ceva cu useri in aplicatia web, sa te poti loga, sa ai un sold, sa poti cumpara si vinde actiuni de sendvis (abia acum realizez cat de ridicol suna), etc.
Nu am mai apucat, dar mai sunt urme de aceasta idee in html, unde "Log in" e rendered daca nu are date despre utilizator

- voiam sa fac un simulator pentru api care trecea prin fiecare istoric de preturi si daca era o diferenta intre data ultimului pret si data actuala, ar fi generat date pentru diferenta


Categoric am uitat sa mai mentionez chestii. Orice e neclar, sunt mereu disponibil sa raspund.
