# Introduction to Information Systems – 1300CIS

**King Khalid University**  
**College of Computer Science**  
**Department of Informatics and Computer Systems**

**Assignment:** An Information System in Your Daily Life  

**Name:** [Write your full name here]  
**Student ID:** [Write your student ID here]  
**Section:** [Write your section number here]

---

## 1. Describe Your Experience

The information system I used is the King Khalid University student portal (university registration / academic system). The specific process I focused on is registering for a course for the current academic term. I used the system on **18 November 2026** for the purpose of adding one required course to my study plan so that I could complete my registration before the deadline.

Three steps I completed during this process were as follows:

1. I signed in to the student portal using my university username and password and opened the course registration page.
2. I searched for the course by its code and selected an available section that fit my timetable.
3. I confirmed the selection and submitted the registration request.

One specific detail I observed was a confirmation message that appeared after submission. The message showed that the course had been added successfully and displayed the course code, section number, and credit hours. The system also required me to enter my password again before final confirmation, which helped prevent accidental registration changes.

> **Screenshot note:** Insert 2–3 screenshots here: (1) login / registration page with personal data hidden, (2) course selection screen, (3) confirmation message. Hide your name, ID, and password.

---

## 2. Identify the Information System Components

| Component | Example in the process | Role |
|---|---|---|
| **Hardware** | My laptop (or smartphone) and the university servers that host the portal. | The laptop is the device I used to access the system. The servers store and process registration requests so many students can register at the same time. |
| **Software** | The student portal web application and the web browser (for example, Chrome). | The portal software provides the registration screens, checks available seats, and applies registration rules. The browser displays the interface and sends my requests to the server. |
| **Data** | Course code, section number, my student ID, and the selected term. | These raw facts are entered or retrieved during registration. Without accurate data, the system cannot assign the correct course or update my timetable. |
| **People** | Students (users), academic advisors, and system administrators. | Students use the system to register. Advisors may approve or guide course choices. Administrators maintain the portal, open registration periods, and fix technical problems. |
| **Networks** | The Internet connection between my device and the university network. | The network transfers login data and registration requests securely from my device to the university servers and returns confirmation messages to me. |
| **Database** | The academic database that stores courses, sections, seats, and student records. | The database keeps organized records of offered courses, remaining seats, and my registered courses. When I register, it updates my record and reduces the available seats in that section. |

---

## 3. Explain How Data Becomes Information

Data are raw facts, while information is data that has been processed and organized so that it becomes meaningful for decision-making.

**Two examples of data** entered or recorded during the process:

1. The course code I typed or selected (for example, `1300CIS`).
2. The section number and term I chose.

At that stage, these values are only facts stored by the system.

**One example of information** produced by the system is my updated registered-course list (or registration summary). This summary combines several data items—course name, section, schedule, and credit hours—into a clear result that shows whether registration succeeded and how my timetable looks.

This information helps me as a user because I can immediately confirm that the correct course was added and plan my weekly schedule. It also helps the organization (the university) because staff can monitor section capacity, manage classroom resources, and support academic planning based on accurate registration results.

---

## 4. Identify a Problem and Suggest an Improvement

**Problem:** During peak registration hours the portal sometimes became slow, and the available-seats number did not refresh quickly. As a result, I tried to select a section that appeared available, but the system later rejected the request because the seats had already been taken.

**Impact:** This caused wasted time, frustration, and the risk of missing a preferred section. Students may need to repeat the search and selection steps several times, especially when many users access the system at once.

**Suggested improvement:** The system should display a real-time seat counter and show a clear message such as “Seats just filled—please choose another section” before final submission. Adding an automatic page refresh every few seconds, or a live update of seat availability, would reduce failed attempts.

**System component involved:** This improvement mainly involves the **Software** (registration application interface and update logic) and the **Database** (accurate, up-to-date seat records). The **Networks** component is also related because faster and more reliable communication supports timely updates.

---

## 5. How the System Supports Confidentiality, Integrity, and Availability (CIA Triad)

Based on my experience with the university registration system, the CIA triad appears as follows.

**Confidentiality:** The system protects private academic data by requiring a username and password before access. Only the authenticated student can view personal records such as registered courses and grades. This prevents unauthorized people from seeing sensitive information.

**Integrity:** The system maintains the correctness of registration data by applying rules before saving changes—for example, checking prerequisites, section capacity, and schedule conflicts. After a successful registration, the confirmation message and updated course list show that the stored record matches what I selected. This helps ensure that student records are accurate and not changed incorrectly.

**Availability:** The portal is expected to be accessible online during the official registration period so students can register from different locations and devices. When the system is available, I can complete registration on time. When it becomes slow or temporarily unavailable during peak hours, availability is weakened, which shows why continuous access is important for both students and the university.

---

## References

1. King Khalid University student portal / academic registration system (personal use experience).
2. Course materials: Introduction to Information Systems – 1300CIS (system components and CIA triad concepts).

## Use of AI Tools

I used an AI tool to improve English wording and to organize the answers according to the assignment questions. The selected system, process steps, observations, problem, and examples are based on my own use of the university registration system. I reviewed and edited the final text before submission.

---

## Submission checklist (for you before upload)

1. Replace `[Write your full name/ID/section]` with your real details.
2. Change the date and any example details if your real experience was different.
3. Add your own screenshots and hide personal information.
4. In Word: Times New Roman 12, 1.5 line spacing, 2.5 cm margins.
5. Keep the document within **3 pages maximum**.
6. Export/save as PDF and name it: `StudentID_Assignment.pdf`
7. Submit on Blackboard before the deadline.
