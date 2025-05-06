def job_schedule(jobs):
    jobs.sort(key=lambda x: x[1], reverse=True)  # Sort by profit descending
    max_deadline = max(jobs, key=lambda x: x[2])[2]  # Find max deadline
    slot = [False] * max_deadline  # Create time slots
    profit = 0

    for i in range(len(jobs)):
        deadline = jobs[i][2] - 1  # 0-based index
        while deadline >= 0 and slot[deadline]:  # Find free slot
            deadline -= 1
        if deadline >= 0:
            slot[deadline] = True  # Book slot
            profit += jobs[i][1]   # Add profit

    return profit

jobs = [(1, 50, 2), (2, 10, 1), (3, 20, 2), (4, 30, 1), (5, 40, 3)]
print(job_schedule(jobs))  # Output: 120
