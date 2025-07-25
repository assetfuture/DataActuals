# DataActuals

## 1. Data Quality and Validation Checks (Pre-Ingestion)

- Before ingestion, perform data quality spot checks to ensure compliance with data standards:

**File Format Validation**
  - Validate file format, column headers, title naming conventions, currency formats, and date formats.

### Master Data Alignment
  - Ensure that all Client Item IDs are mapped and consistent with the Source (e.g., AF Item IDs in the reference database).

### Replacement Record Validation
  - Confirm that any replacement entries reference active records in the system.

## Step 2: Data Ingestion via Python 

- Place the validated file in the designated data landing zone linked to the Python ingestion process.

- Specify the Primary Key associated with the relevant account for lineage tracking.

- Ensure that field names (column headers) in the CSV align exactly with expected schema definitions.
          - Example: DATA_SHEET should match the expected worksheet/tab name in the data model.

- Maintain file and process metadata for auditability and traceability.
