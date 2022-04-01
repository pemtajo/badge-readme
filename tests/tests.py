#!/usr/bin/python3
# coding=UTF-8
import unittest, json
from unittest import TestCase
from unittest.mock import MagicMock, patch

from services.credly import Credly
from main import generate_new_readme

BASE_FOLDER="tests/"
FOLDER_MARKDOWNS=BASE_FOLDER+"markdowns/"
FOLDER_HTML=BASE_FOLDER+"html/"


def return_markdown(filename):
    with open(FOLDER_MARKDOWNS + filename, "r") as fh:
        return fh.read()


class Tests(TestCase):
    def test_canary(self):
        self.assertTrue(True)

class TestBadgeSize(TestCase):
    def setUp(self):
        self.maxDiff = None

        self.mocks = {}
        self.patches = []

        badge_size_patch = patch('services.credly.BADGE_SIZE', new='200')
        self.mocks['badge_size'] = badge_size_patch.start()
        self.patches.append(badge_size_patch)

    def tearDown(self):
        for patch_ in self.patches:
            patch_.stop()
    
    def test_happy_day(self):
        data = Credly(FOLDER_HTML+"happy_day.html").get_markdown()
        self.assertEqual(
            '[![Docker Essentials: A Developer Introduction](https://images.credly.com/size/200x200/images/08216781-93cb-4ba1-8110-8eb3401fa8ce/Docker_Essentials_-_ISDN.png)](http://www.credly.com/badges/24bcb006-58f8-494c-85e3-dfee10ea7b57 "Docker Essentials: A Developer Introduction")\n[![IBM Blockchain Essentials V2](https://images.credly.com/size/200x200/images/8e6bba9c-544d-46b0-bc7b-324fc85042ba/Blockchain_Essentials_V2.png)](http://www.credly.com/badges/47065bcc-63f9-4b1f-b403-48bcdbc78f54 "IBM Blockchain Essentials V2")\n[![Enterprise Design Thinking - Team Essentials for AI](https://images.credly.com/size/200x200/images/09f644d1-eed2-4279-bc49-1e26cddc9d3d/Team_Essentials.png)](http://www.credly.com/badges/5e280a76-446b-431a-80f0-7d2dc448a407 "Enterprise Design Thinking - Team Essentials for AI")\n[![Security and Privacy by Design Foundations](https://images.credly.com/size/200x200/images/c1ca6570-bdc6-40e9-8992-722050788418/Security-_-Privacy-by-Design-Foundational.png)](http://www.credly.com/badges/e4d08b6b-ee34-4fc9-9a1b-87c43a887233 "Security and Privacy by Design Foundations")\n[![IBM Blockchain Consulting](https://images.credly.com/size/200x200/images/28e2c951-1859-4812-807f-3b637e6403e5/Blockchain-consulting.png)](http://www.credly.com/badges/42efe367-3744-438a-8c03-59622c69c893 "IBM Blockchain Consulting")\n[![Watson Discovery Service Foundations](https://images.credly.com/size/200x200/images/edeaee50-64ff-42f0-a872-f4e2119ed463/Watson_Discovery_Service_-_Foundations.png)](http://www.credly.com/badges/06796b84-6cb6-40ea-9853-b4b8843e65da "Watson Discovery Service Foundations")\n[![Watson Discovery Foundations](https://images.credly.com/size/200x200/images/8c805fb7-b7e1-4b45-b933-7ee09385ea03/Watson_Academy_-_Discovery__-_Foundations.png)](http://www.credly.com/badges/b4f04f7d-a5dd-45bd-bfd1-1a0d29801bf8 "Watson Discovery Foundations")\n[![IBM Cloud Garage Test-Driven Development (TDD)](https://images.credly.com/size/200x200/images/71ea5682-2233-434c-a2c5-dd3f7fb8d5e9/Garage_Method_-_Test_driven_Development_V1_-__Final.png)](http://www.credly.com/badges/d9c9d869-b2e3-4cd2-a77d-7d53197b821e "IBM Cloud Garage Test-Driven Development (TDD)")\n[![Watson Discovery Service for Developers](https://images.credly.com/size/200x200/images/01774ad1-fbff-4ddc-8b28-fd7953cb7ff6/Watson_Discovery_Service_-_Developers.png)](http://www.credly.com/badges/0506d841-cd61-4c0e-aad9-83714a9920a9 "Watson Discovery Service for Developers")',
            data,
        )

