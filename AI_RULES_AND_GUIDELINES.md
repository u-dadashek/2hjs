# AI Rules and Guidelines for 2HJS Project

This document outlines the rules, best practices, and guidelines that AI must follow when assisting with the development of the `2HJS` project.

## 1. Memlog System

- Always create/verify the 'memlog' folder when starting any project.
- The memlog folder must contain: `tasks.log`(), `changelog.md`, `stability_checklist.md`, and `url_debug_checklist.md`.
- Verify and update these files before providing any responses or taking any actions.
- Use these logs to track user progress, system state, and persistent data between conversations.

## 2. Task Breakdown and Execution

- Break down all user instructions into clear, numbered steps.
- Include both actions and reasoning for each step.
- Flag potential issues before they arise.
- Verify the completion of each step before proceeding to the next.
- If errors occur, document them, return to previous steps, and retry as needed.

## 3. Credential Management

- Explain the purpose of each credential when requesting from users.
- Guide users to obtain any missing credentials.
- Always test the validity of credentials before using them.
- Never store credentials in plaintext; use environment variables, specifically using Pydantic models for validation and storage.
- Implement proper refresh procedures for expiring credentials.
- Provide guidance on secure credential storage methods, and implement appropriate security mechanisms to safeguard API keys.

## 4. Code Structure and Organization

- Keep files small and modular, and follow all relevant style guides including PEP 8 and use `black` to ensure consistent formatting.
- Split large components into smaller, manageable parts using a structured, well-organized project.
- Move constants, configurations, and long strings to separate files (e.g., `config.py`, `prompts/` folder, and models).
- Use descriptive names for files, functions, variables, and methods.
- Document all file dependencies and maintain a clean project structure.

## 5. Error Handling and Reporting

- Implement detailed and actionable error reporting, always using try/except blocks.
- Log errors with context and timestamps, including line numbers where errors occur.
- Provide users with clear steps for error recovery and resolution based on the error.
- Track error history to identify patterns, and correct them.
- Implement escalation procedures for unresolved issues, including when to ask for help from a human.
- Ensure all systems have robust error handling mechanisms, and report that they are working properly.

## 6. Third-Party Services Integration

- Verify that the user has completed all setup requirements for each service and is able to properly connect to them.
- Check all necessary permissions and settings for the application and the service.
- Test service connections before using them in workflows.
- Document version requirements and service dependencies, including how to set up and manage API keys and other authentication data.
- Prepare contingency plans for potential service outages or failures, as well as how to fall back to a safe state.

## 7. Dependencies and Libraries

- Always use the most stable versions of dependencies to ensure compatibility, and that are maintained and supported.
- Regularly update libraries, but avoid changes that might disrupt functionality without a thorough plan to avoid those disruptions.
- Use `pip` for all dependency management.

## 8. Code Documentation

- Write clear, concise comments for all sections of code.
- Use only one set of triple quotes for docstrings to prevent syntax errors. Use docstrings extensively and use them to clearly document all inputs, outputs, and side effects of all functions, methods, and classes, including raised exceptions.
- Document the purpose and expected behavior of functions, modules, and classes using docstrings and comments.

## 9. Change Management

- Review all changes to assess their impact on other parts of the project, particularly in regards to data flow, database persistence, model usage, and test results.
- Test all changes thoroughly to ensure consistency, and verify that all tests pass without any failures.
- Document all changes, their outcomes, and any corrective actions in the `changelog.md` file.

## 10. Problem-Solving Approach

- Exhaust all options before determining an action is impossible.
- When evaluating feasibility, check alternatives in all directions: up/down and left/right.
- Only conclude an action cannot be performed after all possibilities have been tested.

## 11. Testing and Quality Assurance

- Implement comprehensive unit tests for all components, and for every possible code path, and edge case.
- Perform integration testing to ensure different parts of the system work together as a complete unit.
- Conduct thorough end-to-end testing to validate user workflows and all expected outputs.
- Maintain high test coverage and document it in the `stability_checklist.md` file.
- Ensure all tests are designed to run automatically as a part of continuous integration workflows.

## 12. Security Best Practices

- Implement proper authentication and authorization mechanisms, and avoid storing keys or secrets directly in the code, and instead pull them from environment variables.
- Use secure communication protocols (HTTPS) for all network interactions, and use proper keys when working with external APIs.
- Sanitize and validate all user inputs to prevent injection attacks, using try/except blocks with appropriate error handling.
- Regularly update dependencies to patch known vulnerabilities, and avoid including libraries that may have security issues.
- Follow the principle of least privilege in system design.

## 13. Performance Optimization

- Optimize database queries for efficiency, and always verify that the data returned is correct, and that indexes are being used, where applicable.
- Implement caching strategies where appropriate, and make sure the cached data is used in the correct and appropriate way.
- Minimize network requests and payload sizes, and ensure you are only asking for what is needed, and not any extraneous information.
- Use asynchronous operations for I/O-bound tasks (e.g. database connections, LLM API calls, file downloads).
- Regularly profile the application to identify and address performance bottlenecks.

## 14. Compliance and Standards

- Ensure the application complies with relevant data protection regulations (e.g., GDPR, CCPA), using try/except blocks when processing any external or user data.
- Follow accessibility standards (WCAG) to make the application usable by people with disabilities.
- Adhere to industry-standard coding conventions and style guides (PEP8).

## 15. Documentation

- Maintain up-to-date API documentation.
- Provide clear, step-by-step guides for setup and deployment, that are consistent with the tools being used.
- Document known issues and their workarounds in the `stability_checklist.md` file.
- Keep user guides and FAQs current with each feature update, always testing to make sure the documented instructions are valid.

## 16. Data Driven Approach
 -  All analysis and conclusions must be directly supported by evidence extracted from SEC filings or other provided documents.
 -  Avoid any speculation, assumptions, or bias when making recommendations, always citing the exact place where the information came from.
 - All decisions must be based on the data provided.

Remember, these rules and guidelines must be followed without exception. Always refer back to this document when making decisions or providing assistance during the development process.