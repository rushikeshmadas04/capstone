"""
Seed script for Feedback Management System
Run from backend directory: python seed.py
"""

import random
from datetime import datetime, timedelta, date
from werkzeug.security import generate_password_hash

from app import create_app
from app.config.database import db
from app.models.user import User, UserRole
from app.models.course import Course
from app.models.faculty import Faculty
from app.models.skill import Skill
from app.models.student import Student
from app.models.training_program import TrainingProgram, ProgramStatus
from app.models.enrollment import Enrollment, AttendanceStatus
from app.models.attendance import Attendance
from app.models.feedback import Feedback


app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # ──────────────────────────────────────────────
    # 1. SKILLS
    # ──────────────────────────────────────────────
    skill_names = [
        "Python", "Java", "JavaScript", "TypeScript", "C++", "C#",
        "SQL", "React", "Angular", "Node.js", "Django", "Flask",
        "Spring Boot", "Machine Learning", "Data Analysis",
        "Cloud Computing", "AWS", "Docker", "Kubernetes", "DevOps",
        "REST API", "GraphQL", "MongoDB", "PostgreSQL", "Git",
        "Linux", "Cybersecurity", "Network Administration",
        "Project Management", "Agile/Scrum", "UI/UX Design",
        "Blockchain", "AI/Deep Learning", "Big Data", "Spark",
        "TensorFlow", "Tableau", "Power BI", "Microservices",
        "System Design", "Data Structures", "Algorithms",
        "Operating Systems", "Compiler Design", "Computer Networks",
        "Software Testing", "CI/CD", "Terraform", "Ansible",
        "Rust", "Go", "Swift", "Kotlin", "PHP", "Ruby",
        "Scala", "R", "MATLAB", "SAS", "Hadoop",
        "Natural Language Processing", "Computer Vision",
        "Reinforcement Learning", "Generative AI",
        "Prompt Engineering", "Robotics", "IoT",
        "Embedded Systems", "VLSI Design", "Signal Processing",
        "Quantum Computing", "AR/VR Development",
    ]

    skills = []
    for name in skill_names:
        s = Skill(name=name)
        db.session.add(s)
        skills.append(s)
    db.session.flush()

    # ──────────────────────────────────────────────
    # 2. USERS (Admin, Coordinator, Participants)
    # ──────────────────────────────────────────────
    admin_password = generate_password_hash("Admin123")
    coordinator_password = generate_password_hash("Coo123")
    participant_password = generate_password_hash("Part123")

    admin = User(
        name="Admin User",
        email="admin@feedback.com",
        password_hash=admin_password,
        role=UserRole.ADMIN,
    )
    db.session.add(admin)

    coordinator_data = [
        ("Priya Sharma", "coordinator@feedback.com"),
        ("Amit Deshmukh", "coordinator2@feedback.com"),
        ("Sneha Kulkarni", "coordinator3@feedback.com"),
        ("Vikrant Rao", "coordinator4@feedback.com"),
        ("Divya Nair", "coordinator5@feedback.com"),
        ("Rajiv Mishra", "coordinator6@feedback.com"),
    ]

    coordinators = []
    for name, email in coordinator_data:
        u = User(
            name=name,
            email=email,
            password_hash=coordinator_password,
            role=UserRole.COORDINATOR,
        )
        db.session.add(u)
        coordinators.append(u)
    db.session.flush()

    # 50 standalone participants (not students)
    participant_names = [
        ("Rahul Verma", "participant01@feedback.com"),
        ("Sneha Patil", "participant02@feedback.com"),
        ("Karan Mehta", "participant03@feedback.com"),
        ("Aisha Khan", "participant04@feedback.com"),
        ("Deepak Joshi", "participant05@feedback.com"),
        ("Nisha Reddy", "participant06@feedback.com"),
        ("Saurabh Gupta", "participant07@feedback.com"),
        ("Pooja Singh", "participant08@feedback.com"),
        ("Manish Dubey", "participant09@feedback.com"),
        ("Aditi Bose", "participant10@feedback.com"),
        ("Tarun Malhotra", "participant11@feedback.com"),
        ("Shreya Chakraborty", "participant12@feedback.com"),
        ("Nikhil Pandey", "participant13@feedback.com"),
        ("Kavya Iyer", "participant14@feedback.com"),
        ("Ashish Saxena", "participant15@feedback.com"),
        ("Megha Kulkarni", "participant16@feedback.com"),
        ("Ravi Prasad", "participant17@feedback.com"),
        ("Simran Kaur", "participant18@feedback.com"),
        ("Gaurav Sinha", "participant19@feedback.com"),
        ("Tanvi Deshpande", "participant20@feedback.com"),
        ("Abhishek Nair", "participant21@feedback.com"),
        ("Ishita Menon", "participant22@feedback.com"),
        ("Varun Bhat", "participant23@feedback.com"),
        ("Neha Kapoor", "participant24@feedback.com"),
        ("Sunil Kulkarni", "participant25@feedback.com"),
        ("Riya Sharma", "participant26@feedback.com"),
        ("Mukesh Tiwari", "participant27@feedback.com"),
        ("Harini Pillai", "participant28@feedback.com"),
        ("Prakash Das", "participant29@feedback.com"),
        ("Anjali Ghosh", "participant30@feedback.com"),
        ("Dinesh Verma", "participant31@feedback.com"),
        ("Sunita Jadhav", "participant32@feedback.com"),
        ("Kamal Raj", "participant33@feedback.com"),
        ("Pooja Bhatt", "participant34@feedback.com"),
        ("Sanjay Kulkarni", "participant35@feedback.com"),
        ("Rekha Sharma", "participant36@feedback.com"),
        ("Mohan Lal", "participant37@feedback.com"),
        ("Geeta Devi", "participant38@feedback.com"),
        ("Ajay Chauhan", "participant39@feedback.com"),
        ("Usha Rani", "participant40@feedback.com"),
        ("Mahesh Pandit", "participant41@feedback.com"),
        ("Sudha Menon", "participant42@feedback.com"),
        ("Vikas Sharma", "participant43@feedback.com"),
        ("Asha Kumari", "participant44@feedback.com"),
        ("Rajesh Kalluri", "participant45@feedback.com"),
        ("Manju Gupta", "participant46@feedback.com"),
        ("Suresh Pillai", "participant47@feedback.com"),
        ("Kiran Bhat", "participant48@feedback.com"),
        ("Nitin Deshmukh", "participant49@feedback.com"),
        ("Sapna Reddy", "participant50@feedback.com"),
    ]

    participant_users = []
    for name, email in participant_names:
        u = User(
            name=name,
            email=email,
            password_hash=participant_password,
            role=UserRole.PARTICIPANT,
        )
        db.session.add(u)
        participant_users.append(u)
    db.session.flush()

    # ──────────────────────────────────────────────
    # 3. COURSES
    # ──────────────────────────────────────────────
    course_data = [
        ("CS101", "Introduction to Computer Science", "Fundamentals of computing and programming", 30),
        ("CS201", "Data Structures & Algorithms", "Arrays, trees, graphs, sorting, searching", 45),
        ("CS301", "Object Oriented Programming", "OOP principles using Java/C++", 40),
        ("CS401", "Database Management Systems", "SQL, normalization, transactions", 35),
        ("CS501", "Operating Systems", "Process management, memory, file systems", 40),
        ("CS601", "Computer Networks", "OSI model, TCP/IP, routing, protocols", 35),
        ("CS701", "Software Engineering", "SDLC, agile, testing, project management", 30),
        ("AI101", "Introduction to AI", "Search, logic, planning, NLP basics", 45),
        ("AI201", "Machine Learning", "Supervised, unsupervised, reinforcement learning", 50),
        ("AI301", "Deep Learning", "Neural networks, CNNs, RNNs, transformers", 50),
        ("AI401", "Natural Language Processing", "Text processing, transformers, LLMs", 40),
        ("AI501", "Computer Vision", "Image processing, detection, segmentation", 40),
        ("WD101", "Web Development Fundamentals", "HTML, CSS, JavaScript basics", 30),
        ("WD201", "Frontend Development", "React/Angular, state management, routing", 40),
        ("WD301", "Backend Development", "Node.js, Flask, REST APIs, auth", 40),
        ("WD401", "Full Stack Development", "End-to-end web app development", 50),
        ("CL101", "Cloud Computing Basics", "Virtualization, IaaS, PaaS, SaaS", 30),
        ("CL201", "AWS Cloud Practitioner", "EC2, S3, RDS, Lambda, IAM", 40),
        ("CL301", "Docker & Kubernetes", "Containerization and orchestration", 35),
        ("CY101", "Cybersecurity Fundamentals", "Threats, vulnerabilities, defense strategies", 35),
        ("DA101", "Data Analysis with Python", "Pandas, NumPy, Matplotlib", 35),
        ("DA201", "Big Data Analytics", "Hadoop, Spark, data pipelines", 40),
        ("PM101", "Project Management", "Planning, scheduling, risk management", 30),
        ("PM201", "Agile & Scrum Methodology", "Sprint planning, stand-ups, retrospectives", 25),
        ("UX101", "UI/UX Design Principles", "Wireframing, prototyping, user research", 30),
    ]

    courses = []
    for code, title, desc, dur in course_data:
        c = Course(code=code, title=title, description=desc, duration_days=dur)
        db.session.add(c)
        courses.append(c)
    db.session.flush()

    # ──────────────────────────────────────────────
    # 4. FACULTY
    # ──────────────────────────────────────────────
    faculty_data = [
        ("Dr. Anand Patel", "anand.patel@feedback.com"),
        ("Dr. Meena Iyer", "meena.iyer@feedback.com"),
        ("Prof. Suresh Kumar", "suresh.kumar@feedback.com"),
        ("Dr. Kavita Joshi", "kavita.joshi@feedback.com"),
        ("Prof. Ravi Menon", "ravi.menon@feedback.com"),
        ("Dr. Nisha Gupta", "nisha.gupta@feedback.com"),
        ("Prof. Arjun Reddy", "arjun.reddy@feedback.com"),
        ("Dr. Pooja Desai", "pooja.desai@feedback.com"),
        ("Prof. Vikram Singh", "vikram.singh@feedback.com"),
        ("Dr. Lakshmi Nair", "lakshmi.nair@feedback.com"),
        ("Prof. Deepak Verma", "deepak.verma@feedback.com"),
        ("Dr. Shalini Bose", "shalini.bose@feedback.com"),
        ("Prof. Manish Tiwari", "manish.tiwari@feedback.com"),
        ("Dr. Priyanka Chauhan", "priyanka.chauhan@feedback.com"),
        ("Prof. Rajesh Kulkarni", "rajesh.kulkarni@feedback.com"),
    ]

    faculties = []
    for name, email in faculty_data:
        f = Faculty(name=name, email=email)
        db.session.add(f)
        faculties.append(f)
    db.session.flush()

    # Assign 3-5 random skills to each faculty
    for f in faculties:
        f.skills = random.sample(skills, random.randint(3, 5))
    db.session.flush()

    # ──────────────────────────────────────────────
    # 5. PARTICIPANT USERS + STUDENTS (75 total)
    # ──────────────────────────────────────────────
    first_names = [
        "Aarav", "Vivaan", "Aditya", "Arjun", "Sai", "Rohan", "Vihaan", "Krishna",
        "Ishaan", "Shaurya", "Atharv", "Advik", "Pranav", "Advaith", "Aarush",
        "Ananya", "Diya", "Priya", "Aanya", "Aadhya", "Saanvi", "Myra", "Sara",
        "Anvi", "Pihu", "Navya", "Riya", "Kiara", "Aisha", "Harini", "Meera",
        "Tanvi", "Kavya", "Ishita", "Divya", "Neha", "Shreya", "Pooja", "Simran",
        "Kiran", "Geeta", "Sunita", "Rekha", "Usha", "Asha", "Manju", "Sudha",
        "Amit", "Sanjay", "Mohan", "Rajesh", "Suresh", "Dinesh", "Mahesh", "Ramesh",
        "Sachin", "Aakash", "Nitin", "Rahul", "Manoj", "Ashish", "Ravi", "Karan",
        "Gaurav", "Abhishek", "Tarun", "Nikhil", "Varun", "Mukesh", "Prakash", "Sunil",
        "Deepak", "Pankaj", "Ajay",
    ]

    last_names = [
        "Sharma", "Verma", "Patel", "Kumar", "Singh", "Gupta", "Reddy", "Nair",
        "Iyer", "Desai", "Joshi", "Mishra", "Tiwari", "Chauhan", "Kulkarni",
        "Bose", "Menon", "Pillai", "Rao", "Das", "Banerjee", "Mukherjee", "Chatterjee",
        "Sen", "Ghosh", "Malhotra", "Kapoor", "Khanna", "Sinha", "Pandey",
        "Saxena", "Bhat", "Naik", "Hegde", "Kamath", "Shetty", "Pai", "Fernandes",
        "D'Souza", "Dsouza", "Pereira", "Lobo", "Gomes", "Martins", "Almeida",
    ]

    # Generate 75 unique student emails
    student_users = []
    student_records = []

    for i in range(75):
        first = random.choice(first_names)
        last = random.choice(last_names)
        idx = i + 1
        email = f"student{idx:03d}@feedback.com"
        name = f"{first} {last}"

        user = User(
            name=name,
            email=email,
            password_hash=participant_password,
            role=UserRole.PARTICIPANT,
        )
        db.session.add(user)
        student_users.append(user)

    db.session.flush()

    for i, user in enumerate(student_users):
        course = random.choice(courses)
        student = Student(
            name=user.name,
            email=user.email,
            course_id=course.id,
        )
        db.session.add(student)
        student_records.append(student)

    db.session.flush()

    # ──────────────────────────────────────────────
    # 6. TRAINING PROGRAMS
    # ──────────────────────────────────────────────
    locations = [
        "Room 101, Block A", "Room 205, Block B", "Hall 3, Main Building",
        "Lab 4, CS Department", "Seminar Hall, Block C", "Room 302, Block D",
        "Auditorium, Main Campus", "Lab 7, IT Building", "Room 108, Block A",
        "Conference Room, Admin", "Room 405, Block E", "Lab 2, Engineering",
        "Room 210, Block B", "Hall 1, Convention Center", "Room 303, Block C",
    ]

    programs = []
    program_configs = [
        (courses[0], coordinators[0].id),   # CS101
        (courses[1], coordinators[0].id),   # CS201
        (courses[2], coordinators[0].id),   # CS301
        (courses[3], coordinators[1].id),   # CS401
        (courses[4], coordinators[1].id),   # CS501
        (courses[7], coordinators[2].id),   # AI101
        (courses[8], coordinators[2].id),   # AI201
        (courses[9], coordinators[2].id),   # AI301
        (courses[12], coordinators[3].id),  # WD101
        (courses[13], coordinators[3].id),  # WD201
        (courses[14], coordinators[4].id),  # WD301
        (courses[15], coordinators[4].id),  # WD401
        (courses[16], coordinators[5].id),  # CL101
        (courses[17], coordinators[5].id),  # CL201
        (courses[18], coordinators[5].id),  # CL301
        (courses[19], coordinators[1].id),  # CY101
        (courses[20], coordinators[2].id),  # DA101
        (courses[21], coordinators[3].id),  # DA201
        (courses[22], coordinators[4].id),  # PM101
        (courses[23], coordinators[5].id),  # PM201
    ]

    base_date = date(2025, 1, 6)

    for idx, (course, coord_id) in enumerate(program_configs):
        start = base_date + timedelta(weeks=idx * 3)
        end = start + timedelta(days=course.duration_days)
        location = random.choice(locations)
        capacity = random.choice([30, 40, 50, 60])

        # Vary statuses: some completed, some scheduled, some cancelled
        if idx < 5:
            status = ProgramStatus.COMPLETED
        elif idx == 19:
            status = ProgramStatus.CANCELLED
        else:
            status = ProgramStatus.SCHEDULED

        program = TrainingProgram(
            course_id=course.id,
            coordinator_id=coord_id,
            start_date=start,
            end_date=end,
            location=location,
            capacity=capacity,
            status=status,
        )
        db.session.add(program)
        programs.append(program)

    db.session.flush()

    # Assign 3-5 faculties to each program
    for p in programs:
        p.faculties = random.sample(faculties, random.randint(3, 5))
    db.session.flush()

    # ──────────────────────────────────────────────
    # 7. ENROLLMENTS
    # ──────────────────────────────────────────────
    enrollments = []
    enrolled_set = set()

    for student in student_records:
        # Enroll each student in 1-3 programs
        num_programs = random.randint(1, 3)
        chosen = random.sample(programs, min(num_programs, len(programs)))

        for program in chosen:
            key = (student.id, program.id)
            if key in enrolled_set:
                continue

            # Check capacity
            current_count = sum(1 for e in enrollments if e.program_id == program.id)
            if current_count >= program.capacity:
                continue

            enrolled_set.add(key)

            # For completed programs, set most as ATTENDED; for others REGISTERED
            if program.status == ProgramStatus.COMPLETED:
                att_status = random.choices(
                    [AttendanceStatus.ATTENDED, AttendanceStatus.NO_SHOW],
                    weights=[85, 15]
                )[0]
            elif program.status == ProgramStatus.CANCELLED:
                att_status = AttendanceStatus.REGISTERED
            else:
                att_status = AttendanceStatus.REGISTERED

            enrollment = Enrollment(
                student_id=student.id,
                program_id=program.id,
                attendance_status=att_status,
            )
            db.session.add(enrollment)
            enrollments.append(enrollment)

    db.session.flush()

    # ──────────────────────────────────────────────
    # 8. ATTENDANCE RECORDS (for ATTENDED enrollments)
    # ──────────────────────────────────────────────
    attended_enrollments = [
        e for e in enrollments
        if e.attendance_status == AttendanceStatus.ATTENDED
    ]

    for enrollment in attended_enrollments:
        program = enrollment.program
        if program.status != ProgramStatus.COMPLETED:
            continue

        num_days = random.randint(5, min(program.capacity, 15))
        program_start = program.start_date

        for d in range(num_days):
            att_date = program_start + timedelta(days=d * 2)
            if att_date > program.end_date:
                break
            # 85% chance present on each day
            present = random.random() < 0.85
            att = Attendance(
                enrollment_id=enrollment.id,
                attendance_date=att_date,
                present=present,
            )
            db.session.add(att)

    db.session.flush()

    # ──────────────────────────────────────────────
    # 9. FEEDBACK (for attended enrollments)
    # ──────────────────────────────────────────────
    feedback_comments = [
        "Excellent teaching, very clear explanations.",
        "Good course content, would recommend.",
        "The professor was knowledgeable and engaging.",
        "Learned a lot, practical examples were helpful.",
        "Course was well-structured and organized.",
        "Great hands-on projects and assignments.",
        "Could use more real-world case studies.",
        "Very informative and well-paced.",
        "The labs were extremely useful.",
        "Great depth of coverage on topics.",
        "Nice course, but pace could be faster.",
        "Professor explained complex topics simply.",
        "Would love an advanced follow-up course.",
        "Very interactive and participatory sessions.",
        "Assignments were challenging and meaningful.",
        "Good balance of theory and practice.",
        "The guest lectures added great value.",
        "Documentation and references provided were helpful.",
        "Well-organized syllabus and timely feedback.",
        "Room temperature was too cold sometimes.",
        "Could improve on time management in lectures.",
        "Overall a wonderful learning experience.",
        "The project work was the best part.",
        "Slightly rushed towards the end.",
        "Would appreciate more coding exercises.",
    ]

    for enrollment in attended_enrollments:
        program = enrollment.program
        # Only give feedback for completed programs
        if program.status != ProgramStatus.COMPLETED:
            continue

        for faculty in program.faculties:
            rating = random.randint(2, 5)
            comment = random.choice(feedback_comments)
            fb = Feedback(
                enrollment_id=enrollment.id,
                faculty_id=faculty.id,
                rating=rating,
                comments=comment,
            )
            db.session.add(fb)

    db.session.commit()

    # ──────────────────────────────────────────────
    # SUMMARY
    # ──────────────────────────────────────────────
    print("=" * 55)
    print("  SEED DATA CREATED SUCCESSFULLY!")
    print("=" * 55)
    print(f"  Skills:          {len(skills)}")
    print(f"  Users:           {User.query.count()}")
    print(f"    - Admin:       1   (admin@feedback.com / Admin123)")
    print(f"    - Coordinator: 6   (coordinator@feedback.com ... coordinator6@feedback.com / Coo123)")
    print(f"    - Participant: 51  (participant@feedback.com + participant01-50@feedback.com / Part123)")
    print(f"    - Students:    {len(student_users)}  (student001@feedback.com ... student075@feedback.com / Part123)")
    print(f"  Courses:         {len(courses)}")
    print(f"  Faculty:         {len(faculties)}")
    print(f"  Students:        {len(student_records)}")
    print(f"  Programs:        {len(programs)}")
    print(f"  Enrollments:     {len(enrollments)}")
    print(f"  Attendance:      {Attendance.query.count()}")
    print(f"  Feedbacks:       {Feedback.query.count()}")
    print("=" * 55)
    print("  PASSWORDS:")
    print("    Admin:       Admin123")
    print("    Coordinator: Coo123")
    print("    Participant: Part123")
    print("=" * 55)
