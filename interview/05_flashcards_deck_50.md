# 🗂️ Microsoft Azure & Cloud Architecture Flashcard Deck (50 Active Recall Questions)

> **Coverage**: Core Compute, Networking, Storage, Databases, Data & AI (Fabric/Databricks/OpenAI), Security & FinOps
> **Target Certifications**: AZ-900, DP-203, DP-600, DP-700, AZ-305

---

### 1. What are the 4 levels of the Azure scope hierarchy?

**Answer:**  
Root Management Group -> Child Management Groups -> Subscriptions -> Resource Groups -> Resources. Policy and RBAC permissions inherit transitively downward.

---

### 2. How many IP addresses are reserved by Azure in every subnet?

**Answer:**  
5 IP addresses: .0 (Network address), .1 (Default gateway), .2 and .3 (Azure DNS mapping), and .255 (Broadcast address).

---

### 3. What is an Azure Availability Zone (AZ)?

**Answer:**  
Physically separate datacenters within an Azure region, each with independent power, cooling, and networking, providing high-availability fault domain protection.

---

### 4. What is the difference between an NSG and an Azure Firewall?

**Answer:**  
An NSG is a basic, stateful Layer 3/4 packet filter applied at subnet or NIC level. Azure Firewall is a managed Layer 3-7 stateful firewall with threat intelligence, FQDN filtering, and centralized routing.

---

### 5. What is an Azure Private Endpoint?

**Answer:**  
A network interface that assigns a private IP address from your VNet to an Azure PaaS service (e.g. Azure SQL, Storage, Key Vault), keeping all traffic within the Microsoft backbone network.

---

### 6. What is the purpose of Private DNS Zone linking in Azure?

**Answer:**  
It resolves the public FQDN (e.g. `mydb.database.windows.net`) to the private IP (`10.x.x.x`) assigned by the Private Endpoint, preventing queries from routing to the public internet.

---

### 7. Explain the difference between System-Assigned and User-Assigned Managed Identity.

**Answer:**  
System-Assigned: Tied 1:1 to a specific Azure resource lifecycle; deleted automatically when resource is deleted. User-Assigned: Standalone Azure identity resource; can be assigned to multiple VMs or containers.

---

### 8. What is Microsoft Fabric OneLake?

**Answer:**  
The 'OneDrive for data': a unified, SaaS, multi-cloud multi-tenant data lake built natively on Azure Data Lake Storage (ADLS Gen2) and Delta Lake table format.

---

### 9. What is Power BI Direct Lake mode in Microsoft Fabric?

**Answer:**  
A breakthrough semantic model storage mode that queries Delta Parquet files directly from OneLake without importing data into memory or generating SQL translations via DirectQuery.

---

### 10. What is the difference between Hot, Cool, Cold, and Archive Blob storage tiers?

**Answer:**  
Hot: Lowest access cost, highest storage cost (active data). Cool: Lower storage, 30-day min retention. Cold: Lower storage, 90-day min retention. Archive: Lowest storage, hours retrieval latency, 180-day min retention.

---

### 11. What is the difference between LRS, ZRS, GRS, and GZRS storage redundancy?

**Answer:**  
LRS: 3 copies in 1 DC. ZRS: 3 copies across 3 AZs in same region. GRS: LRS in primary + asynchronous copy to paired secondary region. GZRS: ZRS in primary + LRS in secondary.

---

### 12. What is Azure Bicep?

**Answer:**  
A domain-specific language (DSL) for deploying Azure resources declaratively, offering cleaner syntax, better modularity, and automatic dependency management compared to raw ARM JSON templates.

---

### 13. What is the Azure Hub-and-Spoke network topology?

**Answer:**  
A central Hub VNet hosts shared networking infrastructure (Azure Firewall, ExpressRoute Gateway, VPN Gateway, DNS), while Spoke VNets host application workloads peered to the Hub.

---

### 14. Is Azure VNet peering transitive by default?

**Answer:**  
No. Spoke A peered to Hub cannot communicate with Spoke B unless User Defined Routes (UDRs) and an IP forwarding NVA/Firewall are deployed in the Hub.

---

### 15. What is an ExpressRoute Gateway?

**Answer:**  
A dedicated network gateway that connects an on-premises network to Azure via a private dedicated fiber connection (bypassing the public internet) with SLA guarantees.

---

### 16. What are the 5 consistency levels in Azure Cosmos DB?

