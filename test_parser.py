lines = [
    "LoginTest, PASS",
    "LoginTest, fail",
    "CheckoutTest,FAIL",
    "PaymentTest, PASS",
    "BadLineNoComma",
    ",FAIL",
    "SyncTest,SKIP"
]

passCount = 0
failCount = 0
invalidCount = 0
totalValid = 0

perTest = {}
errors = []

for line in lines:
    line = line.strip()
    if not line:
        continue

    if "," not in line:
        invalidCount += 1
        errors.append(line)
        continue

    testName, status = line.split(",", 1)
    testName = testName.strip()
    status = status.strip().upper()

    if not testName or status not in ["PASS", "FAIL"]:
        invalidCount += 1
        errors.append(line)
        continue

    totalValid += 1

    if testName not in perTest:
        perTest[testName] = {"pass": 0, "fail": 0}

    if status == "PASS":
        passCount += 1
        perTest[testName]["pass"] += 1
    else:
        failCount += 1
        perTest[testName]["fail"] += 1

# Find top failing test
topFailingTest = None
maxFails = -1

for test in sorted(perTest.keys()):
    if perTest[test]["fail"] > maxFails:
        maxFails = perTest[test]["fail"]
        topFailingTest = test

result = {
    "totalValid": totalValid,
    "passCount": passCount,
    "failCount": failCount,
    "invalidCount": invalidCount,
    "perTest": perTest,
    "topFailingTest": topFailingTest
}

print(result)
