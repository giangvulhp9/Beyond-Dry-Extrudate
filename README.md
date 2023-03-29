# Beyond-Dry-Extrudate
Dry extrudate calculator project utilizing streamlit

Extrudate is used as a base of almost all products.
Common mixing process:
<br /> 1/ Extrudate are sieved and classified into Large, Medium, and Fine (pre-hydrated PSD). This is also what we measure.
<br /> 2/ Sieved extrudate will then be hydrated (hydrated-extrudate) for certain amount of time before adding other ingredients in.

![Dry extrudate](https://user-images.githubusercontent.com/129092996/228688552-fac56ee3-e064-4a9c-9f22-ee48f14af9da.png)



Usually, regularly used extrudate has decent amount of water concentration and is stored in a freezer to prevent microbio growth. To reduce cost of operation, Dry extrudate with significanly less water concentration is proposed as it can be stored in room temperature and last longer. However, we concern that using Dry extrudate might cause changes in texture of products

<br /> Objective: Replace regular extrudate with Dry extrudate without compensation in texture. 

<br /> Assumption: texture of products is solely dictated by the hydrated particle size distribution (PSD).

<br />*Input*: 
- Amount and ratio of pre-hydrated regular extrudate used in product
- Hydrated PSD of regular extrudate 
- Hydrated PSD of dry extrudate

<br />*Output*:
- Amount of pre-hydrated Dry extrudate used in product

#### Theory Frame work:


![Dry extrudate calculator (1)](https://user-images.githubusercontent.com/129092996/228015115-8a986d45-01bc-4980-960d-aa689a293862.png)

- "Control PSD" : Hydrated PSD in grams of the final product from regular_extrudate
- "Dry_fine" : ratio of hydrated medium and fine after hydrating dry_fine_extrudate
- "Dry_medium" : ratio of hydrated large and medium after hydrating dry_fine_extrudate
- "Purple-plane" : all possible Hydrated PSD can achieved from the sample dry_extrudate 


![Dry extrudate calculator (2)](https://user-images.githubusercontent.com/129092996/228018134-a5ba256e-d899-4044-ae08-4b8aa5200f24.png)

The best optimized Hydrated PSD from the dry_Extrudate is the projective perpendicular point on the "purple plane" from the known Hydrated PSD of the regular_extrudate. From this, the two scalars for vectors "Dry_fine" and "Dry_medium" required to meet the optimized vector (origin to the projective point) equal to the amount needed from the prehydrated dry_extrudate.

#### Math Formula:

<br /> $\ x=\ \left(A^{T}A\right)^{-1}A^{T}y$
<pre>
From the formula, output "x" is the (2x1) matrix contains <b>amount</b> of medium and fine prehydrated dry_extrudate we need to used 

x = [dry_medium]
    [dry_fine  ]

"A" is a (3x2) matrix, represents the "purprle plane" or all possible combination of hydrated PSD from given dry_extrudate. This matrix would contains information of hydrated PSD <b>ratio</b> of "Dry_medium" and "Dry_fine." 

A = [Dry_medium_Large     Dry_fine_Large ]
    [Dry_medium_Medium    Dry_fine_Medium]
    [Dry_medium_Fine      Dry_fine_Fine  ]
    
"y" is a (3x1) matrix, contains the information of the <b>amount</b> hydrated PSD of the regular extrudate, or the "Control PSD"

y = [control_Large ]
    [control_Medium]
    [control_Fine  ]    
  
<pre>
source: https://jeffycyang.github.io/from-least-squares-regression-to-the-fundamental-theorem-of-linear-algebra/index.html
