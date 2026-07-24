"""
Capstone Content Generator — Offline Structured Database
"""
import random


def _rnd_phone(country):
    if country == "France":
        return f"+33 6 {random.randint(10,99)} {random.randint(10,99)} {random.randint(10,99)} {random.randint(10,99)}"
    elif country == "Belgique":
        return f"+32 4{random.randint(70,99)} {random.randint(10,99)} {random.randint(10,99)} {random.randint(10,99)}"
    elif country == "Ghana":
        p = random.choice(['24','20','26','27','54','55'])
        return f"+233 {p} {random.randint(100,999)} {random.randint(1000,9999)}"
    elif country == "Ireland":
        p = random.choice(['3','5','6','7'])
        return f"+353 8{p} {random.randint(100,999)} {random.randint(1000,9999)}"
    return f"+33 6 {random.randint(10,99)} {random.randint(10,99)} {random.randint(10,99)} {random.randint(10,99)}"

POOL = {
    "France": {
        "cities": [
            {"city":"Lyon","address":"14 Rue de la Part-Dieu","uni":"Université Claude Bernard Lyon 1","lycee":"Lycée du Parc, Lyon","stage":"Métropole de Lyon, Direction Environnement"},
            {"city":"Toulouse","address":"8 Allée Jean Jaurès","uni":"Université Paul Sabatier, Toulouse","lycee":"Lycée Pierre de Fermat, Toulouse","stage":"Direction Régionale de l\'Environnement, Toulouse"},
            {"city":"Bordeaux","address":"22 Cours de l\'Intendance","uni":"Université de Bordeaux, UFR Sciences","lycee":"Lycée Montaigne, Bordeaux","stage":"Bordeaux Métropole, Service Climat"},
            {"city":"Nantes","address":"5 Rue de Strasbourg","uni":"Université de Nantes","lycee":"Lycée Clemenceau, Nantes","stage":"Nantes Métropole, Direction Transition Écologique"},
            {"city":"Strasbourg","address":"18 Place Kléber","uni":"Université de Strasbourg","lycee":"Lycée Fustel de Coulanges, Strasbourg","stage":"Eurométropole de Strasbourg, Pôle Environnement"},
            {"city":"Rennes","address":"11 Rue de la Monnaie","uni":"Université de Rennes 1, UFR Sciences","lycee":"Lycée Émile Zola, Rennes","stage":"Rennes Métropole, Direction Énergie Climat"},
            {"city":"Montpellier","address":"3 Place de la Comédie","uni":"Université de Montpellier","lycee":"Lycée Joffre, Montpellier","stage":"Montpellier Méditerranée Métropole, Service Environnement"},
            {"city":"Grenoble","address":"9 Rue Félix Poulat","uni":"Université Grenoble Alpes","lycee":"Lycée Champollion, Grenoble","stage":"Grenoble Alpes Métropole, Direction Énergie"},
        ],
        "companies": [
            {"name":"EDF Renouvelables","poste_en":"Intern - Solar Project Assistant","desc_en":"EDF Renewables develops large-scale solar and wind projects in France.","skills_en":["Solar PV energy","Excel and analysis tools","Project management","Analytical skills"],"formation_en":"Bachelor\'s in energy or engineering","exp_en":["Energy coursework","Solar academic project","Excel proficiency","Teamwork experience"]},
            {"name":"Engie Green","poste_en":"Intern - Wind Environmental Studies","desc_en":"Engie Green is France\'s leading renewable energy producer. This internship focuses on environmental impact studies for wind farms.","skills_en":["Ecology and biodiversity","GIS tools","Technical writing","Teamwork"],"formation_en":"Bachelor\'s in environment or geography","exp_en":["Interest in biodiversity","Writing skills","Climate awareness","Adaptability"]},
            {"name":"TotalEnergies Renouvelables","poste_en":"Intern - Wind Energy Engineer","desc_en":"TotalEnergies develops onshore and offshore wind farms. This internship focuses on turbine optimization.","skills_en":["Wind energy","Python or MATLAB","Industrial environment","Scientific rigor"],"formation_en":"Master\'s in engineering","exp_en":["Fluid mechanics coursework","Numerical simulation","Python programming","Scientific methodology"]},
            {"name":"Voltalia","poste_en":"Intern - Solar Project Manager","desc_en":"Voltalia is an independent renewable energy producer in 20 countries, developing solar plants in France.","skills_en":["Solar system sizing","Mapping and AutoCAD","Communication","Organization"],"formation_en":"Bachelor\'s in renewable energy","exp_en":["Renewable energy training","Solar installation project","Event organization","Academic presentations"]},
            {"name":"Neoen","poste_en":"Intern - Solar Performance Analyst","desc_en":"Neoen is a leading global independent renewable energy producer. This internship involves solar plant performance analysis.","skills_en":["Data analysis","Advanced Excel and Power BI","Solar energy","Attention to detail"],"formation_en":"Master\'s in data science or energy","exp_en":["Data visualization projects","Advanced Excel skills","Energy systems coursework","Data competition experience"]},
            {"name":"Akuo Energy","poste_en":"Intern - Solar Farm Developer","desc_en":"Akuo Energy is a French independent renewable energy producer developing solar, wind and biomass projects across 20 countries.","skills_en":["Solar project development","Land assessment and planning","Stakeholder management","Environmental compliance"],"formation_en":"Bachelor's in Energy or Environmental Science","exp_en":["Renewable energy coursework","Planning or assessment experience","Communication skills","Environmental regulation awareness"]},
            {"name":"Boralex","poste_en":"Intern - Wind Energy Analyst","desc_en":"Boralex is a major wind energy developer in France with over 3 GW of installed capacity, focusing on onshore wind and solar across Europe.","skills_en":["Wind resource assessment","Data analysis and visualization","Energy market understanding","Technical reporting"],"formation_en":"Bachelor's in Engineering or Data Science","exp_en":["Wind energy knowledge","Data analysis with Python or Excel","Understanding of energy markets","Report writing experience"]},
            {"name":"Valorem","poste_en":"Intern - Wind Project Development","desc_en":"Valorem is an independent wind and solar developer in France, conducting feasibility studies for new wind projects.","skills_en":["Environmental law","Office tools","Administrative writing","Stakeholder dialogue"],"formation_en":"Bachelor\'s in environment or law","exp_en":["Environmental policy coursework","Local government experience","Structured report writing","Public consultation experience"]},
        ],
    },
    "Belgique": {
        "cities_en": [
            {"city":"Leuven","address":"37 Main Street, Leuven","uni":"KU Leuven","lycee":"Montgomery International School","stage":"SPW Énergie, Leuven"},
            {"city":"Ghent","address":"40 Main Street, Ghent","uni":"Ghent University","lycee":"Bogaerts International School","stage":"SPW Énergie, Ghent"},
            {"city":"Louvain-la-Neuve","address":"29 Main Street, Louvain-la-Neuve","uni":"Université catholique de Louvain","lycee":"Brussels International Catholic School","stage":"SPW Énergie, Louvain-la-Neuve"},
            {"city":"Brussels","address":"30 Main Street, Brussels","uni":"Vrije Universiteit Brussel","lycee":"St. John’s International School","stage":"SPW Énergie, Brussels"},
            {"city":"Brussels","address":"41 Main Street, Brussels","uni":"Université libre de Bruxelles","lycee":"BEPS International School","stage":"SPW Énergie, Brussels"},
            {"city":"Antwerp","address":"38 Main Street, Antwerp","uni":"University of Antwerp","lycee":"EEBA European School of Brussels","stage":"SPW Énergie, Antwerp"},
            {"city":"Liège","address":"12 Main Street, Liège","uni":"University of Liège","lycee":"International School Ghent","stage":"SPW Énergie, Liège"},
            {"city":"Hasselt","address":"23 Main Street, Hasselt","uni":"Hasselt University","lycee":"Internationale Deutsche Schule Brüssel","stage":"SPW Énergie, Hasselt"},
            {"city":"Mons","address":"9 Main Street, Mons","uni":"University of Mons","lycee":"ISF Waterloo International School","stage":"SPW Énergie, Mons"},
            {"city":"Namur","address":"20 Main Street, Namur","uni":"University of Namur","lycee":"The British International School","stage":"SPW Énergie, Namur"},
            {"city":"Mechelen","address":"7 Main Street, Mechelen","uni":"Thomas More University of Applied Sciences","lycee":"The British School of Brussels","stage":"SPW Énergie, Mechelen"},
            {"city":"Antwerp","address":"42 Main Street, Antwerp","uni":"AP University of Applied Sciences and Arts","lycee":"BEPS International School Secondary Campus","stage":"SPW Énergie, Antwerp"},
            {"city":"Ghent","address":"47 Main Street, Ghent","uni":"Artevelde University of Applied Sciences","lycee":"European School Brussels I","stage":"SPW Énergie, Ghent"},
            {"city":"Antwerp","address":"24 Main Street, Antwerp","uni":"KdG University of Applied Sciences and Arts","lycee":"European School Brussels II","stage":"SPW Énergie, Antwerp"},
            {"city":"Hasselt","address":"5 Main Street, Hasselt","uni":"PXL University of Applied Sciences and Arts","lycee":"European School Brussels III","stage":"SPW Énergie, Hasselt"},
            {"city":"Brussels","address":"17 Main Street, Brussels","uni":"Odisee University of Applied Sciences","lycee":"European School Brussels IV","stage":"SPW Énergie, Brussels"},
            {"city":"Leuven","address":"11 Main Street, Leuven","uni":"UCLL University of Applied Sciences","lycee":"International Montessori School","stage":"SPW Énergie, Leuven"},
            {"city":"Bruges","address":"41 Main Street, Bruges","uni":"VIVES University of Applied Sciences","lycee":"International School of Flanders","stage":"SPW Énergie, Bruges"},
            {"city":"Kortrijk","address":"1 Main Street, Kortrijk","uni":"Howest University of Applied Sciences","lycee":"Montgomery International School Antwerp","stage":"SPW Énergie, Kortrijk"},
            {"city":"Liège","address":"47 Main Street, Liège","uni":"HEC Liège","lycee":"Antwerp International School","stage":"SPW Énergie, Liège"},
            {"city":"Brussels","address":"32 Main Street, Brussels","uni":"Haute École Léonard de Vinci","lycee":"International School of Leuven","stage":"SPW Énergie, Brussels"},
            {"city":"Brussels","address":"23 Main Street, Brussels","uni":"EPHEC","lycee":"Louvain International School","stage":"SPW Énergie, Brussels"},
            {"city":"Brussels","address":"38 Main Street, Brussels","uni":"Haute École Bruxelles-Brabant","lycee":"Bogaerts International School South Campus","stage":"SPW Énergie, Brussels"},
            {"city":"Liège","address":"37 Main Street, Liège","uni":"Haute École de la Province de Liège","lycee":"Ecole Internationale Le Verseau","stage":"SPW Énergie, Liège"},
            {"city":"Brussels","address":"25 Main Street, Brussels","uni":"Royal Military Academy","lycee":"British International School of Brussels (junior)","stage":"SPW Énergie, Brussels"},
            {"city":"Brussels","address":"47 Main Street, Brussels","uni":"Haute École Francisco Ferrer","lycee":"Da Vinci International School Antwerp","stage":"SPW Énergie, Brussels"},
            {"city":"Brussels","address":"10 Main Street, Brussels","uni":"Haute École Galilée","lycee":"International School of Tervuren","stage":"SPW Énergie, Brussels"},
            {"city":"Brussels","address":"30 Main Street, Brussels","uni":"Haute École Lucia de Brouckère","lycee":"St. Paul’s British Primary School","stage":"SPW Énergie, Brussels"},
            {"city":"Brussels","address":"2 Main Street, Brussels","uni":"Haute École ICHEC-ECAM-ISFSC","lycee":"Christian International School of Brussels","stage":"SPW Énergie, Brussels"},
            {"city":"Namur","address":"40 Main Street, Namur","uni":"Haute École Albert Jacquard","lycee":"International School of Mons","stage":"SPW Énergie, Namur"},
            {"city":"Liège","address":"5 Main Street, Liège","uni":"Haute École Charlemagne","lycee":"Ghent International School","stage":"SPW Énergie, Liège"},
            {"city":"Liège","address":"28 Main Street, Liège","uni":"Haute École de la Ville de Liège","lycee":"Ecole Européenne de Bruxelles-Argenteuil","stage":"SPW Énergie, Liège"},
            {"city":"Libramont","address":"2 Main Street, Libramont","uni":"Haute École Robert Schuman","lycee":"Sint-John’s International School Waterloo","stage":"SPW Énergie, Libramont"},
            {"city":"Liège","address":"39 Main Street, Liège","uni":"HELMo","lycee":"Ecole Internationale Montgomery","stage":"SPW Énergie, Liège"},
            {"city":"Mons","address":"27 Main Street, Mons","uni":"Haute École Condorcet","lycee":"Ecole Internationale Kingsdale","stage":"SPW Énergie, Mons"},
            {"city":"Mons","address":"11 Main Street, Mons","uni":"Haute École Louvain en Hainaut","lycee":"Ecole Internationale Providence","stage":"SPW Énergie, Mons"},
            {"city":"Mons","address":"8 Main Street, Mons","uni":"Haute École en Hainaut","lycee":"Ecole Internationale Bascule","stage":"SPW Énergie, Mons"},
            {"city":"Charleroi","address":"12 Main Street, Charleroi","uni":"Haute École Provinciale de Hainaut - Condorcet","lycee":"Ecole Internationale SIBS","stage":"SPW Énergie, Charleroi"},
            {"city":"Namur","address":"49 Main Street, Namur","uni":"Haute École de Namur-Liège-Luxembourg","lycee":"International School of Belgium","stage":"SPW Énergie, Namur"},
            {"city":"Brussels","address":"48 Main Street, Brussels","uni":"LUCA School of Arts","lycee":"Ecole Internationale Le Monde","stage":"SPW Énergie, Brussels"},
            {"city":"Antwerp","address":"11 Main Street, Antwerp","uni":"Karel de Grote University of Applied Sciences and Arts","lycee":"Bilingual International School of Brussels","stage":"SPW Énergie, Antwerp"},
            {"city":"Brussels","address":"22 Main Street, Brussels","uni":"Erasmus University College Brussels","lycee":"Ecole Internationale Champagnat","stage":"SPW Énergie, Brussels"},
            {"city":"Ghent","address":"49 Main Street, Ghent","uni":"HOGENT University of Applied Sciences and Arts","lycee":"Ecole Internationale Edelweiss","stage":"SPW Énergie, Ghent"},
            {"city":"Hasselt","address":"18 Main Street, Hasselt","uni":"UC Leuven-Limburg","lycee":"Ecole Internationale Les Petits Moussaillons","stage":"SPW Énergie, Hasselt"},
            {"city":"Geel","address":"22 Main Street, Geel","uni":"Thomas More Kempen","lycee":"Ecole Internationale Le Petit Monde","stage":"SPW Énergie, Geel"},
            {"city":"Turnhout","address":"35 Main Street, Turnhout","uni":"Thomas More Turnhout","lycee":"Ecole Internationale Jardin d’Enfants","stage":"SPW Énergie, Turnhout"},
            {"city":"Aalst","address":"33 Main Street, Aalst","uni":"Odisee Aalst Campus","lycee":"Ecole Internationale Le P’tit Bouchon","stage":"SPW Énergie, Aalst"},
            {"city":"Hasselt","address":"45 Main Street, Hasselt","uni":"PXL Education Campus","lycee":"Ecole Internationale Les Coccinelles","stage":"SPW Énergie, Hasselt"},
            {"city":"Kortrijk","address":"29 Main Street, Kortrijk","uni":"VIVES Kortrijk Campus","lycee":"Ecole Internationale Les Papillons","stage":"SPW Énergie, Kortrijk"},
            {"city":"Bruges","address":"31 Main Street, Bruges","uni":"Howest Bruges Campus","lycee":"International School of Brussels","stage":"SPW Énergie, Bruges"}
        ],
        "companies": [
            {"name":"Luminus (EDF Belgique)","poste_en":"Intern - Wind Project Development","desc_en":"Luminus is Belgium\'s second-largest electricity producer. This internship covers wind farm development.","skills_en":["Onshore wind energy","Project management","Regulatory analysis","Bilingual communication"],"formation_en":"Bachelor\'s in energy or engineering","exp_en":["Environmental science education","Academic renewable energy project","Analysis tools","Multicultural teamwork"]},
            {"name":"Eneco Belgium","poste_en":"Intern - Solar Energy Analyst","desc_en":"Eneco Belgium develops solar and wind projects. This internship covers solar performance analysis.","skills_en":["Energy data analysis","Excel and monitoring","Solar PV knowledge","Analytical thinking"],"formation_en":"Bachelor\'s in engineering","exp_en":["Energy systems coursework","Data analysis with Excel","Energy transition interest","International teamwork"]},
            {"name":"Storm","poste_en":"Intern - Citizen Wind Project","desc_en":"Storm is a Belgian citizen wind project developer that encourages local participation and benefit sharing.","skills_en":["Wind projects","Citizen consultation","GIS mapping","Autonomy"],"formation_en":"Bachelor\'s in environment","exp_en":["Environmental science","Social communication","Collaborative projects","Social economy interest"]},
            {"name":"Aspiravi","poste_en":"Intern - Wind Farm Development","desc_en":"Aspiravi is a Belgian renewable energy company developing and operating onshore wind farms across Flanders and Wallonia.","skills_en":["Wind energy development","Environmental permitting","Community engagement","GIS analysis"],"formation_en":"Bachelor's in Environmental Science or Engineering","exp_en":["Wind energy coursework","Environmental regulation knowledge","Community outreach experience","Spatial analysis skills"]},
            {"name":"Parkwind","poste_en":"Intern - Offshore Wind Engineering","desc_en":"Parkwind is a Belgian offshore wind developer with over 1 GW of operational capacity in the North Sea, pioneering large-scale offshore wind in Europe.","skills_en":["Offshore engineering","Marine environmental assessment","Project scheduling","Technical analysis"],"formation_en":"Bachelor's or Master's in Marine or Mechanical Engineering","exp_en":["Marine environment knowledge","Engineering project experience","Data analysis capability","Interest in offshore energy"]},
            {"name":"Elicio","poste_en":"Intern - Renewable Energy Analyst","desc_en":"Elicio develops, builds, and operates wind farms and solar parks in Belgium and internationally, with a focus on sustainable energy production.","skills_en":["Energy market analysis","Financial modelling basics","Wind and solar resource assessment","Reporting and documentation"],"formation_en":"Bachelor's in Energy, Finance or Engineering","exp_en":["Energy systems knowledge","Spreadsheet and analytical skills","Interest in energy markets","Clear written communication"]},
            {"name":"Windvision","poste_en":"Intern - Solar and Wind Operations","desc_en":"Windvision is an independent Belgian renewable energy company that develops, constructs and operates wind and solar projects across Europe.","skills_en":["Renewable energy operations","Performance monitoring","Maintenance coordination","Health and safety awareness"],"formation_en":"Bachelor's in Engineering or Energy","exp_en":["Renewable energy training","Operational monitoring experience","Organizational skills","Safety-aware mindset"]},
            {"name":"Electrabel (Engie Belgique)","poste_en":"Intern - Wind Turbine Maintenance","desc_en":"Electrabel is Belgium\'s largest electricity producer. This internship covers preventive wind turbine maintenance.","skills_en":["Industrial maintenance","SCADA systems","Outdoor work","Safety standards"],"formation_en":"Bachelor\'s in mechanical engineering","exp_en":["Engineering training","Laboratory projects","Safety protocols","Industrial site experience"]},
        ],
    },
    "Ghana": {
        "cities_en": [
            {"city":"Legon","address":"18 Main Street, Legon","uni":"University of Ghana","lycee":"St. Thomas Aquinas SHS","stage":"Energy Commission of Ghana, Legon"},
            {"city":"Kumasi","address":"3 Main Street, Kumasi","uni":"Kwame Nkrumah University of Science and Technology","lycee":"Kumasi High School","stage":"Energy Commission of Ghana, Kumasi"},
            {"city":"Cape Coast","address":"36 Main Street, Cape Coast","uni":"University of Cape Coast","lycee":"Mfantsipim School","stage":"Energy Commission of Ghana, Cape Coast"},
            {"city":"Winneba","address":"6 Main Street, Winneba","uni":"University of Education, Winneba","lycee":"Winneba Senior High School","stage":"Energy Commission of Ghana, Winneba"},
            {"city":"Tamale","address":"1 Main Street, Tamale","uni":"University for Development Studies","lycee":"Tamale SHS","stage":"Energy Commission of Ghana, Tamale"},
            {"city":"Accra","address":"11 Main Street, Accra","uni":"University of Professional Studies, Accra","lycee":"Ghana International School","stage":"Energy Commission of Ghana, Accra"},
            {"city":"Tarkwa","address":"28 Main Street, Tarkwa","uni":"University of Mines and Technology","lycee":"Tarkwa Senior High School","stage":"Energy Commission of Ghana, Tarkwa"},
            {"city":"Ho","address":"36 Main Street, Ho","uni":"University of Health and Allied Sciences","lycee":"Mawuli School","stage":"Energy Commission of Ghana, Ho"},
            {"city":"Sunyani","address":"3 Main Street, Sunyani","uni":"University of Energy and Natural Resources","lycee":"St. James Seminary SHS","stage":"Energy Commission of Ghana, Sunyani"},
            {"city":"Navrongo","address":"4 Main Street, Navrongo","uni":"C.K. Tedam University for Technology and Applied Sciences","lycee":"Notre Dame Seminary SHS","stage":"Energy Commission of Ghana, Navrongo"},
            {"city":"Wa","address":"29 Main Street, Wa","uni":"Simon Diedong Dombo University for Business and Integrated Development Studies","lycee":"St. Francis Xavier SHS","stage":"Energy Commission of Ghana, Wa"},
            {"city":"Kumasi & Mampong","address":"20 Main Street, Kumasi & Mampong","uni":"Akenten Appiah-Menka University of Skills Training and Entrepreneurial Development","lycee":"Opoku Ware School","stage":"Energy Commission of Ghana, Kumasi & Mampong"},
            {"city":"Somanya","address":"45 Main Street, Somanya","uni":"University of Environment and Sustainable Development","lycee":"Somanya Methodist School","stage":"Energy Commission of Ghana, Somanya"},
            {"city":"Legon","address":"45 Main Street, Legon","uni":"Ghana Institute of Management and Public Administration","lycee":"Achimota School","stage":"Energy Commission of Ghana, Legon"},
            {"city":"Tesano","address":"2 Main Street, Tesano","uni":"Ghana Communication Technology University","lycee":"Achimota School","stage":"Energy Commission of Ghana, Tesano"},
            {"city":"Accra","address":"26 Main Street, Accra","uni":"Accra Technical University","lycee":"Accra High School","stage":"Energy Commission of Ghana, Accra"},
            {"city":"Bolgatanga","address":"40 Main Street, Bolgatanga","uni":"Bolgatanga Technical University","lycee":"Bolgatanga SHS","stage":"Energy Commission of Ghana, Bolgatanga"},
            {"city":"Cape Coast","address":"8 Main Street, Cape Coast","uni":"Cape Coast Technical University","lycee":"Mfantsipim School","stage":"Energy Commission of Ghana, Cape Coast"},
            {"city":"Kumasi","address":"40 Main Street, Kumasi","uni":"Kumasi Technical University","lycee":"Kumasi High School","stage":"Energy Commission of Ghana, Kumasi"},
            {"city":"Koforidua","address":"7 Main Street, Koforidua","uni":"Koforidua Technical University","lycee":"Pope John SHS","stage":"Energy Commission of Ghana, Koforidua"},
            {"city":"Tamale","address":"12 Main Street, Tamale","uni":"Tamale Technical University","lycee":"Tamale SHS","stage":"Energy Commission of Ghana, Tamale"},
            {"city":"Ho","address":"8 Main Street, Ho","uni":"Ho Technical University","lycee":"Mawuli School","stage":"Energy Commission of Ghana, Ho"},
            {"city":"Takoradi","address":"36 Main Street, Takoradi","uni":"Takoradi Technical University","lycee":"Ghana Secondary Technical School","stage":"Energy Commission of Ghana, Takoradi"},
            {"city":"Sunyani","address":"43 Main Street, Sunyani","uni":"Sunyani Technical University","lycee":"St. James Seminary SHS","stage":"Energy Commission of Ghana, Sunyani"},
            {"city":"Wa","address":"38 Main Street, Wa","uni":"Wa Technical University","lycee":"St. Francis Xavier SHS","stage":"Energy Commission of Ghana, Wa"},
            {"city":"Accra","address":"44 Main Street, Accra","uni":"Regional Maritime University","lycee":"Tema Secondary School","stage":"Energy Commission of Ghana, Accra"},
            {"city":"Accra","address":"18 Main Street, Accra","uni":"Consular and Diplomatic Service University","lycee":"Achimota School","stage":"Energy Commission of Ghana, Accra"},
            {"city":"Haatso","address":"22 Main Street, Haatso","uni":"Academic City University","lycee":"St. Mary's SHS","stage":"Energy Commission of Ghana, Haatso"},
            {"city":"Amasaman","address":"11 Main Street, Amasaman","uni":"Heritage Christian University","lycee":"Amasaman Senior High School","stage":"Energy Commission of Ghana, Amasaman"},
            {"city":"Gomoa Fetteh Kakraba","address":"49 Main Street, Gomoa Fetteh Kakraba","uni":"KAAF University","lycee":"Gomoa Senior High School","stage":"Energy Commission of Ghana, Gomoa Fetteh Kakraba"},
            {"city":"Oyibi","address":"41 Main Street, Oyibi","uni":"Valley View University","lycee":"Presbyterian SHS","stage":"Energy Commission of Ghana, Oyibi"},
            {"city":"Accra","address":"4 Main Street, Accra","uni":"Open University of West Africa","lycee":"Achimota School","stage":"Energy Commission of Ghana, Accra"},
            {"city":"Legon","address":"21 Main Street, Legon","uni":"Trinity Theological Seminary","lycee":"St. Thomas Aquinas SHS","stage":"Energy Commission of Ghana, Legon"},
            {"city":"Akropong-Akuapem","address":"11 Main Street, Akropong-Akuapem","uni":"Akrofi-Christaller Institute of Theology, Mission and Culture","lycee":"Okuapeman School","stage":"Energy Commission of Ghana, Akropong-Akuapem"},
            {"city":"Accra","address":"2 Main Street, Accra","uni":"Central University","lycee":"West African SHS","stage":"Energy Commission of Ghana, Accra"},
            {"city":"Sowutuom","address":"24 Main Street, Sowutuom","uni":"Pentecost University","lycee":"Odorgonno SHS","stage":"Energy Commission of Ghana, Sowutuom"},
            {"city":"Koforidua","address":"9 Main Street, Koforidua","uni":"All Nations University","lycee":"Pope John SHS","stage":"Energy Commission of Ghana, Koforidua"},
            {"city":"Berekuso","address":"48 Main Street, Berekuso","uni":"Ashesi University","lycee":"Adonten Senior High School","stage":"Energy Commission of Ghana, Berekuso"},
            {"city":"Kpong","address":"21 Main Street, Kpong","uni":"Ensign Global University","lycee":"Akosombo International School","stage":"Energy Commission of Ghana, Kpong"},
            {"city":"Cantonments","address":"34 Main Street, Cantonments","uni":"Accra Institute of Technology","lycee":"Ghana International School","stage":"Energy Commission of Ghana, Cantonments"},
            {"city":"Adabraka","address":"26 Main Street, Adabraka","uni":"African University College of Communications","lycee":"Accra High School","stage":"Energy Commission of Ghana, Adabraka"},
            {"city":"Nkoranza","address":"49 Main Street, Nkoranza","uni":"Anglican University College of Technology","lycee":"Nkoranza SHS","stage":"Energy Commission of Ghana, Nkoranza"},
            {"city":"Accra","address":"29 Main Street, Accra","uni":"University College of Design and Technology","lycee":"Achimota School","stage":"Energy Commission of Ghana, Accra"},
            {"city":"Fiapre","address":"39 Main Street, Fiapre","uni":"Catholic University College of Ghana","lycee":"Sunyani SHS","stage":"Energy Commission of Ghana, Fiapre"},
            {"city":"Kumasi","address":"42 Main Street, Kumasi","uni":"Christian Service University","lycee":"Opoku Ware School","stage":"Energy Commission of Ghana, Kumasi"},
            {"city":"Teshie","address":"3 Main Street, Teshie","uni":"Family Health Medical School","lycee":"Labone SHS","stage":"Energy Commission of Ghana, Teshie"},
            {"city":"East Legon","address":"18 Main Street, East Legon","uni":"Islamic University College, Ghana","lycee":"St. Thomas Aquinas SHS","stage":"Energy Commission of Ghana, East Legon"},
            {"city":"East Legon","address":"16 Main Street, East Legon","uni":"Knutsford University College","lycee":"Action Senior High School","stage":"Energy Commission of Ghana, East Legon"},
            {"city":"Accra","address":"20 Main Street, Accra","uni":"Lancaster University Ghana","lycee":"Ghana International School","stage":"Energy Commission of Ghana, Accra"},
            {"city":"Dansoman","address":"10 Main Street, Dansoman","uni":"Methodist University Ghana","lycee":"St. John's Grammar SHS","stage":"Energy Commission of Ghana, Dansoman"}
        ],
        "companies": [
            {"name":"Bui Power Authority","poste_en":"Intern - Solar Plant Operations","desc_en":"Bui Power Authority operates Ghana\'s first grid-connected solar plant (50 MWp). This internship involves monitoring plant performance.","skills_en":["Solar PV systems","Office tools and analysis","Electrical engineering","Attention to detail"],"formation_en":"Bachelor\'s in Electrical Engineering","exp_en":["Electrical engineering coursework","Solar systems project","Excel for data tracking","Campus sustainability initiatives"]},
            {"name":"Destra Energy Group","poste_en":"Intern - Renewable Project Development","desc_en":"Destra Energy develops renewable projects across West Africa. This internship supports feasibility studies for new solar installations.","skills_en":["Renewable technologies","Research and analysis","Presentation tools","English communication"],"formation_en":"Bachelor\'s in Environmental Science or Energy","exp_en":["Energy systems coursework","Renewable energy feasibility research","Report and presentation preparation","Interest in sustainable development"]},
            {"name":"Daystar Power Ghana","poste_en":"Intern - Commercial Solar Installer","desc_en":"Daystar Power provides solar-as-a-service solutions to businesses across West Africa, with over 100 MW installed capacity.","skills_en":["Commercial solar systems","Customer relationship management","Project coordination","Technical documentation"],"formation_en":"Bachelor's in Engineering or Business","exp_en":["Commercial awareness and client relations","Technical documentation experience","Project coordination skills","Interest in solar energy access"]},
            {"name":"Suka Solar Ghana","poste_en":"Intern - Solar Systems Technician","desc_en":"Suka Solar provides residential and commercial solar solutions in Ghana with European-standard equipment and extensive warranties.","skills_en":["Solar PV installation","Electrical wiring basics","Customer service","Quality assurance"],"formation_en":"Diploma or Bachelor's in Electrical Engineering","exp_en":["Electrical systems training","Hands-on technical experience","Customer interaction skills","Quality-focused mindset"]},
            {"name":"Tino Solutions","poste_en":"Intern - Solar PV Project Coordinator","desc_en":"Tino Solutions is a leading renewable energy EPC company in Ghana specializing in turnkey solar PV solutions for public, industrial, and residential projects.","skills_en":["Solar PV project management","AutoCAD or design tools","Procurement and logistics","Stakeholder communication"],"formation_en":"Bachelor's in Engineering or Project Management","exp_en":["Project planning experience","Technical drawing skills","Supply chain awareness","Professional communication"]},
            {"name":"Energy Masters Ghana","poste_en":"Intern - Renewable Energy Consultant","desc_en":"Energy Masters provides comprehensive renewable energy solutions from consultation to maintenance, with a focus on customized sustainable energy systems.","skills_en":["Energy assessment and auditing","Microsoft Office and reporting","Client consultation","Sustainable energy knowledge"],"formation_en":"Bachelor's in Environmental Science or Energy","exp_en":["Energy auditing or assessment coursework","Report writing experience","Client-facing communication","Sustainability knowledge"]},
            {"name":"Volta River Authority (VRA)","poste_en":"Intern - Renewable Energy Planning","desc_en":"The Volta River Authority is Ghana's primary hydroelectric and thermal power generator, expanding into solar and wind energy across the country.","skills_en":["Power systems and grid integration","Data analysis and monitoring","Regulatory knowledge","Technical report writing"],"formation_en":"Bachelor's in Electrical Engineering or Energy","exp_en":["Power systems coursework","Data analysis experience","Understanding of energy regulation","Technical writing ability"]},
            {"name":"PEGA Africa","poste_en":"Intern - Off-Grid Solar Distribution","desc_en":"PEGA Africa provides pay-as-you-go solar systems to off-grid communities in Ghana and Côte d\'Ivoire.","skills_en":["Off-grid solar and pay-as-you-go","Community engagement","Data entry and CRM","Rural travel willingness"],"formation_en":"Bachelor\'s in Business or Development Studies","exp_en":["Rural community volunteering","Energy access interest","English and local language communication","Customer data management"]},
        ],
    },
    "Ireland": {
        "cities_en": [
            {"city":"Dublin","address":"24 Main Street, Dublin","uni":"Trinity College Dublin","lycee":"Holy Child School","stage":"SEAI, Dublin"},
            {"city":"Dublin","address":"13 Main Street, Dublin","uni":"University College Dublin","lycee":"Grace International School","stage":"SEAI, Dublin"},
            {"city":"Cork","address":"38 Main Street, Cork","uni":"University College Cork","lycee":"Millennium City School","stage":"SEAI, Cork"},
            {"city":"Galway","address":"9 Main Street, Galway","uni":"University of Galway","lycee":"Unity Community School","stage":"SEAI, Galway"},
            {"city":"Maynooth","address":"28 Main Street, Maynooth","uni":"Maynooth University","lycee":"Oyibi Basic School","stage":"SEAI, Maynooth"},
            {"city":"Limerick","address":"17 Main Street, Limerick","uni":"University of Limerick","lycee":"Adenta Community School","stage":"SEAI, Limerick"},
            {"city":"Dublin","address":"25 Main Street, Dublin","uni":"Dublin City University","lycee":"Christ the King School","stage":"SEAI, Dublin"},
            {"city":"Dublin","address":"20 Main Street, Dublin","uni":"Royal College of Surgeons in Ireland","lycee":"Dansoman Basic School","stage":"SEAI, Dublin"},
            {"city":"Dublin","address":"3 Main Street, Dublin","uni":"Technological University Dublin","lycee":"Galaxy International School","stage":"SEAI, Dublin"},
            {"city":"Cork & Kerry","address":"48 Main Street, Cork & Kerry","uni":"Munster Technological University","lycee":"American International School","stage":"SEAI, Cork & Kerry"},
            {"city":"Galway","address":"48 Main Street, Galway","uni":"Atlantic Technological University","lycee":"Lincoln Community School","stage":"SEAI, Galway"},
            {"city":"Waterford & Carlow","address":"43 Main Street, Waterford & Carlow","uni":"South East Technological University","lycee":"Dansoman Basic School","stage":"SEAI, Waterford & Carlow"},
            {"city":"Athlone","address":"2 Main Street, Athlone","uni":"Technological University of the Shannon","lycee":"Lincoln Community School","stage":"SEAI, Athlone"},
            {"city":"Dundalk","address":"12 Main Street, Dundalk","uni":"Dundalk Institute of Technology","lycee":"Dundalk Grammar School","stage":"SEAI, Dundalk"},
            {"city":"Dún Laoghaire","address":"49 Main Street, Dún Laoghaire","uni":"Dún Laoghaire Institute of Art, Design and Technology","lycee":"Grace International School","stage":"SEAI, Dún Laoghaire"},
            {"city":"Dublin","address":"9 Main Street, Dublin","uni":"National College of Art and Design","lycee":"Millennium City School","stage":"SEAI, Dublin"},
            {"city":"Dublin","address":"34 Main Street, Dublin","uni":"Marino Institute of Education","lycee":"Unity Community School","stage":"SEAI, Dublin"},
            {"city":"Limerick","address":"48 Main Street, Limerick","uni":"Mary Immaculate College","lycee":"Oyibi Basic School","stage":"SEAI, Limerick"},
            {"city":"Maynooth","address":"32 Main Street, Maynooth","uni":"St. Patrick's College, Maynooth","lycee":"Adenta Community School","stage":"SEAI, Maynooth"},
            {"city":"Dublin","address":"9 Main Street, Dublin","uni":"National College of Ireland","lycee":"Christ the King School","stage":"SEAI, Dublin"},
            {"city":"Dublin","address":"20 Main Street, Dublin","uni":"Griffith College","lycee":"Morning Star School","stage":"SEAI, Dublin"},
            {"city":"Dublin","address":"7 Main Street, Dublin","uni":"Dublin Business School","lycee":"CUS Dublin","stage":"SEAI, Dublin"},
            {"city":"Dublin","address":"18 Main Street, Dublin","uni":"American College Dublin","lycee":"Galaxy International School","stage":"SEAI, Dublin"},
            {"city":"Dublin","address":"10 Main Street, Dublin","uni":"IBAT College Dublin","lycee":"American International School","stage":"SEAI, Dublin"},
            {"city":"Dublin","address":"8 Main Street, Dublin","uni":"Independent College Dublin","lycee":"Lincoln Community School","stage":"SEAI, Dublin"},
            {"city":"Cork","address":"1 Main Street, Cork","uni":"Cork College of FET","lycee":"Ballina Community School","stage":"SEAI, Cork"},
            {"city":"Tralee","address":"45 Main Street, Tralee","uni":"Kerry College","lycee":"Abbey Vocational School","stage":"SEAI, Tralee"},
            {"city":"Dublin","address":"12 Main Street, Dublin","uni":"Ballyfermot College of Further Education","lycee":"St. Benildus College","stage":"SEAI, Dublin"},
            {"city":"Dublin","address":"1 Main Street, Dublin","uni":"Coláiste Dhúlaigh College of Further Education","lycee":"Willow Park School","stage":"SEAI, Dublin"},
            {"city":"Dublin","address":"7 Main Street, Dublin","uni":"Crumlin College of Further Education","lycee":"Ballinteer Community School","stage":"SEAI, Dublin"},
            {"city":"Dublin","address":"1 Main Street, Dublin","uni":"Dundrum College of Further Education","lycee":"Sacred Heart Secondary School","stage":"SEAI, Dublin"},
            {"city":"Dublin","address":"35 Main Street, Dublin","uni":"Inchicore College of Further Education","lycee":"Newtown School","stage":"SEAI, Dublin"},
            {"city":"Dublin","address":"17 Main Street, Dublin","uni":"Pearse College","lycee":"St. Tiernan's Community School","stage":"SEAI, Dublin"},
            {"city":"Dublin","address":"46 Main Street, Dublin","uni":"Stillorgan College of Further Education","lycee":"St. Benildus College","stage":"SEAI, Dublin"},
            {"city":"Blackrock","address":"13 Main Street, Blackrock","uni":"Blackrock Further Education Institute","lycee":"Willow Park School","stage":"SEAI, Blackrock"},
            {"city":"Cork","address":"43 Main Street, Cork","uni":"Cork College of Commerce","lycee":"St. Andrew's College","stage":"SEAI, Cork"},
            {"city":"Drogheda","address":"4 Main Street, Drogheda","uni":"College of Further Education and Training, Drogheda","lycee":"Willow Park School","stage":"SEAI, Drogheda"}
        ],
        "companies": [
            {"name":"SSE Renewables","poste_en":"Intern - Offshore Wind Development","desc_en":"SSE Renewables is a leading European offshore wind developer, building major wind farms off the Irish coast.","skills_en":["Offshore wind and marine environments","GIS and environmental assessment","Report writing","Multidisciplinary teamwork"],"formation_en":"Bachelor\'s or Master\'s in environment or engineering","exp_en":["Marine biology or impact assessment","Wind energy research","GIS software proficiency","Technical report writing"]},
            {"name":"Bord na Móna","poste_en":"Intern - Renewable Energy Transition","desc_en":"Bord na Móna is transitioning to renewables with its Brown to Green strategy, developing wind, solar and biomass projects.","skills_en":["Ireland\'s energy landscape","Ecology and restoration","Data analysis","Communication"],"formation_en":"Bachelor\'s in environment or ecology","exp_en":["Ecology and climate science","Environmental monitoring fieldwork","Analysis with Python or R","Just transition interest"]},
            {"name":"Energia Group","poste_en":"Intern - Renewable Energy Development","desc_en":"Energia Group has invested over 1 billion euros in Ireland's energy market, operating 16 onshore wind farms generating over 350 MW of green electricity.","skills_en":["Wind energy systems","Project development","Stakeholder engagement","Regulatory compliance"],"formation_en":"Bachelor's in Engineering or Environmental Science","exp_en":["Wind energy coursework","Project planning experience","Communication skills","Understanding of energy regulations"]},
            {"name":"BNRG Renewables","poste_en":"Intern - Solar Farm Development","desc_en":"BNRG is a Dublin-based company that finances, builds, and operates solar farms, managing the entire lifecycle of its energy projects.","skills_en":["Solar farm planning","Financial analysis basics","Land assessment","Environmental impact awareness"],"formation_en":"Bachelor's in Environmental Science or Planning","exp_en":["Renewable energy coursework","Financial or analytical skills","Field assessment experience","Environmental awareness"]},
            {"name":"DP Energy","poste_en":"Intern - Renewable Project Planning","desc_en":"DP Energy is a Cork-based Irish company developing large renewable energy projects worldwide across onshore wind, offshore wind, and solar PV.","skills_en":["Renewable project planning","GIS and mapping tools","Environmental assessment","Stakeholder consultation"],"formation_en":"Bachelor's in Environmental Science or Engineering","exp_en":["GIS or mapping experience","Environmental impact assessment","Project coordination","Consultation or communication skills"]},
            {"name":"Statkraft Ireland","poste_en":"Intern - Wind Energy Operations","desc_en":"Statkraft is Europe's largest generator of renewable energy, operating onshore wind farms across Ireland since acquiring Element Power in 2018.","skills_en":["Wind farm operations","Performance monitoring","Health and safety compliance","Data-driven decision making"],"formation_en":"Bachelor's in Engineering or Energy","exp_en":["Wind energy systems knowledge","Data monitoring experience","Safety-conscious approach","Analytical problem-solving"]},
            {"name":"Greenvolt Next Ireland","poste_en":"Intern - Commercial Solar Solutions","desc_en":"Greenvolt Next delivers smart, scalable renewable energy systems for businesses across Ireland, from solar PV to battery storage solutions.","skills_en":["Commercial solar design","Battery storage systems","Client needs assessment","Project delivery"],"formation_en":"Bachelor's in Engineering or Business","exp_en":["Solar energy knowledge","Customer-facing experience","Project management basics","Technical documentation"]},
            {"name":"ESB (Electricity Supply Board)","poste_en":"Intern - Wind Farm Operations","desc_en":"ESB is Ireland\'s leading energy utility with a growing wind portfolio. This internship involves performance monitoring.","skills_en":["Wind systems and turbines","Data analysis and SCADA","Problem-solving","On-site work"],"formation_en":"Bachelor\'s in mechanical or electrical engineering","exp_en":["Mechanics and electrical systems","Lab practical experience","Energy systems modelling","Ireland\'s energy transition interest"]},
        ],
    },
}


