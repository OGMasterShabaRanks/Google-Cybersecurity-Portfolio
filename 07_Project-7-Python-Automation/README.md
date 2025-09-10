### **Project Title: Automated Log Parser & Analysis Script**

-----

**1. Project Overview**

  * **Goal:** To write a Python script that automates a common cybersecurity task—analyzing log files for suspicious activity—in order to improve efficiency and provide quick insights.
  * **Scenario:** This project simulates a daily task for a security analyst: reviewing a large volume of log data for indicators of compromise. Manually sifting through thousands of lines of log data is inefficient and prone to human error. The objective was to create an automated solution to streamline this process.
  * **Key Deliverables:**
      * The **Python script (`.py` file)** itself, with clear comments explaining the code.
      * A detailed explanation of the script's purpose and functionality in this `README.md`.
      * A sample output file to demonstrate the script's findings.

-----

**2. Skills Demonstrated**

  * **Python Scripting**
  * **Log Analysis**
  * **Automation**
  * **File I/O** (Input/Output)
  * **Regular Expressions**

-----

**3. Tools & Technologies**

  * **Language:** Python 3
  * **Libraries:** Standard Python libraries (no external packages needed)
  * **Concepts:**
      * Regular Expressions (Regex)
      * Conditional Logic
      * Automation of repetitive tasks

-----

**4. The Process: My Methodical Approach**

This project demonstrates the power of automation and scripting, a core focus of **Course 7** of the Google Cybersecurity Certificate. My process for developing this script was systematic and problem-oriented.

#### **Phase 1: Problem Identification**

  * **Action:** I identified the problem of manual log review. I recognized that a security analyst could spend a significant amount of time sifting through thousands of log entries to find specific events, such as failed login attempts or unauthorized access.
  * **Reference to Cert:** This phase aligns with the certificate's emphasis on using automation to solve real-world security challenges, improving both efficiency and accuracy.

#### **Phase 2: Script Development**

  * **Action:** I wrote a Python script designed to read a log file line by line. Using regular expressions, the script was programmed to search for specific patterns that indicate suspicious activity, such as "failed login," "access denied," or other custom strings.
  * **Reference to Cert:** This stage directly applies the practical skills learned in **Course 7**, where we were introduced to Python for security tasks, including file handling and using regular expressions to parse complex text data.

#### **Phase 3: Output and Reporting**

  * **Action:** The script was designed to not just find the patterns, but to also extract key information—such as the timestamp, source IP address, and username—and compile it into a clean, easy-to-read output. This provides a concise summary of all suspicious activity, ready for further investigation.
  * **Reference to Cert:** This demonstrates a core principle of effective automation: the output must be useful. By creating a report rather than just a simple count, the script provides a valuable artifact for an analyst to act upon.

-----

**5. Results and Key Takeaways**

This project demonstrates my ability to use Python as a practical tool for cybersecurity. The script effectively automates a tedious, time-consuming process, allowing an analyst to focus on higher-level threat intelligence and response. The most valuable lesson was learning how to apply scripting to solve a real-world problem, proving that even a basic understanding of a language like Python can significantly enhance an analyst's capabilities and efficiency.

### **Key Deliverable & Artifacts**

  * **[View the Python log parser script here.](log_parser.py)**
  * **[View the sample log script output here.](sample-log-output.txt)**