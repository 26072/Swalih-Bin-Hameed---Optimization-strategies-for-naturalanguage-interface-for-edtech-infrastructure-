# =============================================================================
# knowledge_base.py
# Project  : Optimization Strategies for Natural Language Interface
#            for EdTech Infrastructure
# Roll No  : PRJN26-127
# Purpose  : Contains all predefined responses for the EdTech CLI Chatbot.
# =============================================================================

# Separator constant — used in f-string responses to avoid
# the "=" * 45 implicit-concatenation repetition bug.
_S = "=" * 45

# ---------------------------------------------------------------------------
# KEYWORD GROUPS
# ---------------------------------------------------------------------------
KEYWORD_MAP = {
    "greet": [
        "hello", "hi", "hey", "good morning", "good afternoon",
        "good evening", "howdy", "greetings", "sup", "what's up"
    ],
    "farewell": [
        "bye", "goodbye", "exit", "quit", "see you", "later",
        "take care", "cya", "logout", "close"
    ],
    "help": [
        "help", "assist", "support", "what can you do", "commands",
        "options", "menu", "guide", "how to use", "features"
    ],
    "status": [
        "show status", "status", "system status", "platform status",
        "server status", "check status", "current status", "is it working"
    ],
    "about": [
        "about", "who are you", "what are you", "describe yourself",
        "your purpose", "what is this", "info"
    ],
    "course_list": [
        "list courses", "show courses", "available courses", "courses", "course",
        "all courses", "course catalog", "what courses", "courses offered",
        "browse courses", "view courses"
    ],
    "course_enroll": [
        "enroll", "join course", "register course", "sign up course",
        "how to enroll", "course registration", "add course",
        "i want to join", "subscribe course"
    ],
    "course_fee": [
        "course fee", "fees", "cost", "price", "how much",
        "payment", "charges", "tuition", "scholarship", "discount"
    ],
    "course_duration": [
        "duration", "how long", "course length",
        "time to complete", "course period"
    ],
    "course_certificate": [
        "certificate", "certification", "certified", "get certificate",
        "course completion", "diploma", "degree", "credential"
    ],
    "assignment_status": [
        "assignment status", "my assignment", "check assignment",
        "assignment due", "pending assignment", "show assignment",
        "assignments", "assignment", "homework", "task status", "project status"
    ],
    "assignment_submit": [
        "submit assignment", "how to submit", "upload assignment",
        "submission", "turn in", "hand in", "send assignment"
    ],
    "assignment_deadline": [
        "deadline", "due date", "last date",
        "when is assignment due", "submission date", "cutoff date"
    ],
    "grades": [
        "grades", "grade", "my grade", "marks", "mark", "score", "result",
        "performance", "report card", "transcript", "gpa",
        "show marks", "check grade"
    ],
    "progress": [
        "progress", "my progress", "course progress", "completion",
        "how much done", "percentage complete", "learning progress"
    ],
    "schedule": [
        "schedule", "timetable", "class timing", "lecture time",
        "when is class", "class schedule", "upcoming class",
        "today's class", "live session"
    ],
    "faculty": [
        "faculty", "instructor", "teacher", "professor", "mentor",
        "tutor", "who teaches", "contact instructor", "trainer"
    ],
    "account_login": [
        "login", "log in", "sign in", "can't login", "forgot password",
        "reset password", "account access", "username", "password"
    ],
    "account_profile": [
        "profile", "my profile", "update profile", "edit profile",
        "account details", "personal info", "change name", "change email"
    ],
    "tech_support": [
        "not working", "error", "bug", "issue", "problem", "glitch",
        "crash", "broken", "technical issue", "report bug", "help me fix"
    ],
    "contact": [
        "contact", "reach out", "phone", "call us", "email",
        "support email", "helpdesk", "customer care", "contact us"
    ],
    "resources": [
        "resources", "study material", "pdf", "notes", "video",
        "lecture notes", "download", "reading material", "ebook", "textbook"
    ],
    "quiz": [
        "quiz", "test", "exam", "mock test", "practice test",
        "assessment", "mcq", "online exam", "take test"
    ],
}