VOLUNTEERS = [
    {
        "org": "Youth Environmental Movement",
        "role": "Campus Sustainability Ambassador",
        "bullets": [
            "Led tree-planting and clean energy awareness campaigns across campus",
            "Organized renewable energy workshops for secondary school students",
            "Managed social media content promoting climate action and carbon reduction"
        ]
    },
    {
        "org": "Friends of the Earth (local chapter)",
        "role": "Community Energy Organizer",
        "bullets": [
            "Campaigned for stronger climate legislation and renewable energy incentives at local level",
            "Organized community workshops on residential energy efficiency and heat pumps",
            "Created educational content on wind and solar power potential for municipal forums"
        ]
    },
    {
        "org": "Local Environmental Association",
        "role": "Climate Awareness Educator",
        "bullets": [
            "Organized awareness workshops on climate change adaptation for youth groups",
            "Wrote articles on local energy solutions and microgrids for the association blog",
            "Coordinated a team of 15 volunteers at public environmental outreach events"
        ]
    },
    {
        "org": "Green Youth Coalition",
        "role": "Eco-Project Coordinator",
        "bullets": [
            "Led sustainability projects in partnership with local secondary schools",
            "Organized film screenings and public debates on the European energy transition",
            "Managed community clean-up events and electronic waste recycling drives"
        ]
    },
    {
        "org": "Climate Action Network (local branch)",
        "role": "Youth Climate Delegate",
        "bullets": [
            "Participated in advocacy campaigns for national renewable energy policy targets",
            "Helped organize a regional climate summit for young engineering professionals",
            "Developed technical presentation materials on solar PV and wind energy basics"
        ]
    },
    {
        "org": "Renewable Energy Student Association",
        "role": "Technical Workshop Facilitator",
        "bullets": [
            "Facilitated hands-on student workshops on solar panel soldering and battery wiring",
            "Invited industry guest speakers from local wind farm operators for career panels",
            "Co-authored a student whitepaper on campus decarbonization strategies"
        ]
    },
    {
        "org": "Zero Waste & Circular Economy Network",
        "role": "Circular Economy Lead",
        "bullets": [
            "Initiated a campus-wide composting and resource reuse audit",
            "Hosted public webinars on life cycle assessment (LCA) and sustainable design",
            "Partnered with local businesses to reduce single-use plastic consumption"
        ]
    },
    {
        "org": "Coastal & Marine Conservation Group",
        "role": "Ecological Monitoring Assistant",
        "bullets": [
            "Assisted marine biologists in monitoring coastal habitat health near offshore sites",
            "Compiled fieldwork data logs on local avian migration and water quality metrics",
            "Engaged local fishing communities on marine spatial planning awareness"
        ]
    }
]