**Answer:**  
1. Strong (linearizable). 2. Bounded Staleness (guaranteed time/version lag). 3. Session (read-your-own-writes, default). 4. Consistent Prefix (no out-of-order reads). 5. Eventual (weakest, lowest latency).

---

### 17. What is Azure Data Factory Integration Runtime (IR), and what are the 3 types?

**Answer:**  
The compute infrastructure ADF uses for data movement and dispatch: 1. Azure IR (serverless cloud). 2. Self-Hosted IR (on-prem/private network behind firewalls). 3. Azure-SSIS IR (for legacy SSIS packages).

---

### 18. What is Azure Databricks Unity Catalog?

**Answer:**  
A unified governance solution for Databricks Lakehouse providing 3-level namespaces (`catalog.schema.table`), row-level security, column masking, audit logging, and open data sharing.

---

### 19. What is Azure OpenAI Service, and how does it guarantee enterprise data privacy?

**Answer:**  
Enterprise-hosted OpenAI models (GPT-4o, o1, embeddings) inside Azure tenant boundaries. Customer prompts and data are never used to train base models and adhere to enterprise HIPAA/SOC2 controls.

---

### 20. What is Azure AI Search (formerly Cognitive Search)?

**Answer:**  
A high-performance cloud search engine supporting hybrid search (keyword BM25 + dense vector cosine search) with semantic reranking for enterprise RAG applications.

---

### 21. What is Azure Event Hubs vs Azure Service Bus?

**Answer:**  
Event Hubs: High-throughput, partitioned, append-only distributed log (big data streaming, Kafka API). Service Bus: Enterprise message broker with FIFO queues, pub/sub topics, transactions, and dead-letter queues.

---

### 22. What is Azure Front Door?

**Answer:**  
A global, scalable entry-point and Layer 7 reverse proxy / CDN with integrated Web Application Firewall (WAF), SSL offloading, and global Anycast failover across paired regions.

---

### 23. What is Azure Traffic Manager?

**Answer:**  
A DNS-based traffic load balancer that distributes client requests across regional public endpoints using routing methods (Priority, Weighted, Performance, Geographic).

---

### 24. What is the difference between Azure Application Gateway and Azure Load Balancer?

**Answer:**  
Application Gateway: Layer 7 HTTP/HTTPS reverse proxy with cookie-based affinity, SSL termination, and WAF. Azure Load Balancer: Ultra-low latency Layer 4 TCP/UDP transport-level load balancer.

---

### 25. What is an Azure Managed Disk Snapshot?

**Answer:**  
A full, read-only copy of a managed VHD disk stored as standard blob storage, used for point-in-time recovery, backup, and VM cloning.

---

### 26. Why should developers avoid leaving unattached Premium SSD Managed Disks?

**Answer:**  
Unattached managed disks continue to bill 24/7 for their full provisioned gigabytes even if no VM is attached.

---

### 27. What is Azure Cost Management & Billing Anomaly Alerting?

**Answer:**  
A native FinOps feature that uses machine learning to detect unusual daily spending spikes above historical baselines and triggers automated webhooks/emails.

---

### 28. What is an Azure Reserved Instance (RI)?

**Answer:**  
A 1-year or 3-year commitment for compute (VMs, SQL Databases, Databricks) providing up to 72% cost savings compared to pay-as-you-go pricing.

---

### 29. What is Azure Hybrid Benefit?

**Answer:**  
A licensing benefit that allows customers to use existing on-premises Windows Server and SQL Server licenses with Software Assurance to save up to 85% on Azure cloud VMs and databases.

---

### 30. What is Azure Policy?

**Answer:**  
A governance engine that enforces organizational rules and compliance at scale (e.g. denying public IPs on VMs, enforcing mandatory tags, restricting allowed regions).

---

### 31. What are the 3 effect modes of an Azure Policy definition?

**Answer:**  
`Audit` (logs non-compliant resources), `Deny` (blocks resource creation), and `DeployIfNotExists` / `Modify` (automatically remediates non-compliant resources).

---

### 32. What is Azure Key Vault Soft-Delete and Purge Protection?

**Answer:**  
Soft-Delete retains deleted keys/secrets for 90 days. Purge Protection enforces that a deleted vault or secret cannot be permanently purged until the retention period expires, preventing ransomware deletion.

---

### 33. What is Azure Monitor Log Analytics Workspace?

