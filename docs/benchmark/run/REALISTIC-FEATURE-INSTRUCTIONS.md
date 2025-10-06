# Realistic Feature Implementation Challenge

**Your Mission**: Implement 2 missing features for the OLAF VSCode Extension based on user requests.

**Rules**:
- Analyze user requests to understand requirements
- Design and implement features from scratch
- Follow existing codebase patterns
- Write appropriate tests
- Each feature should be a separate commit

---

## Feature Request #1: Installation Status Check

**User Request**:
> "Hey, I installed OLAF a while ago but I'm not sure if it's working properly. Sometimes I get weird errors and I want to check if my installation is corrupted or something. Can you add a command to show me what version I have installed and if everything is OK? It would be really helpful for troubleshooting."

**Additional Context from Support Tickets**:
- Users often can't tell if OLAF is properly installed
- Installation corruption causes confusing error messages
- Support team needs users to provide installation details
- Users want to verify their setup before reporting issues

---

## Feature Request #2: GitHub Authentication Check

**User Request**:
> "I keep getting authentication errors when trying to install OLAF. It's super frustrating because the installation starts and then fails halfway through with some GitHub API error. Can you add a way to test my GitHub authentication before I try to install? That way I can fix auth issues upfront instead of wasting time on failed installs."

**Additional Context from Support Tickets**:
- 40% of installation failures are due to GitHub auth issues
- Users don't realize their tokens have expired
- Installation failures waste time and cause frustration
- Users need guidance on fixing authentication problems

---

## Implementation Guidelines

**What You Need to Figure Out**:
- How to integrate with existing command system
- What information users actually need to see
- How to handle various error scenarios gracefully
- What constitutes a "healthy" installation
- How to validate GitHub authentication properly
- What actionable guidance to provide users

**Success Criteria**:
- Features solve the actual user problems described
- Implementation follows existing code patterns
- Error handling is robust and user-friendly
- Commands are discoverable and easy to use
- Code is maintainable and well-tested

