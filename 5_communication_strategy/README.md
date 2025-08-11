# DataCents: Audience & Communication Strategy

## 📑 Table of Contents

- [Objective](#objective)
- [1. Target Audience Analysis](#1-target-audience-analysis)
  - [Persona 1: The Risk & Compliance Leader](#persona-1-the-risk--compliance-leader)
  - [Persona 2: The Technology & Implementation Leader](#persona-2-the-technology--implementation-leader)
- [2. Outreach Strategy: How We Will Reach Them](#2-outreach-strategy-how-we-will-reach-them)
  - [1. Optimize the Hub (The Website)](#1-optimize-the-hub-the-website)
  - [2. Engage in Their Environment (LinkedIn)](#2-engage-in-their-environment-linkedin)
  - [3. Direct (but soft) Outreach](#3-direct-but-soft-outreach)
- [3. The Communication Artifact](#3-the-communication-artifact)

---

## Objective

To engage key decision-makers in the FinTech lending space, demonstrating the
value of the DataCents model in mitigating credit risk and driving business
growth. We want them to see our project not just as academic research, but as a
viable, data-driven solution to a core business problem.

[Back to Top](#datacents-audience--communication-strategy)

---

## 1. Target Audience Analysis

Our primary targets are influential leaders at top P2P lending and FinTech
companies, specifically **Lending Club** and **Upstart**. We have identified key
individuals and created personas to guide our outreach.

---

### Persona 1: The Risk & Compliance Leader

**Target Individuals:**

- Annie Armstrong (Chief Risk Officer,  [Lending Club](https://www.lendingclub.com/))
- Annie Delgado (Chief Risk Officer, [Upstart](https://www.upstart.com/))

**Who They Are:**

As CROs, they are directly responsible for the company's risk management
framework. This includes credit risk, model governance, regulatory compliance,
and fraud prevention. Their world revolves around quantifying, mitigating, and
reporting on risk.

**Capabilities & Mindset:**

- Highly data-literate and analytical.
- Understands and scrutinizes statistical models (e.g., ROC AUC, F1-Score).
- Thinks in terms of portfolio performance, loss reduction, and regulatory
  soundness.

**Constraints:**

- Extremely time-poor and inundated with data.
- Skeptical of "black box" solutions; requires transparency and interpretability
  (our SHAP analysis is key here).
- Must justify any new model or tool with a clear ROI and ensure it meets strict
  compliance standards.

**What We Want Them to Learn:**

- Our XGBoost model has a proven accuracy (**0.72 ROC AUC**) in predicting loan
  defaults.
- The model is interpretable and identifies key risk drivers (interest rate,
  FICO, DTI), aligning with their domain expertise.
- Our *State-Level Risk* feature offers a unique dimension to risk assessment
  that they may not currently be using.

**How We Hope They Will Act:**

- Recognize the potential of our model to enhance their existing risk assessment
  frameworks.
- Initiate a conversation or connect us with their internal Head of Data Science
  or Credit Risk Modeling team for a technical deep-dive.

[Back to Top](#datacents-audience--communication-strategy)

---

### Persona 2: The Technology & Implementation Leader

**Target Individual:**

- Jordan Cheng (Chief Technology Officer,  
  [Lending Club](https://www.lendingclub.com/))

**Who They Are:**

The CTO is responsible for the company's technology stack, data infrastructure,
and the implementation of new models into production environments.

**Capabilities & Mindset:**

- Focuses on scalability, reliability, and ease of integration.
- Evaluates projects based on technical feasibility and resource requirements.
- Interested in modern, efficient technologies (like XGBoost).

**Constraints:**

- Manages a complex roadmap of competing tech priorities.
- Concerned with data security and the cost of implementation.

**What We Want Them to Learn:**

- Our model is built on a standard, well-documented tech stack  
  (Python, Scikit-learn, XGBoost).
- The project is well-structured  
  ([GitHub Repo](https://github.com/dadishimwe/datacents)) and ready for
  technical due diligence.

**How We Hope They Will Act:**

- See our project as technically sound and viable for potential integration.
- Greenlight a technical exploration or a pilot project with their data
  engineering/ML Ops teams.

[Back to Top](#datacents-audience--communication-strategy)

---

## 2. Outreach Strategy: How We Will Reach Them

Our approach is a targeted, multi-channel strategy focused on **LinkedIn**,
leveraging our primary communication artifact: the  
**DataCents Project Website**.

---

### 1. Optimize the Hub (The Website)

The website at  
[https://dadishimwe.github.io/datacents/](https://dadishimwe.github.io/datacents/)
is our central hub. It already presents the key takeaway, the team, and the
problem. We will ensure it prominently features links to:

- The [GitHub Repo](https://github.com/MIT-Emerging-Talent/ET6-CDSP-group-15-repo.git)
for technical
  validation
- The *Technical White Paper* for in-depth analysis

[Back to Top](#datacents-audience--communication-strategy)

---

### 2. Engage in Their Environment (LinkedIn)

**Join Key Groups:** We will join the professional networks where our target
audience is active:

- [Credit Risk Management Professionals Network](
  https://www.linkedin.com/groups/8943675/)
- [FinTech Professionals Network](
  https://www.linkedin.com/groups/8820573/)
- [Peer-to-Peer Lending Professionals](
  https://www.linkedin.com/groups/7469353/)

**Share Valuable Content:**

We will post a concise summary of our key findings in these groups. The post
will include a compelling visual (like our SHAP summary plot) and a link back
to our project website.

**Example Post:**

> Fascinating insights from our analysis of 2M+ P2P loans.  
> We found that interest rate and loan grade are the biggest predictors of  
> default, and our XGBoost model can predict it with **72% accuracy**.  
> We believe this has huge implications for risk management.  
> See the full breakdown on our project site:  
> [DataCents Project Website](https://dadishimwe.github.io/datacents/)

[Back to Top](#datacents-audience--communication-strategy)

---

### 3. Direct (but soft) Outreach

After engaging in groups, team members can send personalized connection
requests on LinkedIn to our target individuals.

**Example Message to a CRO:**

> Hello Ms. Armstrong, I saw you are a member of the Credit Risk Professionals  
> group. My team and I recently completed a project analyzing default predictors
> in Lending Club's data that I thought might interest you. Our findings are **on**
> our project site if you'd like to take a look.  
> All the best, [Sender Name].

[Back to Top](#datacents-audience--communication-strategy)

---

## 3. The Communication Artifact

Our primary communication artifact is the **DataCents Project Website**.
It provides a comprehensive, accessible, and dynamic platform to showcase our
work. It serves as the central, multi-layered resource that all outreach
efforts will direct traffic to.

[Back to Top](#datacents-audience--communication-strategy)

---