**Answer:**  
The centralized storage repository for metrics and logs collected from Azure resources, queried using Kusto Query Language (KQL).

---

### 34. What is Kusto Query Language (KQL)?

**Answer:**  
A read-only query language optimized for exploring massive structured and semi-structured time-series telemetry data across Azure Monitor, Microsoft Sentinel, and Fabric Real-Time Intelligence.

---

### 35. What is Azure Kubernetes Service (AKS) Azure CNI vs Kubenet?

**Answer:**  
Azure CNI: Every pod receives a real, routable IP address from the Azure VNet subnet. Kubenet: Pods receive virtual IPs from an internal overlay network and use NAT to access the VNet.

---

### 36. What is Azure Container Apps (ACA)?

**Answer:**  
A fully managed, serverless container platform built on Kubernetes (K8s), KEDA (event-driven autoscaling), and Dapr, allowing developers to run microservices without managing Kubernetes clusters.

---

### 37. What is Azure Cosmos DB Request Unit (RU)?

**Answer:**  
The normalized currency of Cosmos DB throughput measuring the CPU, memory, and IOPS required to perform a database operation (e.g. reading a 1KB document = 1 RU).

---

### 38. What is the difference between Azure SQL Database and Azure SQL Managed Instance?

**Answer:**  
Azure SQL Database: Fully managed serverless/provisioned DBaaS with high availability. Managed Instance: Near 100% compatibility with on-prem SQL Server engine (cross-database queries, SQL Agent, CLR, linked servers).

---

### 39. What is Azure Synapse Dedicated SQL Pool (formerly Azure SQL DW)?

**Answer:**  
An MPP (Massively Parallel Processing) columnar relational data warehouse using DWUs (Data Warehouse Units) with distributed hash/replicated tables.

---

### 40. What is Microsoft Purview?

**Answer:**  
An enterprise data governance and data security platform providing automated data cataloging, lineage tracking, sensitive data discovery, and access policy management.

---

### 41. What is Azure Logic Apps?

**Answer:**  
A serverless, low-code iPaaS integration workflow service with 400+ pre-built connectors to SaaS, on-prem, and cloud systems.

---

### 42. What is Azure Functions Consumption Plan vs Premium Plan?

**Answer:**  
Consumption Plan: Serverless, scales from 0 to thousands, pay per execution, subject to cold starts. Premium Plan: Pre-warmed instances (zero cold starts), VNet integration, unlimited execution duration.

---

### 43. What is Azure Site Recovery (ASR)?

**Answer:**  
A native Disaster Recovery as a Service (DRaaS) solution that orchestrates replication, failover, and failback of physical and virtual machines between Azure regions or from on-premises to Azure.

---

### 44. What is Azure Service Health vs Azure Resource Health?

**Answer:**  
Service Health: Global dashboard reporting Microsoft datacenter outages and planned maintenance affecting your subscription. Resource Health: Granular health status of a specific Azure resource instance.

---

### 45. What is an Azure Application Gateway Ingress Controller (AGIC)?

**Answer:**  
A Kubernetes pod that monitors AKS ingress resources and dynamically translates them into Azure Application Gateway routing rules and backend pools.

---

### 46. What is Azure Spot VM?

**Answer:**  
Unused Azure compute capacity available at up to 90% discount, subject to eviction when Azure requires the capacity back (ideal for stateless batch jobs).

---

### 47. What is Azure Blueprints (transitioning to Azure Template Specs / Deployment Stacks)?

**Answer:**  
A declarative framework for defining repeatable packages of Azure resources, RBAC role assignments, policy assignments, and resource groups for landing zone provisioning.

---

### 48. What is Azure Defender for Cloud (Microsoft Defender for Cloud)?

**Answer:**  
A Cloud Security Posture Management (CSPM) and Cloud Workload Protection Platform (CWPP) that provides continuous security posture scoring and threat detection.

---

### 49. What is Azure Data Lake Storage Gen2 (ADLS Gen2)?

**Answer:**  
Blob storage enhanced with a Hierarchical Namespace (HNS), allowing true directory renaming, directory-level atomic operations, and POSIX-compliant ACLs for big data analytics engines.

---

### 50. What is the single most critical security rule for Azure PaaS access?

**Answer:**  
Disable public network access entirely on all storage accounts, databases, and key vaults, enforcing access exclusively through Private Endpoints and Managed Identities.

---
