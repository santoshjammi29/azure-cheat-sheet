# 🧠 Curriculum Topics Directory — 91 Topics Covered

> **Curriculum Scope**: **91 Production Topics** verified against real-world lakehouse internals, query engines, and distributed architectures.
> **Organization**: Grouped by **Relevant Functional Sections** and then by **Difficulty Level**.
> **Navigation**: All sections are **collapsible and collapsed by default** for rapid scanning.
> **Live Web Hub**: Explore interactive search and mindmaps at [moderndataengineer.uk/concepts](https://moderndataengineer.uk/concepts).

---

## 📑 Topics Directory at a Glance

| Pillar / Module | Topics | Functional Sections Covered | Status |
|:---|:---:|:---|:---:|
| ⚡ **Microsoft Fabric & OneLake Architecture** | **39** | OneLake & Cross-Cloud Shortcuts, Direct Lake Mode & Semantic Models, Workload Engines, F-SKU Capacities & Governance | ✅ Collapsible Deck |
| 🔄 **Azure Data Factory (ADF) & Resilient Orchestration** | **27** | Control Flow, Pipelines & Parameterization, Integration Runtimes (Azure IR / Self-Hosted IR), Data Movement, Managed VNets & Security | ✅ Collapsible Deck |
| 📊 **Power BI & VertiPaq Analytics Engine** | **25** | VertiPaq Engine & Columnar Compression, DAX Evaluation Context & Calculations, Composite Models, Semantic Refresh & Aggregations | ✅ Collapsible Deck |

---

## 📚 Comprehensive Topic Specifications (Grouped by Section & Difficulty)

<details>
<summary><b>⚡ Microsoft Fabric & OneLake Architecture (39 Topics across 3 Sections)</b> — <i>Click to expand module</i></summary>

<details>
<summary>&nbsp;&nbsp;📂 <b>Section: OneLake & Cross-Cloud Shortcuts (18 Topics)</b> — <i>Click to expand functional domain</i></summary>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🟢 Easy: <b>🟢 Easy (Level 1) (3 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **Lakehouse** | `🟢 Easy` | An architecture that combines the flexible, cost-effective file storage of a data lake with the ACID transactions of a data warehouse. |
| 2 | **OneLake** | `🟢 Easy` | A single, unified, logical data lake for the entire organization, built on ADLS Gen2 using open Delta Parquet format. |
| 3 | **Shortcuts** | `🟢 Easy` | Virtual links in OneLake that point to other storage locations (internal or external) without copying the actual files. |

</details>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🟡 Intermediate: <b>🟡 Intermediate (Level 2) (4 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **Dataflows Gen2** | `🟡 Intermediate` | A visual, low-code data transformation tool built on Power Query that ingests and transforms data, outputting results directly into Fabric data destinations (Lakehouse, Warehouse, SQL Database). |
| 2 | **Direct Lake Mode** | `🟡 Intermediate` | A Power BI storage mode that reads Delta Parquet files directly from OneLake without importing or running SQL queries. |
| 3 | **Fabric Warehouse COPY INTO Command** | `🟡 Intermediate` | A high-throughput, parallelized T-SQL bulk ingestion command in Microsoft Fabric Warehouse and Azure Synapse optimized for loading external Parquet, CSV, or ORC files from ADLS Gen2. |
| 4 | **Mirroring** | `🟡 Intermediate` | A zero-ETL, fully managed solution that replicates operational databases (Azure SQL, Cosmos DB, Snowflake) in near real-time directly into OneLake as Delta Lake tables. |

</details>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🔴 Advanced: <b>🔴 Advanced (Level 3) (5 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **Eventhouse OneLake Availability Synchronization** | `🔴 Advanced` | The streaming synchronization bridge in Microsoft Fabric Real-Time Intelligence that mirrors KQL database tables into OneLake Delta Parquet format without retroactively duplicating historical data. |
| 2 | **Fabric Eventstream Architecture: Event Hub to Lakehouse** | `🔴 Advanced` | Microsoft Fabric's no-code/low-code real-time ingestion service that streams high-throughput IoT telemetry from Azure Event Hubs through real-time processors into Lakehouse Delta tables. |
| 3 | **Fabric Real-Time Hub & Eventstreams** | `🔴 Advanced` | A unified SaaS event streaming hub capturing, transforming, and routing streaming data to OneLake and KQL databases. |
| 4 | **KQL Database (Real-Time Intelligence)** | `🔴 Advanced` | A high-performance database optimized for real-time telemetry, log analytics, and event streams, queried using Kusto Query Language (KQL) and integrated with OneLake. |
| 5 | **Purview Metadata Enrichment & Non-Destructive Cataloging** | `🔴 Advanced` | The architectural principle ensuring that metadata enrichment, classifications, and business definitions applied in Microsoft Purview do not modify source Fabric storage objects. |

</details>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🟣 Architect: <b>🟣 Staff Architect (Level 4) (6 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **Fabric Storage Workload Decision Matrix: Warehouse vs Lakehouse vs KQL** | `🟣 Architect` | The architectural decision framework evaluating Microsoft Fabric Warehouse, Lakehouse, KQL Database, and OneLake based on transactional consistency, query engines, and data paradigms. |
| 2 | **Microsoft Fabric OneLake Shortcuts** | `🟣 Architect` | Zero-copy virtualization pointers linking external ADLS Gen2, AWS S3, or Google Cloud Storage buckets into OneLake. |
| 3 | **MPP 60-Distribution Storage Topology** | `🟣 Architect` | The MPP 60-Distribution Topology is the distributed storage architecture in Azure Synapse Analytics that partitions table storage across exactly 60 underlying database distributions. |
| 4 | **OneLake Data Mesh & Domain Governance Boundaries** | `🟣 Architect` | The multi-workspace decentralized domain architecture partitioning OneLake into autonomous product domains with automated governance gates. |
| 5 | **OneLake Tenant-Scoped Namespace & Shortcuts Architecture** | `🟣 Architect` | The unified SaaS data lake architecture of Microsoft Fabric where a single hierarchical namespace serves the entire enterprise tenant, eliminating data silos via zero-copy shortcuts. |
| 6 | **PolyBase & MPP Parallel Data Loading** | `🟣 Architect` | PolyBase is a data virtualization and high-speed ingestion technology in Azure Synapse and SQL Server that leverages MPP compute nodes to read external cloud storage blocks in parallel. |

</details>

</details>

<details>
<summary>&nbsp;&nbsp;📂 <b>Section: Direct Lake Mode & Semantic Models (5 Topics)</b> — <i>Click to expand functional domain</i></summary>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🔴 Advanced: <b>🔴 Advanced (Level 3) (3 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **Power BI Service Cloud Refresh Schema Drift** | `🔴 Advanced` | Power BI Service Cloud Refresh Schema Drift is a production outage scenario where cloud scheduled data refreshes fail following backend database column deletions or renames. |
| 2 | **Semantic Link** | `🔴 Advanced` | A Python library ('sempy') that establishes a bidirectional bridge between Spark DataFrames and Power BI semantic models. |
| 3 | **XMLA Endpoint** | `🔴 Advanced` | An industry-standard communication protocol that allows external client tools to connect directly to Fabric semantic models. |

</details>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🟣 Architect: <b>🟣 Staff Architect (Level 4) (2 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **Direct Lake Fallback & V-Order Columnar Optimization** | `🟣 Architect` | The in-memory columnar caching architecture where Power BI VertiPaq reads Delta Parquet directly without translation, and the architectural gates that prevent DirectQuery fallback. |
| 2 | **Fabric Automated Lineage & Decoupled Purview RBAC** | `🟣 Architect` | The governance security model where Fabric automated lineage capture requires specific workspace settings, while Purview enforces role-based access control completely independent of Fabric permissions. |

</details>

</details>

<details>
<summary>&nbsp;&nbsp;📂 <b>Section: Workload Engines, F-SKU Capacities & Governance (16 Topics)</b> — <i>Click to expand functional domain</i></summary>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🟢 Easy: <b>🟢 Easy (Level 1) (1 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **Copilot in Microsoft Fabric** | `🟢 Easy` | An AI-powered assistant integrated into Fabric to generate code, summarize datasets, and build reporting visuals. |

</details>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🟡 Intermediate: <b>🟡 Intermediate (Level 2) (5 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **Fabric Capacities (F-SKUs)** | `🟡 Intermediate` | The shared pool of compute resources (expressed in Capacity Units or CUs) that powers all workloads in Microsoft Fabric. |
| 2 | **Fabric Deployment Pipelines** | `🟡 Intermediate` | Built-in CI/CD release management facilitating automated promotion of Fabric workspaces from dev to test to prod. |
| 3 | **Git Integration** | `🟡 Intermediate` | A feature that connects Fabric workspaces directly to Azure DevOps or GitHub repositories for source control of item metadata. |
| 4 | **Medallion Architecture** | `🟡 Intermediate` | A data curation pattern consisting of three distinct layers: Bronze (raw), Silver (cleansed), and Gold (curated). |
| 5 | **Real-Time Intelligence** | `🟡 Intermediate` | A workload suite in Fabric designed to ingest, process, and analyze high-volume streaming data in real-time. |

</details>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🔴 Advanced: <b>🔴 Advanced (Level 3) (4 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **Fabric KQL Database (Eventhouse)** | `🔴 Advanced` | A high-performance columnar time-series database optimized for real-time telemetry, logs, and free-text search. |
| 2 | **Purview Data Quality Rules: Definition vs Execution** | `🔴 Advanced` | The governance boundary establishing that data quality rules in Microsoft Purview are centralized definitions, whereas execution requires separate implementation across compute engines. |
| 3 | **V-Order Serialization** | `🔴 Advanced` | A Microsoft-proprietary optimization algorithm applied to Delta Parquet files to accelerate read speeds. |
| 4 | **Workspace Managed Identities** | `🔴 Advanced` | System-assigned identities created at the workspace level to secure access to Azure resources without storing credentials. |

</details>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🟣 Architect: <b>🟣 Staff Architect (Level 4) (6 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **Fabric & Purview Tenant Co-location & Native Architecture** | `🟣 Architect` | The mandatory single-tenant governance architecture requiring Microsoft Purview and Microsoft Fabric to reside within the exact same Azure Active Directory (Microsoft Entra ID) tenant for native metadata, lineage, and policy integration. |
| 2 | **Fabric Capacity Unit (CU) Smoothing & Throttling** | `🟣 Architect` | The mathematical governor algorithm Microsoft Fabric uses to distribute interactive and background computational spikes over 24-hour moving averages. |
| 3 | **Fabric Declarative Git Integration & ALM Pipelines** | `🟣 Architect` | The enterprise Application Lifecycle Management (ALM) framework integrating Fabric workspaces with Git repositories and multi-stage deployment pipelines. |
| 4 | **Fabric Workspace Roles: Viewer vs Member vs Admin vs Capacity Admin** | `🟣 Architect` | The role-based access control (RBAC) hierarchy governing content authoring, access administration, and capacity resource allocation within Microsoft Fabric workspaces. |
| 5 | **Microsoft Fabric Capacity Unit (CU) Smoothing** | `🟣 Architect` | The multi-hour algorithmic capacity governance in Microsoft Fabric that averages high-intensity compute spikes over 24-hour evaluation windows. |
| 6 | **Microsoft Purview in Fabric & GDPR Compliance** | `🟣 Architect` | The unified data governance integration within Microsoft Fabric (via the Purview Hub) providing automated data discovery, PII classification, sensitivity labeling, and cross-workspace lineage essential for GDPR compliance. |

</details>

</details>

</details>

<details>
<summary><b>🔄 Azure Data Factory (ADF) & Resilient Orchestration (27 Topics across 3 Sections)</b> — <i>Click to expand module</i></summary>

<details>
<summary>&nbsp;&nbsp;📂 <b>Section: Control Flow, Pipelines & Parameterization (12 Topics)</b> — <i>Click to expand functional domain</i></summary>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🟢 Easy: <b>🟢 Easy (Level 1) (2 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **Pipeline** | `🟢 Easy` | A logical grouping of activities that coordinates and executes data workflows. |
| 2 | **Trigger** | `🟢 Easy` | The mechanism that defines when a data pipeline execution should be started. |

</details>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🟡 Intermediate: <b>🟡 Intermediate (Level 2) (3 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **ADF Bounded ForEach Concurrency** | `🟡 Intermediate` | Configuring the `batchCount` parameter on ForEach activities to limit parallel pipeline invocations. |
| 2 | **Schema Drift** | `🟡 Intermediate` | The capability of a data pipeline to gracefully handle changes in source schemas (added or renamed columns) without crashing. |
| 3 | **Tumbling Window Trigger** | `🟡 Intermediate` | A specialized time-slice trigger that supports state tracking, dependencies, and backfilling. |

</details>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🔴 Advanced: <b>🔴 Advanced (Level 3) (3 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **ADF CI/CD and Global Parameters** | `🔴 Advanced` | The deployment pipeline process that promotes ADF configurations across environments using ARM Templates. |
| 2 | **ADF Tumbling Window Self-Dependency** | `🔴 Advanced` | Configuring tumbling window triggers to depend on the successful completion of the preceding time window slice. |
| 3 | **Metadata-driven Pipelines** | `🔴 Advanced` | A pipeline design pattern where the orchestration parameters are read from an external SQL control table. |

</details>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🟣 Architect: <b>🟣 Staff Architect (Level 4) (4 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **ADF Metadata-Driven Ingestion Framework** | `🟣 Architect` | An enterprise pipeline architecture where a single parameterized Azure Data Factory pipeline orchestrates extraction for thousands of tables guided by a SQL control database. |
| 2 | **ADF Pipeline Idempotency & Concurrency Governance** | `🟣 Architect` | Fault-tolerant orchestration patterns ensuring pipeline retries produce identical results without data duplication, race conditions, or connection pool exhaustion. |
| 3 | **Metadata-Driven Dynamic ETL Framework Architecture** | `🟣 Architect` | Universal pipeline architecture orchestrating thousands of heterogeneous table ingestions dynamically using database control tables and parameterized activities. |
| 4 | **Metadata-Driven Pipeline Orchestration: GetMetadata and ForEach** | `🟣 Architect` | A scalable Data Factory pipeline design pattern that dynamically controls data ingestion workflows by querying centralized metadata tables using Lookup, ForEach, and GetMetadata activities. |

</details>

</details>

<details>
<summary>&nbsp;&nbsp;📂 <b>Section: Integration Runtimes (Azure IR / Self-Hosted IR) (4 Topics)</b> — <i>Click to expand functional domain</i></summary>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🟢 Easy: <b>🟢 Easy (Level 1) (1 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **SHIR Auto-Update** | `🟢 Easy` | The automated mechanism that downloads and applies updates to Self-Hosted Integration Runtime nodes. |

</details>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🟡 Intermediate: <b>🟡 Intermediate (Level 2) (1 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **Self-hosted Integration Runtime (SHIR)** | `🟡 Intermediate` | The compute infrastructure used to run copy activities and scan metadata on private networks. |

</details>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🔴 Advanced: <b>🔴 Advanced (Level 3) (1 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **ADF Self-Hosted Integration Runtime (SHIR)** | `🔴 Advanced` | An agent installed on an on-premises machine or private cloud virtual network that enables Azure Data Factory to securely access and copy data from protected internal network sources. |

</details>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🟣 Architect: <b>🟣 Staff Architect (Level 4) (1 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **Self-Hosted Integration Runtime (SHIR) High-Availability Clustering** | `🟣 Architect` | Scalable multi-node agent topology linking cloud data factories to on-premises enterprise networks with automated failover and dynamic load balancing. |

</details>

</details>

<details>
<summary>&nbsp;&nbsp;📂 <b>Section: Data Movement, Managed VNets & Security (11 Topics)</b> — <i>Click to expand functional domain</i></summary>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🟢 Easy: <b>🟢 Easy (Level 1) (2 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **Linked Service** | `🟢 Easy` | The connection definition that defines connection strings and credentials to external resources in ADF. |
| 2 | **Variables vs Parameters** | `🟢 Easy` | Orchestration primitives defining constant configuration inputs (Parameters) vs dynamic execution values (Variables). |

</details>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🟡 Intermediate: <b>🟡 Intermediate (Level 2) (5 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **ADF REST API Pagination Handling** | `🟡 Intermediate` | Configuring pagination rules (AbsoluteUrl, QueryParameters, NextSibling) to incrementally extract paginated JSON feeds. |
| 2 | **Data Factory Managed Airflow** | `🟡 Intermediate` | A managed service in ADF that hosts Apache Airflow environments, enabling Python-based DAG orchestration. |
| 3 | **Managed Private Endpoints** | `🟡 Intermediate` | Private IP addresses provisioned inside the ADF Managed Virtual Network to secure connections to Azure resources. |
| 4 | **Managed Virtual Network (Managed VNet)** | `🟡 Intermediate` | A secure networking feature that runs ADF Integration Runtimes inside a dedicated private network boundary, connecting to services via Private Endpoints. |
| 5 | **Mapping Data Flows** | `🟡 Intermediate` | A visual, code-free data transformation tool in ADF that executes on an underlying Spark cluster. |

</details>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🔴 Advanced: <b>🔴 Advanced (Level 3) (3 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **ADF Mapping Data Flows vs. Azure Databricks** | `🔴 Advanced` | The architectural decision framework comparing ADF's visual, code-free Spark execution engine (Mapping Data Flows) against code-first Azure Databricks compute for enterprise ETL/ELT. |
| 2 | **Azure Synapse Link** | `🔴 Advanced` | A cloud-native, zero-ETL synchronization service that continuously replicates operational data into analytical stores. |
| 3 | **Dynamic Parameterization** | `🔴 Advanced` | The practice of using runtime parameters to configure connection strings, dataset schemas, and targets. |

</details>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🟣 Architect: <b>🟣 Staff Architect (Level 4) (1 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **ADF Managed Private Endpoint Provisioning & Timeout Bypass** | `🟣 Architect` | Enterprise network security architecture managing lifecycle, approval protocols, and timeout bypass for private endpoints inside ADF Managed Virtual Networks. |

</details>

</details>

</details>

<details>
<summary><b>📊 Power BI & VertiPaq Analytics Engine (25 Topics across 3 Sections)</b> — <i>Click to expand module</i></summary>

<details>
<summary>&nbsp;&nbsp;📂 <b>Section: VertiPaq Engine & Columnar Compression (5 Topics)</b> — <i>Click to expand functional domain</i></summary>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🟢 Easy: <b>🟢 Easy (Level 1) (1 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **Import Mode** | `🟢 Easy` | A storage mode where data is loaded and compressed directly into the Power BI Analysis Services memory engine. |

</details>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🟡 Intermediate: <b>🟡 Intermediate (Level 2) (1 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **DirectQuery Mode** | `🟡 Intermediate` | A storage mode where Power BI does not import data, but queries the source system in real-time. |

</details>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🔴 Advanced: <b>🔴 Advanced (Level 3) (1 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **VertiPaq Engine** | `🔴 Advanced` | The in-memory columnar database engine that powers Power BI datasets and Analysis Services models. |

</details>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🟣 Architect: <b>🟣 Staff Architect (Level 4) (2 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **Power BI Direct Lake Mode & VertiPaq Paging** | `🟣 Architect` | A semantic model connectivity mode in Microsoft Fabric where the VertiPaq engine loads Delta Parquet columnar files directly from OneLake into memory without scheduled refresh. |
| 2 | **VertiPaq Engine Columnar Compression & Cardinality Reduction** | `🟣 Architect` | Low-level memory optimization strategies governing dictionary encoding, Run-Length Encoding (RLE), and bit-packing in the VertiPaq engine. |

</details>

</details>

<details>
<summary>&nbsp;&nbsp;📂 <b>Section: DAX Evaluation Context & Calculations (6 Topics)</b> — <i>Click to expand functional domain</i></summary>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🟢 Easy: <b>🟢 Easy (Level 1) (2 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **Row Context** | `🟢 Easy` | The active row evaluation environment in DAX that occurs during calculated column evaluations or iterator loops. |
| 2 | **Visual Calculations** | `🟢 Easy` | DAX calculations defined and executed directly within a specific visual, bypassing semantic model structure changes. |

</details>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🟡 Intermediate: <b>🟡 Intermediate (Level 2) (2 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **Calculation Groups** | `🟡 Intermediate` | A model design pattern that uses the SELECTEDMEASURE() function to define dynamic, reusable DAX calculations that can be applied to any visual metric. |
| 2 | **Filter Context** | `🟡 Intermediate` | The active filtering parameters applied to a visual at the time of DAX measure execution. |

</details>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🔴 Advanced: <b>🔴 Advanced (Level 3) (2 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **CALCULATE Function** | `🔴 Advanced` | The primary DAX function used to modify the active Filter Context or trigger Context Transition. |
| 2 | **DAX Calculation Groups** | `🔴 Advanced` | Dynamic calculation modifiers in tabular models allowing a single calculation item (e.g. YTD, YoY%) to apply across all base measures. |

</details>

</details>

<details>
<summary>&nbsp;&nbsp;📂 <b>Section: Composite Models, Semantic Refresh & Aggregations (14 Topics)</b> — <i>Click to expand functional domain</i></summary>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🟢 Easy: <b>🟢 Easy (Level 1) (1 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **Star Schema** | `🟢 Easy` | A dimensional data modeling design containing central fact tables surrounded by descriptive dimension tables. |

</details>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🟡 Intermediate: <b>🟡 Intermediate (Level 2) (4 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **Power BI Project (.pbip)** | `🟡 Intermediate` | A developer-focused directory save format that stores reports and semantic models as separate text-based files to enable Git source control and CI/CD. |
| 2 | **Query Folding** | `🟡 Intermediate` | The capability of Power Query to compile visual transformation steps into a single SQL statement executed by the source database. |
| 3 | **Row-Level Security (RLS)** | `🟡 Intermediate` | A security feature that restricts database row access for specific users based on active role filters. |
| 4 | **TMDL Declarative Semantic Modeling** | `🟡 Intermediate` | A human-readable, folder-based serialization format for Power BI semantic models designed for Git version control. |

</details>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🔴 Advanced: <b>🔴 Advanced (Level 3) (5 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **Composite Models** | `🔴 Advanced` | A model design that combines tables with different storage modes (Import and DirectQuery) in a single dataset. |
| 2 | **Hybrid Tables** | `🔴 Advanced` | A semantic model partition design that combines historical cached data (Import) with real-time live data (DirectQuery). |
| 3 | **Incremental Refresh** | `🔴 Advanced` | A pattern that partitions datasets so only recently changed data slices are refreshed. |
| 4 | **Power BI Aggregation Tables (Dual Storage)** | `🔴 Advanced` | Creating pre-aggregated in-memory tables mapped to detail tables, allowing visual queries to hit memory whenever possible. |
| 5 | **Tabular Model Definition Language (TMDL)** | `🔴 Advanced` | A human-readable, indentation-based YAML-like language used to define semantic model metadata and structures. |

</details>

<details>
<summary>&nbsp;&nbsp;&nbsp;&nbsp;🟣 Architect: <b>🟣 Staff Architect (Level 4) (4 Topics)</b></summary>

| # | Topic / Concept | Difficulty | Architectural Definition & Core Principle |
|:---:|---|:---:|---|
| 1 | **Composite Models & Hybrid Table Partitioning** | `🟣 Architect` | Multi-tiered storage engine architecture combining Import, DirectQuery, and Dual storage modes in a single enterprise semantic model. |
| 2 | **Object-Level Security (OLS) & Dynamic RLS at Scale** | `🟣 Architect` | Fine-grained security architecture enforcing dynamic row filters and complete column/table metadata obfuscation across enterprise user bases. |
| 3 | **Power BI Direct Lake Framing Operation & Capacity Units** | `🟣 Architect` | The sub-second, metadata-only refresh mechanism in Power BI Direct Lake mode that synchronizes Delta Lake table schemas and file pointers without loading or copying data, consuming minimal CUs. |
| 4 | **XMLA Endpoint Governance & Large Dataset Storage Format** | `🟣 Architect` | Programmatic semantic model manipulation, automated partition management, and scale-out architecture via XMLA read/write endpoints. |

</details>

</details>

</details>

---

## 🌐 Ecosystem Interlinking
All curriculum topics are synchronized across the 14-repository Modern Data Engineering ecosystem:
- [Modern Data Engineer Hub](https://github.com/santoshjammi29/moderndataengineer) — Central edge web platform and 921-topic encyclopedia
- [Databricks Handbook](https://github.com/santoshjammi29/databricks-handbook) — Unity Catalog, Delta Lake 3.x, and Lakeflow
- [PySpark Handbook](https://github.com/santoshjammi29/pyspark-handbook) — Distributed compute & PySpark internals
- [SQL Handbook](https://github.com/santoshjammi29/sql-handbook) — Query engine optimization & relational internals
- [dbt Handbook](https://github.com/santoshjammi29/dbt-handbook) — Analytics engineering, contracts, and modeling
- [Streaming Handbook](https://github.com/santoshjammi29/streaming-handbook) — Event streaming, Kafka, and Flink
- [DataOps & CI/CD Handbook](https://github.com/santoshjammi29/dataops-cicd-handbook) — Airflow, orchestration, and infrastructure
- [System Design Handbook](https://github.com/santoshjammi29/data-system-design-handbook) — Distributed architecture and scalability
- [Interview Handbook](https://github.com/santoshjammi29/data-engineering-interview-handbook) — 20 Knowledge Pillars & architectural defense
- [Azure Cheat Sheet](https://github.com/santoshjammi29/azure-cheat-sheet) — Fabric, OneLake, and ADF enterprise blueprints
- [Security Handbook](https://github.com/santoshjammi29/security-handbook) — Zero-trust, IAM, and lakehouse governance
