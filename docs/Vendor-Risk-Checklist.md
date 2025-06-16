# Vendor Risk Assessment Checklist

## Overview
This checklist provides a comprehensive framework for evaluating third-party vendors across multiple risk domains. Each section contains weighted questions that contribute to the overall risk score.

---

## 1. Security Controls & Infrastructure (Weight: 25%)

### 1.1 Data Protection
- [ ] Does the vendor encrypt data at rest using industry-standard encryption (AES-256)?
- [ ] Is data encrypted in transit using TLS 1.2 or higher?
- [ ] Are encryption keys managed through a secure key management system?
- [ ] Does the vendor have documented data classification policies?

### 1.2 Access Management
- [ ] Is multi-factor authentication (MFA) enforced for all administrative accounts?
- [ ] Does the vendor implement role-based access controls (RBAC)?
- [ ] Are privileged accounts regularly reviewed and audited?
- [ ] Is there a formal user access provisioning/deprovisioning process?

### 1.3 Network Security
- [ ] Does the vendor maintain network segmentation between environments?
- [ ] Are firewalls and intrusion detection systems implemented?
- [ ] Is regular vulnerability scanning performed on all systems?
- [ ] Are security patches applied within defined timeframes?

### 1.4 Incident Response
- [ ] Does the vendor have a documented incident response plan?
- [ ] Are security incidents reported to customers within 24 hours?
- [ ] Is there a dedicated security team or CISO?
- [ ] Are incident response procedures tested regularly?

---

## 2. Compliance & Certifications (Weight: 20%)

### 2.1 Industry Certifications
- [ ] SOC 2 Type II certification (current within 12 months)
- [ ] ISO 27001 certification
- [ ] PCI DSS compliance (if applicable)
- [ ] FedRAMP authorization (if applicable)

### 2.2 Regulatory Compliance
- [ ] GDPR compliance documentation and DPA available
- [ ] HIPAA compliance (if handling PHI)
- [ ] CCPA compliance (if applicable)
- [ ] Industry-specific regulations addressed

### 2.3 Audit & Assessment
- [ ] Regular third-party security assessments performed
- [ ] Penetration testing conducted annually
- [ ] Vulnerability assessments performed quarterly
- [ ] Compliance audit results available for review

---

## 3. Data Governance & Privacy (Weight: 20%)

### 3.1 Data Handling
- [ ] Clear data processing purposes documented
- [ ] Data retention policies defined and enforced
- [ ] Secure data deletion procedures in place
- [ ] Data portability options available

### 3.2 Data Location & Transfer
- [ ] Data processing locations clearly identified
- [ ] Cross-border data transfer safeguards implemented
- [ ] Data residency requirements can be met
- [ ] Subprocessor agreements in place

### 3.3 Privacy Controls
- [ ] Privacy impact assessments conducted
- [ ] Data subject rights procedures documented
- [ ] Privacy by design principles implemented
- [ ] Data breach notification procedures defined

---

## 4. Business Continuity & Resilience (Weight: 15%)

### 4.1 Availability & Uptime
- [ ] SLA guarantees 99.9% uptime or higher
- [ ] Redundant systems and failover capabilities
- [ ] Geographic distribution of data centers
- [ ] Real-time monitoring and alerting systems

### 4.2 Backup & Recovery
- [ ] Regular automated backups performed
- [ ] Backup integrity testing conducted
- [ ] Disaster recovery plan documented and tested
- [ ] RTO/RPO objectives defined and achievable

### 4.3 Vendor Stability
- [ ] Vendor has been in business for 3+ years
- [ ] Financial stability demonstrated
- [ ] Key personnel retention strategies
- [ ] Alternative vendor options identified

---

## 5. Operational Security (Weight: 10%)

### 5.1 Personnel Security
- [ ] Background checks performed on all employees
- [ ] Security awareness training provided regularly
- [ ] Confidentiality agreements signed by all staff
- [ ] Insider threat monitoring programs in place

### 5.2 Physical Security
- [ ] Data centers have appropriate physical security controls
- [ ] Visitor access controls and logging implemented
- [ ] Environmental controls (fire, flood, temperature) in place
- [ ] Secure disposal of hardware and media

---

## 6. Contract & Legal (Weight: 10%)

### 6.1 Contractual Protections
- [ ] Comprehensive service level agreements (SLAs)
- [ ] Data processing addendum (DPA) executed
- [ ] Liability and indemnification clauses appropriate
- [ ] Termination and data return procedures defined

### 6.2 Legal & Regulatory
- [ ] Vendor operates in stable legal jurisdiction
- [ ] No significant legal or regulatory issues
- [ ] Intellectual property protections in place
- [ ] Export control compliance addressed

---

## Risk Scoring Matrix

### Score Calculation
- **Critical (4 points)**: Failure represents immediate high risk
- **High (3 points)**: Significant risk that requires mitigation
- **Medium (2 points)**: Moderate risk with acceptable controls
- **Low (1 point)**: Minimal risk, standard controls sufficient

### Risk Thresholds
- **Low Risk**: 85-100% compliance
- **Medium Risk**: 70-84% compliance  
- **High Risk**: 55-69% compliance
- **Critical Risk**: Below 55% compliance

### Weighted Category Scores
Each category is weighted according to its importance:
- Security Controls: 25% of total score
- Compliance: 20% of total score
- Data Governance: 20% of total score
- Business Continuity: 15% of total score
- Operational Security: 10% of total score
- Contract & Legal: 10% of total score

---

## Assessment Instructions

1. **Preparation**: Gather vendor documentation, certifications, and contracts
2. **Evaluation**: Complete each section with vendor-provided evidence
3. **Scoring**: Assign points based on the risk scoring matrix
4. **Calculation**: Apply category weights to determine overall risk score
5. **Remediation**: Develop action plans for high-risk areas
6. **Monitoring**: Schedule regular reassessments based on risk level

## Documentation Requirements

For each assessment, maintain:
- Completed checklist with evidence references
- Supporting documentation and certifications
- Risk score calculations and justifications
- Identified gaps and remediation plans
- Reassessment schedule and responsibilities