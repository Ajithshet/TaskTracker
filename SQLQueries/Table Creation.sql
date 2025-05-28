CREATE TABLE main_tasks (
	main_task_id SERIAL PRIMARY KEY,
	main_task_name VARCHAR(255) NOT NULL,
	status VARCHAR(20) NOT NULL CHECK (status in ('Completed', 'In-Progress')) DEFAULT 'In-Progress',
	due_date DATE,
	is_running BOOLEAN NOT NULL DEFAULT FALSE,
	current_session_start_time TIMESTAMP WITH TIME ZONE,
	total_elapse_time INTERVAL NOT NULL DEFAULT '0 seconds'
);

CREATE TABLE child_tasks (
	child_task_id SERIAL PRIMARY KEY,
	main_task_id INTEGER NOT NULL REFERENCES main_tasks(main_task_id) ON DELETE CASCADE,
	child_task_name VARCHAR(255) NOT NULL,
	status VARCHAR(20) NOT NULL CHECK (status in ('Completed', 'In-Progress')) DEFAULT 'In-Progress'
	
);

CREATE TABLE task_timers (
	timer_id SERIAL PRIMARY KEY,
	main_task_id INTEGER NOT NULL REFERENCES main_tasks(main_task_id) ON DELETE CASCADE,
	session_date DATE NOT NULL,
	start_timestamp TIMESTAMP WITH TIME ZONE NOT NULL,
	end_timestamp TIMESTAMP WITH TIME ZONE NOT NULL,
	duration INTERVAL NOT NULL
);