I understand. My apologies for the repeated error with the links. I have identified the mistake and will provide the corrected `README.md` with the links formatted correctly to work within the `project-4-linux-sql` folder.

Here is the finalized `README.md` for your **Linux & SQL Security Analysis** project.

-----

### **Project Title: Linux & SQL Security Analysis**

-----

**1. Project Overview**

  * **Goal:** To demonstrate proficiency in using **Linux command-line** tools and **SQL queries** to perform essential security-related tasks, such as system auditing, log analysis, and database security checks.
  * **Scenario:** This project simulates the role of a junior cybersecurity analyst tasked with auditing a server and a user database. The objective is to use foundational tools to identify security misconfigurations and potential malicious activity.
  * **Key Deliverables:**
      * A **Linux Scripting** section showcasing how to use commands to perform security audits and log analysis.
      * A **SQL Query Analysis** section demonstrating how to query a database to find security-relevant information, such as finding all users with a specific access level or analyzing failed login attempts.

-----

**2. Skills Demonstrated**

  * **Linux Command Line**
  * **File Permissions** & **User Management**
  * **SQL Queries**
  * **Log Analysis**
  * **Bash Scripting**
  * **System Auditing**

-----

**3. Tools & Technologies**

  * **Operating System:** Linux (e.g., Ubuntu, Kali Linux)
  * **Tools:**
      * Bash (for command-line operations)
      * SQL (e.g., SQLite, MySQL, PostgreSQL)
  * **Concepts:**
      * Access Control Models
      * Database Security

-----

**4. The Process: My Methodical Approach**

This project applies the fundamental skills from the Google Cybersecurity Certificate's **Course 4**, "Tools of the Trade," by using both Linux and SQL in a practical, security-focused manner.

#### **Phase 1: Linux System Auditing & Log Analysis**

  * **Action:** I began by performing a simulated system audit using key Linux commands. This involved checking file and directory permissions to ensure proper access control, investigating user accounts, and analyzing log files to search for suspicious activity like repeated failed login attempts.
  * **Reference to Cert:** This phase directly applies the knowledge from **Course 4**, where we learned how to navigate the Linux file system and use commands like `ls -l` for permissions, `grep` for log analysis, and `chmod` to enforce security best practices.

**Code Snippets:**

```bash
# Check file permissions and ownership of a critical directory
ls -l /var/www/html/

# Search for "failed password" attempts in the authentication log
grep "Failed password" /var/log/auth.log

# Change permissions on a private key to restrict access
chmod 600 ~/.ssh/id_rsa
```

#### **Phase 2: SQL Database Security Auditing**

  * **Action:** I used SQL to query a hypothetical user database to identify potential security vulnerabilities. I wrote queries to find users with privileged access levels, analyze patterns of failed login attempts, and check for weak password hashes.
  * **Reference to Cert:** This task showcases the application of SQL for security purposes, a key skill taught in **Course 4**. It demonstrates how a security analyst can use database queries as a powerful tool for investigation.

**SQL Queries:**

```sql
-- Find users with administrative or elevated privileges
SELECT username, role FROM users WHERE role = 'admin' OR role = 'privileged';

-- Count the number of failed login attempts per user
SELECT username, COUNT(*) as failed_attempts FROM login_logs WHERE status = 'failed' GROUP BY username ORDER BY failed_attempts DESC;
```

-----

**5. Results and Key Takeaways**

This project demonstrates my proficiency with two of the most fundamental tools in a cybersecurity analyst's toolkit: the Linux command line and SQL. The most valuable takeaway was realizing how these seemingly simple tools can be leveraged to perform complex investigations and audits. This project proves my ability to navigate and secure systems and databases at a foundational level, a critical skill for any entry-level cybersecurity role.

### **Key Deliverable & Artifacts**

  * **[View the sample SQL queries here.](sql_queries.pdf)**
  * **[View the Linux commands here.](linux-comands.pdf)**