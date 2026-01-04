
X1  - Credit limit (NT dollars)
X2  - Gender (1=male, 2=female)
X3  - Education level
X4  - Marital status
X5  - Age
X6-X11  - Repayment status (last 6 months)
X12-X17 - Bill amount (last 6 months)
X18-X23 - Payment amount (last 6 months)
Y   - Default next month (1=yes, 0=no)


## Target Variable

**default**
- 1 → Defaulted in the following month
- 0 → Did not default



## Identifier

**ID**
- Unique client identifier  
- Dropped during preprocessing (not predictive)



## Credit Limit

**X1 – LIMIT_BAL**
- Total credit limit (in NT dollars), including individual and family credit


## Demographic Variables

### X2 – SEX
- 1 → Male
- 2 → Female


### X3 – EDUCATION
- 1 → Graduate school
- 2 → University
- 3 → High school
- 4 → Others
- 0 → Unknown
- 5, 6 → Unknown / Other (grouped as "Others" in practice)


### X4 – MARRIAGE
- 1 → Married
- 2 → Single
- 3 → Others
- 0 → Unknown


### X5 – AGE
- Age in years


## Repayment Status (Past 6 Months)

**X6 – PAY_0**  
**X7 – PAY_2**  
**X8 – PAY_3**  
**X9 – PAY_4**  
**X10 – PAY_5**  
**X11 – PAY_6**

Repayment status definition:
- -1 → Paid duly
- 0 → Paid duly
- 1 → Payment delayed by 1 month
- 2 → Payment delayed by 2 months
- 3 → Payment delayed by 3 months
- 4 → Payment delayed by 4 months
- 5 → Payment delayed by 5 months
- 6 → Payment delayed by 6 months
- 7 → Payment delayed by 7 months
- 8 → Payment delayed by 8 months
- 9 → Payment delayed by 9 months or more

Higher values indicate **higher credit risk**.


## Bill Amounts (Past 6 Months)

**X12 – BILL_AMT1**  
**X13 – BILL_AMT2**  
**X14 – BILL_AMT3**  
**X15 – BILL_AMT4**  
**X16 – BILL_AMT5**  
**X17 – BILL_AMT6**

- Statement balance (in NT dollars)
- Reflects outstanding credit exposure over time


## Payment Amounts (Past 6 Months)

**X18 – PAY_AMT1**  
**X19 – PAY_AMT2**  
**X20 – PAY_AMT3**  
**X21 – PAY_AMT4**  
**X22 – PAY_AMT5**  
**X23 – PAY_AMT6**

- Amount paid by the customer (in NT dollars)
- Indicates repayment behavior and liquidity

## Notes on Data Usage

- Categorical variables are encoded numerically as provided in the raw dataset
- Feature scaling is applied during preprocessing
- Repayment history variables are key drivers of default risk
- Encoded values are retained for modelling but documented here for interpretability and governance

## Interpretation

- Higher repayment delays and bill amounts increase default risk
- Higher payment amounts and stable repayment behavior reduce default risk
- Demographic features provide supporting risk context but are not sole decision drivers