PROFILES = [
    "Motivated student specializing in renewable energy systems and environmental sustainability. Strong technical foundation in data analysis, project coordination, and scientific research. Seeking an internship to apply academic knowledge in a real-world clean energy environment.",
    "Dedicated energy systems learner committed to the global transition toward zero-carbon power. Experienced in multidisciplinary teamwork, GIS spatial analysis, and community engagement. Eager to contribute to utility-scale wind and solar projects.",
    "Results-oriented student with a deep focus on clean technology and energy efficiency. Proficient in data modeling, technical report writing, and environmental monitoring. Seeking hands-on experience in renewable project development.",
    "Environmentally conscious student with strong analytical, technical, and communication abilities. Academic preparation in climate science, smart grid integration, and energy policy. Aspiring to launch a career in sustainable infrastructure.",
    "Proactive engineering student passionate about combating climate change through technological innovation. Skilled in Python data analysis, PVSyst simulation basics, and project planning. Seeking a role to drive tangible decarbonization impact.",
    "Analytical student with a keen interest in wind energy resource assessment and SCADA data monitoring. Proven track record in academic research, spatial mapping, and environmental impact evaluation.",
    "Sustainability-focused student with expertise in life cycle assessment (LCA), carbon accounting, and regulatory compliance. Eager to assist clean energy developers in environmental permitting and feasibility studies.",
    "Driven student with a strong background in electrical energy systems, battery storage solutions, and microgrids. Passionate about applying modeling skills to optimize commercial solar PV installations.",
    "Forward-thinking student focused on environmental management and ecological restoration. Skilled in field survey methodologies, GIS mapping, and public stakeholder communication.",
    "Enthusiastic green transition advocate combining technical engineering coursework with practical project coordination experience. Looking to support innovative clean tech initiatives in a fast-paced environment."
]

