def add_task(task_list, new_task):
    return task_list + [new_task]

def complete_task(task_list, completed_task):
    return list(map(lambda t: t if t != completed_task else f"[COMPLETED] {t}", task_list))

def filter_incomplete_tasks(task_list):
    return list(filter(lambda t: "[COMPLETED]" not in t, task_list))
