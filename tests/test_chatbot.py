# =============================================================================
# test_chatbot.py
# Project  : Optimization Strategies for Natural Language Interface
#            for EdTech Infrastructure
# Roll No  : PRJN26-127
# Purpose  : Unit tests for the matcher module using Python's built-in
#            unittest framework. Validates all 3 matching strategies.
# Run      : python -m pytest tests/test_chatbot.py -v
#         OR  python tests/test_chatbot.py
# =============================================================================

import sys
import os
import unittest

# Make sure the parent directory is in the path so we can import matcher
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from matcher import match_intent, is_farewell, normalize
from knowledge_base import RESPONSES


class TestNormalize(unittest.TestCase):
    """Tests for the normalize() helper function."""

    def test_lowercase(self):
        self.assertEqual(normalize("HELLO"), "hello")

    def test_strip_whitespace(self):
        self.assertEqual(normalize("  help  "), "help")

    def test_mixed_case_and_spaces(self):
        self.assertEqual(normalize("  Show Status "), "show status")

    def test_empty_string(self):
        self.assertEqual(normalize(""), "")


class TestExactMatch(unittest.TestCase):
    """Tests for Strategy 1: Exact keyword matching."""

    def test_hello(self):
        response = match_intent("hello")
        self.assertEqual(response, RESPONSES["greet"])

    def test_help(self):
        response = match_intent("help")
        self.assertEqual(response, RESPONSES["help"])

    def test_status(self):
        response = match_intent("status")
        self.assertEqual(response, RESPONSES["status"])

    def test_bye(self):
        response = match_intent("bye")
        self.assertEqual(response, RESPONSES["farewell"])

    def test_grades(self):
        response = match_intent("grades")
        self.assertEqual(response, RESPONSES["grades"])

    def test_quiz(self):
        response = match_intent("quiz")
        self.assertEqual(response, RESPONSES["quiz"])

    def test_enroll(self):
        response = match_intent("enroll")
        self.assertEqual(response, RESPONSES["course_enroll"])


class TestPhraseMatch(unittest.TestCase):
    """Tests for Strategy 2: Phrase/substring matching."""

    def test_show_status(self):
        response = match_intent("show status")
        self.assertEqual(response, RESPONSES["status"])

    def test_list_courses(self):
        response = match_intent("list courses")
        self.assertEqual(response, RESPONSES["course_list"])

    def test_assignment_status(self):
        response = match_intent("assignment status")
        self.assertEqual(response, RESPONSES["assignment_status"])

    def test_submit_assignment(self):
        response = match_intent("submit assignment")
        self.assertEqual(response, RESPONSES["assignment_submit"])

    def test_course_fee(self):
        response = match_intent("course fee")
        self.assertEqual(response, RESPONSES["course_fee"])

    def test_forgot_password(self):
        response = match_intent("forgot password")
        self.assertEqual(response, RESPONSES["account_login"])


class TestKeywordScan(unittest.TestCase):
    """Tests for Strategy 3: Individual word scan in a sentence."""

    def test_sentence_with_hello(self):
        response = match_intent("I want to say hello to you")
        self.assertEqual(response, RESPONSES["greet"])

    def test_sentence_with_help(self):
        response = match_intent("Can you please help me")
        self.assertEqual(response, RESPONSES["help"])

    def test_sentence_with_grades(self):
        response = match_intent("I want to check my grades")
        self.assertEqual(response, RESPONSES["grades"])

    def test_sentence_with_schedule(self):
        response = match_intent("What is the timetable for this week")
        self.assertEqual(response, RESPONSES["schedule"])

    def test_sentence_with_certificate(self):
        response = match_intent("How do I get a certificate")
        self.assertEqual(response, RESPONSES["course_certificate"])

    def test_sentence_with_faculty(self):
        response = match_intent("Who is the faculty for Python")
        self.assertEqual(response, RESPONSES["faculty"])


class TestCaseInsensitivity(unittest.TestCase):
    """Tests to ensure matching is case-insensitive."""

    def test_uppercase_hello(self):
        response = match_intent("HELLO")
        self.assertEqual(response, RESPONSES["greet"])

    def test_mixed_case_help(self):
        response = match_intent("HeLp")
        self.assertEqual(response, RESPONSES["help"])

    def test_upper_status(self):
        response = match_intent("SHOW STATUS")
        self.assertEqual(response, RESPONSES["status"])

    def test_upper_grades(self):
        response = match_intent("GRADES")
        self.assertEqual(response, RESPONSES["grades"])


class TestFallback(unittest.TestCase):
    """Tests for the fallback/unknown response."""

    def test_random_gibberish(self):
        response = match_intent("xyzabc123nonsense")
        self.assertEqual(response, RESPONSES["unknown"])

    def test_empty_like_input(self):
        response = match_intent("   ")
        self.assertEqual(response, RESPONSES["unknown"])

    def test_unrecognized_phrase(self):
        response = match_intent("what is the capital of France")
        self.assertEqual(response, RESPONSES["unknown"])


class TestIsFarewell(unittest.TestCase):
    """Tests for the is_farewell() function."""

    def test_bye(self):
        self.assertTrue(is_farewell("bye"))

    def test_exit(self):
        self.assertTrue(is_farewell("exit"))

    def test_quit(self):
        self.assertTrue(is_farewell("quit"))

    def test_goodbye(self):
        self.assertTrue(is_farewell("goodbye"))

    def test_see_you(self):
        self.assertTrue(is_farewell("see you"))

    def test_not_farewell(self):
        self.assertFalse(is_farewell("hello"))

    def test_not_farewell_help(self):
        self.assertFalse(is_farewell("help"))

    def test_uppercase_exit(self):
        self.assertTrue(is_farewell("EXIT"))



class TestNewKeywords(unittest.TestCase):
    """Tests for keywords added after initial release."""

    def test_assignments_plural(self):
        response = match_intent("assignments")
        self.assertEqual(response, RESPONSES["assignment_status"])

    def test_assignment_singular(self):
        response = match_intent("assignment")
        self.assertEqual(response, RESPONSES["assignment_status"])

    def test_courses_plural(self):
        response = match_intent("courses")
        self.assertEqual(response, RESPONSES["course_list"])

    def test_course_singular(self):
        response = match_intent("course")
        self.assertEqual(response, RESPONSES["course_list"])

    def test_marks(self):
        response = match_intent("marks")
        self.assertEqual(response, RESPONSES["grades"])

    def test_grade_singular(self):
        response = match_intent("grade")
        self.assertEqual(response, RESPONSES["grades"])

    def test_email(self):
        response = match_intent("email")
        self.assertEqual(response, RESPONSES["contact"])


if __name__ == "__main__":
    print("=" * 60)
    print("  EduBot Test Suite — PRJN26-127")
    print("=" * 60)
    unittest.main(verbosity=2)