INTERESTS = [
    "Renewable energy • Hiking • Photography • Volunteering",
    "Sustainable development • Cycling • Science reading • Gardening",
    "Clean technology • Running • Documentaries • Community service",
    "Green innovation • Rock climbing • Podcasts • Local community",
    "Climate action • Swimming • Creative writing • Environmental advocacy",
    "Offshore wind systems • Sailing • Chess • Environmental blogging",
    "Solar PV technology • Biking • Electronics tinkering • Nature conservation",
    "Circular economy • Urban gardening • Upcycling • Community organizing"
]

DEGREES = [
    "BSc Environmental Science",
    "BSc Geography and Sustainable Planning",
    "BSc Physics & Energy Studies",
    "BSc Life Sciences & Ecology",
    "BSc Civil & Environmental Engineering",
    "BSc Agricultural & Environmental Science",
    "BEng Energy Systems Engineering",
    "BSc Natural Sciences"
]

SPECS = [
    "Energy and Sustainable Development",
    "Environmental Management & Policy",
    "Renewable Energy Systems & Microgrids",
    "Climate Science & Resource Analytics",
    "Ecology & Conservation Biology",
    "Green Building Performance & Energy Auditing"
]

PROJECTS = [
    "Feasibility study of a community solar PV farm",
    "Urban air quality analysis using low-cost sensor networks",
    "Wind resource assessment and capacity factor modeling for a local site",
    "Carbon footprint Life Cycle Assessment (LCA) of residential energy use",
    "Performance analysis and shading simulation of rooftop solar installations",
    "Environmental impact assessment of onshore wind turbines on local wildlife",
    "Grid integration modeling for battery energy storage systems (BESS)",
    "Energy efficiency audit and retrofitting roadmap for a municipal building"
]

