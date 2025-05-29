class DataHandling:
    @staticmethod
    def get_complete_task(main_tasks, child_tasks):
        child_task_map = {}
        tasks_full = []

        for child_row in child_tasks:
            child_task_id, main_task_id, child_task_name, status = child_row
            if main_task_id not in child_task_map:
                child_task_map[main_task_id] = []
            child_task_map[main_task_id].append({
                "child_task_id": child_task_id,
                "child_task_name": child_task_name,
                "status": status
            })

        for main_row in main_tasks:
            main_task_id, main_task_name, status, due_date, is_running, current_session_start_time, total_elapsed_time = \
                main_row
            tasks_full.append({
                "main_task_id": main_task_id,
                "main_task_name": main_task_name,
                "status": status,
                "due_date": due_date,
                "is_running": is_running,
                "current_session_start_time": current_session_start_time,
                "total_elapsed_time": total_elapsed_time,
                "child_tasks": child_task_map.get(main_task_id, [])
            })

        return tasks_full
