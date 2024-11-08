import json

# Paths for input and output files
swiftlint_report_path = "sonar-reports/SonarSwiftSample-swiftlint.json"
sonarqube_report_path = "sonar-reports/generic-lint-report.json"

# Mapping SwiftLint severity to SonarQube severity
severity_mapping = {
    "error": "MAJOR",
    "warning": "MINOR"
}

# Read SwiftLint JSON report
with open(swiftlint_report_path, "r") as file:
    swiftlint_issues = json.load(file)

# Prepare the SonarQube Generic Issue Data format structure
sonarqube_issues = {"issues": []}

for issue in swiftlint_issues:
    # Map SwiftLint fields to SonarQube format
    sonarqube_issue = {
        "engineId": "swiftlint",
        "ruleId": issue["rule_id"],
        "severity": severity_mapping.get(issue["severity"], "INFO"),
        "type": "CODE_SMELL",  # SwiftLint issues are typically code smells
        "primaryLocation": {
            "message": issue["reason"],
            "filePath": issue["file"],
            "textRange": {
                "startLine": issue["line"],
                "endLine": issue["line"],
                "startColumn": issue.get("character", 1),  # Default to 1 if not provided
                "endColumn": issue.get("character", 1)  # Default to 1 if not provided
            }
        },
        "effortMinutes": 5  # Optional, can adjust based on rule severity if desired
    }
    
    # Add issue to the list
    sonarqube_issues["issues"].append(sonarqube_issue)

# Write the converted report to a new JSON file
with open(sonarqube_report_path, "w") as file:
    json.dump(sonarqube_issues, file, indent=2)

print(f"Converted SwiftLint report saved to {sonarqube_report_path}")
