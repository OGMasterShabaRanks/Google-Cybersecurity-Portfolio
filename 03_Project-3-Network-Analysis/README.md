### **Project Title: Network Traffic Analysis & Hardening Report**

---

**1. Project Overview**

* **Goal:** The primary goal of this project was to analyze network traffic data to identify security vulnerabilities and provide a detailed report on how to strengthen the network's defenses.

* **Scenario:** This project simulates a security audit of a small business network. I was given a captured packet file (`.pcap`) and tasked with acting as a cybersecurity analyst to investigate the network's behavior, identify unsecure communications, and recommend a strategy for system hardening.

* **Key Deliverables:**
    * A **Network Analysis Report** detailing my findings, including evidence of any vulnerabilities discovered.
    * A list of recommended **Network Hardening** techniques and security controls to mitigate identified risks.

**2. Skills Demonstrated**

* **Packet Analysis** (using Wireshark)
* **Network Protocol Analysis** (TCP/IP, HTTP, FTP)
* **Network Security**
* **Vulnerability Identification**
* **System Hardening**
* **Technical Reporting**

**3. Tools & Technologies**

* **Tools:**
    * Wireshark (or tcpdump)
    * Text Editor (for the report)

* **Concepts:**
    * TCP/IP Model
    * Unencrypted Communications (e.g., clear-text passwords)
    * Network Hardening Best Practices

**4. The Process: My Methodical Approach**

This project was a hands-on application of the networking concepts and principles taught in the Google Cybersecurity Certificate. My process was divided into two key phases: analysis and recommendation.

* **Phase 1: Traffic Analysis & Investigation**
    * **Action:** Using Wireshark, I methodically analyzed the provided `.pcap` file. I applied display filters to isolate specific protocols (e.g., HTTP, FTP) and looked for patterns of suspicious or unencrypted traffic. My investigation focused on identifying clear-text credentials, unsecure data transfers, and any unusual communication between hosts.
    * **Reference to Cert:** This process directly applies the knowledge gained in **Course 3**, which covers how to use network protocol analyzers to investigate network traffic and understand communication protocols.

* **Phase 2: Vulnerability Identification and Reporting**
    * **Action:** After identifying key vulnerabilities, such as a user transmitting their password in clear text, I documented my findings in a structured report. I included screenshots from Wireshark (in the form of a TCP/HTTP log screenshot) as evidence and clearly explained the security risks associated with each vulnerability.
    * **Reference to Cert:** This task reinforces the critical-thinking skills emphasized throughout the program, particularly the ability to identify security flaws and articulate their importance to stakeholders.

**5. Results and Key Takeaways**

This project demonstrated my ability to not only use a crucial cybersecurity tool like Wireshark but also to interpret the data it provides. The most significant takeaway was understanding the importance of encryption and the dangers of unsecure protocols. This project proves my foundational skill in analyzing network behavior and providing actionable recommendations to protect a network.

### **Key Deliverable & Artifacts**

* **[View the full Wireshark TCP/HTTP log screenshot](screenshots/wireshark-TCP-HTTP-log-screenshot.png)**
* **[View the full network analysis report](network-analysis-report.pdf)**
* **[View the full network hardening report](network-hardening-report.pdf)**