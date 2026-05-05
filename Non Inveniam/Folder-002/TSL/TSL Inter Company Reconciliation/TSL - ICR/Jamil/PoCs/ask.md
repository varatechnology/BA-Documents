
# Matching Engine
	1. It is observed that, pass rules are defined by the user to reconsile the line items. These pass rules are placed in order. If any one of the pass rule is satisfied by any pair of lineitems, further checking is avoided and reconcilation reusult item is created. We have 4 lineitem L1, L2, L3, L4. 
		a. L1, L2, L3 is matching by rule 1
		b. L2 and L4 are matching by rule 3
In the above scenario, how result item should be created ? 
	2. If the line items are falling under the pass rules of two different balances, then should we skip that pair? Or do the calculations?
	3. For mapping, there is Fields are specified with a range. 
		a. Is that range for creating a recon item?
		b. If the field selected is not a number, then what is the mapping logic?
	4. For effective calculation, is only the Fields are taken care of ? If not then what are the fields are always taken to perform the reconcilation job? 
	5. In case of TSL Payable - TBSL Receivable, is TBSL plays customer role for TSL? 
	6. According to my observation, most of the time, the criteria for grouping is always same for both side. But there is a possiblity of having different combination correspondence to Related Party line items. is it ?
	7. If you show the pass rule (10 and 11) for ICR 00 - TSL Payable - Tata Bluescope Receivable > Tata Bluescope Customer Reversals (BG), it will be helpful.
	8. Any rule for ICR 00 - TSL Payable - Tata Bluescope Receivable > TSL GRIR Reversals (BG).
	9. Any rule for ICR 00 - TSL Payable - Tata Bluescope Receivable > TSL Provision Reversals (BG)
	10. What is GL Mapping for Account Mapping ?
	*11. It may be possible that, some txns are under Pass Rule 1,2,3,6,7. During, calculation it is found that, by Pass Rule 1, 2, 3 it is not matched or partially matching. But, under Pass Rule 6, it is found Matched. I am just trying to say that, these transaction fulfilling the data source criteria and grouping criteria for Pass Rule 1,2,3,6,7. At the time execution, the pass rule 6 founds it is a Matched transaction. 
	Then should I conclude with the result of Pass Rule 6 or earlier ones ? 
# Report Generation
	1. It is clear that there is some pass rules to perform ICR task. What is role of those pass rules to generate required reports like Form2, SOA, Transaction Reco etc. 
	
# Recon Item
	1. If you again show us the resulting reconsilation results, it will be helpful.
	2. For currently, whatever we have developed, we are trying to reach a matching state primarily on the basis of Reference. Is there anything like our result item is creating in your system ?
	3. What is rpt fields ?
	4. By means of vendor code, we can identify the role of TSL for the transaction and according to that the Entity Type.
		a. Is this information is maintained for all lineitems ?
		b. Is there any possibility that there is same vendor code used for two types of role? If it is, then in what situation ? 
	5. 