# ---------------------------------------------------------------------------
# RESPONSES — using f-strings with _S separator to avoid repetition bug
# ---------------------------------------------------------------------------
RESPONSES = {
    "greet": (
        "👋 Hello! Welcome to EduBot — your EdTech assistant!\n"
        "I can help you with courses, assignments, grades, schedules and more.\n"
        "Type 'help' to see all available commands."
    ),

    "farewell": (
        "👋 Goodbye! Keep learning and stay curious.\n"
        "Visit EduBot anytime. Happy learning! 🎓"
    ),

    "help": f"""📚 EDUBOT HELP MENU
{_S}
  Courses      -> list courses / enroll / fees / duration / certificate
  Assignments  -> assignment status / submit / deadline
  Grades       -> grades / progress
  Schedule     -> schedule / timetable
  Faculty      -> faculty / instructor
  Account      -> login / profile
  Support      -> tech support / contact
  Resources    -> resources / quiz
  General      -> status / about / help / exit
{_S}
Type any keyword from the above list to get a response!""",

    "status": f"""✅ PLATFORM STATUS — All Systems Operational
{_S}
  Learning Portal   : Online  [OK]
  Video Streaming   : Online  [OK]
  Assignment Portal : Online  [OK]
  Student Database  : Online  [OK]
  Live Sessions     : Online  [OK]
{_S}
Uptime: 99.97%""",

    "about": (
        "🤖 About EduBot\n"
        "EduBot is a CLI & Web chatbot for EdTech platforms.\n"
        "It uses Python and basic keyword/string matching.\n\n"
        "Project : Optimization Strategies for Natural Language Interface\n"
        "          for EdTech Infrastructure\n"
        "Roll No : PRJN26-127\n"
        "Tech    : Python, Basic String Matching"
    ),

    "course_list": f"""📋 AVAILABLE COURSES
{_S}
  1. Python Programming Fundamentals     [6 Weeks]
  2. Web Development (HTML/CSS/JS)       [8 Weeks]
  3. Data Science & Analytics            [10 Weeks]
  4. Machine Learning Basics             [12 Weeks]
  5. Cloud Computing & DevOps            [8 Weeks]
  6. Cybersecurity Essentials            [6 Weeks]
  7. Mobile App Development              [10 Weeks]
  8. Database Management (SQL/NoSQL)     [6 Weeks]
{_S}
Type 'enroll' to join any course.""",

    "course_enroll": (
        "📝 HOW TO ENROLL IN A COURSE\n"
        "  Step 1 -> Visit the Student Portal: https://edubot.example.com\n"
        "  Step 2 -> Log in with your student credentials.\n"
        "  Step 3 -> Navigate to 'Course Catalog'.\n"
        "  Step 4 -> Click 'Enroll' on your desired course.\n"
        "  Step 5 -> Complete payment (if applicable) and confirm.\n\n"
        "Enrollment is confirmed instantly via email.\n"
        "Need help? Type 'contact' to reach our support team."
    ),

    "course_fee": f"""💰 COURSE FEES STRUCTURE
{_S}
  Python Fundamentals     : Rs.2,999  (Free trial: 7 days)
  Web Development         : Rs.3,999
  Data Science            : Rs.5,999
  Machine Learning        : Rs.6,999
  Cloud & DevOps          : Rs.4,999
  Cybersecurity           : Rs.3,499
  Mobile Development      : Rs.4,499
  Database Management     : Rs.2,999
{_S}
Scholarships available for meritorious students.""",

    "course_duration": (
        "Duration ranges from 6 to 12 weeks.\n"
        "  Short courses  : 6 weeks  (2-3 hrs/week)\n"
        "  Medium courses : 8-10 weeks (4-5 hrs/week)\n"
        "  Long courses   : 12 weeks (6-8 hrs/week)\n\n"
        "Self-paced options are available for all courses."
    ),

    "course_certificate": (
        "🏆 COURSE CERTIFICATES\n"
        "  Certificate issued upon 100% course completion.\n"
        "  Certificates are digitally signed and verifiable online.\n"
        "  Download from 'My Achievements' section.\n"
        "  Can be shared directly to LinkedIn.\n\n"
        "Minimum passing score: 60% in all assessments."
    ),

    "assignment_status": f"""📌 YOUR ASSIGNMENT STATUS
{_S}
  [Python Module 3] : Submitted  (Graded: 85/100)
  [Web Dev Task 2]  : Pending    (Due: 2026-04-28)
  [DS Project 1]    : Not Started (Due: 2026-05-05)
{_S}
Type 'submit assignment' to learn how to submit.""",

    "assignment_submit": (
        "📤 HOW TO SUBMIT AN ASSIGNMENT\n"
        "  Step 1 -> Log in to the Student Portal.\n"
        "  Step 2 -> Go to 'My Courses' -> Select the course.\n"
        "  Step 3 -> Click on the assignment name.\n"
        "  Step 4 -> Upload your file (PDF, ZIP, or .py accepted).\n"
        "  Step 5 -> Click 'Submit' and note your submission ID.\n\n"
        "Late submissions may lose 10% marks per day."
    ),

    "assignment_deadline": (
        "📅 UPCOMING ASSIGNMENT DEADLINES\n"
        "  Web Dev Task 2   -> 2026-04-28  (5 days left)\n"
        "  DS Project 1     -> 2026-05-05  (12 days left)\n"
        "  ML Assignment 1  -> 2026-05-10  (17 days left)\n\n"
        "Set reminders in your profile to never miss a deadline!"
    ),

    "grades": f"""📊 YOUR GRADES
{_S}
  Python Fundamentals:
    Quiz 1     -> 90/100
    Quiz 2     -> 82/100
    Assignment -> 85/100
    Overall    -> 85.7%  (Grade: A)
  Web Development:
    Quiz 1     -> 78/100
    Assignment -> Pending
{_S}
Type 'progress' to see your overall course completion.""",

    "progress": (
        "📈 YOUR LEARNING PROGRESS\n"
        "  Python Fundamentals : [========  ]  80% Complete\n"
        "  Web Development     : [=====     ]  50% Complete\n"
        "  Data Science        : [==        ]  20% Complete\n\n"
        "Keep going! You are on track to earn 2 certificates this month."
    ),

    "schedule": f"""🗓️  UPCOMING CLASS SCHEDULE
{_S}
  Today (Wed, Apr 23):
    -> Python: Variables & Data Types  [4:00 PM - 5:30 PM]
  Tomorrow (Thu, Apr 24):
    -> Web Dev: CSS Flexbox            [5:00 PM - 6:30 PM]
  Fri, Apr 25:
    -> Data Science: Pandas Basics     [3:00 PM - 4:30 PM]
{_S}
Join via the portal: https://edubot.example.com/live""",

    "faculty": f"""👩‍🏫 FACULTY & INSTRUCTORS
{_S}
  Python & ML   : Dr. Priya Sharma   [priya@edubot.com]
  Web Dev       : Mr. Arjun Mehta   [arjun@edubot.com]
  Data Science  : Dr. Riya Patel    [riya@edubot.com]
  Cloud & DevOps: Mr. Sameer Gupta  [sameer@edubot.com]
  Cybersecurity : Ms. Nisha Rao     [nisha@edubot.com]
{_S}
Message instructors directly from the portal.""",

    "account_login": (
        "🔐 LOGIN HELP\n"
        "  Visit: https://edubot.example.com/login\n"
        "  Enter your registered email and password.\n\n"
        "Forgot Password?\n"
        "  -> Click 'Forgot Password' on the login page.\n"
        "  -> A reset link will be sent to your registered email.\n"
        "  -> Link expires in 30 minutes.\n\n"
        "Still having trouble? Type 'contact' for support."
    ),

    "account_profile": (
        "👤 PROFILE MANAGEMENT\n"
        "  Log in -> Click your avatar -> 'Edit Profile'\n"
        "  You can update: Name, Email, Phone, Profile Photo\n"
        "  Email changes require verification via OTP.\n\n"
        "Keep your profile updated for personalized recommendations!"
    ),

    "tech_support": (
        "🛠️  TECHNICAL SUPPORT\n"
        "  Common fixes:\n"
        "  Videos not loading  -> Clear browser cache / Try incognito\n"
        "  Login issues        -> Reset password or use OTP login\n"
        "  Assignment upload   -> Check file size (max 50MB) and format\n"
        "  Page not loading    -> Check your internet connection\n\n"
        "Email  : support@edubot.com\n"
        "Phone  : +91-9876543210 (Mon-Sat, 9AM-6PM)"
    ),

    "contact": f"""📞 CONTACT US
{_S}
  Email  : support@edubot.com
  Phone  : +91-9876543210
  Chat   : https://edubot.example.com/chat
  Hours  : Monday-Saturday, 9 AM - 6 PM IST
  Office : EduBot HQ, Bangalore, India
{_S}
Average response time: less than 2 hours on working days.""",

    "resources": f"""📚 STUDY RESOURCES
{_S}
  Lecture Notes  -> Portal -> My Courses -> Resources
  Video Lectures -> Streamed on the portal (HD quality)
  E-Books        -> Free for enrolled students
  Code Samples   -> GitHub: github.com/edubot-samples
  Cheat Sheets   -> Available in PDF format
{_S}
All resources accessible for 1 year after enrollment.""",

    "quiz": (
        "📝 QUIZZES & ASSESSMENTS\n"
        "  Log in -> My Courses -> Select Course -> 'Take Quiz'\n\n"
        "  Rules:\n"
        "  Each quiz: 10-20 MCQ questions\n"
        "  Time limit: 20-30 minutes\n"
        "  You get 2 attempts per quiz\n"
        "  Passing score: 60%\n"
        "  Results shown immediately after submission\n\n"
        "Good luck! Type 'grades' to check past scores."
    ),

    "unknown": (
        "I didn't quite understand that.\n"
        "Here are some things I can help you with:\n"
        "  -> Type 'help' for a full list of commands\n"
        "  -> Type 'list courses' to browse available courses\n"
        "  -> Type 'status' to check platform status\n"
        "  -> Type 'contact' to reach a human agent\n\n"
        "Tip: Use simple keywords like 'grades', 'schedule', 'enroll'!"
    ),
}
