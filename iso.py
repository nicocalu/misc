'''
-----------
IT TOLERANCES
-----------
'''
tolerances = [ #each sublist corresponds to a different size range
    [0.5,0.8,1.2,2,3,4,6,10,14,25,40,60,0.1,0.14,0.25,0.4,0.6,1.0,1.4],
    [0.6,1,1.5,2.5,4,5,8,12,18,30,48,75,0.12,0.18,0.3,0.48,0.75,1.2,1.8],
    [0.6,1,1.5,2.5,4,6,9,15,22,36,58,90,0.15,0.22,0.36,0.58,0.9,1.5,2.2],
    [0.8,1.2,2,3,5,8,11,18,27,43,70,110,0.18,0.27,0.43,0.7,1.1,1.8,2.7],
    [1,1.5,2.5,4,6,9,13,21,33,52,84,130,0.21,0.33,0.52,0.84,1.3,2.1,3.3],
    [1,1.5,2.5,4,7,11,16,25,39,62,100,160,0.25,0.39,0.62,1.0,1.6,2.5,3.9],
    [1.2,2,3,5,8,13,19,30,46,74,120,190,0.3,0.46,0.74,1.2,1.9,3.0,4.6],
    [1.5,2.5,4,6,10,15,22,35,54,87,140,220,0.35,0.54,0.87,1.4,2.2,3.5,5.4],
    [2,3.5,5,8,12,18,25,40,63,100,160,250,0.4,0.63,1.0,1.6,2.5,4.0,6.3],
    [3,4.5,7,10,14,20,29,46,72,115,185,290,0.46,0.72,1.15,1.85,2.9,4.6,7.2],
    [4,6,8,12,16,23,32,52,81,130,210,320,0.52,0.81,1.3,2.1,3.2,5.2,8.1],
    [5,7,9,13,18,25,36,57,89,140,230,360,0.57,0.89,1.4,2.3,3.6,5.7,8.9],
    [6,8,10,15,20,27,40,63,97,155,250,400,0.63,0.97,1.55,2.5,4.0,6.3,9.7],
    [0,9,11,16,22,32,44,70,110,175,280,440,0.7,1.1,1.75,2.8,4.4,7.0,11.0],
    [0,10,13,18,25,36,50,80,125,200,320,500,0.8,1.25,2.0,3.2,5.0,8.0,12.5],
    [0,11,15,21,28,40,56,90,140,230,360,560,0.9,1.4,2.3,3.6,5.6,9.0,14.0],
    [0,13,18,24,33,47,66,105,165,260,420,660,1.05,1.65,2.6,4.2,6.6,10.5,16.5],
    [0,15,21,29,39,55,78,125,195,310,500,780,1.25,1.95,3.1,5.0,7.8,12.5,19.5],
    [0,18,25,35,46,65,92,150,230,370,600,920,1.5,2.3,3.7,6.0,9.2,15.0,23.0],
    [0,22,30,41,55,78,110,175,280,440,700,1100,1.75,2.8,4.4,7.0,11.0,17.5,28.0],
    [0,26,36,50,68,96,135,210,330,540,860,1350,2.1,3.3,5.4,8.6,13.5,21.0,33.0]
    ]

'''
-----------
SIZES
-----------
'''
sizes = [3,6,10,18,30,50,80,120,180,250,315,400,500,630,800,1000,1250,1600,2000,2500,3150]

sizes_subdivided = [3,6,10,14,18,24,30,40,50,65,80,100,120,140,160,180,200,225,250,280,315,355,400,450,500]

'''
-----------
SHAFT DEVIATIONS
-----------
'''
deviations_shaft_abc = [ #upper limit deviations, subdivided, each list is a diferent identifier (as the rest of the deviations except where specified)
    [-270,-270,-280,-290,-290,-300,-300,-310,-320,-340,-360,-380,-410,-460,-520,-580,-660,-740,-820,-920,-1050,-1200,-1350,-1500,-1650],
    [-140,-140,-150,-150,-150,-160,-160,-170,-180,-190,-200,-220,-240,-260,-280,-310,-340,-380,-420,-480,-540,-600,-680,-760,-840],
    [-60,-70,-80,-95,-95,-110,-110,-120,-130,-140,-150,-170,-180,-200,-210,-230,-240,-260,-280,-300,-330,-360,-400,-440,-480]
]