GRADES = [
    "First Class Honours",
    "Upper Second Class Honours (2:1)",
    "Distinction",
    "High Merit",
    "Academic Honors List"
]

COURSEWORK_POOLS = [
    "Solar PV System Sizing, Inverter Electronics, Financial Modeling & Project Management.",
    "Wind Resource Assessment, SCADA Telemetry, Fluid Mechanics & Environmental Impact.",
    "Grid Integration of Renewables, Power Systems Analysis, Smart Metering & Battery Storage.",
    "Environmental Impact Assessment (EIA), Ecological Restoration, Biodiversity Monitoring & GIS.",
    "Carbon Accounting & Life Cycle Assessment (LCA), Sustainability Reporting & Energy Policy.",
    "Energy Auditing & Building Efficiency, HVAC Optimization, Green Architecture Standards.",
    "GIS Spatial Analysis, Remote Sensing for Clean Energy, Climate Data Analytics & Python.",
    "Hydroelectric Engineering, Marine Renewable Systems, Hydrology & Environmental Law.",
    "Biomass Energy Conversion, Waste-to-Energy Sizing, Circular Economy & Process Engineering.",
    "Renewable Energy Economics, Power Markets, Project Finance & Feasibility Studies."
]

ACADEMIC_STANDINGS = [
    "Ranked in the top 5% of the graduating class. Recipient of the Green Pathways Academic Excellence Award.",
    "First Class Honors candidate. Named to the Dean's List for four consecutive academic semesters.",
    "Awarded Best Undergraduate Capstone Research Project in Renewable Energy Systems.",
    "Green Pathways Merit Scholar. Recognized for outstanding laboratory and analytical research.",
    "Ranked in the top 10% of the class. Department Representative for Sustainability Initiatives.",
    "Graduated with High Distinction. Recipient of the Regional Climate Innovation Student Grant.",
    "Top academic standing in Power Systems & Environmental Analytics coursework.",
    "Selected as Student Presenter at the Annual Green Energy & Sustainability Conference."
]

