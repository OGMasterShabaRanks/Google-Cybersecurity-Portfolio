### **Project Title: Automating Allowed IP addresses using Python Algorithms**

-----

**1. Project Overview**

  * **Goal:** To create a Python algorithm that automates the process of updating a file of approved IP addresses by removing IP addresses from a separate "remove list." This automation improves efficiency and ensures the accuracy of the allow list.
  * **Scenario:** This project simulates a real-world task for a cybersecurity professional: managing IP-based access control. Manually updating a list of IP addresses is tedious and prone to human error, especially as IP addresses are added and removed over time. The objective was to create an automated solution to streamline this critical security process.
  * **Key Deliverables:**
      * The **Python script** reference guide, with clear explanations on where they could possibly fit within your algorithm.
      * A detailed explanation of the script's purpose and functionality in this `README.md`.
      * A sample output to demonstrate the algorithm's findings.

-----

**2. Skills Demonstrated**

  * **Python Scripting**
  * **File I/O (Input/Output)**
  * **Data Structures (Lists and Strings)**
  * **Conditional Logic**
  * **Automation of Repetitive Tasks**

-----

**3. Tools & Technologies**

  * **Language:** Python 3  
  * **Libraries:** Standard Python libraries (no external packages needed)  
  * **Concepts:**
      * `with` statements for file handling  
      * `for` loops for iteration  
      * Conditional statements (`if`)  
      * String and list methods (`.split()`, `.join()`, `.remove()`)

-----

**4. The Process: My Methodical Approach**

This project demonstrates the power of automation and scripting, a core focus of **Course 7** of the Google Cybersecurity Certificate. My process for developing this algorithm was systematic and problem-oriented.

#### **Phase 1: Problem Identification**

  * **Action:** I identified the problem of manual IP allow list management at my organization. I recognized that relying on a person to manually remove IP addresses could lead to security vulnerabilities if the list was not updated in a timely or accurate manner.
  * **Reference to Cert:** This phase aligns with the certificate's emphasis on using automation to solve real-world security challenges, improving both efficiency and accuracy.

#### **Phase 2: Algorithm Development**

  * **Action:** I wrote a Python algorithm to read the `"allow_list.txt"` file into a list of IP addresses. It then iterates through a separate remove list and uses conditional logic to remove any matching IP addresses from the allow list.
  * **Reference to Cert:** This stage directly applies the practical skills learned in **Course 7**, where we were introduced to Python for security tasks, including file handling, data manipulation, and applying conditional logic.

#### **Phase 3: File Update and Reporting**

  * **Action:** The algorithm converts the revised list of IP addresses back into a string and rewrites the `"allow_list.txt"` file. This provides a final, accurate allow list without needing manual intervention.
  * **Reference to Cert:** This demonstrates a core principle of effective automation: the output must be useful. By automatically updating the allow list, the algorithm provides a valuable security artifact for the organization.

-----

**5. Results and Key Takeaways**

This project demonstrates my ability to use Python as a practical tool for cybersecurity. The algorithm effectively automates a tedious and security-critical task, allowing an administrator to focus on higher-level security posture management. The most valuable lesson was learning how to apply scripting to solve a real-world problem, proving that even a basic understanding of a language like Python can significantly enhance an organization's security capabilities and efficiency.

### **Key Deliverable & Artifacts**

  * **[View the Python IP reference guide here.](python-commands.pdf)**  
  * **[View the  automated ip allowed list updater algorithm breakdon here.](automated-ip-allow-list-updater.pdf)** 