deviations_shaft =[ #upper limit deviations
    [-34,-46,-56,-70,-85,-100],
    [-20,-30,-40,-50,-65,-80,-100,-120,-145,-170,-190,-210,-230,-260,-290,-320,-350,-390,-430,-480,-520],
    [-14,-20,-25,-32,-40,-50,-60,-72,-85,-100,-110,-125,-135,-145,-160,-170,-195,-220,-240,-260,-290],
    [-10,-14,-18,-23,-25,-35],
    [-6,-10,-13,-16,-20,-25,-30,-36,-43,-50,-56,-62,-68,-76,-80,-86,-98,-110,-120,-130,-145],
    [-4,-6,-8,-10,-12,-15],
    [-2,-4,-5,-6,-7,-9,-10,-12,-14,-15,-17,-18,-20,-22,-24,-26,-28,-30,-32,-34,-38],
    [0 for i in range(len(sizes))]
]

deviations_shaft_j =[ #lower limit deviations
    [-2,-2,-2,-3,-4,-5,-7,-9,-11,-13,-16,-18,-20],#IT5 
    [-2,-2,-2,-3,-4,-5,-7,-9,-11,-13,-16,-18,-20], #IT6
    [-4,-4,-5,-6,-8,-10,-12,-15,-18,-21,-26,-28,-32], #IT7
    [-6] #IT8
]

deviations_shaft_k =[ #lower limit deviations
    [0,1,1,1,2,2,2,3,3,4,4,4,5,0,0,0,0,0,0,0,0], #IT4, IT5, IT6 and IT7
    [0 for i in range(len(sizes))] #everything else
]

deviations_shaft_mnp = [ #lower limit deviations
    [2,4,6,7,8,9,11,13,15,17,20,21,23,26,30,34,40,48,58,68,76],
    [4,8,10,12,15,17,20,23,27,31,34,37,40,44,50,56,66,78,92,110,135],
    [6,12,15,18,22,26,32,37,43,50,56,62,68,78,88,100,120,140,170,195,240]
]

deviations_shaft_rzc =[ #lower limit devitations starting from r, subdivided
    [10,15,19,23,23,28,28,34,34,41,43,51,54,63,65,68,77,80,84,94,98,108,114,126,132,150,155,175,185,210,220,250,260,300,330,370,400,440,460,550,580],
    [14,19,23,28,28,35,35,43,43,53,59,71,79,92,100,108,122,130,140,158,170,190,208,232,252,280,310,340,380,430,470,520,580,640,720,820,920,1000,1100,1250,1400],
    [None,None,None,None,None,None,41,48,54,66,75,91,104,122,134,146,166,180,196,218,240,268,294,330,360,400,450,500,560,620,680,780,840,960,1050,1200,1350,1500,1650,1900,2100],
    [18,23,28,33,33,41,48,60,70,87,102,124,144,170,190,210,236,258,284,315,350,390,435,490,540,600,660,740,840,940,1050,1150,1300,1450,1600,1850,2000,2300,2500,2900,3200],
    [None,None,None,None,39,47,55,68,81,102,120,146,172,202,228,252,284,310,340,385,425,475,530,595,660],
    [20,28,34,40,45,54,64,80,97,122,146,178,210,248,280,310,350,385,425,475,525,590,660,740,820],
    [None,None,None,None,None,63,75,94,114,144,174,214,254,300,340,380,425,470,520,580,650,730,820,920,1000],
    [26,35,42,50,60,73,88,112,136,172,210,258,310,365,415,465,520,575,640,710,790,900,1000,1100,1250],
    [32,42,52,64,77,98,118,148,180,226,274,335,400,470,535,600,670,740,820,920,1000,1150,1300,1450,1600],
    [40,50,67,90,108,136,160,200,242,300,360,445,525,620,700,780,880,960,1050,1200,1300,1500,1650,1850,2100],
    [60,80,97,130,150,188,218,274,325,405,480,585,690,800,900,1000,1150,1250,1350,1550,1700,1900,2100,2400,2600]
]
grades_shaft = ['a','b','c','cd','d','e','ef','f','fg','h','j','js','k','m','n','p','r','s','t','u','v','x','y','z','za','zb','zc']

'''
-----------
HOLE DEVIATIONS
-----------
'''


assert len(sizes) == 21
assert len(tolerances) == 21
for v in tolerances:
    assert len(v) == 19