PLACEMENT_BULLETS_POOL = [
    "Analyzed solar PV performance and irradiance data using PVSyst and Excel, compiling weekly energy yield reports",
    "Assisted senior engineers in conducting environmental impact assessments (EIA) for proposed renewable energy sites",
    "Created detailed GIS spatial mapping layers in QGIS to evaluate prospective onshore wind farm development zones",
    "Monitored real-time SCADA telemetry logs to track turbine power curves and identify operational maintenance anomalies",
    "Performed comprehensive energy efficiency audits on commercial facility lighting and HVAC equipment",
    "Calculated Scope 1, 2, and 3 carbon emission baselines for corporate client sustainability disclosures",
    "Prepared technical compliance documentation and grid connection checklists for regional utility filings",
    "Modeled battery storage degradation curves and economic peak-shaving feasibility scenarios",
    "Supported field ecological survey teams in documenting local biodiversity metrics around project boundaries",
    "Compiled stakeholder consultation logs and community feedback surveys for local renewable planning approval",
    "Synthesized meteorological wind anemometer data to evaluate seasonal capacity factors and wake loss effects",
    "Drafted technical presentation decks and executive briefings for client site inspection visits",
    "Participated in site feasibility assessments evaluating land topography, grid proximity, and solar access",
    "Maintained project tracking dashboards in Power BI to monitor task milestones and environmental permit statuses"
]


