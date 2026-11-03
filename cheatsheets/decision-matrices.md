# 🧭 Azure Architecture Decision Trees & Comparison Matrices

Definitive decision matrices and flowcharts for choosing the optimal Azure service across Compute, Storage, Databases, Messaging, Networking, and Big Data Analytics.

---

## 📑 Table of Contents
1. [Compute Selection Decision Tree](#1-compute-selection-decision-tree)
2. [Database & Storage Selection Matrix](#2-database--storage-selection-matrix)
3. [Messaging & Event Streaming Decision Guide](#3-messaging--event-streaming-decision-guide)
4. [Analytics & Lakehouse Engine Comparison (Fabric vs. Databricks vs. Synapse)](#4-analytics--lakehouse-engine-comparison)
5. [Load Balancing & Ingress Guide](#5-load-balancing--ingress-guide)

---

## 1. Compute Selection Decision Tree

```mermaid
flowchart TD
    Start([New Workload Deployment]) --> Q_OS{Do you need direct OS / kernel access or custom drivers?}
    Q_OS -- Yes --> VM[Azure Virtual Machines / VMSS]
    Q_OS -- No --> Q_Container{Is application packaged in Docker containers?}
    
    Q_Container -- No --> Q_EventDriven{Is it pure event-driven code executed on triggers?}
    Q_EventDriven -- Yes --> Fn[Azure Functions (Serverless)]
    Q_EventDriven -- No --> AppService[Azure App Service (PaaS Web/API)]

    Q_Container -- Yes --> Q_K8sOrchestration{Do you need full Kubernetes API, custom CRDs, or fine-grained cluster control?}
    Q_K8sOrchestration -- Yes --> AKS[Azure Kubernetes Service (AKS)]
    Q_K8sOrchestration -- No --> Q_Microservices{Microservices with Dapr, KEDA, and scale-to-zero?}
    Q_Microservices -- Yes --> ACA[Azure Container Apps (ACA)]
    Q_Microservices -- No --> AppServiceContainer[App Service on Containers / ACI]
```

### Compute Services Comparison

| Dimension | Azure Functions | Azure App Service | Azure Container Apps (ACA) | Azure Kubernetes Service (AKS) | Azure Virtual Machines |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Abstraction Level** | Serverless Code (FaaS) | Managed Platform (PaaS) | Serverless Container (CaaS) | Managed Kubernetes (K8s) | Infrastructure (IaaS) |
| **Container Native?** | Optional | Optional | **Yes** | **Yes** | Optional |
| **Scale-to-Zero?** | Yes | No (Always reserved) | **Yes** (via KEDA) | With KEDA / Virtual Nodes | No (Manual deallocation) |
| **Cold Starts** | Possible (Flex tier minimizes) | None (Warm instances) | Minimal | None | N/A |
| **Networking** | VNet Injection (Flex/Premium) | VNet Integration / Private EP | Managed VNet / Private EP | Full CNI Overlay / Network Policies | Full VNet Control |
| **Operational Overhead** | Near Zero | Minimal | Low | Medium to High | High (OS Patching, AMIs) |
| **Best Used For** | Event processing, webhook handlers, scheduled timers | Monolithic web apps, REST APIs, traditional CMS | Cloud-native microservices, background queues, AI agents | Complex microservice graphs, Service Mesh, multi-tenant SaaS | Legacy software, Windows domain dependencies, GPU workloads |

---

## 2. Database & Storage Selection Matrix

```mermaid
flowchart TD
    StartData([Storage / Database Selection]) --> Q_Structured{Structured relational data with strict SQL ACID?}
    
    Q_Structured -- Yes --> Q_Scale{Single-node RDBMS or globally distributed multi-region?}
    Q_Scale -- Multi-Region / NoSQL --> Cosmos[Azure Cosmos DB]
    Q_Scale -- Single-Node / HA --> Q_Engine{Preferred SQL Engine?}
    Q_Engine -- T-SQL / SQL Server --> AzureSQL[Azure SQL Database / Managed Instance]
    Q_Engine -- PostgreSQL --> PgFlex[Azure Database for PostgreSQL Flexible]
    Q_Engine -- MySQL --> MyFlex[Azure Database for MySQL Flexible]
    
    Q_Structured -- No --> Q_DataLake{Analytical Big Data Lakehouse or General File/Object?}
    Q_DataLake -- Analytical Lakehouse --> ADLS[Azure Data Lake Storage Gen2 (HNS)]
    Q_DataLake -- General File/Object --> Q_Protocol{File Protocol (SMB/NFS) or HTTP REST?}
    Q_Protocol -- HTTP REST Blob --> Blob[Azure Blob Storage]
    Q_Protocol -- SMB / Enterprise NFS --> Q_IOPS{Ultra-high IOPS / sub-millisecond?}
    Q_IOPS -- Yes --> ANF[Azure NetApp Files]
    Q_IOPS -- Standard --> AzureFiles[Azure Files]
```

### Database Comparison

| Service | Data Model | Scalability | SLA | Consistency | Best For |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Azure Cosmos DB** | Document, Key-Value, Graph, Vector | Horizontal (Unlimited auto-partitioning) | 99.999% (Multi-region) | 5 Tunable Levels (Strong to Eventual) | Low-latency globally distributed apps, retail carts, gaming profiles |
| **Azure SQL Database** | Relational (T-SQL) | Vertical + Hyperscale (up to 100TB) | 99.995% | Strong (ACID) | Enterprise line-of-business applications, financial ledgers |
| **Azure PostgreSQL Flexible** | Relational + `pgvector` | Vertical + Read Replicas + Citus | 99.99% | Strong (ACID) | Open-source web stacks, GIS (`PostGIS`), AI RAG embeddings |
| **ADLS Gen2** | Object Storage with POSIX Hierarchy | Exabytes | 99.9% to 99.99% | Strong (Read-after-write) | Big data lakehouses, Spark, Delta Lake, Fabric OneLake, Hadoop |

---

## 3. Messaging & Event Streaming Decision Guide

| Requirement | Azure Event Hubs | Azure Service Bus | Azure Event Grid | Azure IoT Hub |
| :--- | :--- | :--- | :--- | :--- |
| **Type** | Big Data Streaming / Telemetry | Enterprise Message Broker | Reactive Pub/Sub Event Router | Device-to-Cloud Bidirectional Gateway |
| **Protocol** | Kafka, AMQP, HTTPS | AMQP, HTTPS | HTTP Webhooks, MQTT, CloudEvents | MQTT, AMQP, HTTPS |
| **Throughput** | Millions of events/sec | Thousands of messages/sec | High-frequency reactive routing | Millions of connected devices |
| **Ordering** | Partition-level key ordering | Sessions (FIFO strictly guaranteed) | No strict order guaranteed | Per-device message ordering |
| **Message Operations** | Append-only streaming replay | Peek-lock, Dead-lettering, Poison queue, Duplicate detection | Push delivery with exponential backoff retry | Device twins, remote firmware commands |
| **Ideal Scenarios** | IoT ingestion, clickstream analytics, Kafka migration | Order processing, financial transactions, workflow decoupling | Serverless triggers (Blob created ➔ Resize), system events | Connected vehicle fleets, industrial smart sensors |

---

## 4. Analytics & Lakehouse Engine Comparison

### Microsoft Fabric vs. Azure Databricks vs. Azure Synapse

| Dimension | Microsoft Fabric | Azure Databricks | Azure Synapse Analytics |
| :--- | :--- | :--- | :--- |
| **Architectural Model** | Unified SaaS Data Platform | Lakehouse Platform (Managed PaaS) | Traditional PaaS MPP + Spark |
| **Primary Storage Layer** | **OneLake** (Single tenant-wide Delta Parquet foundation) | Customer Managed ADLS Gen2 with **Unity Catalog** | ADLS Gen2 (Decoupled per workspace) |
| **Power BI Integration** | **Direct Lake Mode** (Sub-second in-memory queries directly on Parquet) | DirectQuery or Import Mode | DirectQuery or Import Mode |
| **Zero-Copy Sharing** | **OneLake Shortcuts** (Virtualize S3, GCS, ADLS without copying data) | Delta Sharing (Open cross-platform sharing protocol) | Azure Data Share (Scheduled copying) |
| **Compute Engine** | Shared F-SKU Capacity (Spark, T-SQL Warehouse, KQL Eventhouse) | Databricks Runtimes, Photon Engine, Databricks SQL Serverless | Dedicated SQL Pools (60 Distributions), Serverless SQL, Spark |
| **Governance Engine** | Microsoft Purview Native Integration | **Unity Catalog** (3-level namespace: `catalog.schema.table`) | Synapse Studio / Azure Purview |
| **FinOps Predictability** | Fixed monthly F-SKU with 24-hr automatic workload smoothing | Consumption-based DBU (Databricks Units) + Azure VM costs | DWU provisioned hourly + Serverless \$5/TB scanned |
| **Recommended Verdict** | **Best for Microsoft-centric enterprise ecosystems**, Power BI heavy reporting, and fast time-to-market. | **Best for complex distributed PySpark pipelines**, advanced AI/ML modeling (MLflow), and multi-cloud portability. | **Legacy maintenance**; new modern workloads should target Fabric or Azure Databricks. |

---

## 5. Load Balancing & Ingress Guide

| Dimension | Azure Front Door | Azure Application Gateway | Azure Load Balancer | Azure API Management (APIM) |
| :--- | :--- | :--- | :--- | :--- |
| **Scope** | Global (Anycast Edge network) | Regional | Regional | Regional or Multi-region |
| **OSI Layer** | Layer 7 (HTTP/HTTPS) | Layer 7 (HTTP/HTTPS/WebSocket) | Layer 4 (TCP/UDP) | Layer 7 (API Specific) |
| **Routing Logic** | URL path, Host header, Anycast latency | URL path, Host header, Cookie affinity | IP 5-tuple hash | API paths, policies, token inspection |
| **WAF Support?** | **Yes** (Edge-based global WAF) | **Yes** (OWASP ModSecurity Core Rule Set) | No | Optional with App Gateway / Front Door |
| **SSL / TLS Offload** | Yes (At the Microsoft edge) | Yes (At regional gateway) | No (Passthrough) | Yes |
| **Key Use Case** | Global web acceleration, CDN caching, dynamic site delivery | Regional microservice ingress, AKS ingress controller | Low-latency private TCP load balancing between VM tiers | API rate limiting, JWT validation, developer portals |

---

[← Back to Main Cheat Sheet](../README.md)