def fundamental_tolerance(nominal_size: int,tolerance_grade: int) -> int:  
    """Calculates the fundamental tolerance given a nominal size and a tolerance grade in micrometers

    Args:
        nominal_size (int): the nominal size of the part in mm (from 0 to 3150)
        tolerance_grade (int): the tolerance grade of the part (from 0 to -)

    Raises:
        ValueError: if the arguments fall out of the normal range

    Returns:
        int: the fundamental tolerance of that certain part
    """
    if nominal_size > 3150:
        raise ValueError('Nominal sizes only go up to 3150mm')
    
    elif nominal_size < 0 :
        raise ValueError('Nominal sizes cannot be negative')
    
    elif nominal_size > 500 and tolerance_grade == 0:
        raise ValueError("Tolerance grade IT0 does is not defined for nominal sizes bigger than 500mm")
    
    elif tolerance_grade < 0:
        raise ValueError("Tolerance grades cannot be negative")
    
    else:
        s=0
        while (sizes[s] < nominal_size):
            s +=1

        if tolerance_grade > 18:
            return tolerances[s][18] * (tolerance_grade-18)* 10/5 *1000
        elif tolerance_grade >= 12:
            return tolerances[s][tolerance_grade] * 1000
        else:
            return tolerances[s][tolerance_grade]
        
def fundamental_deviation_shaft(identifier: str, nominal_size: int, tolerance_grade=None) -> list:
    """returns the fundamental deviation of a shaft given the identifier letter, nominal 
    size and optional tolerance grade, in micrometers

    Args:
        identifier (str): the identifier letter 
        nominal_size (int): the nominal size in mm
        tolerance_grade (int, optional): the tolerance grade of the part. Defaults to None.

    Raises:
        ValueError: If the arguments are not in the range allowed, or the deviation is undefined

    Returns:
        list: list containing the deviation amount and if its either an upper or lower limit deviation
    """
    if not (identifier in grades_shaft):
        raise ValueError("The identifier is not recognized")
    elif nominal_size < 0:
        raise ValueError("The nominal size cannot be negative")
    elif nominal_size > 3150:
        raise ValueError("Nominal Sizes cannot go over 3150 mm")
    elif (identifier in ['js','j','k']) and tolerance_grade == None:
        raise LookupError("The fund. dev. of grades j, js and k depend on a tolerance grade")
    else:

        idn = grades_shaft.index(identifier)

        if idn < 3: #ids a,b,c
            s=0
            while (sizes_subdivided[s] < nominal_size):
                s +=1
            return [deviations_shaft_abc[idn][s],'upper']

        elif idn < 10: #ids cd to h
            if idn in [3,6,8] and nominal_size > 50:
                raise ValueError('Deviation not defined for sizes above 50mm')
            idn -= 3
            s=0
            while (sizes[s] < nominal_size):
                s +=1
            return [deviations_shaft[idn][s],'upper']

        elif idn == 10: #ids j
            if nominal_size > 500:
                raise ValueError('Deviation not defined for sizes above 500mm')
            elif not (tolerance_grade in [5,6,7,8]):
                raise ValueError("Deviation j is only defined for IT between 5 and 8")
            elif nominal_size > 3 and tolerance_grade == 8:
                raise ValueError('Deviation j for IT8 is only defined for sizes up to 3mm')
            else:
                s=0
                while (sizes[s] < nominal_size):
                    s +=1
                return [deviations_shaft_j[tolerance_grade-5][s],'lower']

        elif idn == 11: #ids js
            return [fundamental_tolerance(nominal_size,tolerance_grade)/2,'upper']

        elif idn == 12: #ids k
            s=0
            while (sizes[s] < nominal_size):
                s +=1
            if tolerance_grade in [4,5,6,7]: 
                return [deviations_shaft_k[0][s],'lower']
            else:
                return [deviations_shaft_k[1][s],'lower']


        elif idn < 16: #ids m,n,p
            s=0
            while (sizes[s] < nominal_size):
                s +=1
            idn -= 13
            return [deviations_shaft_mnp[idn][s],'lower']

        else:
            if idn >= 20 and nominal_size > 500:
                raise ValueError(f"Deviation '{identifier}' is not defined for sizes above 500mm")
            s=0
            while (sizes_subdivided[s] < nominal_size):
                s +=1
            idn -= 16
            div = deviations_shaft_rzc[idn][s]
            if div == None:
                raise ValueError(f"Deviation '{identifier}' is not defined for sizes below {sizes_subdivided[deviations_shaft_rzc[idn].count(None)-1]}")
            else:
                return [div,"lower"]

    
print(fundamental_deviation_shaft('s',275))
print(fundamental_deviation_shaft('c',500))
print(fundamental_deviation_shaft('j',2,6))