class TestNumberLastBadges(TestCase):
    def setUp(self):
        self.maxDiff = None

        self.mocks = {}
        self.patches = []

        badge_size_patch = patch('services.credly.NUMBER_LAST_BADGES', new=1)
        self.mocks['badge_size'] = badge_size_patch.start()
        self.patches.append(badge_size_patch)

    def tearDown(self):
        for patch_ in self.patches:
            patch_.stop()
    
    def test_happy_day(self):
        data = Credly(FOLDER_HTML+"happy_day.html").get_markdown()
        self.assertEqual(
            '[![Docker Essentials: A Developer Introduction](https://images.credly.com/size/110x110/images/08216781-93cb-4ba1-8110-8eb3401fa8ce/Docker_Essentials_-_ISDN.png)](http://www.credly.com/badges/24bcb006-58f8-494c-85e3-dfee10ea7b57 "Docker Essentials: A Developer Introduction")',
            data,
        )
class TestsCredly(TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_happy_day(self):
        data = Credly(FOLDER_HTML+"happy_day.html").get_markdown()
        self.assertEqual(
            '[![Docker Essentials: A Developer Introduction](https://images.credly.com/size/110x110/images/08216781-93cb-4ba1-8110-8eb3401fa8ce/Docker_Essentials_-_ISDN.png)](http://www.credly.com/badges/24bcb006-58f8-494c-85e3-dfee10ea7b57 "Docker Essentials: A Developer Introduction")\n[![IBM Blockchain Essentials V2](https://images.credly.com/size/110x110/images/8e6bba9c-544d-46b0-bc7b-324fc85042ba/Blockchain_Essentials_V2.png)](http://www.credly.com/badges/47065bcc-63f9-4b1f-b403-48bcdbc78f54 "IBM Blockchain Essentials V2")\n[![Enterprise Design Thinking - Team Essentials for AI](https://images.credly.com/size/110x110/images/09f644d1-eed2-4279-bc49-1e26cddc9d3d/Team_Essentials.png)](http://www.credly.com/badges/5e280a76-446b-431a-80f0-7d2dc448a407 "Enterprise Design Thinking - Team Essentials for AI")\n[![Security and Privacy by Design Foundations](https://images.credly.com/size/110x110/images/c1ca6570-bdc6-40e9-8992-722050788418/Security-_-Privacy-by-Design-Foundational.png)](http://www.credly.com/badges/e4d08b6b-ee34-4fc9-9a1b-87c43a887233 "Security and Privacy by Design Foundations")\n[![IBM Blockchain Consulting](https://images.credly.com/size/110x110/images/28e2c951-1859-4812-807f-3b637e6403e5/Blockchain-consulting.png)](http://www.credly.com/badges/42efe367-3744-438a-8c03-59622c69c893 "IBM Blockchain Consulting")\n[![Watson Discovery Service Foundations](https://images.credly.com/size/110x110/images/edeaee50-64ff-42f0-a872-f4e2119ed463/Watson_Discovery_Service_-_Foundations.png)](http://www.credly.com/badges/06796b84-6cb6-40ea-9853-b4b8843e65da "Watson Discovery Service Foundations")\n[![Watson Discovery Foundations](https://images.credly.com/size/110x110/images/8c805fb7-b7e1-4b45-b933-7ee09385ea03/Watson_Academy_-_Discovery__-_Foundations.png)](http://www.credly.com/badges/b4f04f7d-a5dd-45bd-bfd1-1a0d29801bf8 "Watson Discovery Foundations")\n[![IBM Cloud Garage Test-Driven Development (TDD)](https://images.credly.com/size/110x110/images/71ea5682-2233-434c-a2c5-dd3f7fb8d5e9/Garage_Method_-_Test_driven_Development_V1_-__Final.png)](http://www.credly.com/badges/d9c9d869-b2e3-4cd2-a77d-7d53197b821e "IBM Cloud Garage Test-Driven Development (TDD)")\n[![Watson Discovery Service for Developers](https://images.credly.com/size/110x110/images/01774ad1-fbff-4ddc-8b28-fd7953cb7ff6/Watson_Discovery_Service_-_Developers.png)](http://www.credly.com/badges/0506d841-cd61-4c0e-aad9-83714a9920a9 "Watson Discovery Service for Developers")',
            data,
        )

class testsHappyDayHTML(TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_not_tag(self):
        no_tags = return_markdown("no_tags.md")
        self.assertEqual("# badge-readme\nThis is example file", no_tags)

        badges = Credly(FOLDER_HTML+"happy_day.html").get_markdown()
        new_readme = generate_new_readme(badges, no_tags)
        self.assertEqual("# badge-readme\nThis is example file", new_readme)

        self.assertEqual(no_tags, new_readme)

    def test_with_tags_no_text_between(self):
        with_tags_no_text_between = return_markdown("with_tags_no_text_between.md")
        self.assertEqual(
            "# badge-readme\nThis is example file\n<!--START_SECTION:badges-->\n<!--END_SECTION:badges-->",
            with_tags_no_text_between,
        )

        badges = Credly(FOLDER_HTML+"happy_day.html").get_markdown()
        new_readme = generate_new_readme(badges, with_tags_no_text_between)
        self.assertEqual(
            '# badge-readme\nThis is example file\n<!--START_SECTION:badges-->\n[![Docker Essentials: A Developer Introduction](https://images.credly.com/size/110x110/images/08216781-93cb-4ba1-8110-8eb3401fa8ce/Docker_Essentials_-_ISDN.png)](http://www.credly.com/badges/24bcb006-58f8-494c-85e3-dfee10ea7b57 "Docker Essentials: A Developer Introduction")\n[![IBM Blockchain Essentials V2](https://images.credly.com/size/110x110/images/8e6bba9c-544d-46b0-bc7b-324fc85042ba/Blockchain_Essentials_V2.png)](http://www.credly.com/badges/47065bcc-63f9-4b1f-b403-48bcdbc78f54 "IBM Blockchain Essentials V2")\n[![Enterprise Design Thinking - Team Essentials for AI](https://images.credly.com/size/110x110/images/09f644d1-eed2-4279-bc49-1e26cddc9d3d/Team_Essentials.png)](http://www.credly.com/badges/5e280a76-446b-431a-80f0-7d2dc448a407 "Enterprise Design Thinking - Team Essentials for AI")\n[![Security and Privacy by Design Foundations](https://images.credly.com/size/110x110/images/c1ca6570-bdc6-40e9-8992-722050788418/Security-_-Privacy-by-Design-Foundational.png)](http://www.credly.com/badges/e4d08b6b-ee34-4fc9-9a1b-87c43a887233 "Security and Privacy by Design Foundations")\n[![IBM Blockchain Consulting](https://images.credly.com/size/110x110/images/28e2c951-1859-4812-807f-3b637e6403e5/Blockchain-consulting.png)](http://www.credly.com/badges/42efe367-3744-438a-8c03-59622c69c893 "IBM Blockchain Consulting")\n[![Watson Discovery Service Foundations](https://images.credly.com/size/110x110/images/edeaee50-64ff-42f0-a872-f4e2119ed463/Watson_Discovery_Service_-_Foundations.png)](http://www.credly.com/badges/06796b84-6cb6-40ea-9853-b4b8843e65da "Watson Discovery Service Foundations")\n[![Watson Discovery Foundations](https://images.credly.com/size/110x110/images/8c805fb7-b7e1-4b45-b933-7ee09385ea03/Watson_Academy_-_Discovery__-_Foundations.png)](http://www.credly.com/badges/b4f04f7d-a5dd-45bd-bfd1-1a0d29801bf8 "Watson Discovery Foundations")\n[![IBM Cloud Garage Test-Driven Development (TDD)](https://images.credly.com/size/110x110/images/71ea5682-2233-434c-a2c5-dd3f7fb8d5e9/Garage_Method_-_Test_driven_Development_V1_-__Final.png)](http://www.credly.com/badges/d9c9d869-b2e3-4cd2-a77d-7d53197b821e "IBM Cloud Garage Test-Driven Development (TDD)")\n[![Watson Discovery Service for Developers](https://images.credly.com/size/110x110/images/01774ad1-fbff-4ddc-8b28-fd7953cb7ff6/Watson_Discovery_Service_-_Developers.png)](http://www.credly.com/badges/0506d841-cd61-4c0e-aad9-83714a9920a9 "Watson Discovery Service for Developers")\n<!--END_SECTION:badges-->',
            new_readme,
        )

        self.assertNotEqual(with_tags_no_text_between, new_readme)

    def test_with_tags_text_between(self):
        with_tags_text_between = return_markdown("with_tags_text_between.md")
        self.assertEqual(
            '# badge-readme\nThis is example file\n<!--START_SECTION:badges-->\n<p align="left"><a href="http://www.credly.com/badges/d9c9d869-b2e3-4cd2-a77d-7d53197b821e" title="IBM Cloud Garage Test-Driven Development (TDD)"><img src="https://images.credly.com/size/110x110/images/71ea5682-2233-434c-a2c5-dd3f7fb8d5e9/Garage_Method_-_Test_driven_Development_V1_-__Final.png" alt="IBM Cloud Garage Test-Driven Development (TDD)"></img></a><a href="http://www.credly.com/badges/e3408ee5-bb9a-4e84-a7c2-5d3aa83b16ef" title="People Skills - Communication, Presentation, Collaboration, and Problem Solving"><img src="https://images.credly.com/size/110x110/images/973b6bc2-5b3a-4ff2-b40e-1a46fe1b3a56/People-Skills-Communications.png" alt="People Skills - Communication, Presentation, Collaboration, and Problem Solving"></img></a><a href="http://www.credly.com/badges/0506d841-cd61-4c0e-aad9-83714a9920a9" title="Watson Discovery Service for Developers"><img src="https://images.credly.com/size/110x110/images/01774ad1-fbff-4ddc-8b28-fd7953cb7ff6/Watson_Discovery_Service_-_Developers.png" alt="Watson Discovery Service for Developers"></img></a><a href="http://www.credly.com/badges/06796b84-6cb6-40ea-9853-b4b8843e65da" title="Watson Discovery Service Foundations"><img src="https://images.credly.com/size/110x110/images/edeaee50-64ff-42f0-a872-f4e2119ed463/Watson_Discovery_Service_-_Foundations.png" alt="Watson Discovery Service Foundations"></img></a><a href="http://www.credly.com/badges/e4d08b6b-ee34-4fc9-9a1b-87c43a887233" title="Security and Privacy by Design Foundations"><img src="https://images.credly.com/size/110x110/images/c1ca6570-bdc6-40e9-8992-722050788418/Security-_-Privacy-by-Design-Foundational.png" alt="Security and Privacy by Design Foundations"></img></a><a href="http://www.credly.com/badges/42efe367-3744-438a-8c03-59622c69c893" title="IBM Blockchain Consulting"><img src="https://images.credly.com/size/110x110/images/28e2c951-1859-4812-807f-3b637e6403e5/Blockchain-consulting.png" alt="IBM Blockchain Consulting"></img></a><a href="http://www.credly.com/badges/47065bcc-63f9-4b1f-b403-48bcdbc78f54" title="IBM Blockchain Essentials V2"><img src="https://images.credly.com/size/110x110/images/8e6bba9c-544d-46b0-bc7b-324fc85042ba/Blockchain_Essentials_V2.png" alt="IBM Blockchain Essentials V2"></img></a><a href="http://www.credly.com/badges/24bcb006-58f8-494c-85e3-dfee10ea7b57" title="Docker Essentials: A Developer Introduction"><img src="https://images.credly.com/size/110x110/images/08216781-93cb-4ba1-8110-8eb3401fa8ce/Docker_Essentials_-_ISDN.png" alt="Docker Essentials: A Developer Introduction"></img></a><a href="http://www.credly.com/badges/b4f04f7d-a5dd-45bd-bfd1-1a0d29801bf8" title="Watson Discovery Foundations"><img src="https://images.credly.com/size/110x110/images/8c805fb7-b7e1-4b45-b933-7ee09385ea03/Watson_Academy_-_Discovery__-_Foundations.png" alt="Watson Discovery Foundations"></img></a><a href="http://www.credly.com/badges/5e280a76-446b-431a-80f0-7d2dc448a407" title="Enterprise Design Thinking - Team Essentials for AI"><img src="https://images.credly.com/size/110x110/images/09f644d1-eed2-4279-bc49-1e26cddc9d3d/Team_Essentials.png" alt="Enterprise Design Thinking - Team Essentials for AI"></img></a><a href="http://www.credly.com/badges/6267a487-d693-44e6-acb2-d9e17df66e14" title="Enterprise Design Thinking Practitioner"><img src="https://images.credly.com/size/110x110/images/bc08972c-3c7d-4b99-82a0-c94bcca36674/Badges_v8-07_Practitioner.png" alt="Enterprise Design Thinking Practitioner"></img></a></p>\n<!--END_SECTION:badges-->',
            with_tags_text_between,
        )

        badges = Credly(FOLDER_HTML+"happy_day.html").get_markdown()
        new_readme = generate_new_readme(badges, with_tags_text_between)
        self.assertEqual(
            '# badge-readme\nThis is example file\n<!--START_SECTION:badges-->\n[![Docker Essentials: A Developer Introduction](https://images.credly.com/size/110x110/images/08216781-93cb-4ba1-8110-8eb3401fa8ce/Docker_Essentials_-_ISDN.png)](http://www.credly.com/badges/24bcb006-58f8-494c-85e3-dfee10ea7b57 "Docker Essentials: A Developer Introduction")\n[![IBM Blockchain Essentials V2](https://images.credly.com/size/110x110/images/8e6bba9c-544d-46b0-bc7b-324fc85042ba/Blockchain_Essentials_V2.png)](http://www.credly.com/badges/47065bcc-63f9-4b1f-b403-48bcdbc78f54 "IBM Blockchain Essentials V2")\n[![Enterprise Design Thinking - Team Essentials for AI](https://images.credly.com/size/110x110/images/09f644d1-eed2-4279-bc49-1e26cddc9d3d/Team_Essentials.png)](http://www.credly.com/badges/5e280a76-446b-431a-80f0-7d2dc448a407 "Enterprise Design Thinking - Team Essentials for AI")\n[![Security and Privacy by Design Foundations](https://images.credly.com/size/110x110/images/c1ca6570-bdc6-40e9-8992-722050788418/Security-_-Privacy-by-Design-Foundational.png)](http://www.credly.com/badges/e4d08b6b-ee34-4fc9-9a1b-87c43a887233 "Security and Privacy by Design Foundations")\n[![IBM Blockchain Consulting](https://images.credly.com/size/110x110/images/28e2c951-1859-4812-807f-3b637e6403e5/Blockchain-consulting.png)](http://www.credly.com/badges/42efe367-3744-438a-8c03-59622c69c893 "IBM Blockchain Consulting")\n[![Watson Discovery Service Foundations](https://images.credly.com/size/110x110/images/edeaee50-64ff-42f0-a872-f4e2119ed463/Watson_Discovery_Service_-_Foundations.png)](http://www.credly.com/badges/06796b84-6cb6-40ea-9853-b4b8843e65da "Watson Discovery Service Foundations")\n[![Watson Discovery Foundations](https://images.credly.com/size/110x110/images/8c805fb7-b7e1-4b45-b933-7ee09385ea03/Watson_Academy_-_Discovery__-_Foundations.png)](http://www.credly.com/badges/b4f04f7d-a5dd-45bd-bfd1-1a0d29801bf8 "Watson Discovery Foundations")\n[![IBM Cloud Garage Test-Driven Development (TDD)](https://images.credly.com/size/110x110/images/71ea5682-2233-434c-a2c5-dd3f7fb8d5e9/Garage_Method_-_Test_driven_Development_V1_-__Final.png)](http://www.credly.com/badges/d9c9d869-b2e3-4cd2-a77d-7d53197b821e "IBM Cloud Garage Test-Driven Development (TDD)")\n[![Watson Discovery Service for Developers](https://images.credly.com/size/110x110/images/01774ad1-fbff-4ddc-8b28-fd7953cb7ff6/Watson_Discovery_Service_-_Developers.png)](http://www.credly.com/badges/0506d841-cd61-4c0e-aad9-83714a9920a9 "Watson Discovery Service for Developers")\n<!--END_SECTION:badges-->',
            new_readme,
        )

        self.assertNotEqual(with_tags_text_between, new_readme)

class testNotTagsHTML(TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_not_tag(self):
        no_tags = return_markdown("no_tags.md")
        self.assertEqual("# badge-readme\nThis is example file", no_tags)

        badges = Credly(FOLDER_HTML+"no_badges.html").get_markdown()
        new_readme = generate_new_readme(badges, no_tags)
        self.assertEqual("# badge-readme\nThis is example file", new_readme)

        self.assertEqual(no_tags, new_readme)

    def test_with_tags_no_text_between(self):
        with_tags_no_text_between = return_markdown("with_tags_no_text_between.md")
        self.assertEqual(
            "# badge-readme\nThis is example file\n<!--START_SECTION:badges-->\n<!--END_SECTION:badges-->",
            with_tags_no_text_between,
        )

        badges = Credly(FOLDER_HTML+"no_badges.html").get_markdown()
        new_readme = generate_new_readme(badges, with_tags_no_text_between)
        self.assertEqual(
            "# badge-readme\nThis is example file\n<!--START_SECTION:badges-->\n<!--END_SECTION:badges-->",
            new_readme,
        )

        self.assertEqual(with_tags_no_text_between, new_readme)

    def test_with_tags_text_between(self):
        with_tags_text_between = return_markdown("with_tags_text_between.md")
        self.assertEqual(
            '# badge-readme\nThis is example file\n<!--START_SECTION:badges-->\n<p align="left"><a href="http://www.credly.com/badges/d9c9d869-b2e3-4cd2-a77d-7d53197b821e" title="IBM Cloud Garage Test-Driven Development (TDD)"><img src="https://images.credly.com/size/110x110/images/71ea5682-2233-434c-a2c5-dd3f7fb8d5e9/Garage_Method_-_Test_driven_Development_V1_-__Final.png" alt="IBM Cloud Garage Test-Driven Development (TDD)"></img></a><a href="http://www.credly.com/badges/e3408ee5-bb9a-4e84-a7c2-5d3aa83b16ef" title="People Skills - Communication, Presentation, Collaboration, and Problem Solving"><img src="https://images.credly.com/size/110x110/images/973b6bc2-5b3a-4ff2-b40e-1a46fe1b3a56/People-Skills-Communications.png" alt="People Skills - Communication, Presentation, Collaboration, and Problem Solving"></img></a><a href="http://www.credly.com/badges/0506d841-cd61-4c0e-aad9-83714a9920a9" title="Watson Discovery Service for Developers"><img src="https://images.credly.com/size/110x110/images/01774ad1-fbff-4ddc-8b28-fd7953cb7ff6/Watson_Discovery_Service_-_Developers.png" alt="Watson Discovery Service for Developers"></img></a><a href="http://www.credly.com/badges/06796b84-6cb6-40ea-9853-b4b8843e65da" title="Watson Discovery Service Foundations"><img src="https://images.credly.com/size/110x110/images/edeaee50-64ff-42f0-a872-f4e2119ed463/Watson_Discovery_Service_-_Foundations.png" alt="Watson Discovery Service Foundations"></img></a><a href="http://www.credly.com/badges/e4d08b6b-ee34-4fc9-9a1b-87c43a887233" title="Security and Privacy by Design Foundations"><img src="https://images.credly.com/size/110x110/images/c1ca6570-bdc6-40e9-8992-722050788418/Security-_-Privacy-by-Design-Foundational.png" alt="Security and Privacy by Design Foundations"></img></a><a href="http://www.credly.com/badges/42efe367-3744-438a-8c03-59622c69c893" title="IBM Blockchain Consulting"><img src="https://images.credly.com/size/110x110/images/28e2c951-1859-4812-807f-3b637e6403e5/Blockchain-consulting.png" alt="IBM Blockchain Consulting"></img></a><a href="http://www.credly.com/badges/47065bcc-63f9-4b1f-b403-48bcdbc78f54" title="IBM Blockchain Essentials V2"><img src="https://images.credly.com/size/110x110/images/8e6bba9c-544d-46b0-bc7b-324fc85042ba/Blockchain_Essentials_V2.png" alt="IBM Blockchain Essentials V2"></img></a><a href="http://www.credly.com/badges/24bcb006-58f8-494c-85e3-dfee10ea7b57" title="Docker Essentials: A Developer Introduction"><img src="https://images.credly.com/size/110x110/images/08216781-93cb-4ba1-8110-8eb3401fa8ce/Docker_Essentials_-_ISDN.png" alt="Docker Essentials: A Developer Introduction"></img></a><a href="http://www.credly.com/badges/b4f04f7d-a5dd-45bd-bfd1-1a0d29801bf8" title="Watson Discovery Foundations"><img src="https://images.credly.com/size/110x110/images/8c805fb7-b7e1-4b45-b933-7ee09385ea03/Watson_Academy_-_Discovery__-_Foundations.png" alt="Watson Discovery Foundations"></img></a><a href="http://www.credly.com/badges/5e280a76-446b-431a-80f0-7d2dc448a407" title="Enterprise Design Thinking - Team Essentials for AI"><img src="https://images.credly.com/size/110x110/images/09f644d1-eed2-4279-bc49-1e26cddc9d3d/Team_Essentials.png" alt="Enterprise Design Thinking - Team Essentials for AI"></img></a><a href="http://www.credly.com/badges/6267a487-d693-44e6-acb2-d9e17df66e14" title="Enterprise Design Thinking Practitioner"><img src="https://images.credly.com/size/110x110/images/bc08972c-3c7d-4b99-82a0-c94bcca36674/Badges_v8-07_Practitioner.png" alt="Enterprise Design Thinking Practitioner"></img></a></p>\n<!--END_SECTION:badges-->',
            with_tags_text_between,
        )

        badges = Credly(FOLDER_HTML+"no_badges.html").get_markdown()
        new_readme = generate_new_readme(badges, with_tags_text_between)
        self.assertEqual(
            '# badge-readme\nThis is example file\n<!--START_SECTION:badges-->\n<p align="left"><a href="http://www.credly.com/badges/d9c9d869-b2e3-4cd2-a77d-7d53197b821e" title="IBM Cloud Garage Test-Driven Development (TDD)"><img src="https://images.credly.com/size/110x110/images/71ea5682-2233-434c-a2c5-dd3f7fb8d5e9/Garage_Method_-_Test_driven_Development_V1_-__Final.png" alt="IBM Cloud Garage Test-Driven Development (TDD)"></img></a><a href="http://www.credly.com/badges/e3408ee5-bb9a-4e84-a7c2-5d3aa83b16ef" title="People Skills - Communication, Presentation, Collaboration, and Problem Solving"><img src="https://images.credly.com/size/110x110/images/973b6bc2-5b3a-4ff2-b40e-1a46fe1b3a56/People-Skills-Communications.png" alt="People Skills - Communication, Presentation, Collaboration, and Problem Solving"></img></a><a href="http://www.credly.com/badges/0506d841-cd61-4c0e-aad9-83714a9920a9" title="Watson Discovery Service for Developers"><img src="https://images.credly.com/size/110x110/images/01774ad1-fbff-4ddc-8b28-fd7953cb7ff6/Watson_Discovery_Service_-_Developers.png" alt="Watson Discovery Service for Developers"></img></a><a href="http://www.credly.com/badges/06796b84-6cb6-40ea-9853-b4b8843e65da" title="Watson Discovery Service Foundations"><img src="https://images.credly.com/size/110x110/images/edeaee50-64ff-42f0-a872-f4e2119ed463/Watson_Discovery_Service_-_Foundations.png" alt="Watson Discovery Service Foundations"></img></a><a href="http://www.credly.com/badges/e4d08b6b-ee34-4fc9-9a1b-87c43a887233" title="Security and Privacy by Design Foundations"><img src="https://images.credly.com/size/110x110/images/c1ca6570-bdc6-40e9-8992-722050788418/Security-_-Privacy-by-Design-Foundational.png" alt="Security and Privacy by Design Foundations"></img></a><a href="http://www.credly.com/badges/42efe367-3744-438a-8c03-59622c69c893" title="IBM Blockchain Consulting"><img src="https://images.credly.com/size/110x110/images/28e2c951-1859-4812-807f-3b637e6403e5/Blockchain-consulting.png" alt="IBM Blockchain Consulting"></img></a><a href="http://www.credly.com/badges/47065bcc-63f9-4b1f-b403-48bcdbc78f54" title="IBM Blockchain Essentials V2"><img src="https://images.credly.com/size/110x110/images/8e6bba9c-544d-46b0-bc7b-324fc85042ba/Blockchain_Essentials_V2.png" alt="IBM Blockchain Essentials V2"></img></a><a href="http://www.credly.com/badges/24bcb006-58f8-494c-85e3-dfee10ea7b57" title="Docker Essentials: A Developer Introduction"><img src="https://images.credly.com/size/110x110/images/08216781-93cb-4ba1-8110-8eb3401fa8ce/Docker_Essentials_-_ISDN.png" alt="Docker Essentials: A Developer Introduction"></img></a><a href="http://www.credly.com/badges/b4f04f7d-a5dd-45bd-bfd1-1a0d29801bf8" title="Watson Discovery Foundations"><img src="https://images.credly.com/size/110x110/images/8c805fb7-b7e1-4b45-b933-7ee09385ea03/Watson_Academy_-_Discovery__-_Foundations.png" alt="Watson Discovery Foundations"></img></a><a href="http://www.credly.com/badges/5e280a76-446b-431a-80f0-7d2dc448a407" title="Enterprise Design Thinking - Team Essentials for AI"><img src="https://images.credly.com/size/110x110/images/09f644d1-eed2-4279-bc49-1e26cddc9d3d/Team_Essentials.png" alt="Enterprise Design Thinking - Team Essentials for AI"></img></a><a href="http://www.credly.com/badges/6267a487-d693-44e6-acb2-d9e17df66e14" title="Enterprise Design Thinking Practitioner"><img src="https://images.credly.com/size/110x110/images/bc08972c-3c7d-4b99-82a0-c94bcca36674/Badges_v8-07_Practitioner.png" alt="Enterprise Design Thinking Practitioner"></img></a></p>\n<!--END_SECTION:badges-->',
            new_readme,
        )

        self.assertEqual(with_tags_text_between, new_readme)

class testNoChangesHTML(TestCase):
    def setUp(self):
        self.maxDiff = None

    def test_not_changes(self):
        no_changes = return_markdown("no_changes_happy_day.md")
        self.assertEqual(
            '# badge-readme\nThis is example file\n<!--START_SECTION:badges-->\n[![Docker Essentials: A Developer Introduction](https://images.credly.com/size/110x110/images/08216781-93cb-4ba1-8110-8eb3401fa8ce/Docker_Essentials_-_ISDN.png)](http://www.credly.com/badges/24bcb006-58f8-494c-85e3-dfee10ea7b57 "Docker Essentials: A Developer Introduction")\n[![IBM Blockchain Essentials V2](https://images.credly.com/size/110x110/images/8e6bba9c-544d-46b0-bc7b-324fc85042ba/Blockchain_Essentials_V2.png)](http://www.credly.com/badges/47065bcc-63f9-4b1f-b403-48bcdbc78f54 "IBM Blockchain Essentials V2")\n[![Enterprise Design Thinking - Team Essentials for AI](https://images.credly.com/size/110x110/images/09f644d1-eed2-4279-bc49-1e26cddc9d3d/Team_Essentials.png)](http://www.credly.com/badges/5e280a76-446b-431a-80f0-7d2dc448a407 "Enterprise Design Thinking - Team Essentials for AI")\n[![Security and Privacy by Design Foundations](https://images.credly.com/size/110x110/images/c1ca6570-bdc6-40e9-8992-722050788418/Security-_-Privacy-by-Design-Foundational.png)](http://www.credly.com/badges/e4d08b6b-ee34-4fc9-9a1b-87c43a887233 "Security and Privacy by Design Foundations")\n[![IBM Blockchain Consulting](https://images.credly.com/size/110x110/images/28e2c951-1859-4812-807f-3b637e6403e5/Blockchain-consulting.png)](http://www.credly.com/badges/42efe367-3744-438a-8c03-59622c69c893 "IBM Blockchain Consulting")\n[![Watson Discovery Service Foundations](https://images.credly.com/size/110x110/images/edeaee50-64ff-42f0-a872-f4e2119ed463/Watson_Discovery_Service_-_Foundations.png)](http://www.credly.com/badges/06796b84-6cb6-40ea-9853-b4b8843e65da "Watson Discovery Service Foundations")\n[![Watson Discovery Foundations](https://images.credly.com/size/110x110/images/8c805fb7-b7e1-4b45-b933-7ee09385ea03/Watson_Academy_-_Discovery__-_Foundations.png)](http://www.credly.com/badges/b4f04f7d-a5dd-45bd-bfd1-1a0d29801bf8 "Watson Discovery Foundations")\n[![IBM Cloud Garage Test-Driven Development (TDD)](https://images.credly.com/size/110x110/images/71ea5682-2233-434c-a2c5-dd3f7fb8d5e9/Garage_Method_-_Test_driven_Development_V1_-__Final.png)](http://www.credly.com/badges/d9c9d869-b2e3-4cd2-a77d-7d53197b821e "IBM Cloud Garage Test-Driven Development (TDD)")\n[![Watson Discovery Service for Developers](https://images.credly.com/size/110x110/images/01774ad1-fbff-4ddc-8b28-fd7953cb7ff6/Watson_Discovery_Service_-_Developers.png)](http://www.credly.com/badges/0506d841-cd61-4c0e-aad9-83714a9920a9 "Watson Discovery Service for Developers")\n<!--END_SECTION:badges-->',
            no_changes,
        )

        badges = Credly(FOLDER_HTML+"happy_day.html").get_markdown()
        new_readme = generate_new_readme(badges, no_changes)
        self.assertEqual(
            '# badge-readme\nThis is example file\n<!--START_SECTION:badges-->\n[![Docker Essentials: A Developer Introduction](https://images.credly.com/size/110x110/images/08216781-93cb-4ba1-8110-8eb3401fa8ce/Docker_Essentials_-_ISDN.png)](http://www.credly.com/badges/24bcb006-58f8-494c-85e3-dfee10ea7b57 "Docker Essentials: A Developer Introduction")\n[![IBM Blockchain Essentials V2](https://images.credly.com/size/110x110/images/8e6bba9c-544d-46b0-bc7b-324fc85042ba/Blockchain_Essentials_V2.png)](http://www.credly.com/badges/47065bcc-63f9-4b1f-b403-48bcdbc78f54 "IBM Blockchain Essentials V2")\n[![Enterprise Design Thinking - Team Essentials for AI](https://images.credly.com/size/110x110/images/09f644d1-eed2-4279-bc49-1e26cddc9d3d/Team_Essentials.png)](http://www.credly.com/badges/5e280a76-446b-431a-80f0-7d2dc448a407 "Enterprise Design Thinking - Team Essentials for AI")\n[![Security and Privacy by Design Foundations](https://images.credly.com/size/110x110/images/c1ca6570-bdc6-40e9-8992-722050788418/Security-_-Privacy-by-Design-Foundational.png)](http://www.credly.com/badges/e4d08b6b-ee34-4fc9-9a1b-87c43a887233 "Security and Privacy by Design Foundations")\n[![IBM Blockchain Consulting](https://images.credly.com/size/110x110/images/28e2c951-1859-4812-807f-3b637e6403e5/Blockchain-consulting.png)](http://www.credly.com/badges/42efe367-3744-438a-8c03-59622c69c893 "IBM Blockchain Consulting")\n[![Watson Discovery Service Foundations](https://images.credly.com/size/110x110/images/edeaee50-64ff-42f0-a872-f4e2119ed463/Watson_Discovery_Service_-_Foundations.png)](http://www.credly.com/badges/06796b84-6cb6-40ea-9853-b4b8843e65da "Watson Discovery Service Foundations")\n[![Watson Discovery Foundations](https://images.credly.com/size/110x110/images/8c805fb7-b7e1-4b45-b933-7ee09385ea03/Watson_Academy_-_Discovery__-_Foundations.png)](http://www.credly.com/badges/b4f04f7d-a5dd-45bd-bfd1-1a0d29801bf8 "Watson Discovery Foundations")\n[![IBM Cloud Garage Test-Driven Development (TDD)](https://images.credly.com/size/110x110/images/71ea5682-2233-434c-a2c5-dd3f7fb8d5e9/Garage_Method_-_Test_driven_Development_V1_-__Final.png)](http://www.credly.com/badges/d9c9d869-b2e3-4cd2-a77d-7d53197b821e "IBM Cloud Garage Test-Driven Development (TDD)")\n[![Watson Discovery Service for Developers](https://images.credly.com/size/110x110/images/01774ad1-fbff-4ddc-8b28-fd7953cb7ff6/Watson_Discovery_Service_-_Developers.png)](http://www.credly.com/badges/0506d841-cd61-4c0e-aad9-83714a9920a9 "Watson Discovery Service for Developers")\n<!--END_SECTION:badges-->',
            new_readme,
        )

        self.assertEqual(no_changes, new_readme)