# Compliance Frameworks for Third-Party Risk Assessment

## 📋 Overview
This document provides a comprehensive breakdown of major compliance frameworks used in third-party risk assessments. Understanding these frameworks is crucial for evaluating vendor compliance and ensuring your organization meets regulatory requirements.

---

## 🔒 NIST Cybersecurity Framework (CSF)

### Description
The National Institute of Standards and Technology (NIST) Cybersecurity Framework provides a policy framework of computer security guidance for how private sector organizations can assess and improve their ability to prevent, detect, and respond to cyber attacks.

### Core Functions
1. **Identify (ID)**
   - Asset Management
   - Business Environment
   - Governance
   - Risk Assessment
   - Risk Management Strategy

2. **Protect (PR)**
   - Identity Management and Access Control
   - Awareness and Training
   - Data Security
   - Information Protection Processes
   - Maintenance
   - Protective Technology

3. **Detect (DE)**
   - Anomalies and Events
   - Security Continuous Monitoring
   - Detection Processes

4. **Respond (RS)**
   - Response Planning
   - Communications
   - Analysis
   - Mitigation
   - Improvements

5. **Recover (RC)**
   - Recovery Planning
   - Improvements
   - Communications

### Vendor Assessment Questions
- Does the vendor have documented cybersecurity policies aligned with NIST CSF?
- How does the vendor identify and manage cybersecurity risks?
- What protective measures are in place for data and systems?
- How quickly can the vendor detect security incidents?
- What is the vendor's incident response process?
- How does the vendor recover from cybersecurity incidents?

---

## 🛡️ ISO 27001 - Information Security Management

### Description
ISO 27001 is an international standard that specifies requirements for establishing, implementing, maintaining, and continually improving an information security management system (ISMS).

### Key Control Areas (Annex A)
1. **Information Security Policies** (A.5)
2. **Organization of Information Security** (A.6)
3. **Human Resource Security** (A.7)
4. **Asset Management** (A.8)
5. **Access Control** (A.9)
6. **Cryptography** (A.10)
7. **Physical and Environmental Security** (A.11)
8. **Operations Security** (A.12)
9. **Communications Security** (A.13)
10. **System Acquisition, Development and Maintenance** (A.14)
11. **Supplier Relationships** (A.15)
12. **Information Security Incident Management** (A.16)
13. **Information Security Aspects of Business Continuity** (A.17)
14. **Compliance** (A.18)

### Vendor Assessment Questions
- Is the vendor ISO 27001 certified by an accredited certification body?
- When was the last surveillance/recertification audit?
- Does the vendor maintain a documented ISMS?
- How does the vendor manage information security risks?
- What controls are in place for access management?
- How are security incidents handled and reported?

---

## 🔍 SOC 2 (Service Organization Control 2)

### Description
SOC 2 is an auditing procedure that ensures service providers securely manage data to protect client interests and privacy. It focuses on five "Trust Service Criteria."

### Trust Service Criteria
1. **Security**
   - Protection against unauthorized access
   - Logical and physical access controls
   - System monitoring

2. **Availability**
   - System uptime and performance
   - Monitoring and incident response
   - Change management

3. **Processing Integrity**
   - Accurate, complete, and timely processing
   - Data validation and error handling
   - System monitoring for processing failures

4. **Confidentiality**
   - Protection of confidential information
   - Data classification and handling
   - Access controls for sensitive data

5. **Privacy**
   - Collection, use, retention, and disposal of personal information
   - Privacy notice and consent management
   - Data subject rights

### SOC 2 Report Types
- **Type I**: Tests design effectiveness at a specific point in time
- **Type II**: Tests design and operating effectiveness over a period (typically 6-12 months)

### Vendor Assessment Questions
- Does the vendor have a current SOC 2 Type II report?
- Which Trust Service Criteria are covered in the report?
- Are there any exceptions or management responses?
- How recent is the report (within the last 12 months)?
- Can the vendor provide the SOC 2 report under NDA?

---

## 🌍 GDPR (General Data Protection Regulation)

### Description
The General Data Protection Regulation is a legal framework that sets guidelines for the collection and processing of personal information from individuals who live in the European Union.

### Key Principles
1. **Lawfulness, Fairness, and Transparency**
2. **Purpose Limitation**
3. **Data Minimization**
4. **Accuracy**
5. **Storage Limitation**
6. **Integrity and Confidentiality**
7. **Accountability**

### Key Requirements
- **Data Protection Impact Assessments (DPIA)**
- **Privacy by Design and by Default**
- **Data Subject Rights**
  - Right to Access
  - Right to Rectification
  - Right to Erasure
  - Right to Restrict Processing
  - Right to Data Portability
  - Right to Object
