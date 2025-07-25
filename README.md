# DataActuals

# Data Ingestion Process

## 1. Data Quality and Validation Checks (Pre-Ingestion)

Before ingestion, perform data quality spot checks to ensure compliance with data standards:

- **Schema Conformance**:
  - Validate file format, column headers, title naming conventions, currency formats, and date formats.
  
- **Master Data Alignment**:
  - Ensure that all **Client Item IDs** are mapped and consistent with the **AF ID**.

- **Replacement Record Validation**:
  - Confirm that any replacement entries reference **active records** in the system (referential integrity).

---

## 2. Data Ingestion via Python 

- Place the validated file in the designated **folder** linked to the Python ingestion process.
  
- Specify the **Primary Key** associated with the relevant account for lineage tracking.
  
- Ensure that **field names (column headers)** in the CSV align exactly with expected schema definitions.
  - Example: `DATA_SHEET` should match the expected worksheet/tab name in the data model.


---

## 3. SQL Data Load and Transformation

- After Python processing, confirm that data has been successfully sync to the **dbo.DataActuals**.

- For **replacement records**:
  - Perform **data deactivation** for old records.
  - Load new records with updated values:
    - Set `SurveyCondition = 1`
    - Apply new `SurveyConditionDate`

- Recommend to maintain a clear audit trail of changes.

---

## 4. Reporting and Notification

- For accounts requiring follow-up post-extraction, notify the relevant **Customer Success Data Owner** once ingestion is complete.
  
- Confirm successful ingestion, move file from **To do** to **Complete** folder.

---

## Notes
**IRT** account require additional extraction steps after ingestion. 
