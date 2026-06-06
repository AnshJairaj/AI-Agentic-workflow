from concurrent.futures import ThreadPoolExecutor

from agents import *


def execute_parallel(agent_list):

    results = []

    with ThreadPoolExecutor() as executor:

        futures = [
            executor.submit(agent.execute, "Task")
            for agent in agent_list
        ]

        for future in futures:
            results.append(future.result())

    return results


def run_learning_workflow():

    output = []

    assessment = SkillAssessmentAgent(
        "Skill Assessment Agent"
    )

    output.append(
        assessment.execute(
            "Skill Assessment Completed"
        )
    )

    profile = EmployeeProfileAgent(
        "Employee Profile Agent"
    )

    gap = SkillGapAgent(
        "Skill Gap Agent"
    )

    output.extend(
        execute_parallel(
            [profile, gap]
        )
    )

    course = CourseSearchAgent(
        "Course Search Agent"
    )

    output.append(
        course.execute(
            "Courses Recommended"
        )
    )

    path = LearningPathAgent(
        "Learning Path Agent"
    )

    output.append(
        path.execute(
            "Roadmap Created"
        )
    )

    cert = CertificationAgent(
        "Certification Agent"
    )

    output.append(
        cert.execute(
            "Certificate Generated"
        )
    )

    return output


def run_recruitment_workflow():

    screening = ResumeScreeningAgent(
        "Resume Screening Agent"
    )

    ranking = CandidateRankingAgent(
        "Candidate Ranking Agent"
    )

    interview = InterviewAgent(
        "Interview Agent"
    )

    offer = OfferLetterAgent(
        "Offer Letter Agent"
    )

    output = []

    output.extend(
        execute_parallel(
            [screening, ranking]
        )
    )

    output.append(
        interview.execute(
            "Interview Scheduled"
        )
    )

    output.append(
        offer.execute(
            "Offer Generated"
        )
    )

    return output


def run_it_workflow():

    ticket = TicketAgent(
        "Ticket Agent"
    )

    diag = DiagnosticAgent(
        "Diagnostic Agent"
    )

    res = ResolutionAgent(
        "Resolution Agent"
    )

    return [
        ticket.execute("Ticket Created"),
        diag.execute("Issue Diagnosed"),
        res.execute("Issue Resolved")
    ]


def run_procurement_workflow():

    vendor = VendorSearchAgent(
        "Vendor Search Agent"
    )

    budget = BudgetValidationAgent(
        "Budget Validation Agent"
    )

    po = PurchaseOrderAgent(
        "Purchase Order Agent"
    )

    output = []

    output.extend(
        execute_parallel(
            [vendor, budget]
        )
    )

    output.append(
        po.execute(
            "PO Generated"
        )
    )

    return output


def run_leave_workflow():

    leave = LeaveRequestAgent(
        "Leave Request Agent"
    )

    policy = PolicyValidationAgent(
        "Policy Validation Agent"
    )

    approval = ApprovalAgent(
        "Approval Agent"
    )

    return [
        leave.execute("Leave Requested"),
        policy.execute("Policy Verified"),
        approval.execute("Leave Approved")
    ]