- **Breach Notification** (72 hours to supervisory authority)
- **Data Protection Officer (DPO)** requirements

### Vendor Assessment Questions
- How does the vendor ensure GDPR compliance for EU data subjects?
- What is the vendor's lawful basis for processing personal data?
- How does the vendor handle data subject requests?
- What data protection measures are implemented?
- How quickly can the vendor report data breaches?
- Does the vendor have a designated DPO?
- Are Data Processing Agreements (DPA) in place?

---

## 🏥 HIPAA (Health Insurance Portability and Accountability Act)

### Description
HIPAA establishes national standards for protecting sensitive patient health information from being disclosed without patient consent or knowledge.

### Key Rules
1. **Privacy Rule**
   - Protects Protected Health Information (PHI)
   - Patient rights regarding their health information
   - Permitted uses and disclosures

2. **Security Rule**
   - Administrative Safeguards
   - Physical Safeguards
   - Technical Safeguards

3. **Breach Notification Rule**
   - Notification requirements for PHI breaches
   - 60-day notification to affected individuals
   - Annual summary for smaller breaches

### Security Safeguards
**Administrative Safeguards:**
- Security Officer designation
- Workforce training and access management
- Information access management
- Security awareness and training

**Physical Safeguards:**
- Facility access controls
- Workstation use and media controls
- Device and media controls

**Technical Safeguards:**
- Access control
- Audit controls
- Integrity
- Person or entity authentication
- Transmission security

### Vendor Assessment Questions
- Is the vendor HIPAA compliant for handling PHI?
- Does the vendor sign Business Associate Agreements (BAA)?
- What safeguards are in place to protect PHI?
- How does the vendor handle HIPAA breach incidents?
- What audit controls are implemented?
- How is PHI transmitted and stored securely?

---

## 📊 Compliance Mapping Matrix

| Framework | Focus Area | Certification Required | Audit Frequency | Key Documentation |
|-----------|------------|----------------------|----------------|-------------------|
| NIST CSF | Cybersecurity | No | Self-assessment | Framework implementation |
| ISO 27001 | Information Security | Yes | Annual | Certificate, ISMS documentation |
| SOC 2 | Service Controls | Report-based | Annual | SOC 2 Type II report |
| GDPR | Data Protection | No | Ongoing | DPA, Privacy policies |
| HIPAA | Healthcare Data | No | Ongoing | BAA, Risk assessment |

---

## 🎯 Vendor Assessment Checklist

### Pre-Assessment
- [ ] Identify applicable compliance frameworks
- [ ] Determine required certifications/reports
- [ ] Prepare framework-specific questionnaires
- [ ] Set compliance expectations and requirements

### During Assessment
- [ ] Request relevant certifications and reports
- [ ] Verify certification validity and scope
- [ ] Review exception items and management responses
- [ ] Assess gap remediation plans
- [ ] Validate control implementation through evidence

### Post-Assessment
- [ ] Document compliance status for each framework
- [ ] Identify compliance gaps and risks
- [ ] Develop remediation timeline if needed
- [ ] Establish ongoing monitoring requirements
- [ ] Plan for periodic compliance reviews

---

## 🔄 Continuous Monitoring

### Key Activities
1. **Certificate/Report Renewal Tracking**
   - Monitor expiration dates
   - Request updated documentation
   - Validate continued compliance

2. **Regulatory Updates**
   - Stay informed of framework changes
   - Update assessment criteria
   - Communicate changes to vendors

3. **Incident Monitoring**
   - Track vendor security incidents
   - Assess compliance impact
   - Review incident response effectiveness

4. **Performance Metrics**
   - Compliance adherence rates
   - Time to remediate gaps
   - Vendor compliance maturity scores

---

## 📚 Additional Resources

### Official Documentation
- [NIST Cybersecurity Framework](https://www.nist.gov/cyberframework)
- [ISO 27001 Standard](https://www.iso.org/isoiec-27001-information-security.html)
- [AICPA SOC 2 Reports](https://www.aicpa.org/interestareas/frc/assuranceadvisoryservices/aicpasoc2report.html)
- [GDPR Official Text](https://gdpr-info.eu/)
- [HHS HIPAA Guidelines](https://www.hhs.gov/hipaa/index.html)

### Industry Resources
- NIST Special Publications (800 series)
- ISO 27001 Toolkit and templates
- SOC 2 readiness assessments
- GDPR compliance checklists
- HIPAA security risk assessment tools

---

*Last Updated: June 2025*
*Document Version: 1.0*