def generate_content(name, email, country, lang="en"):
    name = " ".join(name.split())
    pool = POOL.get(country, POOL["France"])
    
    # Pick city from EN data or regular cities
    if "cities_en" in pool:
        loc = random.choice(pool["cities_en"])
    else:
        loc = random.choice(pool["cities"])
    
    city = loc["city"]
    phone = _rnd_phone(country)
    comps = random.sample(pool["companies"], 2)
    c1, c2 = comps[0], comps[1]
    vol = random.choice(VOLUNTEERS)
    
    # Randomize years
    grad_year = random.choice([2025, 2026, 2027])
    start_year = grad_year - 3
    edu_years = f"{start_year} – {grad_year}"
    sec_year = str(start_year)
    vol_start = random.choice(["Jan.","Mar.","Sep.","Oct."])
    vol_year = random.choice([2024, 2025])
    stage_month = random.choice(["June","May","April","March"])
    stage_year = random.choice([2023, 2024, 2025])
    
    # Clean join helper to prevent double "and"
    def clean_join(items):
        if not items:
            return ""
        cleaned = [it.strip().lower() for it in items]
        if len(cleaned) == 1:
            return cleaned[0]
        if len(cleaned) == 2:
            it1, it2 = cleaned[0], cleaned[1]
            if "and" in it1:
                return f"{it1}, as well as {it2}"
            return f"{it1} and {it2}"
        else:
            first_part = ", ".join(cleaned[:-1])
            last_item = cleaned[-1]
            if "and" in last_item:
                return f"{first_part}, along with {last_item}"
            return f"{first_part}, and {last_item}"

    # 10 structurally different summary styles
    s1 = c1['skills_en']; s2 = c2['skills_en']
    uni = loc['uni']
    summaries = [
        # Style 1: Goal-first
        lambda: f"My goal is simple: to contribute meaningfully to the renewable energy transition. After completing my studies at {uni}, I began researching opportunities where I could put my knowledge into practice. Two positions stood out. {c1['name']} is hiring a {c1['poste_en']} in {city}. {c1['desc_en']} What excites me most is the chance to work on {s1[0].lower()}. I also found an opportunity at {c2['name']} for a {c2['poste_en']} in the same region. {c2['desc_en']} Both roles would push me to grow in areas like {clean_join([s2[1], s1[2]])}. I am ready for this step.",
        # Style 2: Problem-focused
        lambda: f"Climate change demands urgent action, and the renewable energy sector is where solutions are being built every day. That conviction grew stronger during my time at {uni}, where I studied energy systems and sustainability. Now, I want to move from theory to practice. I discovered that {c1['name']} offers a {c1['poste_en']} position in {city}. {c1['desc_en']} Separately, {c2['name']} has an opening for a {c2['poste_en']}. {c2['desc_en']} Either role would give me real experience in {clean_join([s1[0], s2[0]])}, skills that are critical for this sector. I am committed to being part of the solution.",
        # Style 3: Story-driven
        lambda: f"It started with a question: how can one person make a difference in the fight against climate change? That question led me to {uni}, where I explored renewable energy, environmental science, and sustainable development. It led me to the Green Pathways program, which sharpened my professional skills. And now it leads me to two specific opportunities. The first is at {c1['name']}, a {c1['poste_en']} role based in {city}. {c1['desc_en']} The second is at {c2['name']}, offering a {c2['poste_en']} position. {c2['desc_en']} I have the skills — {clean_join([s1[0], s2[1]])}, as well as analytical thinking — and the motivation. What I need now is the opportunity to prove it.",
        # Style 4: Skills-focused
        lambda: f"Throughout my education at {uni}, I developed a diverse skill set that I believe makes me a strong candidate for internships in renewable energy. My abilities include {clean_join([s1[0], s1[1], s2[0]])}. I am now looking to apply these competencies in a professional setting. Two opportunities align well with my profile. {c1['name']} is seeking a {c1['poste_en']} in {city}, focusing on {c1['desc_en'].split('.')[0].lower()}. Meanwhile, {c2['name']} has a {c2['poste_en']} role that involves {c2['desc_en'].split('.')[0].lower()}. Both positions offer the kind of hands-on experience that would accelerate my professional growth and deepen my commitment to the energy transition.",
        # Style 5: Conversational
        lambda: f"If someone asked me where I see myself in five years, my answer would be clear: working in renewable energy, helping communities access clean power. That vision took shape at {uni} and became sharper through the Green Pathways program. Right now, I am looking at two paths forward. One leads to {c1['name']}, where I could work as a {c1['poste_en']} in {city}. {c1['desc_en']} The other leads to {c2['name']} and their {c2['poste_en']} role. {c2['desc_en']} Both would help me build practical experience in {clean_join([s1[0], s2[1]])}. I am excited about either direction.",
        # Style 6: Analytical
        lambda: f"After careful analysis of the renewable energy job market in my region, I identified two internship positions that match both my qualifications and career objectives. Position one: {c1['poste_en']} at {c1['name']}, located in {city}. {c1['desc_en']} Key requirements include {clean_join([s1[0], s1[1]])}, which I developed at {uni}. Position two: {c2['poste_en']} at {c2['name']}, also in {city}. {c2['desc_en']} This role emphasizes {clean_join([s2[0], s2[1]])}. My academic preparation, including coursework in sustainability and environmental analysis, positions me well for either role. I am confident in my ability to deliver value from day one.",
        # Style 7: Passion-led
        lambda: f"Renewable energy is not just a career choice for me — it is a calling. Every course I took at {uni}, every project I completed, reinforced my desire to work in this field. The Green Pathways program gave me the professional tools to turn that passion into action. I have identified two internships that would allow me to do exactly that. At {c1['name']}, the {c1['poste_en']} role in {city} offers a chance to work on real projects. {c1['desc_en']} At {c2['name']}, the {c2['poste_en']} position provides a different but equally valuable perspective. {c2['desc_en']} I bring strong skills in {clean_join([s1[0], s2[0]])}, and an unwavering commitment to sustainability.",
        # Style 8: Future-oriented
        lambda: f"The energy landscape is changing rapidly, and professionals who can bridge technical knowledge with practical application will be in high demand. My studies at {uni} have prepared me for this reality. I understand both the science behind renewable energy and the project management skills needed to implement it. Looking ahead, I see two clear opportunities to begin my career. {c1['name']} is offering a {c1['poste_en']} position in {city}. {c1['desc_en']} Additionally, {c2['name']} has a {c2['poste_en']} role available. {c2['desc_en']} With expertise in {s1[0].lower()} and a growing knowledge of {s2[1].lower()}, I am well-positioned to contribute immediately.",
        # Style 9: Compact and direct
        lambda: f"I am seeking an internship in renewable energy. My background: {uni}, with skills in {clean_join([s1[0], s1[1], s2[0]])}. Two opportunities interest me. First: {c1['poste_en']} at {c1['name']} in {city}. {c1['desc_en']} I would bring my {s1[0].lower()} expertise to this role. Second: {c2['poste_en']} at {c2['name']}. {c2['desc_en']} My {s2[0].lower()} skills make me a strong fit. Through the Green Pathways program, I have refined my professional competencies and am ready to start contributing to the energy transition.",
        # Style 10: Reflective
        lambda: f"Looking back at my time at {uni}, I realize that every module, every group project, and every late-night study session was building toward one thing: a career in renewable energy. The Green Pathways program confirmed this direction and helped me articulate my goals more clearly. I have now identified two internship opportunities that feel right. {c1['name']} is looking for a {c1['poste_en']} in {city}. {c1['desc_en']} I find this appealing because of the focus on {s1[0].lower()}. There is also an opening at {c2['name']} as a {c2['poste_en']}. {c2['desc_en']} What draws me to this role is the emphasis on {clean_join([s2[0], s2[1]])}. I feel ready to take this next step.",
    ]

    # For CV improvements, let's filter out duplicates and join cleanly
    imp_skills = []
    for s in c1['skills_en'] + c2['skills_en']:
        s_clean = s.strip().lower()
        if "data analysis" not in s_clean and s_clean not in imp_skills:
            imp_skills.append(s_clean)
    profile_skill = imp_skills[0] if len(imp_skills) > 0 else "renewable energy systems"
    section_skill = imp_skills[1] if len(imp_skills) > 1 else "technical report writing"
    cv_improvements = f"1. Added a professional summary highlighting my skills in {profile_skill}. 2. Updated skills section with {section_skill} and data analysis tools. 3. Integrated link to my optimized LinkedIn profile."

    # Dynamic placement role and bullets
    placement_role_title = c1['poste_en']
    placement_bullets_sample = random.sample(PLACEMENT_BULLETS_POOL, 3)

    # Technical and soft skills pools
    tech_skills_pool = [
        "PVSyst Simulation", "QGIS Mapping", "RETScreen Analysis", "AutoCAD", 
        "Python / Pandas", "SCADA Telemetry", "EnergyPlus Modeling", "Homer Energy", 
        "OpenLCA (Carbon Footprint)", "Data Analysis (Excel / Power BI)", "R Statistical Analysis", 
        "SQL Databases", "Solar PV System Sizing", "Wind Resource Assessment", 
        "Energy Auditing", "Power Systems Modeling", "MATLAB / Simulink", 
        "Google Earth Pro", "Technical Report Writing", "Regulatory Compliance", 
        "MS Project Scheduling", "Microgrid Design", "Environmental Impact Assessment (EIA)"
    ]
    soft_skills_pool = [
        "Multidisciplinary Teamwork", "Technical Communication", "Analytical Problem-Solving", 
        "Stakeholder Engagement", "Scientific Research Rigor", "Environmental Advocacy", 
        "Self-Motivation & Autonomy", "Time & Project Management", "Critical Thinking", 
        "Adaptability in Fieldwork", "Public Presentation Skills", "Cross-Cultural Collaboration", 
        "Attention to Technical Detail", "Strategic Decision-Making", "Negotiation & Consensus Building"
    ]

    return {
        "name": name, "email": email, "country": country, "lang": "en",
        "phone": phone, "city": city, "address": loc["address"],
        "edu_years": edu_years, "sec_year": sec_year,
        "vol_dates": f"{vol_start} {vol_year} – Present",
        "stage_date": f"{stage_month} {stage_year}",
        "opportunity1": {
            "company": c1["name"], "position": c1["poste_en"], "location": city,
            "description": c1["desc_en"], "skills": c1["skills_en"],
            "qualification": c1["formation_en"], "my_experience": c1["exp_en"],
        },
        "opportunity2": {
            "company": c2["name"], "position": c2["poste_en"], "location": city,
            "description": c2["desc_en"], "skills": c2["skills_en"],
            "qualification": c2["formation_en"], "my_experience": c2["exp_en"],
        },
        "education": {
            "degree": random.choice(DEGREES),
            "university": loc["uni"],
            "specialization": random.choice(SPECS),
            "project": random.choice(PROJECTS),
            "secondary_school": loc["lycee"],
            "secondary_spec": "Sciences",
            "grade": random.choice(GRADES),
            "coursework": random.choice(COURSEWORK_POOLS),
            "academic_standing": random.choice(ACADEMIC_STANDINGS),
        },
        "experience": {
            "volunteer_org": vol["org"],
            "volunteer_role": vol.get("role", "Volunteer Environmental Educator"),
            "volunteer_bullets": vol["bullets"],
            "placement_org": loc["stage"],
            "placement_role": placement_role_title,
            "placement_bullets": placement_bullets_sample,
        },
        "cv_skills": {
            "left": random.sample(tech_skills_pool, 8),
            "right": random.sample(soft_skills_pool, 8),
        },
        "languages": ["English (Native or Bilingual Proficiency)"],
        "interests": random.choice(INTERESTS),
        "profile_summary": random.choice(PROFILES),
        "capstone_summary": summaries[random.randint(0, len(summaries)-1)](),
        "cv_improvements": cv_improvements,
        "next_steps_immediate": random.sample(["Update my CV and professional profile","Write personalized cover letters","Apply to both identified internships","Connect with industry professionals on LinkedIn","Prepare for interviews"], 4),
        "next_steps_medium": random.sample(["Take additional online training","Attend renewable energy career fairs","Build a professional network in the green sector","Develop project management certifications","Obtain an environmental certification","Gain volunteer experience in sustainability"], 4),
    }